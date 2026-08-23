// LeetCode 3008 - Find Beautiful Indices in the Given Array II
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

using System.Collections.Generic;

public class Solution {
    static void BuildLPS(int[] lps, string pattern) {
        int l = 0, i = 1, s_l = pattern.Length;
        lps[0] = 0;
        while (i < s_l) {
            if (pattern[i] == pattern[l]) {
                l++;
                lps[i] = l;
                i++;
            } else if (l != 0) {
                l = lps[l - 1];
            } else {
                lps[i] = l;
                i++;
            }
        }
    }

    static void Kmp(string s, string pat, int[] lps, List<int> index) {
        int s_len = s.Length, pat_l = pat.Length;
        int i = 0, j = 0;
        while (s_len - i >= pat_l - j) {
            if (s[i] == pat[j]) {
                i++;
                j++;
            }
            if (j == pat_l) {
                index.Add(i - pat_l);
                j = lps[j - 1];
            } else if (i < s_len && s[i] != pat[j]) {
                if (j != 0) j = lps[j - 1];
                else i++;
            }
        }
    }

    public IList<int> BeautifulIndices(string s, string a, string b, int k) {
        int a_len = a.Length, b_len = b.Length;
        int[] lps_a = new int[a_len], lps_b = new int[b_len];
        var a_index = new List<int>();
        var b_index = new List<int>();
        var final = new List<int>();
        BuildLPS(lps_a, a);
        BuildLPS(lps_b, b);
        Kmp(s, a, lps_a, a_index);
        Kmp(s, b, lps_b, b_index);
        int i = 0, j = 0;
        while (i < a_index.Count && j < b_index.Count) {
            if (a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j]) {
                final.Add(a_index[i]);
                i++;
            } else if (a_index[i] - k > b_index[j]) {
                j++;
            } else {
                i++;
            }
        }
        return final;
    }
}
