import os
import shutil  # ファイルの移動やコピーに便利なモジュール

# フォルダの作成
folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"{folder_name} を作成しました！")

# ファイルの作成
file_path = os.path.join(folder_name, "test.txt")
with open(file_path, "w") as file:
    file.write("これは file1.txt の内容です。")

# ファイルの存在確認
if os.path.exists(file_path):
    print(f"{file_path} が存在します！")

# ファイルの移動（shutilを使用）
moved_path = "file1_moved.txt"
shutil.move(file_path, moved_path)
print(f"{file_path} を {moved_path} に移動しました！")

# ファイルの削除
os.remove(moved_path)
print(f"{moved_path} を削除しました！")
