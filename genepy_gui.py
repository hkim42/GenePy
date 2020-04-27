import tkinter as tk
import genepy

class genepy_gui:
    def __init__(self):
        self.window3_open = False
        self.rules0 = ['ALL_FORWARD', 'ALL_REVERSE']
        self.rules1 = ['CONTAINS', 'STARTSWITH', 'ENDSWITH', 'ALL_FORWARD_IF', 'ALL_REVERSE_IF', 'SOME_FORWARD',
                       'SOME_REVERSE']
        self.rules2 = ['MORETHAN', 'EXACTLY', 'THEN', 'WITH', 'ALL_AFTER', 'SOME_AFTER', 'ALL_BEFORE',
                       'SOME_BEFORE', 'ALL_NEXTTO', 'SOME_NEXTTO', 'REPRESSES', 'INDUCES', 'DRIVES']
        
        self.window = tk.Tk()

        self.ent_N = tk.Entry()
        self.ent_N.insert(0, 'Enter Seq. Length')
        self.ent_N.grid(row=0, column=0)

        self.btn_console = tk.Button(text='Launch Console', width=16, height=2)
        self.btn_console.grid(row=0, column=2)
        self.btn_console.bind('<Button-1>', (lambda event: self.handle_btn_console()))
        
        self.btn_run = tk.Button(text='Run Solver', width=16, height=2)
        self.btn_run.grid(row=0, column=4)
        self.btn_run.bind('<Button-1>', self.handle_btn_run())

        ## Grid for Rules ##########################################################
        row_start = 1
        column_start = 0

        row_rule = row_start
        column_rule = column_start
        self.rule_add_lbl(self.window, row_rule, column_rule, 'Counting Rules')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'MORETHAN')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'LESSTHAN')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'EXACTLY')

        row_rule = row_start
        column_rule = column_rule+1
        self.rule_add_lbl(self.window, row_rule, column_rule, 'Pairing Rules')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'THEN')

        row_rule = row_start
        column_rule = column_rule+1
        self.rule_add_lbl(self.window, row_rule, column_rule, 'Positioning Rules')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'STARTSWITH')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'ENDSWITH')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'ALL_AFTER')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'SOME_AFTER')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'ALL_BEFORE')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'ALL_NEXTTO')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'SOME_NEXTTO')
        row_rule = row_rule+1

        row_rule = row_start
        column_rule = column_rule+1
        self.rule_add_lbl(self.window, row_rule, column_rule, 'Orientation Rules')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'ALL_FORWARD_IF')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'ALL_REVERSE_IF')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'SOME_FORWARD')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'SOME_REVERSE')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'ALL_FORWARD')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'ALL_REVERSE')
        row_rule = row_rule+1

        row_rule = row_start
        column_rule = column_rule+1
        self.rule_add_lbl(self.window, row_rule, column_rule, 'Interactions Rules')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'REPRESSES')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'INDUCES')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'DRIVES')
        row_rule = row_rule+1

        self.window.mainloop()

    def handle_btn_console(self):
        self.window3_open = True
        self.window3_text_location = 20
        self.window3 = tk.Tk()

        _frm = tk.Frame(master=self.window3, width=300, height=300)
        _frm.pack(expand=True)
        self._canvas = tk.Canvas(master=_frm, width=300, height=300, scrollregion=(0,0,500,500), background='white')
        
        hbar = tk.Scrollbar(_frm, orient='horizontal')
        hbar.pack(side='bottom', fill='x')
        hbar.config(command=self._canvas.xview)

        vbar = tk.Scrollbar(_frm, orient='vertical')
        vbar.pack(side='right', fill='y')
        vbar.config(command=self._canvas.yview)

        self._canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self._canvas.pack(expand=True)
        
        self.window3.mainloop()
        self.window3_open = False

    # handles for when the user adds a rule
    def handle_btn_add(self, window, txt):
        if self.window3_open == True:
            if txt in self.rules0:
                self._canvas.create_text(20, self.window3_text_location, anchor='w',
                                         text=txt)
            elif txt in self.rules1:
                self._canvas.create_text(20, self.window3_text_location, anchor='w',
                                         text=txt+'    '+self._ent0.get())
            elif txt in self.rules2:
                self._canvas.create_text(20, self.window3_text_location, anchor='w',
                                         text=self._ent0.get()+'    '+txt+'    '+self._ent1.get())
            else:
                raise Exception('something went very wrong here')
            
            self.window3_text_location = self.window3_text_location+20
        
        window.destroy()

    # opens a window after the user clicks a rule
    def handle_btn_rule(self, txt):
        window2 = tk.Tk()
        window2.geometry('250x100')

        self._ent0 = tk.Entry(master=window2)
        self._ent0.insert(0, 'Enter Part Name')
        
        _lbl = tk.Label(master=window2, text=txt)

        self._ent1 = tk.Entry(master=window2)
        self._ent1.insert(0, 'Enter Part Name')

        if txt in self.rules0:
            _lbl.pack()
        elif txt in self.rules1:
            _lbl.pack()
            self._ent0.pack()
        elif txt in self.rules2:
            self._ent0.pack()
            _lbl.pack()
            self._ent1.pack()
        else:
            raise Exception('something went very wrong here')

        btn_add_rule = tk.Button(master=window2, text='Add Rule')
        btn_add_rule.bind('<Button-1>', (lambda event: self.handle_btn_add(window2, txt)))
        btn_add_rule.pack()

        window2.mainloop()

    def handle_btn_run(self):
        pass

    def rule_add_lbl(self, win, _row, _col, txt):
        frm_rule = tk.Frame(master=win, borderwidth=1)
        frm_rule.grid(row=_row, column=_col)
        _lbl = tk.Label(master=frm_rule, text=txt)
        _lbl.pack()

    def rule_add_btn(self, win, _row, _col, txt):
        frm_rule = tk.Frame(master=win, borderwidth=1)
        frm_rule.grid(row=_row, column=_col)
        _btn = tk.Button(master=frm_rule, text=txt, width=16, height=2)
        _btn.bind('<Button-1>', (lambda event: self.handle_btn_rule(txt)))
        _btn.pack()

if __name__ == '__main__':
    foo = genepy_gui()
