from abc import ABC, abstractmethod


class ProductBase(ABC):
    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass

    # @abstractmethod
    # def shipping(self):
    #     pass


class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass


class RugsDetail(DetailBase):

    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"rugs detail: {self.rugs._name}"


class RugsPrice(DetailBase):

    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"rugs price: {self.rugs._price}$"


class GiftCardDetail(DetailBase):
    def __init__(self, card):
        self.card = card

    def show(self):
        return f"company: {self.card.company}"


class GiftCardPrice(DetailBase):
    def __init__(self, card):
        self.card = card

    def show(self):
        return f"gift card min price: {self.card.min_price}\t max price: {self.card.max_price}\t"


class MobileDetails(DetailBase):
    def __init__(self, company_brand):
        self.company_brand = company_brand

    def show(self):
        return f"mobile name : {self.company_brand.mobile_name}\t brand: {self.company_brand.brand}"


class MobilePrice(DetailBase):
    def __init__(self, company_brand):
        self.company_brand = company_brand

    def show(self):
        return f"price : {self.company_brand._price}"


class Rugs(ProductBase):

    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def detail(self):
        return RugsDetail(self)

    @property
    def price(self):
        return RugsPrice(self)


class GiftCard(ProductBase):

    def __init__(self, company, min_price, max_price):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price

    @property
    def detail(self):
        return GiftCardDetail(self)

    @property
    def price(self):
        return GiftCardPrice(self)


class Mobile(ProductBase):
    def __init__(self, mobile_name, brand, price):
        self.mobile_name = mobile_name
        self.brand = brand
        self._price = price

    @property
    def detail(self):
        return MobileDetails(self)

    @property
    def price(self):
        return MobilePrice(self)


if __name__ == "__main__":
    r1 = Rugs('persian rugs', 135)
    r2 = Rugs('nain rugs', 150)

    m1 = Mobile("A7","SAMSUNG",600)
    m2 = Mobile("Y9s",'Huawei',400)

    g1 = GiftCard('google', 20, 60)
    g2 = GiftCard('apple', 20, 60)

    products = [r1, r2, g1, g2,m1,m2]

    for product in products:
        print(product.detail.show())
        print(product.price.show())
        
