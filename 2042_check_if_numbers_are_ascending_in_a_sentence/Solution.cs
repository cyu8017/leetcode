// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

public class Solution {
    public bool AreNumbersAscending(string s) {
        int prev = -1;
        foreach (var tok in s.Split(' ', System.StringSplitOptions.RemoveEmptyEntries)) {
            if (tok[0] >= '0' && tok[0] <= '9') {
                int v = int.Parse(tok);
                if (v <= prev) return false;
                prev = v;
            }
        }
        return true;
    }
}
