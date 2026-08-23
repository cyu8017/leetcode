// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

using System.Collections.Generic;

public class Solution {
    public long CountValidSubarrays(int[] nums, int x) {
        var byRemainder = new List<long>[10];
        for (int i = 0; i < 10; i++) byRemainder[i] = new List<long>();
        byRemainder[0].Add(0);
        long prefix = 0, answer = 0;
        foreach (int value in nums) {
            prefix += value;
            int required = (int)((prefix - x) % 10 + 10) % 10;
            var values = byRemainder[required];
            for (long power = 1; (long)x * power <= prefix; power *= 10) {
                long low = (long)x * power;
                long high = (long)(x + 1) * power - 1;
                long minPrefix = prefix - high, maxPrefix = prefix - low;
                int left = LowerBound(values, minPrefix);
                int right = UpperBound(values, maxPrefix);
                answer += right - left;
                if (power > prefix / 10) break;
            }
            byRemainder[(int)(prefix % 10)].Add(prefix);
        }
        return answer;
    }

    static int LowerBound(List<long> a, long x) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    static int UpperBound(List<long> a, long x) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
