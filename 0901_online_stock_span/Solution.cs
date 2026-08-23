// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

using System.Collections.Generic;

public class StockSpanner {
    private readonly List<(int price, int span)> stack = new();

    public StockSpanner() {}

    public int Next(int price) {
        int span = 1;
        while (stack.Count > 0 && stack[stack.Count - 1].price <= price) {
            span += stack[stack.Count - 1].span;
            stack.RemoveAt(stack.Count - 1);
        }
        stack.Add((price, span));
        return span;
    }
}
