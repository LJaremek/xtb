# xtb
Python library for XTB api

> [!WARNING]
> The library is not an official XTB product, it was created for a student project. Make sure you want to use it!



### Why was this library created?
XTB provides the API and documentation for free.
The problem is that the API is old and is based on web sockets.
For this reason, to work comfortably with this API, it is necessary to wrap it in classes/functions.

Official API documentation: http://developers.xstore.pro/documentation/current



### How to get USER_ID value
After logging in to https://xstation5.xtb.com/ you will find your ID along with your account type (version) in the upper right corner of the screen.
The ID is an eight-digit code. The account version can be "real" or "demo".

> [!CAUTION]
> Remember that when you operate on a "real" account you use real money!



### Example use
Install the repository as a Python library:
``sh
pip install git+https://github.com/LJaremek/xtb.git
```

Use the code in your project
```python
from xtb import XTB

if __name__ == "__main__":
    xtb = XTB(
        os.getenv("USER_ID"),
        os.getenv("PASSWORD"),
        os.getenv("ENV")
    )

    login_status = xtb.login()["status"]
    print("Login:", login_status)

    res = xtb.get_chart_range_request(
        "2014-01-01",  # start date
        "today",  # end date
        "UBI.FR_4",  # company name
        "MN1",  # time period
    )

    print(res)

```
