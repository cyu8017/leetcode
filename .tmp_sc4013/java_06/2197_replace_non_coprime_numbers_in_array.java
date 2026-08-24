// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int[] replaceNonCoprimes(int[] nums) {
        List<Integer> stack = new ArrayList<>();
        for (int x0 : nums) {
            int x = x0;
            while (!stack.isEmpty()) {
                int g = gcd(stack.get(stack.size() - 1), x);
                if (g == 1) break;
                x = stack.get(stack.size() - 1) / g * x;
                stack.remove(stack.size() - 1);
            }
            stack.add(x);
        }
        int[] ans = new int[stack.size()];
        for (int i = 0; i < stack.size(); i++) ans[i] = stack.get(i);
        return ans;
    }
}
