// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    static int Calc(string w) {
        int cnt = 0;
        foreach (char c in w) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++;
        }
        return cnt;
    }

    public string ReverseWords(string s) {
        string[] words = s.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
        int cnt = Calc(words[0]);
        var ans = new List<string>();
        ans.Add(words[0]);
        for (int i = 1; i < words.Length; i++) {
            string w = words[i];
            if (Calc(w) == cnt) {
                char[] arr = w.ToCharArray();
                Array.Reverse(arr);
                w = new string(arr);
            }
            ans.Add(w);
        }
        return string.Join(" ", ans);
    }
}
