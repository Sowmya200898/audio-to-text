import sys

def branch1():
    print("iam a Cat")

    
def default():
    print("hello")

def main():
    if sys.argv[1]== 'branch1':
        branch1()
    else:
        default()


if __name__ == '__main__':
    main()
