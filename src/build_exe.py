import PyInstaller.__main__


for script in ('add_hosts.py', 'clear_hosts.py'):
    PyInstaller.__main__.run([
        script,
        '--distpath', '../dist',
        '--workpath', '../build',
        '--specpath', '../',
        '--clean',
        '--onefile',
        '--noconsole',
    ])
