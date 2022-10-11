import numpy as np
def percentile():
    try:
        n = float(input("Enter a number to find it's percentile: "))
        print("The number you entered is: ",n)
        arr = np.arange(100)
        print("The percentile of {} is: ".format(n),np.percentile(arr,n))
    except ValueError:
        print("Enter a number!")
    except:
        print("Enter correctly")
percentile()