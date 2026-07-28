// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

using System.Collections.Generic;

public class Solution {
    public int ShortestWay(string source, string target) {
        var sourceSet = new HashSet<char>(source);
        foreach (char ch in target) {
            if (!sourceSet.Contains(ch)) {
                return -1;
            }
        }
        int ans = 0, i = 0, n = target.Length;
        while (i < n) {
            ans++;
            foreach (char ch in source) {
                if (i < n && target[i] == ch) {
                    i++;
                }
            }
        }
        return ans;
    }
}
