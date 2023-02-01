COUNTRIES = ['Iran', 'UAE']
VAT = {"Iran": 9, "UAE": 15}

"""
این تمرین همان تمری قسمت قبل که دکوریتور بود هست منتها در اینجا ما از پروکسی استفاده میکنیم تا 
اعتبار یوزر هارا چک کند تا یوزر دیگری نتواند لیست حساب دیگری را حساب کند 
فرق دکوریتور با پروکسی در اینجا مشخص میشود ،ما در دکوریتور دنبال این بودیم که 
یک ویژگی به کلاس یا تابع اضافه کنیم اما در پروکسی مدیریت دسترسی میکنیم
"""


def check_permission(func):
    """
    این تابع تابع دکوریتور هست که فرایند پروکسی کردن را برای ما انجام میدهد در این تابع ما دو ورودی میگیریم یکی پرچرز هست
    که در آن اسم و ادرس افراد ذخیره شده و دیگری یوزری که قصد دارد تصفیه حساب بکند
    در قسمت شرط از پرچر یوزر را با یوزری که میخواهد تصفیه حساب بکند مقایسه میکند و اگر یکی بودند
    اجازه میدهد تا تابع چک اوت ادامه یابد اگر یکی نباشند پیامی دیگر را در قسمت ریترن بر میگرداند
    :param func:
    :return:
    """
    def wrapped_func(obj, user):
        if obj.user == user:
            return func(obj)
        return "You are not allowed to checkout"

    return wrapped_func


class User:
    pass


class Address:
    def __init__(self, country):
        self.country = country


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:
    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.products_list = []

    def add_products(self, products_list):
        """
        این تابع یک کالا را به لیست خرید اضافه میکند
        :param products_list:
        :return:
        """
        if not isinstance(products_list, list):
            products_list = [products_list]
        self.products_list.extend(products_list)

    def total_price(self):
        s = 0
        for product in self.products_list:
            s += product.price
        return s

    @check_permission
    def checkout(self):
        return "Checkout done!"


def calculate_vat(func):
    def wrapped_func(pur):
        vat = VAT[pur.address.country]
        total_price = pur.total_price()
        return total_price + total_price * vat / 100

    return wrapped_func


def show_total_price(p):
    return p.total_price()


@calculate_vat
def show_vat_pluse_price(p):
    return p.toral_price()


if __name__ == "__main__":
    user = User()
    addr_iran = Address(country=COUNTRIES[0])
    addr_uae = Address(country=COUNTRIES[1])

    p1 = Product("Persian rugs", 120)
    p2 = Product("Nain rugs", 145)
    p3 = Product("Galaxy buds", 105)

    products = [p1, p2, p3]

    purchase_iran = Purchase(user=user, address=addr_iran)
    purchase_iran.add_products(p1)
    purchase_iran.add_products([p2, p3])
    # print(show_total_price(purchase_iran))
    # print(show_vat_pluse_price(purchase_iran))

    purchase_uae = Purchase(user=user, address=addr_uae)
    purchase_uae.add_products(p1)
    purchase_uae.add_products([p2, p3])
    # print(show_total_price(purchase_uae))
    # print(show_vat_pluse_price(purchase_uae))

    u1 = User()
    print(purchase_iran.checkout(user))
    print(purchase_uae.checkout(u1))
