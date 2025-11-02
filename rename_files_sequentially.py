import os

# 改名版 000, 001, 002,...
_src = r"G:\其他電腦\Frank MSI Laptop V1\照片(準備棄用)\7. 面試 & 培訓\AWS 培訓"

for i, filename in enumerate(os.listdir(_src)):
    filename_lower = filename.lower()
    if filename_lower.endswith(".jpg") or filename_lower.endswith(".png") or filename_lower.endswith(".jpeg"):
        _ext = os.path.splitext(filename_lower)[1]
        new_name = f"{str(i).zfill(3)}.jpg"
        old_path = os.path.join(_src, filename)
        new_path = os.path.join(_src, new_name)
        print(f"Renaming: {old_path} → {new_path}")
        os.rename(old_path, new_path)

# 不改名版
_src = r"G:\其他電腦\Frank MSI Laptop V1\照片(準備棄用)\7. 面試 & 培訓\AWS 培訓"

for filename in os.listdir(_src):
    # 取得副檔名（不分大小寫）
    name, ext = os.path.splitext(filename)
    if ext.lower() in [".jpg", ".png", ".jpeg"]:
        old_path = os.path.join(_src, filename)
        new_path = os.path.join(_src, name + ".jpg")

        if old_path != new_path:
            print(f"Renaming: {old_path} → {new_path}")
            os.rename(old_path, new_path)
