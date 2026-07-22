// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinDeletions(string s) {
        var count = new int[26];
        foreach (char c in s) count[c - 'a']++;
        var used = new HashSet<int>();
        int ans = 0;
        foreach (int freq in count) {
            int x = freq;
            while (x > 0 && used.Contains(x)) { x--; ans++; }
            used.Add(x);
        }
        return ans;
    }
}
