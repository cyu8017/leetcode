// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length();
        int n2 = s2.length();
        if (n1 > n2) {
            return false;
        }

        int[] need = new int[26];
        int[] window = new int[26];
        for (int i = 0; i < n1; ++i) {
            ++need[s1.charAt(i) - 'a'];
            ++window[s2.charAt(i) - 'a'];
        }

        int matches = 0;
        for (int i = 0; i < 26; ++i) {
            if (need[i] == window[i]) {
                ++matches;
            }
        }
        if (matches == 26) {
            return true;
        }

        for (int right = n1; right < n2; ++right) {
            int add = s2.charAt(right) - 'a';
            int remove = s2.charAt(right - n1) - 'a';

            if (window[add] == need[add]) {
                --matches;
            }
            ++window[add];
            if (window[add] == need[add]) {
                ++matches;
            }

            if (window[remove] == need[remove]) {
                --matches;
            }
            --window[remove];
            if (window[remove] == need[remove]) {
                ++matches;
            }

            if (matches == 26) {
                return true;
            }
        }
        return false;
    }
}
