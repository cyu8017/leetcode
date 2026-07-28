// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> CommonChars(string[] words) {
        int[] common = Count(words[0]);
        for (int w = 1; w < words.Length; w++) {
            int[] cur = Count(words[w]);
            for (int i = 0; i < 26; i++) common[i] = Math.Min(common[i], cur[i]);
        }
        var ans = new List<string>();
        for (int i = 0; i < 26; i++)
            for (int t = 0; t < common[i]; t++)
                ans.Add(((char)('a' + i)).ToString());
        return ans;
    }

    private static int[] Count(string s) {
        var c = new int[26];
        foreach (char ch in s) c[ch - 'a']++;
        return c;
    }
}
