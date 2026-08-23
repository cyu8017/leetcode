// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design_order_management_system/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

class OrderManagementSystem {
    private static class Key {
        final String orderType;
        final int price;
        Key(String orderType, int price) {
            this.orderType = orderType;
            this.price = price;
        }
        @Override public boolean equals(Object o) {
            if (!(o instanceof Key)) return false;
            Key k = (Key) o;
            return price == k.price && Objects.equals(orderType, k.orderType);
        }
        @Override public int hashCode() {
            return Objects.hash(orderType, price);
        }
    }

    Map<Integer, String> orderTypeMap = new HashMap<>();
    Map<Integer, Integer> priceMap = new HashMap<>();
    Map<Key, List<Integer>> t = new HashMap<>();

    public OrderManagementSystem() {}

    public void addOrder(int orderId, String orderType, int price) {
        orderTypeMap.put(orderId, orderType);
        priceMap.put(orderId, price);
        Key key = new Key(orderType, price);
        t.computeIfAbsent(key, k -> new ArrayList<>()).add(orderId);
    }

    public void modifyOrder(int orderId, int newPrice) {
        String orderType = orderTypeMap.get(orderId);
        int oldPrice = priceMap.get(orderId);
        priceMap.put(orderId, newPrice);
        Key oldKey = new Key(orderType, oldPrice);
        List<Integer> oldList = t.get(oldKey);
        for (int i = 0; i < oldList.size(); i++) {
            if (oldList.get(i) == orderId) {
                oldList.remove(i);
                break;
            }
        }
        Key key = new Key(orderType, newPrice);
        t.computeIfAbsent(key, k -> new ArrayList<>()).add(orderId);
    }

    public void cancelOrder(int orderId) {
        String orderType = orderTypeMap.get(orderId);
        int price = priceMap.get(orderId);
        orderTypeMap.remove(orderId);
        priceMap.remove(orderId);
        Key key = new Key(orderType, price);
        List<Integer> list = t.get(key);
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == orderId) {
                list.remove(i);
                break;
            }
        }
    }

    public int[] getOrdersAtPrice(String orderType, int price) {
        Key key = new Key(orderType, price);
        List<Integer> list = t.get(key);
        if (list == null) return new int[0];
        int[] ans = new int[list.size()];
        for (int i = 0; i < list.size(); i++) ans[i] = list.get(i);
        return ans;
    }
}
