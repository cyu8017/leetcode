// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

public class Solution {
    public string RestoreString(string s, int[] indices) {
        char[] answer = new char[s.Length];
        for (int i = 0; i < s.Length; i++) answer[indices[i]] = s[i];
        return new string(answer);
    }
}
