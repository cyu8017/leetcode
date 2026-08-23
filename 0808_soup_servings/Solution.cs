// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

using System.Collections.Generic;

public class Solution {
    public double SoupServings(int n) {
        if (n >= 4800) return 1.0;
        int units = (n + 24) / 25;
        var memo = new Dictionary<long, double>();
        double Dp(int a, int b) {
            if (a <= 0 && b <= 0) return 0.5;
            if (a <= 0) return 1.0;
            if (b <= 0) return 0.0;
            long key = ((long)a << 16) | (uint)b;
            if (memo.TryGetValue(key, out double cached)) return cached;
            double val = 0.25 * (Dp(a - 4, b) + Dp(a - 3, b - 1) + Dp(a - 2, b - 2) + Dp(a - 1, b - 3));
            return memo[key] = val;
        }
        return Dp(units, units);
    }
}
