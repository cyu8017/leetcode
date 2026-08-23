// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

using System.Collections.Generic;

public class Solution {
    public int NumIdenticalPairs(int[] nums) {
        var counts = new Dictionary<int, int>();
        int ans = 0;
        foreach (int n in nums) {
            counts.TryGetValue(n, out int c);
            ans += c;
            counts[n] = c + 1;
        }
        return ans;
    }
}
