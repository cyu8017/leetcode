// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

using System.Collections.Generic;

public class Solution {
    public int UnequalTriplets(int[] nums) {
        var cnt = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
        }
        int ans = 0, n = nums.Length, left = 0;
        foreach (var c in cnt.Values) {
            int right = n - left - c;
            ans += left * c * right;
            left += c;
        }
        return ans;
    }
}
