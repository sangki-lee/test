import tkinter as tk
from tkinter import ttk

def show_greeting():
    name = name_entry.get()
    if name:
        result_label.config(text=f"안녕하세요 {name}님")
    else:
        result_label.config(text="이름을 입력해주세요")

# 메인 윈도우 생성
root = tk.Tk()
root.title("인사 프로그램")
root.geometry("400x200")
root.resizable(False, False)

# 입력 레이블
input_label = tk.Label(root, text="이름을 입력하세요:", font=("Arial", 12))
input_label.pack(pady=10)

# 입력 필드
name_entry = tk.Entry(root, font=("Arial", 12), width=20)
name_entry.pack(pady=5)
name_entry.bind('<Return>', lambda e: show_greeting())  # Enter 키 바인딩

# 확인 버튼
confirm_button = tk.Button(root, text="확인", font=("Arial", 12), command=show_greeting)
confirm_button.pack(pady=10)

# 결과 출력 레이블
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=20)

# 윈도우 실행
root.mainloop()
