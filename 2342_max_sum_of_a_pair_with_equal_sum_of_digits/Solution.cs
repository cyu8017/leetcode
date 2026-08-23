// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

using System.Collections.Generic;

public class Solution {
    public int MaximumSum(int[] nums) {
        int DigitSum(int x) {
            int s = 0;
            while (x > 0) { s += x % 10; x /= 10; }
            return s;
        }
        var best = new Dictionary<int, int>();
        int ans = -1;
        foreach (int x in nums) {
            int ds = DigitSum(x);
            if (best.TryGetValue(ds, out int prev)) {
                if (prev + x > ans) ans = prev + x;
                if (x > prev) best[ds] = x;
            } else best[ds] = x;
        }
        return ans;
    }
}
