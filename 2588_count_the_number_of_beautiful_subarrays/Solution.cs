// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

using System.Collections.Generic;

public class Solution {
    public long BeautifulSubarrays(int[] nums) {
        var freq = new Dictionary<int, int> { [0] = 1 };
        int xorv = 0;
        long ans = 0;
        foreach (int x in nums) {
            xorv ^= x;
            ans += freq.GetValueOrDefault(xorv, 0);
            freq[xorv] = freq.GetValueOrDefault(xorv, 0) + 1;
        }
        return ans;
    }
}
