# LeetCode 3822 - Design Order Management System
# https://leetcode.com/problems/design-order-management-system/

from typing import List


class OrderManagementSystem:
    def __init__(self):
        self.orderTypeMap = {}
        self.priceMap = {}
        self.t = {}

    def _key(self, orderType: int, price: int) -> str:
        return str(orderType) + "#" + str(price)

    def addOrder(self, orderId: int, orderType: int, price: int) -> None:
        self.orderTypeMap[orderId] = orderType
        self.priceMap[orderId] = price
        key = self._key(orderType, price)
        if key not in self.t:
            self.t[key] = []
        self.t[key].append(orderId)

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        orderType = self.orderTypeMap[orderId]
        oldPrice = self.priceMap[orderId]
        self.priceMap[orderId] = newPrice
        oldKey = self._key(orderType, oldPrice)
        oldList = self.t[oldKey]
        for i in range(len(oldList)):
            if oldList[i] == orderId:
                oldList.pop(i)
                break
        key = self._key(orderType, newPrice)
        if key not in self.t:
            self.t[key] = []
        self.t[key].append(orderId)

    def cancelOrder(self, orderId: int) -> None:
        orderType = self.orderTypeMap.pop(orderId)
        price = self.priceMap.pop(orderId)
        key = self._key(orderType, price)
        lst = self.t[key]
        for i in range(len(lst)):
            if lst[i] == orderId:
                lst.pop(i)
                break

    def getOrdersAtPrice(self, orderType: int, price: int) -> List[int]:
        key = self._key(orderType, price)
        lst = self.t.get(key)
        if not lst:
            return []
        return lst[:]
