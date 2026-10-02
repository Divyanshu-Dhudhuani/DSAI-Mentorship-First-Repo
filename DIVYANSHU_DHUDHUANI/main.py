def check(password):
    if (password == "Secret123"):
        return True
    return False


def secret_read():
    with open("password.txt", "r") as file:
        content = file.read()

def main():
    secret_read()

if __name__ == '__main__':
    main()
    
