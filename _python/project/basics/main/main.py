print('First module name: {}'.format(__name__))

def main():
    print("Gets printed only if this file is executed directly")
    pass

if __name__ == '__main__':
    print('Run directly')
    main()

