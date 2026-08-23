// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

using System;
using System.Collections.Generic;

public class Solution {
    private readonly Dictionary<int, int> memo = new Dictionary<int, int>();

    public int MinDays(int n) {
        if (n <= 1) return n;
        if (memo.TryGetValue(n, out int cached)) return cached;
        return memo[n] = 1 + Math.Min(n % 2 + MinDays(n / 2), n % 3 + MinDays(n / 3));
    }
}
