// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

using System;
using System.Collections.Generic;

public class Solution {
    bool IsPrime(long x) {
        if (x < 2) return false;
        long sqrtX = (long)Math.Sqrt(x);
        for (long i = 2; i <= sqrtX; i++) if (x % i == 0) return false;
        return true;
    }
    public long SumOfLargestPrimes(string s) {
        var st = new HashSet<long>();
        int n = s.Length;
        for (int i = 0; i < n; i++) {
            long x = 0;
            for (int j = i; j < n; j++) {
                x = x * 10 + (s[j] - '0');
                if (IsPrime(x)) st.Add(x);
            }
        }
        var nums = new List<long>(st);
        nums.Sort();
        long ans = 0;
        for (int i = nums.Count - 1; i >= 0 && nums.Count - i <= 3; i--)
            ans += nums[i];
        return ans;
    }
}
