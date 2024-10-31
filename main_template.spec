# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main_template.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/Background2.png', '.'), ('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/CardObject.py', '.'), ('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/DeckFrame.py', '.'), ('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/ExportCSVFrame.py', '.'), ('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/LA_v5-06 300x60.xlsx', '.'), ('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/LoadData.py', '.'), ('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/OptimizeDeckFrame.py', '.'), ('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/TestDeckFrame.py', '.'), ('/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/Wiki-Card-Research_2.6.xlsx', '.')],
    hiddenimports=['pandas', 'numpy', 'wx', 'openpyxl', 'openpyxl.cell._writer'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main_template',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/app_icon.icns'],
)
app = BUNDLE(
    exe,
    name='main_template.app',
    icon='/Users/brandonhannan/Documents/Little Alchemist/Little Alchemist Repository/LittleAlchemistAnalyst/app_icon.icns',
    bundle_identifier=None,
)
