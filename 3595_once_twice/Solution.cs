// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

using System.Collections.Generic;

public class Solution {
    public int[] OnceTwice(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        int a = 0, b = 0;
        foreach (var kv in freq) {
            if (kv.Value == 1) a = kv.Key;
            else if (kv.Value == 2) b = kv.Key;
        }
        return new int[] { a, b };
    }
}
