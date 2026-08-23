// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

using System.Collections.Generic;

public class OrderManagementSystem {
    Dictionary<int, string> orderTypeMap = new Dictionary<int, string>();
    Dictionary<int, int> priceMap = new Dictionary<int, int>();
    Dictionary<(string, int), List<int>> t = new Dictionary<(string, int), List<int>>();

    public OrderManagementSystem() {}

    public void AddOrder(int orderId, string orderType, int price) {
        orderTypeMap[orderId] = orderType;
        priceMap[orderId] = price;
        var key = (orderType, price);
        if (!t.ContainsKey(key)) t[key] = new List<int>();
        t[key].Add(orderId);
    }

    public void ModifyOrder(int orderId, int newPrice) {
        string orderType = orderTypeMap[orderId];
        int oldPrice = priceMap[orderId];
        priceMap[orderId] = newPrice;
        var oldKey = (orderType, oldPrice);
        var oldList = t[oldKey];
        for (int i = 0; i < oldList.Count; i++) {
            if (oldList[i] == orderId) {
                oldList.RemoveAt(i);
                break;
            }
        }
        var key = (orderType, newPrice);
        if (!t.ContainsKey(key)) t[key] = new List<int>();
        t[key].Add(orderId);
    }

    public void CancelOrder(int orderId) {
        string orderType = orderTypeMap[orderId];
        int price = priceMap[orderId];
        orderTypeMap.Remove(orderId);
        priceMap.Remove(orderId);
        var key = (orderType, price);
        var list = t[key];
        for (int i = 0; i < list.Count; i++) {
            if (list[i] == orderId) {
                list.RemoveAt(i);
                break;
            }
        }
    }

    public int[] GetOrdersAtPrice(string orderType, int price) {
        var key = (orderType, price);
        if (!t.ContainsKey(key)) return new int[0];
        return t[key].ToArray();
    }
}
