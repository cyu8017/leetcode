// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution {
    public boolean areOccurrencesEqual(String s) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) freq[s.charAt(i) - 'a']++;
        int target = 0;
        for (int f : freq) {
            if (f == 0) continue;
            if (target == 0) target = f;
            else if (f != target) return false;
        }
        return true;
    }
}
