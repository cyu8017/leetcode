// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

using System.Collections.Generic;

public class Solution {
    public long CountInterestingSubarrays(IList<int> nums, int modulo, int k) {
        var freq = new Dictionary<int, int> { [0] = 1 };
        long ans = 0;
        int pref = 0;
        foreach (int v in nums) {
            if (v % modulo == k) pref++;
            int need = (pref - k) % modulo;
            if (need < 0) need += modulo;
            if (freq.ContainsKey(need)) ans += freq[need];
            int key = pref % modulo;
            if (!freq.ContainsKey(key)) freq[key] = 0;
            freq[key]++;
        }
        return ans;
    }
}
