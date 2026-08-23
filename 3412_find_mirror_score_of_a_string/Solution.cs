// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

using System.Collections.Generic;

public class Solution {
    public long CalculateScore(string s) {
        var stacks = new List<int>[26];
        for (int i = 0; i < 26; i++) stacks[i] = new List<int>();
        long ans = 0;
        for (int i = 0; i < s.Length; i++) {
            int ci = s[i] - 'a';
            int mir = 25 - ci;
            if (stacks[mir].Count > 0) {
                int j = stacks[mir][stacks[mir].Count - 1];
                stacks[mir].RemoveAt(stacks[mir].Count - 1);
                ans += i - j;
            } else {
                stacks[ci].Add(i);
            }
        }
        return ans;
    }
}
