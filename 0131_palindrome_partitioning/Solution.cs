// LeetCode 0131 - Palindrome Partitioning
// https://leetcode.com/problems/palindrome-partitioning/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> Partition(string s) {
        var result = new List<IList<string>>();
        Backtrack(0, new List<string>());
        return result;

        void Backtrack(int start, List<string> path) {
            if (start == s.Length) { result.Add(new List<string>(path)); return; }
            for (int end = start; end < s.Length; end++) {
                if (!IsPalindrome(start, end)) continue;
                path.Add(s.Substring(start, end - start + 1));
                Backtrack(end + 1, path);
                path.RemoveAt(path.Count - 1);
            }
        }

        bool IsPalindrome(int left, int right) {
            while (left < right) if (s[left++] != s[right--]) return false;
            return true;
        }
    }
}
