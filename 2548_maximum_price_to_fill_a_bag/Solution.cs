// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

using System;

public class Solution {
    public double MaxPrice(int[][] items, int capacity) {
        Array.Sort(items, (a, b) => (b[0] / (double)b[1]).CompareTo(a[0] / (double)a[1]));
        double ans = 0.0;
        int remain = capacity;
        foreach (var it in items) {
            int price = it[0], weight = it[1];
            if (remain >= weight) {
                ans += price;
                remain -= weight;
            } else {
                ans += (double)price * remain / weight;
                remain = 0;
                break;
            }
        }
        if (remain > 0) return -1;
        return ans;
    }
}
