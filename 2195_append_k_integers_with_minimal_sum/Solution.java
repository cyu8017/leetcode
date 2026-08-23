// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

import java.util.Arrays;

class Solution {
    public long minimalKSum(int[] nums, int k) {
        Arrays.sort(nums);
        long ans = 0;
        int prev = 0;
        for (int x : nums) {
            if (x <= prev) continue;
            int start = prev + 1, end = x - 1;
            if (start <= end) {
                int cnt = end - start + 1;
                if (cnt > k) { end = start + k - 1; cnt = k; }
                ans += (long)(start + end) * cnt / 2;
                k -= cnt;
                if (k == 0) return ans;
            }
            prev = x;
        }
        long s = prev + 1, e = s + k - 1;
        ans += (s + e) * k / 2;
        return ans;
    }
}
