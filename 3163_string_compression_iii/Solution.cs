// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

using System;
using System.Text;

public class Solution {
    public string CompressedString(string word) {
        var ans = new StringBuilder();
        int n = word.Length;
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && word[j] == word[i]) j++;
            int k = j - i;
            while (k > 0) {
                int x = Math.Min(9, k);
                ans.Append((char)('0' + x));
                ans.Append(word[i]);
                k -= x;
            }
            i = j;
        }
        return ans.ToString();
    }
}
