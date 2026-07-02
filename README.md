# 🧹 Digitální Uklízečka (Digital Cleaner)

Jednoduchý automatizační skript v Pythonu, který udržuje pořádek ve složce "Stažené soubory" (Downloads). Automaticky třídí soubory do příslušných složek podle jejich přípony.

## 🚀 O projektu
Jako začínající vývojář jsem chtěl vyřešit reálný problém – nepořádek v souborech. Tento skript analyzuje soubory ve vybraném adresáři a přesouvá je do kategorií:
- **Obrázky:** .jpg, .png, .webp...
- **Dokumenty:** .pdf, .docx, .txt...
- **Instalátory:** .exe, .msi, .zip...
- **Videa:** .mp4, .mkv...

## 🛠 Požadavky (Requirements)
Tento projekt je navržen tak, aby byl lehký a běžel na jakémkoli PC.
- Python 3.x
- Standardní knihovny (`os`, `shutil`) - není potřeba nic instalovat navíc.

## 💻 Jak spustit
1. Ujistěte se, že máte nainstalovaný Python.
2. Stáhněte soubor `main.py`.
3. Otevřete terminál ve složce projektu.
4. Spusťte příkaz:
   ```bash
   python main.py
