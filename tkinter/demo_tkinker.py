import tkinter as tk
import pandas as pd
import random
from matplotlib.backends.backend_tkagg import (
FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from tkinter.messagebox import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib import animation


class load_data(object):
    def __init__(self):
        self.xValues = []
        self.yValues = []
        self.lineName = []
        self.lineColors = []
        self.xMin = 0
        self.xMax = 0
        self.yMax = 0
        self.yMin = 0

    def get_yMin(self):
        yMin = min([min(row) for row in self.yValues])
        return yMin

    def get_yMax(self):
        yMax = max([max(row) for row in self.yValues])
        return yMax

    def get_yNum(self):
        return len(self.yValues[0])

    def get_lineNum(self):
        return len(self.lineName)

    def get_xNum(self):
        return len(self.xValues)

    def get_xStart(self):
        return self.xValues[0]

    def get_xEnd(self):
        return self.xValues[-1]

    # 数据预处理
    def preprocess(self):
        self.xValues = [int(year.split('年')[0]) for year in self.xValues]
        # print(tmpList)
        self.xValues.reverse()
        self.xMin = self.get_xStart()
        self.xMax = self.get_xEnd()
        self.yMax = self.get_yMax()
        self.yMin = self.get_yMin()
        self.lineColors = ['#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(len(self.lineName))]
        # 使数据年份从早至今
        for num in range(self.get_lineNum()):
            self.yValues[num].reverse()
        self.data_dict = dict(zip(self.lineName, self.yValues))
        self.data_dict['time'] = self.xValues
        self.dataset = pd.DataFrame(self.data_dict)



class TestGui(object):
    def __init__(self, init_window_name):
        self.file_input_dirs = None  # 存放文件地址变量
        self.readyReadData = False   # 是否读入数据
        self.init_window_name = init_window_name
        self.init_window_name.title('图表生成')  # 设置窗口标题
        self.init_window_name.geometry('1600x1400')  # 设置窗口大小
        self.init_window_name.attributes("-topmost", 1)  # tk界面置顶
        for i in range(1, 4):
            window.rowconfigure(i, minsize=50)


        # 创建导入文件功能组件容器
        self.input_frame = tk.Frame(master=self.init_window_name)
        self.input_frame.grid(padx=20, pady=5, row=1, column=0, sticky=tk.W)  # 外间距20px,上下间距0，1行，0(从0开始)列
        self.set_x = tk.Frame(master=self.init_window_name)  # 创建存放x轴组件的容器
        self.set_x.grid(padx=20, pady=0, row=2, column=0, sticky=tk.W)
        self.set_y = tk.Frame(master=self.init_window_name)  # 创建存放y轴组件的容器
        self.set_y.grid(padx=20, pady=0, row=3, column=0, sticky=tk.W)
        self.set_title = tk.Frame(master=self.init_window_name)  # 创建存放图像标题的容器
        self.set_title.grid(padx=20, pady=0, row=4, column=0, sticky=tk.W)
        self.set_LineNum = tk.Frame(master=self.init_window_name)  # 创建存放复选曲线组件的容器
        self.set_LineNum.grid(padx=20, pady=0, row=5, column=0, sticky=tk.W)
        self.canvas_frame = tk.Frame(master=self.init_window_name)  # 创建存放日志组件的容器
        self.canvas_frame.grid(padx=20, pady=0, row=6, column=0, sticky=tk.W)
        self.runs_button_frame = tk.Frame(self.init_window_name)  # 创建存放日志组件的容器
        self.runs_button_frame.grid(padx=20, pady=0, row=7, column=0, sticky=tk.W)


        # 导入提示
        self.file_input_title = tk.Label(self.input_frame, text="导入文件地址", font=('SimHei', 15))
        self.file_input_title.grid(padx=20, pady=0, row=0, column=0, sticky=tk.W)
        # 导入路径文本框
        self.file_input_entry = tk.Entry(self.input_frame, font=('SimHei', 12), width=50, )
        self.file_input_entry.grid(padx=0, pady=0, row=0, column=1)
        # 导入文件按钮
        self.file_input_button = tk.Button(self.input_frame, text="选择文件", font=('SimHei', 12), width=15, fg="white",
                                           bg="#1E90FF", command=self.file_input_path)
        self.file_input_button.grid(padx=10, pady=0, row=0, column=2, sticky=tk.W)
        # 重置参数
        self.reset_button = tk.Button(self.input_frame, text="重置图表参数", font=('SimHei', 12), width=15, fg="white",
                                           bg="#1E90FF", command=self.update_default_ui)
        self.reset_button.grid(padx=10, pady=0, row=0, column=3, sticky=tk.W)

        # xMin文字提示
        self.xMin_text = tk.Label(self.set_x, text="xMin:", font=('SimHei', 15))
        self.xMin_text.grid(padx=20, pady=0, row=1, column=0, sticky=tk.W)
        # xMin输入
        self.xMin_spinbox = tk.Spinbox(self.set_x, from_=dataShow.xMin, to=2024, width=10)
        self.xMin_spinbox.grid(padx=20, pady=0, row=1, column=1, sticky=tk.W)
        # xMax文字提示
        self.xMax_text = tk.Label(self.set_x, text="xMax:", font=('SimHei', 15))
        self.xMax_text.grid(padx=20, pady=0, row=1, column=3, sticky=tk.W)
        # xMax输入
        self.xMax_spinbox = tk.Spinbox(self.set_x, from_=dataShow.xMax, to=1000000, width=10)
        self.xMax_spinbox.grid(padx=20, pady=0, row=1, column=4, sticky=tk.W)
        # Stride间隔
        self.xStride = tk.Label(self.set_x, text="xStride:", font=('SimHei', 15))
        self.xStride.grid(padx=20, pady=0, row=1, column=5, sticky=tk.W)
        # Stride输入
        self.xStride_spinbox = tk.Spinbox(self.set_x, from_=0, to=10, width=10)
        self.xStride_spinbox.grid(padx=20, pady=0, row=1, column=6, sticky=tk.W)
        # xLabel文字
        self.xLabel_text = tk.Label(self.set_x, text="xLabel输入:", font=('SimHei', 15))
        self.xLabel_text.grid(padx=30, pady=0, row=1, column=7, sticky=tk.W)
        # title输入
        self.xLabel_entry = tk.Entry(self.set_x, font=('SimHei', 15), width=10)
        self.xLabel_entry.grid(padx=0, pady=0, row=1, column=8)

        # yMin文字提示
        self.yMin_text = tk.Label(self.set_y, text="yMin:", font=('SimHei', 15))
        self.yMin_text.grid(padx=20, pady=0, row=1, column=0, sticky=tk.W)
        # yMin输入
        self.yMin_spinbox = tk.Spinbox(self.set_y, from_=dataShow.yMin, to=2024, width=10)
        self.yMin_spinbox.grid(padx=20, pady=0, row=1, column=1, sticky=tk.W)
        # yMax文字提示
        self.yMax_text = tk.Label(self.set_y, text="yMax:", font=('SimHei', 15))
        self.yMax_text.grid(padx=20, pady=0, row=1, column=3, sticky=tk.W)
        # yMax输入
        self.yMax_spinbox = tk.Spinbox(self.set_y, from_=dataShow.yMax, to=1000000, width=10)
        self.yMax_spinbox.grid(padx=20, pady=0, row=1, column=4, sticky=tk.W)
        # yStride间隔
        self.yStride = tk.Label(self.set_y, text="yStride:", font=('SimHei', 15))
        self.yStride.grid(padx=20, pady=0, row=1, column=5, sticky=tk.W)
        # yStride输入
        self.yStride_value = tk.StringVar()
        self.stride_list = ['等距', '不等距']
        self.yStride_value.set(0)  # 设置默认值 '0'
        # 单选组件参数介绍 text=勾选框文本, variable=赋值对象, value=勾选后的值
        self.choose_yStride_one = tk.Radiobutton(self.set_y, text=self.stride_list[0],
                                             variable=self.yStride_value, value=self.stride_list[0], font=('行楷', 12))
        self.choose_yStride_one.grid(padx=0, pady=0, row=1, column=6)
        self.choose_yStride_two = tk.Radiobutton(self.set_y, text=self.stride_list[1],
                                             variable=self.yStride_value, value=self.stride_list[1], font=('行楷', 12))
        self.choose_yStride_two.grid(padx=0, pady=0, row=1, column=7)
        # yLabel文字
        self.yLabel_text = tk.Label(self.set_y, text="yLabel输入:", font=('SimHei', 15))
        self.yLabel_text.grid(padx=20, pady=0, row=1, column=8, sticky=tk.W)
        # yLabel输入
        self.yLabel_entry = tk.Entry(self.set_y, font=('SimHei', 15), width=10)
        self.yLabel_entry.grid(padx=10, pady=0, row=1, column=9)

        # title文字
        self.title_text = tk.Label(self.set_title, text="图表标题设置:", font=('SimHei', 15))
        self.title_text.grid(padx=20, pady=0, row=1, column=0, sticky=tk.W)
        # title输入
        self.title_entry = tk.Entry(self.set_title, font=('SimHei', 15), width=50)
        self.title_entry.grid(padx=0, pady=0, row=1, column=1)

        # 文字提示
        self.line_text = tk.Label(self.set_LineNum, text="设置展示的曲线:", font=('SimHei', 15))
        self.line_text.grid(padx=20, pady=0, row=1, column=0, sticky=tk.W)

        # Listbox多选模式
        self.listbox = tk.Listbox(self.set_LineNum, selectmode=tk.MULTIPLE, xscrollcommand=True, width=30, height=7)
        self.listbox.grid(padx=0, pady=10, row=1, column=1)
        # 设置全选按钮
        self.lineName_selectAll_button = tk.Button(self.set_LineNum, text="全选", font=('SimHei', 12), width=8,
                                                   # fg="white",bg="#1E90FF",
                                                   command=self.LineName_selectAll)
        self.lineName_selectAll_button.grid(padx=10, pady=10, row=1, column=2, sticky=tk.W)
        # 设置全不选按钮
        self.lineName_selectAll_button = tk.Button(self.set_LineNum, text="清除选项", font=('SimHei', 12), width=8,
                                                   # fg="white", bg="#1E90FF",
                                                   command=self.LineName_selectNone)
        self.lineName_selectAll_button.grid(padx=10, pady=10, row=1, column=3, sticky=tk.W)

        # 创建画布
        # self.animation_canvas = tk.Canvas(self.canvas_frame, width=1500, height=800, bg='white')
        # self.animation_canvas.grid(padx=10, pady=10, row=1, column=0, sticky=tk.W)
        # self.animation_canvas.create_rectangle(50, 50, 150, 150, fill='blue')

        # 创建生成导出按钮
        self.show_animation_button = tk.Button(self.runs_button_frame, text="生成动态曲线", font=('SimHei', 16), width=20, height=2,
                                                   fg="white",
                                                   bg="#1E90FF", command=self.set_line_animation)
        self.show_animation_button.grid(padx=10, pady=10, row=1, column=0, sticky=tk.W)
        self.Export_animation_button = tk.Button(self.runs_button_frame, text="导出视频", font=('SimHei', 16), width=20, height=2,
                                       fg="white",
                                       bg="#1E90FF", command=self.save_animation)
        self.Export_animation_button.grid(padx=10, pady=10, row=1, column=1, sticky=tk.W)
        self.show_line_button = tk.Button(self.runs_button_frame, text="生成折线图", font=('SimHei', 16), width=20, height=2,
                                       fg="white",
                                       bg="#1E90FF", command=self.show_line)
        self.show_line_button.grid(padx=10, pady=10, row=1, column=2, sticky=tk.W)
        self.Export_line_button = tk.Button(self.runs_button_frame, text="导出折线图", font=('SimHei', 16), width=20,
                                          height=2,
                                          fg="white",
                                          bg="#1E90FF", command=self.save_picture)
        self.Export_line_button.grid(padx=10, pady=10, row=1, column=3, sticky=tk.W)


    def file_input_path(self):
        """ 上传文件路径选择 """
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls")])
        self.file_input_dirs = file_path
        if file_path:
            if file_path.lower().endswith('.xls'):
                sheet_name = 'Sheet1'
                index_col = 0
                df = pd.read_excel(file_path, sheet_name=sheet_name, index_col=index_col)
                dataShow.lineName = df.index.tolist()   # 各曲线名称
                dataShow.yValues = df.values.tolist()   # 获取转置后的列数据作为 y 轴数据
                dataShow.xValues = df.columns.tolist()  # 获取行索引作为 x 轴数据
                dataShow.preprocess()                   # 数据预处理，将年份string转为int
                self.readyReadData = True
                self.update_default_ui()

    def param_print(self):
        """ 检查是否导入有效数据 """
        # 如果输入地址和文件选择按钮的值都为None,则提示
        if len(self.file_input_entry.get().strip()) < 1 and self.file_input_dirs is None:
            messagebox.showwarning(title='警告', message='必须输入或选择文件地址!')
            return False
        # 如果输入地址为空则选用文件选择按钮的值
        if len(self.file_input_entry.get().strip()) > 1:
            file_path = self.file_input_entry.get().strip()
        else:
            file_path = self.file_input_dirs
        # file_path_content = f"文件地址为：{file_path}"

    def LineName_selectAll(self):
        """ 选择展示所有曲线 """
        self.listbox.selection_set(0, tk.END)

    def LineName_selectNone(self):
        """ 选择不展示所有曲线 """
        self.listbox.selection_clear(0, tk.END)

    def update_default_ui(self):
        """ 导入数据后更新选项 """
        if self.readyReadData == False:
            showinfo('提示', '请导入数据')
            return
        self.file_input_entry.delete(0, tk.END)  # 将文本输入组件的信息删除
        self.file_input_entry.insert(tk.END, self.file_input_dirs)  # 在文本输入组件，插入文件导入按钮的字符串地址
        self.listbox.delete(0, tk.END)
        for lineName in dataShow.lineName:
            self.listbox.insert(tk.END, lineName)
        self.LineName_selectAll()
        self.yMin_spinbox.delete(0, tk.END)
        self.yMax_spinbox.delete(0, tk.END)
        self.xMin_spinbox.delete(0, tk.END)
        self.xMax_spinbox.delete(0, tk.END)
        self.yMin_spinbox.insert(tk.END, dataShow.yMin*0.7)
        self.yMax_spinbox.insert(tk.END, dataShow.yMax*1.1)
        self.xMin_spinbox.insert(tk.END, dataShow.xMin)
        self.xMax_spinbox.insert(tk.END, dataShow.xMax)
        self.yStride_value.set('不等距')
        self.xStride_spinbox.delete(0, tk.END)
        self.xStride_spinbox.insert(tk.END, 1)

    def test(self):
        selected_indices = self.listbox.curselection()
        for i in selected_indices:
            print(i)
        xlim_left = int(self.xMin_spinbox.get())
        xlim_right = int(self.xMax_spinbox.get())
        ylim_left = int(float(self.yMin_spinbox.get()))
        ylim_right = int(float(self.yMax_spinbox.get()))
        print(xlim_left, xlim_right,ylim_right,ylim_left)
        print(type(xlim_right))
        attributes = [attr for attr in dir(test_gui) if not callable(getattr(test_gui, attr))]
        methods = [method for method in dir(test_gui) if callable(getattr(test_gui, method))]
        print(attributes)
        print(methods)

    def set_line_animation(self):
        if self.readyReadData == False:
            showinfo('提示', '请导入数据')
            return
        if self.check_setui() == False:
            return
        fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 如果要显示中文字体,则在此处设为：SimHei
        plt.rcParams['axes.unicode_minus'] = False  # 显示负号
        if hasattr(self, "animation_canvas") and self.animation_canvas is not None:
            self.animation_canvas.get_tk_widget().destroy()

        def line_animation(current_year):
            if current_year == dataShow.xMax:
                lineanimation.event_source.stop()
            ax.clear()
            yearsNum = current_year - dataShow.xMin + 1
            x = dataShow.xValues
            y = dataShow.yValues

            selected_Lines = self.listbox.curselection()
            title_text = self.title_entry.get()
            yLabel_text = self.yLabel_entry.get()
            xLabel_text = self.xLabel_entry.get()
            xlim_left = int(self.xMin_spinbox.get())
            xlim_right = int(self.xMax_spinbox.get())
            ylim_left = int(float(self.yMin_spinbox.get()))
            ylim_right = int(float(self.yMax_spinbox.get()))
            yStride_text = self.yStride_value.get()
            xStrid = int(self.xStride_spinbox.get())

            for i in selected_Lines:
                ax.plot(x[:yearsNum], y[i][:yearsNum], label=dataShow.lineName[i], color=dataShow.lineColors[i], linestyle='-', marker='o')
                ax.scatter(x[yearsNum - 1], y[i][yearsNum - 1], color=dataShow.lineColors[i], edgecolor='black', s=100, lw=1, zorder=4)
                str = dataShow.lineName[i] + ':{:,.0f}'.format(y[i][yearsNum - 1])
                ax.text(x[yearsNum - 1]+0.05, y[i][yearsNum - 1]*1.05, str, size=10, c=dataShow.lineColors[i], va='top', ha='left', fontweight='bold')

            ax.spines['top'].set_visible(False)  # 去掉上边框
            ax.spines['right'].set_visible(False)  # 去掉右边框
            plt.grid(linestyle="--")
            ax.set_xticks(np.arange(dataShow.xMin, dataShow.xMax + 1, xStrid))
            ax.set_xlim(left=xlim_left, right=xlim_right)
            ax.set_ylim(ymin=ylim_left * 0.7, ymax=ylim_right * 1.1)

            def forword(x):
                return x ** (1 / 2)

            def inverse(x):
                return x ** 1

            if yStride_text == '不等距':
                ax.set_yscale('function', functions=(forword, inverse))

            ax.grid(axis='both', color='gray', lw=1, alpha=.6, ls='--')
            ax.spines['top'].set_visible(False)  # 去掉上边框
            ax.spines['right'].set_visible(False)  # 去掉右边框
            plt.grid(linestyle="--")
            ax.set_xlabel(xLabel_text)
            ax.set_ylabel(yLabel_text)
            ax.set_title(title_text)
            ax.text(.1, .4, current_year, transform=ax.transAxes, color='gray', alpha=.4, size=120,
                    fontfamily="Franklin Gothic Book")
            ax.legend()

        lineanimation = animation.FuncAnimation(fig, line_animation, frames=np.arange(dataShow.xMin, dataShow.xMax + 1), interval=300)
        self.animation_canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.animation_canvas.draw()
        self.canvas_frame.config(width=1400, height=500)
        self.animation_canvas.get_tk_widget().config(width=1400, height=600)
        self.animation_canvas.get_tk_widget().pack()
        self.lineanimation = lineanimation

    def check_setui(self):
        xlim_left = int(self.xMin_spinbox.get())
        xlim_right = int(self.xMax_spinbox.get())
        xStrid = int(self.xStride_spinbox.get())
        ylim_left = int(float(self.yMin_spinbox.get()))
        ylim_right = int(float(self.yMax_spinbox.get()))

        def set_y_default():
            self.yMin_spinbox.delete(0, tk.END)
            self.yMin_spinbox.insert(tk.END, dataShow.yMin * 0.7)
            self.yMax_spinbox.delete(0, tk.END)
            self.yMax_spinbox.insert(tk.END, dataShow.yMax * 1.1)
        def set_x_default():
            self.xMin_spinbox.delete(0, tk.END)
            self.xMin_spinbox.insert(tk.END, dataShow.xMin)
            self.xMax_spinbox.delete(0, tk.END)
            self.xMax_spinbox.insert(tk.END, dataShow.xMax)

        if ylim_left < 0 or ylim_right < 0:
            showinfo('错误', '输入y轴坐标不能小于零')
            set_y_default()
            return False
        if ylim_left >= ylim_right:
            showinfo('错误', 'y轴最大值不能小于等于最小值')
            set_y_default()
            return False
        if xlim_left >= xlim_right:
            showinfo('错误', 'x轴最大值不能小于等于最小值')
            set_x_default()
            return False
        if xlim_left < 0 or xlim_right < 0:
            showinfo('错误', '输入x轴坐标不能小于零')
            set_x_default()
            return False
        if xStrid <= 0 or xStrid >= dataShow.get_xNum():
            showinfo('错误', '请检查x轴网格间隔是否设置正确')
            self.xStride_spinbox.delete(0, tk.END)
            self.xStride_spinbox.insert(tk.END, 1)
            return False
        return True

    def show_line(self):
        if self.readyReadData == False:
            showinfo('提示', '请导入数据')
            return
        if self.check_setui() == False:
            return
        fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 如果要显示中文字体,则在此处设为：SimHei
        plt.rcParams['axes.unicode_minus'] = False  # 显示负号
        if hasattr(self, "animation_canvas") and self.animation_canvas is not None:
            self.animation_canvas.get_tk_widget().destroy()
        ax.clear()
        ax.spines['top'].set_visible(False)  # 去掉上边框
        ax.spines['right'].set_visible(False)  # 去掉右边框
        plt.grid(linestyle="--")
        xStrid = int(self.xStride_spinbox.get())
        x = dataShow.xValues
        y = dataShow.yValues
        selected_Lines = self.listbox.curselection()
        for i in selected_Lines:
            ax.plot(x, y[i], label=dataShow.lineName[i], color=dataShow.lineColors[i], linestyle='-', marker='o')

        title_text = self.title_entry.get()
        yLabel_text = self.yLabel_entry.get()
        xLabel_text = self.xLabel_entry.get()
        xlim_left = int(self.xMin_spinbox.get())
        xlim_right = int(self.xMax_spinbox.get())
        ylim_left = int(float(self.yMin_spinbox.get()))
        ylim_right = int(float(self.yMax_spinbox.get()))
        yStride_text = self.yStride_value.get()

        ax.set_xticks(np.arange(dataShow.xMin, dataShow.xMax + 1, xStrid))
        ax.set_xlim(left=xlim_left, right=xlim_right)
        ax.set_ylim(ymin=ylim_left * 0.7, ymax=ylim_right * 1.1)
        def forword(x):
            return x ** (1 / 2)
        def inverse(x):
            return x ** 1

        if yStride_text == '不等距':
            ax.set_yscale('function', functions=(forword, inverse))

        # ax.grid(axis='both', color='gray', lw=1, alpha=.6, ls='--')

        ax.set_xlabel(xLabel_text)
        ax.set_ylabel(yLabel_text)
        ax.set_title(title_text)
        ax.legend()

        self.animation_canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.animation_canvas.draw()
        self.canvas_frame.config(width=1100, height=500)
        self.animation_canvas.get_tk_widget().config(width=1300, height=600)
        self.animation_canvas.get_tk_widget().pack()
        self.figsave = fig

    def save_animation(self):
        if hasattr(self, 'readyReadData') and self.readyReadData == False:
            showinfo('提示', '请导入数据')
            return
        if hasattr(self, 'lineanimation') and self.lineanimation is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".gif",
                                                     filetypes=[("GIF files", "*.gif"), ("All files", "*.*")])
            if file_path:
                # self.lineanimation.save(file_path)
                self.lineanimation.save(file_path)
        else:
            showinfo('提示', '请先生成动态曲线')

    def save_picture(self):
        if hasattr(self, 'readyReadData') and self.readyReadData == False:
            showinfo('提示', '请导入数据')
            return
        if hasattr(self, 'figsave') and self.figsave is not None:
            from tkinter import filedialog

            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("SVG files", "*.svg"),
                                                                ("All files", "*.*")])
            if file_path:
                self.figsave.savefig(file_path)  # 保存图像到指定路径
        else:
            showinfo('提示', '请先生成折线图')

window = tk.Tk()
dataShow = load_data()

test_gui = TestGui(window)

window.mainloop()

