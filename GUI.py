import tkinter as tk
from tkinter import ttk

def start_spider():
    # 获取用户选择的题目难度
    difficulty = difficulty_combobox.get()
    # 执行筛选操作
    # ...

root = tk.Tk()
root.title("题目筛选")

# 创建一个下拉列表让用户选择题目难度
difficulty_combobox = ttk.Combobox(root)
difficulty_combobox['values'] = ('暂无评定', '入门', '普及-', '普及/提高-', '普及+/提高', '提高+/省选-', '省选/NOI-', 'NOI/NOI+/CTSC')
difficulty_combobox.pack()

# 创建一个按钮，点击按钮时执行筛选操作
start_button = tk.Button(root, text="开始筛选", command=start_spider)
start_button.pack()

root.mainloop()