from connections import *

if __name__ == "__main__":
    #the below works due to __all__ definition in __init__.py for connections package
    wifi.connect_wifi()
    mobile.connect_mobile()