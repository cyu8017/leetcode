// LeetCode 1475 - Final Prices With A Special Discount In A Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

using System.Collections.Generic;
public class Solution {
    public int[] FinalPrices(int[] prices) {
        var ans = (int[])prices.Clone();
        var stack = new Stack<int>();
        for (int i = 0; i < prices.Length; i++) {
            while (stack.Count > 0 && prices[stack.Peek()] >= prices[i])
                ans[stack.Pop()] -= prices[i];
            stack.Push(i);
        }
        return ans;
    }
}
