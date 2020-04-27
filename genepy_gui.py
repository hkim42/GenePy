import tkinter as tk
from genepy import genepy

class genepy_gui:
    def __init__(self):
        self.window3_open = False
        self.rules0 = ['ALL_FORWARD', 'ALL_REVERSE']
        self.rules1 = ['CONTAINS', 'STARTSWITH', 'ENDSWITH', 'ALL_FORWARD_IF', 'ALL_REVERSE_IF', 'SOME_FORWARD',
                       'SOME_REVERSE']
        self.rules2 = ['MORETHAN', 'EXACTLY', 'THEN', 'WITH', 'ALL_AFTER', 'SOME_AFTER', 'ALL_BEFORE',
                       'SOME_BEFORE', 'ALL_NEXTTO', 'SOME_NEXTTO', 'REPRESSES', 'INDUCES', 'DRIVES']
        self.mygp = genepy(1)

        self.window = tk.Tk()

        self.ent_N = tk.Entry()
        self.ent_N.insert(0, 'Enter Seq. Length')
        self.ent_N.grid(row=0, column=0)

        self.btn_console = tk.Button(text='Launch Console', width=16, height=2)
        self.btn_console.grid(row=0, column=1)
        self.btn_console.bind('<Button-1>', (lambda event: self.handle_btn_console()))

        self.ent_sol = tk.Entry()
        self.ent_sol.insert(0, 'Enter No. Solutions')
        self.ent_sol.grid(row=0, column=2)

        self.btn_run = tk.Button(text='Run Solver', width=16, height=2)
        self.btn_run.grid(row=0, column=4)
        self.btn_run.bind('<Button-1>', (lambda event: self.handle_btn_run()))

        ## Grid for Rules ##########################################################
        row_start = 1
        column_start = 0

        row_rule = row_start
        column_rule = column_start
        self.rule_add_lbl(self.window, row_rule, column_rule, 'Counting Rules')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'MORETHAN')
        row_rule = row_rule+1
        self.rule_add_btn(self.window, row_rule, column_rule, 'CONTAINS')
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
        self.rule_add_btn(self.window, row_rule, column_rule, 'SOME_BEFORE')
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
                raise Exception('error0')

            self.window3_text_location = self.window3_text_location+20

        if txt == 'MORETHAN':
            self.mygp.morethan(self._ent0.get(), int(self._ent1.get()))
        elif txt == 'CONTAINS':
            self.mygp.contains(self._ent0.get())
        elif txt == 'EXACTLY':
            self.mygp.exactly(self._ent0.get(), int(self._ent1.get()))
        elif txt == 'THEN':
            self.mygp.then(self._ent0.get(), self._ent1.get())
        elif txt == 'WITH':
            self.mygp.witH(self._ent0.get(), self._ent1.get())
        elif txt == 'STARTSWITH':
            self.mygp.startswith(self._ent0.get())
        elif txt == 'ENDSWITH':
            self.mygp.endswith(self._ent0.get())
        elif txt == 'ALL_AFTER':
            self.mygp.all_after(self._ent0.get(), self._ent1.get())
        elif txt == 'SOME_AFTER':
            self.mygp.some_after(self._ent0.get(), self._ent1.get())
        elif txt == 'ALL_BEFORE':
            self.mygp.all_before(self._ent0.get(), self._ent1.get())
        elif txt == 'SOME_BEFORE':
            self.mygp.some_before(self._ent0.get(), self._ent1.get())
        elif txt == 'ALL_NEXTTO':
            self.mygp.all_nextto(self._ent0.get(), self._ent1.get())
        elif txt == 'SOME_NEXTTO':
            self.mygp.some_nextto(self._ent0.get(), self._ent1.get())
        elif txt == 'ALL_FORWARD_IF':
            self.mygp.all_forward_if(self._ent0.get())
        elif txt == 'ALL_REVERSE_IF':
            self.mygp.all_reverse_if(self._ent0.get())
        elif txt == 'SOME_FORWARD':
            self.mygp.some_forward(self._ent0.get())
        elif txt == 'SOME_REVERSE':
            self.mygp.some_reverse(self._ent0.get())
        elif txt == 'ALL_FORWARD':
           self.mygp.all_forward()
        elif txt == 'ALL_REVERSE':
            self.mygp.all_reverse()
        elif txt == 'REPRESSES':
            self.mygp.represses(self._ent0.get(), self._ent1.get())
        elif txt == 'INDUCES':
            self.mygp.induces(self._ent0.get(), self._ent1.get())
        elif txt == 'DRIVES':
            self.mygp.drives(self._ent0.get(), self._ent1.get())
        else:
            raise Exception('error1')

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
            raise Exception('error2')

        btn_add_rule = tk.Button(master=window2, text='Add Rule')
        btn_add_rule.bind('<Button-1>', (lambda event: self.handle_btn_add(window2, txt)))
        btn_add_rule.pack()

        window2.mainloop()

    def handle_btn_run(self):
        self.mygp.change_length(int(self.ent_N.get()))
        outputs = self.mygp.generate(int(self.ent_sol.get()))

        buf = ''
        for sequence in outputs:
            for ii in range(0, len(sequence)):
                buf = buf + sequence[ii]
                if ii < len(sequence)-1:
                    buf = buf + ' -> '
            self._canvas.create_text(20, self.window3_text_location, anchor='w', text=buf)
            self.window3_text_location = self.window3_text_location+20
            buf = ''

        for x in outputs:
            print(x)

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
