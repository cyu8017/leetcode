// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

using System.Collections.Generic;

public class Solution {
    public IList<int> FindAnagrams(string s, string p) {
        if (p.Length > s.Length) {
            return new List<int>();
        }

        int[] need = new int[26];
        int[] window = new int[26];
        foreach (char ch in p) {
            need[ch - 'a']++;
        }

        List<int> result = new List<int>();
        int left = 0;
        for (int right = 0; right < s.Length; right++) {
            window[s[right] - 'a']++;
            if (right - left + 1 > p.Length) {
                window[s[left] - 'a']--;
                left++;
            }
            if (ArraysEqual(window, need)) {
                result.Add(left);
            }
        }
        return result;
    }

    private static bool ArraysEqual(int[] a, int[] b) {
        for (int i = 0; i < a.Length; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        return true;
    }
}
