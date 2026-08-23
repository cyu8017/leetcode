// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

using System.Collections.Generic;

public class Solution {
    public int MinimumLengthEncoding(string[] words) {
        var good = new HashSet<string>(words);
        foreach (string word in words)
            for (int i = 1; i < word.Length; i++)
                good.Remove(word.Substring(i));
        int ans = 0;
        foreach (string word in good) ans += word.Length + 1;
        return ans;
    }
}
