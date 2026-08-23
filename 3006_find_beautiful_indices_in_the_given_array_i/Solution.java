// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    static void buildLPS(int[] lps, String pattern) {
        int l = 0, i = 1, s_l = pattern.length();
        lps[0] = 0;
        while (i < s_l) {
            if (pattern.charAt(i) == pattern.charAt(l)) {
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

    static void kmp(String s, String pat, int[] lps, List<Integer> index) {
        int s_len = s.length(), pat_l = pat.length();
        int i = 0, j = 0;
        while (s_len - i >= pat_l - j) {
            if (s.charAt(i) == pat.charAt(j)) {
                i++;
                j++;
            }
            if (j == pat_l) {
                index.add(i - pat_l);
                j = lps[j - 1];
            } else if (i < s_len && s.charAt(i) != pat.charAt(j)) {
                if (j != 0) j = lps[j - 1];
                else i++;
            }
        }
    }

    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        int a_len = a.length(), b_len = b.length();
        int[] lps_a = new int[a_len], lps_b = new int[b_len];
        List<Integer> a_index = new ArrayList<>();
        List<Integer> b_index = new ArrayList<>();
        List<Integer> result = new ArrayList<>();
        buildLPS(lps_a, a);
        buildLPS(lps_b, b);
        kmp(s, a, lps_a, a_index);
        kmp(s, b, lps_b, b_index);
        int i = 0, j = 0;
        while (i < a_index.size() && j < b_index.size()) {
            if (a_index.get(i) + k >= b_index.get(j) && a_index.get(i) - k <= b_index.get(j)) {
                result.add(a_index.get(i));
                i++;
            } else if (a_index.get(i) - k > b_index.get(j)) {
                j++;
            } else {
                i++;
            }
        }
        return result;
    }
}
