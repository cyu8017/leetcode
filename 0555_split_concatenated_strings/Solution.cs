// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    public string SplitLoopedString(string[] strs) {
        var bestForms = new string[strs.Length];
        for (int i = 0; i < strs.Length; ++i) {
            string s = strs[i];
            string rev = Reverse(s);
            bestForms[i] = string.CompareOrdinal(s, rev) >= 0 ? s : rev;
        }

        string answer = "";
        for (int i = 0; i < strs.Length; ++i) {
            var mid = new StringBuilder();
            for (int j = i + 1; j < strs.Length; ++j) mid.Append(bestForms[j]);
            for (int j = 0; j < i; ++j) mid.Append(bestForms[j]);
            string midStr = mid.ToString();

            string[] candidates = { strs[i], Reverse(strs[i]) };
            foreach (string candidate in candidates) {
                for (int cut = 0; cut < candidate.Length; ++cut) {
                    string formed = candidate.Substring(cut) + midStr + candidate.Substring(0, cut);
                    if (string.CompareOrdinal(formed, answer) > 0) answer = formed;
                }
            }
        }
        return answer;
    }

    private static string Reverse(string s) {
        char[] arr = s.ToCharArray();
        System.Array.Reverse(arr);
        return new string(arr);
    }
}
