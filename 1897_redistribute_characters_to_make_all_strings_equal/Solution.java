// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution {
    public boolean makeEqual(String[] words) {
        int[] counts = new int[26];
        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                counts[word.charAt(i) - 'a']++;
            }
        }
        int n = words.length;
        for (int total : counts) {
            if (total % n != 0) {
                return false;
            }
        }
        return true;
    }
}
