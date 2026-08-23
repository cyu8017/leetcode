// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

using System.Collections.Generic;

public class Solution {
    public bool CanConvert(string str1, string str2) {
        if (str1 == str2) return true;
        var mapping = new Dictionary<char, char>();
        for (int i = 0; i < str1.Length; i++) {
            if (mapping.ContainsKey(str1[i]) && mapping[str1[i]] != str2[i]) return false;
            mapping[str1[i]] = str2[i];
        }
        return new HashSet<char>(str2).Count < 26;
    }
}
