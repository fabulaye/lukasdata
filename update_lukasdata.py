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
    


def catch_error(result):
    if result.returncode != 0:
        print(f"{result} Error: {result.stderr}")

def update_lukasdata(version,commit_message):
    os.chdir(git_dir)
    change_version(version)
    subprocess.run(build_command)
    print("add_u")
    add_u=subprocess.run("git add -u", capture_output=True,text=True)
    #print(add_u.stderr)
    #catch_error(add_u)
    print("add_all")
    add_all=subprocess.run("git add .",capture_output=True,text=True)
    print(add_all.stderr)
    catch_error(add_all)
    #subprocess.run("git diff --cached")
    print("commit")
    commit=subprocess.run(f"git commit -m {commit_message}")
    print(commit.stderr)
    catch_error(commit)
    subprocess.run("git push origin * main") #hier bin ich nicht sicher
    tar_file="lukasdata-"+version+".tar.gz"
    wheel="lukasdata-"+version+"-py3-none-any.whl"
    subprocess.run(f"twine upload dist\\{tar_file}")
    subprocess.run(f"twine upload dist\\{wheel}")
    

update_lukasdata("1.3.4","\"added 2init\"")
