// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

using System.Collections.Generic;

public class Solution {
    public long CountSubarrays(int[] nums, int k) {
        var pre = new Dictionary<int, int>();
        long ans = 0;
        foreach (int x in nums) {
            var cur = new Dictionary<int, int>();
            foreach (var kv in pre) {
                int key = x & kv.Key;
                if (!cur.ContainsKey(key)) cur[key] = 0;
                cur[key] += kv.Value;
            }
            if (!cur.ContainsKey(x)) cur[x] = 0;
            cur[x]++;
            if (cur.ContainsKey(k)) ans += cur[k];
            pre = cur;
        }
        return ans;
    }
}
