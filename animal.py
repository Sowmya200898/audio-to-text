import sys

def branch2():
    print("iam a dog")

    
def default():
    print("hello")

def main():
    if sys.argv[1]== 'branch2':
        branch1()
    else:
        default()


if __name__ == '__main__':
    main()
