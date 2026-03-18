from setuptools import find_packages,setup
from typing import List
HYP_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:#returns list of reqs
    reqs=[]
    with open(file_path)as f_obj:
        reqs=f_obj.readlines()
        reqs=[req.replace("\n","") for req in reqs]
        if HYP_E_DOT in reqs:
            reqs.remove(HYP_E_DOT)
    return reqs
setup(
    name="MLProject1",
    version="0.0.1",
    author="Aditeya",
    author_email="aditeyamitra.kol@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)