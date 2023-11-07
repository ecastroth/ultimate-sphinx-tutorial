"""Outside file. The user will call this file to make something using the 
code inside the src directory"""
from src.file1 import someFunctionThatUsesThePackages

def other_main():
    """Calls the main func from src/lib1/file1
    
    Normally this function contains some context, parser, etc"""
    someFunctionThatUsesThePackages()

if __name__ == '__main__':
    other_main()
    print('Code is running good!')