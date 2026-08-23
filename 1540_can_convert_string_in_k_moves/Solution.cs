// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

public class Solution {
    public bool CanConvertString(string s, string t, int k) {
        if (s.Length != t.Length) return false;
        int[] used = new int[26];
        for (int i = 0; i < s.Length; i++) {
            int shift = (t[i] - s[i] + 26) % 26;
            if (shift == 0) continue;
            used[shift]++;
            if (shift + 26 * (used[shift] - 1) > k) return false;
        }
        return true;
    }
}
