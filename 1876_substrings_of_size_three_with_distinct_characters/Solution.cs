// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

public class Solution {
    public int CountGoodSubstrings(string s) {
        if (s.Length < 3) {
            return 0;
        }
        int count = 0;
        for (int i = 0; i < s.Length - 2; i++) {
            char a = s[i], b = s[i + 1], c = s[i + 2];
            if (a != b && b != c && a != c) {
                count++;
            }
        }
        return count;
    }
}
