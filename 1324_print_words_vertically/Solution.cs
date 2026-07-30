// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> PrintVertically(string s) {
        var words = s.Split(' ');
        int maxLen = 0;
        foreach (var w in words) maxLen = System.Math.Max(maxLen, w.Length);
        var answer = new List<string>();
        for (int i = 0; i < maxLen; i++) {
            var sb = new StringBuilder();
            foreach (var word in words) sb.Append(i < word.Length ? word[i] : ' ');
            answer.Add(sb.ToString().TrimEnd());
        }
        return answer;
    }
}
