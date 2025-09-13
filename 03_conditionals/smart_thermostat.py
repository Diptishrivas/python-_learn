device_status = "active"
temperature =-40

if device_status=="active":
    if temperature >38:
        print("High temperature")

    else:
        print("temperature is normal")
else:    
    print("device is offline")
    