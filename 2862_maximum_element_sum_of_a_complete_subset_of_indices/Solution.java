// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long maximumSum(List<Integer> nums) {
        int n = nums.size();
        Map<Integer, Long> groups = new HashMap<>();
        long ans = 0;
        for (int i = 1; i <= n; i++) {
            int sf = squareFree(i);
            long sum = groups.getOrDefault(sf, 0L) + nums.get(i - 1);
            groups.put(sf, sum);
            if (sum > ans) ans = sum;
        }
        return ans;
    }

    private int squareFree(int x) {
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
}
