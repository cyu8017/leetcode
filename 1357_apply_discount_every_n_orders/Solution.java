// LeetCode 1357 - Apply Discount Every N Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

import java.util.*;

class Cashier {
    private int n, discount, count;
    private Map<Integer, Integer> price = new HashMap<>();

    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n;
        this.discount = discount;
        for (int i = 0; i < products.length; i++) price.put(products[i], prices[i]);
    }

    public double getBill(int[] product, int[] amount) {
        count++;
        double total = 0;
        for (int i = 0; i < product.length; i++) total += price.get(product[i]) * amount[i];
        if (count % n == 0) return total * (100 - discount) / 100.0;
        return total;
    }
}
