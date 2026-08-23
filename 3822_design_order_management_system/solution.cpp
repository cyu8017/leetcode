// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

class OrderManagementSystem {
    struct Key {
        std::string orderType;
        int price;
        bool operator==(const Key& o) const {
            return orderType == o.orderType && price == o.price;
        }
    };
    struct KeyHash {
        size_t operator()(const Key& k) const {
            return std::hash<std::string>()(k.orderType) ^ (std::hash<int>()(k.price) << 1);
        }
    };
    std::unordered_map<int, std::string> orderTypeMap;
    std::unordered_map<int, int> priceMap;
    std::unordered_map<Key, std::vector<int>, KeyHash> t;

public:
    OrderManagementSystem() {}

    void addOrder(int orderId, std::string orderType, int price) {
        orderTypeMap[orderId] = orderType;
        priceMap[orderId] = price;
        t[{orderType, price}].push_back(orderId);
    }

    void modifyOrder(int orderId, int newPrice) {
        std::string orderType = orderTypeMap[orderId];
        int oldPrice = priceMap[orderId];
        priceMap[orderId] = newPrice;
        Key oldKey{orderType, oldPrice};
        auto& oldList = t[oldKey];
        for (int i = 0; i < (int)oldList.size(); i++) {
            if (oldList[i] == orderId) {
                oldList.erase(oldList.begin() + i);
                break;
            }
        }
        t[{orderType, newPrice}].push_back(orderId);
    }

    void cancelOrder(int orderId) {
        std::string orderType = orderTypeMap[orderId];
        int price = priceMap[orderId];
        orderTypeMap.erase(orderId);
        priceMap.erase(orderId);
        Key key{orderType, price};
        auto& list = t[key];
        for (int i = 0; i < (int)list.size(); i++) {
            if (list[i] == orderId) {
                list.erase(list.begin() + i);
                break;
            }
        }
    }

    std::vector<int> getOrdersAtPrice(std::string orderType, int price) {
        return t[{orderType, price}];
    }
};
