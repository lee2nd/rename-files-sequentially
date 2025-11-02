import os
import glob

base_dir = r"G:\其他電腦\Frank MSI Laptop V1\照片(準備棄用)\1. Family"
path_lst = [f for f in glob.glob(os.path.join(base_dir, "*")) if os.path.isdir(f)]

for folder in path_lst:
    print(f"\n📂 Processing folder: {folder}")

    file_list = sorted(os.listdir(folder))  # 先排序確保順序固定
    img_i = 0  # 圖片計數
    vid_i = 0  # 影片計數

    for filename in file_list:
        filename_lower = filename.lower()
        old_path = os.path.join(folder, filename)

        # 🖼️ 圖片類
        if filename_lower.endswith((".jpg", ".jpeg", ".png")):
            new_ext = ".jpg"
            new_name = f"{str(img_i).zfill(3)}{new_ext}"
            img_i += 1

        # 🎬 影片類
        elif filename_lower.endswith((".mp4", ".mov")):
            new_ext = ".mp4"
            new_name = f"{str(vid_i).zfill(3)}{new_ext}"
            vid_i += 1

        else:
            continue  # 其他檔案略過

        new_path = os.path.join(folder, new_name)

        print(f"Renaming: {old_path} → {new_path}")
        os.rename(old_path, new_path)
