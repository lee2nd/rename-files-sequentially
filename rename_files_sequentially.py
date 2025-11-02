import os

_src = r"G:\其他電腦\Frank MSI Laptop V1\照片(準備棄用)\8. 倉鼠\白白"

for i, filename in enumerate(os.listdir(_src)):
    filename_lower = filename.lower()
    if filename_lower.endswith(".jpg") or filename_lower.endswith(".png"):
        _ext = os.path.splitext(filename_lower)[1]
        new_name = f"{str(i).zfill(3)}{_ext}"
        old_path = os.path.join(_src, filename)
        new_path = os.path.join(_src, new_name)
        print(f"Renaming: {old_path} → {new_path}")
        os.rename(old_path, new_path)
