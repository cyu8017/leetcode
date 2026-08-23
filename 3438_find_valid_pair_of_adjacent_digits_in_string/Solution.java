// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

class Solution {
    public String findValidPair(String s) {
        int[] freq = new int[10];
        for (char c : s.toCharArray()) freq[c - '0']++;
        for (int i = 0; i + 1 < s.length(); i++) {
            int a = s.charAt(i) - '0', b = s.charAt(i + 1) - '0';
            if (a != b && freq[a] == a && freq[b] == b) return s.substring(i, i + 2);
        }
        return "";
    }
}
