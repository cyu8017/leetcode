// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

import java.util.*;

class StockSpanner {
    private final List<int[]> stack = new ArrayList<>();

    public StockSpanner() {}

    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.get(stack.size() - 1)[0] <= price) {
            span += stack.get(stack.size() - 1)[1];
            stack.remove(stack.size() - 1);
        }
        stack.add(new int[] {price, span});
        return span;
    }
}
