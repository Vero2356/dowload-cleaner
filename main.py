import os
import shutil
# rules for choosing right file to put something in it
rules = {
    "Pictures" : [".jpg", ".png", ".gif", ".svg", ".raw"],
    "video" : [".mp4"],
    "Audio" : [".wav", ".mp3"],
    "Documents" : [".pdf", ".docx", ".pptx", ".xlsx", ".potx"],
    "Archives" : [".zip"],
    "Installers" : [".exe", ".iso"],
    "Web" : [".php"],
    "Specialized" : [".drawio", ".ggb", ".mcworld", ".iq"],
}
print (os.getcwd()) # where is this file running

os.chdir(r'C:\Users\pbrav\Downloads')

print (os.getcwd())
# saving the whole every file into one giant string gonna need spliting
files = os.listdir()

print(f"Found {len(files)} files")

for file in files:
    if os.path.isdir(file):
        continue
    
    if file == "main.py":
        continue

    filename, extension = os.path.splitext(file)
    
    extension = extension.lower()

    if not extension:
        continue

    found = False
    for folder_name, ext_list in rules.items():
        if extension in ext_list:

            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"✨ Vytvářím novou složku: {folder_name}")

            try:
                destination = os.path.join(folder_name, file)
                if not os.path.exists(destination):
                    shutil.move(file, destination)
                    print(f"✅ {file} -> {folder_name}")
                else:
                    print(f"⚠️ Soubor {file} už ve složce {folder_name} je.")
            except Exception as e:
                print(f"❌ Chyba u {file}: {e}")

            found = True
            break

print("\n🏁 Hotovo! Vše roztříděno.")
                