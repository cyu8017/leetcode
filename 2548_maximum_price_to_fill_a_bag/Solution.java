// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

import java.util.Arrays;

class Solution {
    public double maxPrice(int[][] items, int capacity) {
        Arrays.sort(items, (a, b) -> Double.compare(b[0] / (double) b[1], a[0] / (double) a[1]));
        double ans = 0.0;
        int remain = capacity;
        for (int[] it : items) {
            int price = it[0], weight = it[1];
            if (remain >= weight) {
                ans += price;
                remain -= weight;
            } else {
                ans += (double) price * remain / weight;
                remain = 0;
                break;
            }
        }
        if (remain > 0) return -1;
        return ans;
    }
}
