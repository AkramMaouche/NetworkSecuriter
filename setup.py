'''
the setup file is essential part for packaging and distributing Pythin projects 

'''

from setuptools import find_packages, setup
from typing import List 


def get_requirments() -> List[str]: 
    '''
    this function will return list of requirments 
    '''
    requirment_lst: List[str]=[]
    try: 
        with open ('requirments.txt','r') as file : 
            lines = file.readlines()
            for line in lines: 
                requirment = line.strip()
                if requirment and requirment != '-e .': 
                    requirment_lst.append(requirment)

    except FileNotFoundError: 
        print("requiremnts.txt file is not found")
    
    return requirment_lst

setup( 
    name = 'Network Securiter',
    version= '0.01',
    author= "Maouche Akram " , 
    author_email= "aghilaztheanalyst@gmail.com",
    packages= find_packages(),
    install_requires = get_requirments()
    )
    

