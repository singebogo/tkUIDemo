from datetime import datetime
from random import choices
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle
from tkinter.filedialog import askdirectory
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from pathlib import Path

from .collapsingFrame import CollapsingFrame

PATH = Path(__file__).parent.parent / 'assets'


class ToolsBar_Top_Left_Right_Layout(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        image_files = {
            'properties-dark': 'icons8_settings_24px.png',
            'properties-light': 'icons8_settings_24px_2.png',
            'add-to-backup-dark': 'icons8_add_folder_24px.png',
            'add-to-backup-light': 'icons8_add_book_24px.png',
            'stop-backup-dark': 'icons8_cancel_24px.png',
            'stop-backup-light': 'icons8_cancel_24px_1.png',
            'play': 'icons8_play_24px_1.png',
            'refresh': 'icons8_refresh_24px_1.png',
            'stop-dark': 'icons8_stop_24px.png',
            'stop-light': 'icons8_stop_24px_1.png',
            'opened-folder': 'icons8_opened_folder_24px.png',
            'logo': 'backup.png'
        }

        self.photoimages = []
        imgpath = Path(__file__).parent.parent / 'assets'
        for key, val in image_files.items():
            _path = imgpath / val
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        self.init_button_bar()
        self.init_left_panel()
        self.init_right_panel()

    def init_button_bar(self):
        # buttonbar
        buttonbar = ttk.Frame(self, style='primary.TFrame')
        buttonbar.pack(fill=X, pady=1, side=TOP)

        ## new backup
        _func = lambda: Messagebox.ok(message='Adding new backup')
        btn = ttk.Button(
            master=buttonbar, text='New backup set',
            image='add-to-backup-light',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

        ## backup
        _func = lambda: Messagebox.ok(message='Backing up...')
        btn = ttk.Button(
            master=buttonbar,
            text='Backup',
            image='play',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)


    def init_left_panel(self):
        # left panel
        left_panel = ttk.Frame(self, style='bg.TFrame')
        left_panel.pack(side=LEFT, fill=Y)

        self.init_backup_summary_CollapsingFrame(left_panel)
        self.init_backup_status_CollapsingFrame(left_panel)
        self.init_other_CollapsingFrame(left_panel)

    def init_backup_summary_CollapsingFrame(self, left_panel):
        ## backup summary (collapsible)
        bus_cf = CollapsingFrame(left_panel)
        bus_cf.pack(fill=X, pady=1)

        ## container
        bus_frm = ttk.Frame(bus_cf, padding=5)
        bus_frm.columnconfigure(1, weight=1)
        bus_cf.add(
            child=bus_frm,
            title='Backup Summary',
            bootstyle=SECONDARY)

        ## destination
        lbl = ttk.Label(bus_frm, text='Destination:')
        lbl.grid(row=0, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='destination')
        lbl.grid(row=0, column=1, sticky=EW, padx=5, pady=2)
        self.setvar('destination', 'd:/test/')

        ## last run
        lbl = ttk.Label(bus_frm, text='Last Run:')
        lbl.grid(row=1, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='lastrun')
        lbl.grid(row=1, column=1, sticky=EW, padx=5, pady=2)
        self.setvar('lastrun', '14.06.2021 19:34:43')

        ## files Identical
        lbl = ttk.Label(bus_frm, text='Files Identical:')
        lbl.grid(row=2, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='filesidentical')
        lbl.grid(row=2, column=1, sticky=EW, padx=5, pady=2)
        self.setvar('filesidentical', '15%')

        ## section separator
        sep = ttk.Separator(bus_frm, bootstyle=SECONDARY)
        sep.grid(row=3, column=0, columnspan=2, pady=10, sticky=EW)

        ## properties button
        _func = lambda: Messagebox.ok(message='Changing properties')
        bus_prop_btn = ttk.Button(
            master=bus_frm,
            text='Properties',
            image='properties-dark',
            compound=LEFT,
            command=_func,
            bootstyle=LINK
        )
        bus_prop_btn.grid(row=4, column=0, columnspan=2, sticky=W)

        ## add to backup button
        _func = lambda: Messagebox.ok(message='Adding to backup')
        add_btn = ttk.Button(
            master=bus_frm,
            text='Add to backup',
            image='add-to-backup-dark',
            compound=LEFT,
            command=_func,
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=0, columnspan=2, sticky=W)

    def init_backup_status_CollapsingFrame(self, left_panel):
        # backup status (collapsible)
        status_cf = CollapsingFrame(left_panel)
        status_cf.pack(fill=BOTH, pady=1)

        status_frm = ttk.Frame(status_cf, padding=10)
        status_frm.columnconfigure(1, weight=1)
        status_cf.add(
            child=status_frm,
            title='Backup Status',
            bootstyle=SECONDARY
        )
        ## progress message
        lbl = ttk.Label(
            master=status_frm,
            textvariable='prog-message',
            font='Helvetica 10 bold'
        )
        lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        self.setvar('prog-message', 'Backing up...')

        ## progress bar
        pb = ttk.Progressbar(
            master=status_frm,
            variable='prog-value',
            bootstyle=SUCCESS
        )
        pb.grid(row=1, column=0, columnspan=2, sticky=EW, pady=(10, 5))
        self.setvar('prog-value', 71)

        ## time started
        lbl = ttk.Label(status_frm, textvariable='prog-time-started')
        lbl.grid(row=2, column=0, columnspan=2, sticky=EW, pady=2)
        self.setvar('prog-time-started', 'Started at: 14.06.2021 19:34:56')

        ## time elapsed
        lbl = ttk.Label(status_frm, textvariable='prog-time-elapsed')
        lbl.grid(row=3, column=0, columnspan=2, sticky=EW, pady=2)
        self.setvar('prog-time-elapsed', 'Elapsed: 1 sec')

        ## time remaining
        lbl = ttk.Label(status_frm, textvariable='prog-time-left')
        lbl.grid(row=4, column=0, columnspan=2, sticky=EW, pady=2)
        self.setvar('prog-time-left', 'Left: 0 sec')

        ## section separator
        sep = ttk.Separator(status_frm, bootstyle=SECONDARY)
        sep.grid(row=5, column=0, columnspan=2, pady=10, sticky=EW)

        ## stop button
        _func = lambda: Messagebox.ok(message='Stopping backup')
        btn = ttk.Button(
            master=status_frm,
            text='Stop',
            image='stop-backup-dark',
            compound=LEFT,
            command=_func,
            bootstyle=LINK
        )
        btn.grid(row=6, column=0, columnspan=2, sticky=W)

        ## section separator
        sep = ttk.Separator(status_frm, bootstyle=SECONDARY)
        sep.grid(row=7, column=0, columnspan=2, pady=10, sticky=EW)

        # current file message
        lbl = ttk.Label(status_frm, textvariable='current-file-msg')
        lbl.grid(row=8, column=0, columnspan=2, pady=2, sticky=EW)
        self.setvar('current-file-msg', 'Uploading: d:/test/settings.txt')

    def init_other_CollapsingFrame(self, left_panel):
        # logo
        lbl = ttk.Label(left_panel, image='logo', style='bg.TLabel')
        lbl.pack(side='bottom')

    def init_right_panel(self):
        # right panel
        right_panel = ttk.Frame(self, padding=(2, 1))
        right_panel.pack(side=RIGHT, fill=BOTH, expand=YES)

        self.init_file_input(right_panel)
        self.init_Treeview(right_panel)
        self.init_scrolling_text_output(right_panel)

    def init_file_input(self, right_panel):
        ## file input
        browse_frm = ttk.Frame(right_panel)
        browse_frm.pack(side=TOP, fill=X, padx=2, pady=1)
        self.file_entry = ttk.Entry(browse_frm, textvariable='folder-path')
        self.file_entry.pack(side=LEFT, fill=X, expand=YES)

        btn = ttk.Button(
            master=browse_frm,
            image='opened-folder',
            bootstyle=(LINK, SECONDARY),
            command=self.get_directory
        )
        btn.pack(side=RIGHT)

    def init_Treeview(self, right_panel):
        ## Treeview
        self.tv = ttk.Treeview(right_panel, show='headings', height=5)
        self.tv.configure(columns=(
            'name', 'state', 'last-modified',
            'last-run-time', 'size'
        ))
        self.tv.column('name', width=150, stretch=True)

        for col in ['last-modified', 'last-run-time', 'size']:
            self.tv.column(col, stretch=False)

        for col in self.tv['columns']:
            self.tv.heading(col, text=col.title(), anchor=W)

        self.tv.pack(fill=X, pady=1)

    def init_scrolling_text_output(self, right_panel):
        ## scrolling text output
        scroll_cf = CollapsingFrame(right_panel)
        scroll_cf.pack(fill=BOTH, expand=YES)

        output_container = ttk.Frame(scroll_cf, padding=1)
        _value = 'Log: Backing up... [Uploading file: D:/sample_file_35.txt]'
        self.setvar('scroll-message', _value)
        st = ScrolledText(output_container)
        st.pack(fill=BOTH, expand=YES)
        scroll_cf.add(output_container, textvariable='scroll-message')

        # seed with some sample data

        ## starting sample directory
        self.file_entry.insert(END, 'D:/text/myfiles/top-secret/samples/')


    def get_directory(self):
        """Open dialogue to get directory and update variable"""
        self.update_idletasks()
        d = askdirectory()
        if d:
            self.setvar('folder-path', d)


