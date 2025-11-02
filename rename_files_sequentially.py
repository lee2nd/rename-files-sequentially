import os

# 改名版 000, 001, 002,...
_src = r"G:\其他電腦\Frank MSI Laptop V1\照片(準備棄用)\9. 貓\貓展"

file_list = sorted(os.listdir(_src))  # 先排序，確保每次一致

img_i = 0  # 圖片編號計數
vid_i = 0  # 影片編號計數

for filename in file_list:
    filename_lower = filename.lower()
    old_path = os.path.join(_src, filename)

    # 🖼️ 處理圖片類
    if filename_lower.endswith((".jpg", ".png", ".jpeg")):
        new_ext = ".jpg"
        new_name = f"{str(img_i).zfill(3)}{new_ext}"
        img_i += 1

    # 🎬 處理影片類
    elif filename_lower.endswith((".mp4", ".mov")):
        new_ext = ".mp4"
        new_name = f"{str(vid_i).zfill(3)}{new_ext}"
        vid_i += 1

    else:
        continue  # 其他副檔名跳過

    new_path = os.path.join(_src, new_name)

    print(f"Renaming: {old_path} → {new_path}")
    os.rename(old_path, new_path)


# 不改名版
_src = r"G:\其他電腦\Frank MSI Laptop V1\照片(準備棄用)\7. 面試 & 培訓\AWS 培訓"

_src = r"G:\其他電腦\Frank MSI Laptop V1\照片(準備棄用)\1. Family"

for filename in os.listdir(_src):
    name, ext = os.path.splitext(filename)
    ext_lower = ext.lower()
    old_path = os.path.join(_src, filename)

    # 1️⃣ 統一圖片格式 → .jpg
    if ext_lower in [".jpg", ".jpeg", ".png"]:
        new_path = os.path.join(_src, name + ".jpg")

    # 2️⃣ 統一影片格式 → .mp4
    elif ext_lower in [".mov", ".mp4"]:
        new_path = os.path.join(_src, name + ".mp4")

    # 3️⃣ 其他副檔名不動
    else:
        continue

    # 避免重複處理同名檔案
    if old_path != new_path:
        print(f"Renaming: {old_path} → {new_path}")
        os.rename(old_path, new_path)
