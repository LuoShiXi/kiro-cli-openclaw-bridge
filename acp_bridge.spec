# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec file for ACP-to-OpenAI Bridge.

Build commands:
  WSL/Linux:  pyinstaller acp_bridge.spec
  macOS:      pyinstaller acp_bridge.spec

Output: dist/acp-bridge (single executable)
"""

import sys
from PyInstaller.utils.hooks import collect_submodules

# Collect all uvicorn and fastapi submodules (they use dynamic imports)
hiddenimports = (
    collect_submodules("uvicorn")
    + collect_submodules("fastapi")
    + collect_submodules("starlette")
    + collect_submodules("anyio")
    + collect_submodules("acp_openai_bridge")
)

a = Analysis(
    ["acp_openai_bridge/main.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "tkinter",
        "matplotlib",
        "numpy",
        "pandas",
        "PIL",
        "scipy",
        "pytest",
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="acp-bridge",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
