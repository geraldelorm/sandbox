import time

def connect() -> None:
    print("Conecting....")
    time.sleep(3)
    print("Connected....")


#Use to check for testing to make use funtion calls are not executed during module load
#shows that this is meant to be run not just loaded
if __name__ == "__main__":
    connect()
