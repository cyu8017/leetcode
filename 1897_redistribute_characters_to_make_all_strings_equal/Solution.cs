// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

public class Solution {
    public bool MakeEqual(string[] words) {
        var counts = new int[26];
        foreach (string word in words) {
            foreach (char ch in word) {
                counts[ch - 'a']++;
            }
        }
        int n = words.Length;
        foreach (int count in counts) {
            if (count % n != 0) {
                return false;
            }
        }
        return true;
    }
}
