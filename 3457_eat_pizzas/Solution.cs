// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

using System;

public class Solution {
    public long MaxWeight(int[] pizzas) {
        Array.Sort(pizzas);
        int n = pizzas.Length;
        int days = n / 4;
        long ans = 0;
        int oddDays = (days + 1) / 2;
        int evenDays = days / 2;
        int idx = n - 1;
        for (int i = 0; i < oddDays; i++) {
            ans += pizzas[idx];
            idx--;
        }
        for (int i = 0; i < evenDays; i++) {
            idx--;
            ans += pizzas[idx];
            idx--;
        }
        return ans;
    }
}
