// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int CanBeTypedWords(string text, string brokenLetters) {
        var broken = new HashSet<char>(brokenLetters);
        int ans = 0;
        foreach (var w in text.Split(' ')) {
            if (!w.Any(c => broken.Contains(c))) ans++;
        }
        return ans;
    }
}