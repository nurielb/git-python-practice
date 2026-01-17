from datetime import datetime


def greet(name):
    return f"Hello, Mr.{name}!\n Time: {datetime.now().isoformat()}"


if __name__ == "__main__":
    user = "World"
    print(greet(user))