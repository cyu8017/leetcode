// LeetCode 1475 - Final Prices With A Special Discount In A Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

import java.util.*;

class Solution {
    public int[] finalPrices(int[] prices) {
        var ans = (int[])prices.Clone();
        var stack = new ArrayDeque<>();
        for (int i = 0; i < prices.length; i++) {
            while (stack.size() > 0 && prices[stack.peek()] >= prices[i])
                ans[stack.pop()] -= prices[i];
            stack.push(i);
        }
        return ans;
    }
}
