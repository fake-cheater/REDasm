import subprocess
import shutil
import os
from tempfile import NamedTemporaryFile
from deploy_vars import *

def do_deploy(filename):
 fp = NamedTemporaryFile(mode="w", delete=False)
 fp.write(os.getenv("DEPLOY_TOKEN"))
 fp.close();
 subprocess.run(["sftp", filename, "-i", [fp.name], os.getenv("DEPLOY_DESTINATION")])
 os.remove(fp.name)

os.chdir("..")

if OS_NAME == "Linux":
 appimagename = "REDasm_" + ARCH  + "_" + BUILD_DATE + ".AppImage"
 shutil.move("REDasm--" + ARCH + ".AppImage", appimagename)
 do_deploy(appimagename)

do_deploy(BUILD_ARCHIVE)
