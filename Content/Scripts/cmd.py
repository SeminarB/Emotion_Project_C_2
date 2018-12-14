#import subprocess
import unreal_engine as ue

#cmd = 'ue.py_exec(ue.find_plugin('UnrealEnginePython').get_base_dir() + '/write.py')'
ue.py_exec(ue.find_plugin('UnrealEnginePython').get_base_dir() + '/write.py')

#subprocess.Popen(cmd)
