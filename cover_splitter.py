# -*- coding: utf-8 -*-
"""Book Cover Splitter: ручное разделение изображений на две части."""
from pathlib import Path
from datetime import datetime
import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from PIL import Image, ImageTk
from split_core import (
    IMAGE_EXTENSIONS, load_source, natural_key, safe_name,
    save_parts, settings_path, split_pixel, part_names, OUTPUT_FORMATS,
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Book Cover Splitter — разделение изображений')
        self.geometry('1240x900');self.minsize(1000,700)
        self.output_dir=None
        self.series=''
        self.part_labels=['Обложка','Корешок']
        self.output_format='SOURCE'
        self.first_number=1
        self.index=None;self.image=None;self.photo=None
        self.row_drag=None
        self.viewport=None;self.loading=False
        self.state_path=settings_path()
        self.rows=[]
        self.restore()
        self.build()
        self.refresh_rows()
        if self.rows:self.table.selection_set('0');self.select()
        self.protocol('WM_DELETE_WINDOW',self.close)

    def book_title(self,index):
        if self.series.strip():
            return f'{self.series.strip()}. Том {self.first_number+index}'
        return self.rows[index]['path'].stem

    def make_row(self,path,fraction=0.9):
        try:
            im=load_source(path)
            split_pixel(im.width,fraction)
            return {'path':Path(path),'size':im.size,'fraction':float(fraction),'error':''}
        except Exception as exc:
            return {'path':Path(path),'size':None,'fraction':0.9,'error':str(exc)}

    def restore(self):
        if not self.state_path.is_file():return
        try:
            state=json.loads(self.state_path.read_text(encoding='utf-8'))
            self.series=str(state.get('series',''))
            chosen=state.get('output_format','SOURCE')
            self.output_format=chosen if chosen in OUTPUT_FORMATS else 'SOURCE'
            labels=state.get('part_labels',['Обложка','Корешок'])
            if isinstance(labels,list) and len(labels)==2 and all(isinstance(v,str) for v in labels):
                self.part_labels=labels
            self.first_number=max(1,int(state.get('first_number',1)))
            if state.get('output_dir'):self.output_dir=Path(state['output_dir'])
            self.rows=[self.make_row(Path(row['path']),float(row.get('fraction',0.9)))
                       for row in state.get('files',[])]
        except (ValueError,KeyError,TypeError,OSError):
            self.rows=[];self.output_dir=None;self.series='';self.first_number=1

    def persist(self):
        state={'series':self.series,'first_number':self.first_number,'part_labels':self.part_labels,'output_format':self.output_format,
               'output_dir':str(self.output_dir) if self.output_dir else None,
               'files':[{'path':str(row['path']),'fraction':row['fraction']} for row in self.rows]}
        self.state_path.parent.mkdir(parents=True,exist_ok=True)
        temporary=self.state_path.with_suffix('.tmp')
        temporary.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
        temporary.replace(self.state_path)

    def add_files(self):
        paths=filedialog.askopenfilenames(title='Выбери изображения',filetypes=[
            ('Изображения','*.jpg *.jpeg *.png *.webp *.bmp *.tif *.tiff *.gif'),('Все файлы','*.*')])
        self.add_paths(paths)

    def add_folder(self):
        folder=filedialog.askdirectory(title='Папка с исходными изображениями')
        if folder:
            self.add_paths(sorted((p for p in Path(folder).iterdir() if p.suffix.lower() in IMAGE_EXTENSIONS),
                                  key=lambda p:natural_key(p.name)))

    def add_paths(self,paths):
        existing={str(row['path'].resolve()) for row in self.rows}
        for path in paths:
            path=Path(path).resolve()
            if str(path) not in existing:
                self.rows.append(self.make_row(path));existing.add(str(path))
        self.persist();self.refresh_rows()
        if self.index is None and self.rows:self.table.selection_set('0');self.select()
        self.status.set(f'Изображений: {len(self.rows)}. Порядок можно менять перетаскиванием строк мышью.')

    def choose_output(self):
        folder=filedialog.askdirectory(title='Папка сохранения',mustexist=True)
        if folder:
            self.output_dir=Path(folder);self.persist();self.update_destination()
        return bool(self.output_dir)

    def update_destination(self):
        self.destination.set(f'Сохранение: {self.output_dir}' if self.output_dir else 'Папка сохранения не выбрана')

    def naming(self):
        value=simpledialog.askstring('Названия','Название серии (пусто — имена исходных файлов):',initialvalue=self.series,parent=self)
        if value is None:return
        self.series=value.strip();self.persist();self.refresh_rows()

    def labels_changed(self,*_):
        self.part_labels=[self.left_name.get(),self.right_name.get()]
        self.persist()
        self.render()

    def format_changed(self,event=None):
        label=self.format_choice.get()
        self.output_format=next(key for key,value in OUTPUT_FORMATS.items() if value==label)
        self.persist()

    def display_labels(self):
        return (self.part_labels[0].strip() or 'Обложка',
                self.part_labels[1].strip() or 'Корешок')

    def numbering(self):
        value=simpledialog.askinteger('Нумерация','Номер первого тома:',initialvalue=self.first_number,minvalue=1,parent=self)
        if value is not None:self.first_number=value;self.persist();self.refresh_rows()

    def move(self,delta):
        if self.index is None:return
        old=self.index;new=old+delta
        if not 0<=new<len(self.rows):return
        self.rows[old],self.rows[new]=self.rows[new],self.rows[old]
        self.index=None;self.refresh_rows();self.table.selection_set(str(new));self.select();self.persist()

    def begin_row_drag(self,event):
        if event.state & 0x0005:  # Ctrl/Shift are reserved for multi-selection.
            self.row_drag=None
            return
        item=self.table.identify_row(event.y)
        self.row_drag={'source':int(item),'y':event.y,'active':False} if item else None

    def row_drag_insertion(self,y):
        item=self.table.identify_row(y)
        if item:
            box=self.table.bbox(item)
            return int(item)+(1 if box and y>=box[1]+box[3]/2 else 0),item
        # Dropping in the empty space below the last row appends it.
        children=self.table.get_children()
        if children:
            first=self.table.bbox(children[0])
            if first and y<first[1]:return 0,None
        return len(self.rows),None

    def clear_drop_highlight(self):
        for item in self.table.get_children():
            self.table.item(item,tags=())
        self.table.configure(cursor='')

    def drag_row(self,event):
        if self.row_drag is None:return
        if abs(event.y-self.row_drag['y'])<4 and not self.row_drag['active']:return
        self.row_drag['active']=True
        if event.y<35:self.table.yview_scroll(-1,'units')
        elif event.y>self.table.winfo_height()-25:self.table.yview_scroll(1,'units')
        _,target=self.row_drag_insertion(event.y)
        self.clear_drop_highlight()
        if target:self.table.item(target,tags=('drop_target',))
        self.table.configure(cursor='fleur')
        return 'break'

    def reorder_row(self,source,insertion):
        destination=max(0,min(len(self.rows)-1,insertion-(1 if source<insertion else 0)))
        if source==destination:return
        row=self.rows.pop(source)
        self.rows.insert(destination,row)
        self.index=None
        self.refresh_rows()
        self.table.selection_set(str(destination))
        self.table.see(str(destination))
        self.select()
        self.persist()
        self.status.set('Порядок сохранён. Нумерация серии обновлена; разрезы остались у своих изображений.')

    def end_row_drag(self,event):
        state=self.row_drag
        self.row_drag=None
        self.clear_drop_highlight()
        if state is None or not state['active']:return
        insertion,_=self.row_drag_insertion(event.y)
        self.reorder_row(state['source'],insertion)
        return 'break'

    def remove(self):
        if self.index is None:return
        old=self.index;self.rows.pop(old);self.index=None;self.image=None
        self.table.delete(*self.table.get_children());self.refresh_rows()
        if self.rows:self.table.selection_set(str(min(old,len(self.rows)-1)));self.select()
        else:self.render()
        self.persist()

    def clear(self):
        self.rows=[];self.index=None;self.image=None
        self.table.delete(*self.table.get_children());self.render();self.persist()
        self.status.set('Список очищен. Файлы на диске не изменены.')

    def build(self):
        menu=tk.Menu(self)
        files=tk.Menu(menu,tearoff=False)
        files.add_command(label='Добавить изображения…',command=self.add_files)
        files.add_command(label='Добавить папку…',command=self.add_folder)
        files.add_separator()
        files.add_command(label='Папка сохранения…',command=self.choose_output)
        files.add_command(label='Убрать выбранное из списка',command=self.remove)
        files.add_command(label='Очистить список',command=self.clear)
        files.add_separator();files.add_command(label='Выход',command=self.close)
        menu.add_cascade(label='Файл',menu=files)
        names=tk.Menu(menu,tearoff=False)
        names.add_command(label='Название серии…',command=self.naming)
        names.add_command(label='Номер первого тома…',command=self.numbering)
        menu.add_cascade(label='Названия',menu=names)
        self.configure(menu=menu)
        outer=ttk.Frame(self,padding=10);outer.pack(fill='both',expand=True)
        ttk.Label(outer,text='Файл → Добавить изображения → подбери X в пикселях или перетащи линию → сохрани.',font=('Segoe UI',11)).pack(anchor='w')
        self.destination=tk.StringVar();self.update_destination()
        ttk.Label(outer,textvariable=self.destination).pack(anchor='w',pady=(3,8))
        names_row=ttk.Frame(outer);names_row.pack(fill='x',pady=(0,8))
        ttk.Label(names_row,text='Левая часть:').pack(side='left')
        self.left_name=tk.StringVar(value=self.part_labels[0])
        ttk.Entry(names_row,textvariable=self.left_name,width=28).pack(side='left',padx=(6,18))
        ttk.Label(names_row,text='Правая часть:').pack(side='left')
        self.right_name=tk.StringVar(value=self.part_labels[1])
        ttk.Entry(names_row,textvariable=self.right_name,width=28).pack(side='left',padx=6)
        format_row=ttk.Frame(outer);format_row.pack(fill='x',pady=(0,8))
        ttk.Label(format_row,text='Формат сохранения:').pack(side='left')
        self.format_choice=ttk.Combobox(format_row,values=list(OUTPUT_FORMATS.values()),state='readonly',width=22)
        self.format_choice.set(OUTPUT_FORMATS[self.output_format])
        self.format_choice.pack(side='left',padx=6)
        self.format_choice.bind('<<ComboboxSelected>>',self.format_changed)
        body=ttk.Frame(outer);body.pack(fill='both',expand=True)
        left=ttk.Frame(body);left.pack(side='left',fill='y',padx=(0,10))
        self.table=ttk.Treeview(left,columns=('vol','name','size','x','spine'),show='headings',height=18,selectmode='extended')
        for col,title,width in [('vol','№',32),('name','Название',160),('size','Исходник',90),('x','X',48),('spine','Правая, px',86)]:
            self.table.heading(col,text=title);self.table.column(col,width=width,anchor='center',stretch=False)
        self.table.pack(fill='y',expand=True);self.table.bind('<<TreeviewSelect>>',lambda e:self.select())
        self.table.tag_configure('drop_target',background='#dbeafe')
        self.table.bind('<ButtonPress-1>',self.begin_row_drag,add='+')
        self.table.bind('<B1-Motion>',self.drag_row)
        self.table.bind('<ButtonRelease-1>',self.end_row_drag,add='+')
        order=ttk.Frame(left);order.pack(fill='x',pady=5)
        ttk.Button(order,text='↑',width=5,command=lambda:self.move(-1)).pack(side='left')
        ttk.Button(order,text='↓',width=5,command=lambda:self.move(1)).pack(side='left',padx=4)
        ttk.Button(order,text='Убрать',command=self.remove).pack(side='left')
        ttk.Label(left,text='Перетаскивай строки мышью для изменения порядка.\nX — от левого края исходника.\nЛевая часть — до линии, правая — после.',justify='left').pack(anchor='w',pady=8)
        right=ttk.Frame(body);right.pack(side='left',fill='both',expand=True)
        controls=ttk.Frame(right);controls.pack(fill='x')
        ttk.Label(controls,text='Разрез X:').pack(side='left')
        self.xvar=tk.StringVar()
        self.spin=ttk.Spinbox(controls,from_=1,to=10000,textvariable=self.xvar,width=8,command=self.changed)
        self.spin.pack(side='left',padx=6)
        self.spin.bind('<Return>',lambda e:self.changed());self.spin.bind('<FocusOut>',lambda e:self.changed())
        ttk.Button(controls,text='−1 px',command=lambda:self.step(-1)).pack(side='left',padx=2)
        ttk.Button(controls,text='+1 px',command=lambda:self.step(1)).pack(side='left',padx=2)
        ttk.Button(controls,text='Применить долю ко всем',command=self.apply_all).pack(side='left',padx=10)
        self.info=tk.StringVar();ttk.Label(right,textvariable=self.info,font=('Segoe UI',11)).pack(anchor='w',pady=6)
        self.canvas=tk.Canvas(right,bg='#30343b',highlightthickness=0)
        self.canvas.pack(fill='both',expand=True)
        self.canvas.bind('<Configure>',lambda e:self.render())
        self.canvas.bind('<Button-1>',self.drag);self.canvas.bind('<B1-Motion>',self.drag)
        buttons=ttk.Frame(outer);buttons.pack(fill='x',pady=(10,0))
        ttk.Button(buttons,text='Сохранить выбранное',command=lambda:self.save(False)).pack(side='left')
        ttk.Button(buttons,text='Пересоздать все',command=lambda:self.save(True)).pack(side='left',padx=10)
        self.status=tk.StringVar(value='Настройки разреза сохраняются автоматически.')
        ttk.Label(outer,textvariable=self.status).pack(anchor='w',pady=(6,0))
        # Typing a valid number updates the preview immediately.
        self.xvar.trace_add('write',lambda *args:self.changed())
        self.left_name.trace_add('write',self.labels_changed)
        self.right_name.trace_add('write',self.labels_changed)

    def refresh_rows(self):
        for i,row in enumerate(self.rows):
            size=row['size']
            if size:
                w,h=size;x=split_pixel(w,row['fraction'])
                vals=(self.first_number+i,self.book_title(i),f'{w}×{h}',x,f'{w-x} px')
            else:vals=(self.first_number+i,self.book_title(i),'Нет файла','—','—')
            if self.table.exists(str(i)):self.table.item(str(i),values=vals)
            else:self.table.insert('', 'end',iid=str(i),values=vals)
    def select(self):
        selected=self.table.selection()
        if not selected:return
        focused=self.table.focus()
        i=int(focused if focused in selected else selected[0])
        if self.index==i:return
        self.index=i;row=self.rows[i];self.image=None
        self.loading=True
        if row['size']:
            try:
                self.image=load_source(row['path']);w,h=self.image.size
                row['size']=(w,h);self.spin.configure(to=w-1)
                self.xvar.set(str(split_pixel(w,row['fraction'])))
            except Exception as exc:row['error']=str(exc)
        else:self.xvar.set('')
        self.loading=False;self.render()
    def changed(self):
        if self.loading or self.image is None:return False
        try:
            x=int(self.xvar.get());w=self.image.width
            if not 1<=x<w:return False
        except ValueError:return False
        self.rows[self.index]['fraction']=x/w
        self.persist();self.refresh_rows();self.render();return True
    def step(self,delta):
        if self.image is None:return
        try:x=int(self.xvar.get())
        except ValueError:return
        self.xvar.set(str(max(1,min(self.image.width-1,x+delta))))
    def render(self):
        self.canvas.delete('all');self.viewport=None
        if self.image is None:
            row=self.rows[self.index] if self.index is not None else None
            self.info.set('Исходник недоступен' if row else 'Добавь изображения через меню «Файл»')
            self.canvas.create_text(15,20,anchor='nw',fill='white',text=str(row['path'])+'\n'+row['error'] if row else 'Нет файлов',width=650)
            self.xvar.set('');return
        w,h=self.image.size
        x=split_pixel(w,self.rows[self.index]['fraction'])
        left_label,right_label=self.display_labels()
        self.info.set(f'Исходник {w}×{h}  |  X = {x} px  |  {left_label} {x}×{h}  |  {right_label} {w-x}×{h}')
        cw,ch=max(10,self.canvas.winfo_width()),max(10,self.canvas.winfo_height())
        scale=min((cw-20)/w,(ch-20)/h)
        if scale<=0:return
        pw,ph=max(1,round(w*scale)),max(1,round(h*scale))
        self.photo=ImageTk.PhotoImage(self.image.convert("RGBA").resize((pw,ph),Image.Resampling.LANCZOS))
        ox,oy=(cw-pw)/2,(ch-ph)/2
        self.canvas.create_image(ox,oy,anchor='nw',image=self.photo)
        self.canvas.create_line(ox+x*pw/w,oy,ox+x*pw/w,oy+ph,fill='#ff3333',width=2)
        self.viewport=(ox,oy,pw,ph)
    def drag(self,event):
        if not self.viewport or self.image is None:return
        ox,oy,pw,ph=self.viewport
        x=round((event.x-ox)*self.image.width/pw)
        self.xvar.set(str(max(1,min(self.image.width-1,x))))
    def apply_all(self):
        if not self.changed():return
        row=self.rows[self.index];ratio=row['fraction']
        for other in self.rows:other['fraction']=ratio
        self.persist();self.refresh_rows()
        self.status.set(f'Ко всем изображениям применено {ratio*100:.4f}% ширины. Реальные X показаны в таблице.')
    def save(self,all_rows):
        selected=set(self.table.selection())
        indices=list(range(len(self.rows))) if all_rows else [
            int(item) for item in self.table.get_children() if item in selected
        ]
        if not indices:
            messagebox.showinfo('Сохранение','Выбери одно или несколько изображений в списке.')
            return
        if self.image is not None and not self.changed():
            messagebox.showerror('Разрез','Введи целое число X от 1 до ширины изображения минус 1.');return
        try:
            left_label,right_label=part_names(*self.part_labels)
        except ValueError as exc:
            messagebox.showerror('Названия частей',str(exc));return
        if self.output_dir is None and not self.choose_output():return
        target=self.output_dir
        if target.drive and not Path(target.anchor).exists():
            messagebox.showerror('Папка назначения',f'Диск недоступен: {target.anchor}');return
        chosen=[self.rows[i] for i in indices]
        stamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f');done=0;errors=[]
        try:
            titles=[safe_name(self.book_title(i)) for i in indices]
        except ValueError as exc:
            messagebox.showerror('Названия',str(exc));return
        if len({title.casefold() for title in titles})!=len(titles):
            messagebox.showerror('Названия','Одинаковые базовые имена файлов. Задай название серии через меню «Названия» — файлы получат разные номера.');return
        for row in chosen:
            try:
                w,h,x=save_parts(row['path'],target,self.book_title(self.rows.index(row)),row['fraction'],stamp,left_label=left_label,right_label=right_label,output_format=self.output_format)
                row['size']=(w,h);done+=1
            except Exception as exc:errors.append(f'{row["path"].name}: {exc}')
        self.refresh_rows();self.status.set(f'Обработано {done} исходников, {done*2} файлов. Папка: {target}')
        if errors:messagebox.showerror('Пропущенные файлы','\n'.join(errors))
        else:messagebox.showinfo('Готово',f'Сохранено {done*2} файлов в\n{target}')
    def close(self):
        self.persist();self.destroy()

if __name__=='__main__':
    try:App().mainloop()
    except Exception as exc:
        import traceback
        traceback.print_exc()
        try:messagebox.showerror('Ошибка',str(exc))
        except Exception:pass
        input('Нажми Enter для закрытия...')
