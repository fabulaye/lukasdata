import subprocess
import os

git_dir="C:/Users/lukas/Documents/GitHub/lukasdata"
os.chdir(git_dir)

build_command="python -m build"


#os.listdir(git_dir+"/dist")

#bei twine die version 

def change_version(version):
    content=[]
    with open(git_dir+"/setup.py","r") as setup:
        for line in setup:
            if line.startswith("    version"):
                line=f"    version='{version}',\n"
                content.append(line)
                print(f"version changed to {version}")
            else:
                content.append(line)
    print(content)
    with open(git_dir+"/setup.py","w") as file:
        file.writelines(content)
    

def update_lukasdata(version,commit_message):
    os.chdir(git_dir)
    change_version(version)
    subprocess.run(build_command)
    subprocess.run("git add -u")
    subprocess.run("git add --all")
    subprocess.run(f"git commit -m {commit_message}")
    subprocess.run("git push origin * main") #hier bin ich nicht sicher
    tar_file="lukasdata-"+version+".tar.gz"
    wheel="lukasdata-"+version+"-py3-none-any.whl"
    subprocess.run(f"twine upload dist\\{tar_file}")
    subprocess.run(f"twine upload dist\\{wheel}")
    #subprocess.run("pip install --upgrade lukasdata")


update_lukasdata("1.3.1","changed package structure")
