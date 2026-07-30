// LeetCode 1357 - Apply Discount Every N Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

using System.Collections.Generic;
public class Cashier {
    int n, discount, count;
    Dictionary<int, int> price = new Dictionary<int, int>();
    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n; this.discount = discount;
        for (int i = 0; i < products.Length; i++) price[products[i]] = prices[i];
    }
    public double GetBill(int[] product, int[] amount) {
        count++;
        double total = 0;
        for (int i = 0; i < product.Length; i++) total += price[product[i]] * amount[i];
        return count % n == 0 ? total * (100 - discount) / 100.0 : total;
    }
}
