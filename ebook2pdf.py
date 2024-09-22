import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cv2
import numpy as np
import pyautogui
import time
import os
import datetime
from PIL import ImageChops, Image
import win32gui
import win32process
import pygame

# グローバル変数の定義
refPt = []
cropping = False
done = False

def get_active_window_info():
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    return title

def screenshot(title, button, span, area):
    span = float(span)
    check_num = 0
    p = 0
    # (この間にスクショを取得するウィンドウをアクティブにする)
    while True:
        time.sleep(1)
        active_window = get_active_window_info()
        if "電子書籍スキャナー" not in active_window:
            break
    time.sleep(3)

    # ページ数分スクリーンショットをとる
    prev_image = None
    image_list = []

    while True:
        p += 1
        # スクリーンショット取得・保存処理
        # キャプチャ範囲： 左上のx座標, 左上のy座標, 幅, 高さ
        s = pyautogui.screenshot(region=(area[0], area[1], area[2] - area[0], area[3] - area[1]))

        # 画像を保存する前に、前の画像と比較
        current_image = s

        if prev_image is not None:
            # 画像が同じかどうか比較
            diff = ImageChops.difference(prev_image, current_image)
            if not diff.getbbox():
                # 画像が同一である場合、ループを終了
                check_num += 1
                if check_num > 10:
                    break
                else:
                    continue

        # 画像をリストに追加
        image_list.append(current_image.convert('RGB'))
        prev_image = current_image

        # ページめくりのためのキー押下
        if button == "left_click":
            pyautogui.click()
        else:
            pyautogui.keyDown(button)
            pyautogui.keyUp(button)

        # 次のスクリーンショットまで待機
        time.sleep(span)

    # すべての画像をPDFに保存
    if image_list:
        pdf_filename = title + ".pdf"
        image_list[0].save(pdf_filename, save_all=True, append_images=image_list[1:])
    else:
        messagebox.showerror("エラー", "画像がありません。")
        return False

    return True

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping, image_copy, dark_image, done

    # 左ボタンが押されたとき
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.clear()
        refPt.append((x, y))
        cropping = True

    # マウスが移動したとき
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            image_copy = dark_image.copy()
            cv2.rectangle(image_copy, refPt[0], (x, y), (255, 255, 255), 2)
            # 指定された領域を明るくする
            x0, y0 = refPt[0]
            x1, y1 = x, y
            if x0 > x1:
                x0, x1 = x1, x0
            if y0 > y1:
                y0, y1 = y1, y0
            bright_region = image[y0:y1, x0:x1]
            image_copy[y0:y1, x0:x1] = bright_region
            cv2.imshow("image", image_copy)

    # 左ボタンが離されたとき
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False

        # 指定された領域を明るくする
        x0, y0 = refPt[0]
        x1, y1 = refPt[1]
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        bright_region = image[y0:y1, x0:x1]
        image_copy[y0:y1, x0:x1] = bright_region
        cv2.rectangle(image_copy, refPt[0], refPt[1], (255, 255, 255), 2)
        cv2.imshow("image", image_copy)

        done = True

def select_roi():
    global image, image_copy, dark_image, done

    # スクリーンショットを取得
    screenshot = pyautogui.screenshot()

    # スクリーンショットをOpenCV形式に変換
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    if image is None:
        print("スクリーンショットの取得に失敗しました。")
        return None
    else:
        # 画像を暗くする
        dark_image = cv2.addWeighted(image, 0.3, np.zeros(image.shape, image.dtype), 0.7, 0)
        image_copy = dark_image.copy()
        done = False

        # ウィンドウの名前を設定
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", click_and_crop)

        while not done:
            cv2.imshow("image", image_copy)
            cv2.waitKey(1)
        
        cv2.destroyAllWindows()

        if len(refPt) == 2:
            x0, y0 = refPt[0]
            x1, y1 = refPt[1]
            if x0 > x1:
                x0, x1 = x1, x0
            if y0 > y1:
                y0, y1 = y1, y0
            return (x0, y0, x1, y1)
        else:
            return None

def area_designation():
    # 範囲選択を行い、選択された範囲の座標を取得
    selected_region = select_roi()
    if selected_region:
        return selected_region
    else:
        print("範囲が選択されませんでした。")

def execute():
    pygame.mixer.init()
    try:
        area = area_designation()
        if area is None:
            raise Exception("範囲が選択されませんでした。")

        success = screenshot(book_title.get(), page_turn.get(), interval_time.get(), area)
        if not success:
            raise Exception("スクリーンショットの取得に失敗しました。")
        
        status_label.config(text="保存完了！")
        if chime_var.get():
            wave_obj = pygame.mixer.Sound("sound_file/hato.wav")
            play_obj = wave_obj.play()
    except Exception as e:
        messagebox.showerror("エラー", f"エラーが発生しました: {e}")

# メインウィンドウの作成
root = tk.Tk()
root.title("電子書籍スキャナー")
root.geometry("400x350")

# 本のタイトル入力
tk.Label(root, text="本のタイトル：").place(x=20, y=20)
book_title = tk.Entry(root, width=40)
book_title.place(x=100, y=20)

# ページめくりオプション
tk.Label(root, text="ページめくり：").place(x=20, y=60)
page_turn = tk.StringVar()
page_turn.set("left")
options = [("←キー", "left"), ("→キー", "right"), ("スペース→キー", "space"), ("左クリック", "left_click")]
for i, (display, value) in enumerate(options):
    tk.Radiobutton(root, text=display, variable=page_turn, value=value).place(x=100, y=60 + i * 30)

# 取得間隔時間
tk.Label(root, text="取得間隔時間：").place(x=20, y=210)
interval_time_var = tk.StringVar(value="1")
interval_time = tk.Entry(root, width=10, textvariable=interval_time_var)
interval_time.place(x=150, y=210)
tk.Label(root, text="(sec)").place(x=210, y=210)

chime_var = tk.BooleanVar()
chime_check = tk.Checkbutton(root, text="終了後チャイムを鳴らす", variable=chime_var)
chime_check.place(x=50, y=250)

# 実行ボタン
execute_button = tk.Button(root, text="実行", command=execute)
execute_button.place(x=150, y=280, width=100, height=30)

# 状態表示ラベル
status_label = tk.Label(root, text="")
status_label.place(x=160, y=320)

root.mainloop()
