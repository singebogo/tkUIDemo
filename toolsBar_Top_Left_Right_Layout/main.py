import ttkbootstrap as ttk
import ctypes
from src.gui.gui import ToolsBar_Top_Left_Right_Layout
from src.utils.trans_imges import pic_transform
from pathlib import Path


class App(ttk.Window):

    def __init__(self):
        super().__init__()

        self.PATH = Path(__file__).parent / 'src' / 'assets'

        img_data = pic_transform(self.PATH / 'logs.png')
        self.title('toolsBar_Top_Left_Right_Layout-singebogo@163.com')
        self.tk.call("wm", "iconphoto", self._w, ttk.PhotoImage(data=img_data))
        self.resizable(False, False)

        # 告诉操作系统使用程序自身的dpi适配
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # 获取屏幕的缩放因子
        ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        # 设置程序缩放
        self.tk.call('tk', 'scaling', ScaleFactor / 75)

        self.place_window_center()

        self.init_data()

    def place_window_center(self):
        """Position the toplevel in the center of the screen. Does not
        account for titlebar height."""
        self.update_idletasks()
        w_height = self.winfo_height()
        w_width = self.winfo_width()
        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - w_width) // 5
        ypos = (s_height - w_height) // 5
        self.geometry(f'+{xpos}+{ypos}')

    def init_data(self):
        # hotkey win+F10
        pass

if __name__ == '__main__':
    app = App()
    ToolsBar_Top_Left_Right_Layout(app)
    app.mainloop()
