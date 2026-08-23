// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

using System.Collections.Generic;

public class Solution {
    public int LargestInteger(int[] nums, int k) {
        int n = nums.Length;
        var cnt = new Dictionary<int, int>();
        for (int i = 0; i + k <= n; i++) {
            var seen = new HashSet<int>();
            for (int j = i; j < i + k; j++) seen.Add(nums[j]);
            foreach (int x in seen) {
                cnt.TryGetValue(x, out int c);
                cnt[x] = c + 1;
            }
        }
        int ans = -1;
        foreach (var kv in cnt) {
            if (kv.Value == 1 && kv.Key > ans) ans = kv.Key;
        }
        return ans;
    }
}
