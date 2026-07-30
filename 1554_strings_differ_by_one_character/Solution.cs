// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

using System.Collections.Generic;

public class Solution {
    public bool DifferByOne(string[] dict) {
        var seen = new HashSet<string>();
        foreach (string word in dict) {
            char[] chars = word.ToCharArray();
            for (int i = 0; i < chars.Length; i++) {
                char original = chars[i];
                chars[i] = '*';
                string pattern = new string(chars);
                if (seen.Contains(pattern)) return true;
                seen.Add(pattern);
                chars[i] = original;
            }
        }
        return false;
    }
}
