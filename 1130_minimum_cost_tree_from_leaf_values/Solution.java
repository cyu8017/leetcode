// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

import java.util.*;

class Solution {
    public int mctFromLeafValues(int[] arr) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(Integer.MAX_VALUE);
        int ans = 0;
        for (int x : arr) {
            while (stack.peek() <= x) {
                int mid = stack.pop();
                ans += mid * Math.min(stack.peek(), x);
            }
            stack.push(x);
        }
        while (stack.size() > 2) {
            ans += stack.pop() * stack.peek();
        }
        return ans;
    }
}
