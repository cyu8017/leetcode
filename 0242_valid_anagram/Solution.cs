// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) {
            return false;
        }
        int[] counts = new int[26];
        for (int index = 0; index < s.Length; index++) {
            counts[s[index] - 'a']++;
            counts[t[index] - 'a']--;
        }
        foreach (int count in counts) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
}
