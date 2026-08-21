import os

# مهدی تلخبی
CUSTOM_NAME = "MyConfig"

# نام دقیق فایل فعلی شما در گیت‌هاب
INPUT_FILE = "configsmehdi.txt" 

# نام فایلی که کانفیگ‌های تغییر نام یافته در آن ذخیره می‌شوند
OUTPUT_FILE = "output.txt"

def update_configs():
    if not os.path.exists(INPUT_FILE):
        print(f"File {INPUT_FILE} not found!")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    count = 1
    for line in lines:
        line = line.strip()
        if line and "#" in line:
            base_url = line.split("#")[0]
            new_line = f"{base_url}#{CUSTOM_NAME}-{count}"
            new_lines.append(new_line)
            count += 1
        elif line:
            new_lines.append(line)
            
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

if __name__ == "__main__":
    update_configs()
