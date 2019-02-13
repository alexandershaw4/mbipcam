# -*- mode: python -*-

block_cipher = None


a = Analysis(['mbipc.py'],
             pathex=['/Users/Alex/code/mbipcam'],
             binaries=[],
             datas=[('view_ipcam.py', '.')],
             hiddenimports=['rumps', 'view_ipcam', 'urllib', 'cv2', 'numpy', 'sys'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mbipc',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='mbipc.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
                'LSUIElement': 'True'
              },
             )
