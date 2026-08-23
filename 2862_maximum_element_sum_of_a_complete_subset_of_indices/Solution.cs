// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

using System.Collections.Generic;

public class Solution {
    public long MaximumSum(IList<int> nums) {
        int n = nums.Count;
        int SquareFree(int x) {
            int res = 1;
            for (int p = 2; p * p <= x; p++) {
                int cnt = 0;
                while (x % p == 0) {
                    x /= p;
                    cnt++;
                }
                if (cnt % 2 == 1) res *= p;
            }
            if (x > 1) res *= x;
            return res;
        }
        var groups = new Dictionary<int, long>();
        long ans = 0;
        for (int i = 1; i <= n; i++) {
            int sf = SquareFree(i);
            if (!groups.ContainsKey(sf)) groups[sf] = 0;
            groups[sf] += nums[i - 1];
            if (groups[sf] > ans) ans = groups[sf];
        }
        return ans;
    }
}
