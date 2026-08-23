// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

using System.Collections.Generic;

public class Solution {
    public int[] NumberOfPairs(int[] nums) {
        var cnt = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
        }
        int pairs = 0, left = 0;
        foreach (var c in cnt.Values) {
            pairs += c / 2;
            left += c % 2;
        }
        return new[] { pairs, left };
    }
}
