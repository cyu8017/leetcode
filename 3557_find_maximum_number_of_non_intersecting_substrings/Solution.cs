// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

using System.Collections.Generic;

public class Solution {
    public int MaxSubstrings(string word) {
        int ans = 0;
        var first = new Dictionary<char, int>();
        for (int i = 0; i < word.Length; i++) {
            char c = word[i];
            if (!first.ContainsKey(c)) first[c] = i;
            else if (i - first[c] + 1 >= 4) {
                ans++;
                first.Clear();
            }
        }
        return ans;
    }
}
