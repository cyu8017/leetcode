// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

using System.Collections.Generic;

public class Solution {
    public int FirstUniqueFreq(int[] nums) {
        var cnt = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
        }
        var freq = new Dictionary<int, int>();
        foreach (var v in cnt.Values) {
            if (!freq.ContainsKey(v)) freq[v] = 0;
            freq[v]++;
        }
        foreach (int x in nums) {
            if (freq[cnt[x]] == 1) return x;
        }
        return -1;
    }
}
