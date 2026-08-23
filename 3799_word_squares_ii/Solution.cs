// LeetCode 3799 - Word Squares Ii
// https://leetcode.com/problems/word-squares-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> WordSquares(string[] words) {
        Array.Sort(words);
        int n = words.Length;
        var ans = new List<IList<string>>();
        for (int i = 0; i < n; i++) {
            string top = words[i];
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                string left = words[j];
                for (int k = 0; k < n; k++) {
                    if (k == j || k == i) continue;
                    string right = words[k];
                    for (int h = 0; h < n; h++) {
                        if (h == k || h == j || h == i) continue;
                        string bottom = words[h];
                        if (top[0] == left[0] && top[3] == right[0] &&
                            bottom[0] == left[3] && bottom[3] == right[3]) {
                            ans.Add(new List<string> { top, left, right, bottom });
                        }
                    }
                }
            }
        }
        return ans;
    }
}
