// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

public class Solution {
    public int MaxRepeating(string sequence, string word) {
        int k = 0;
        string cur = word;
        while (sequence.Contains(cur)) {
            k++;
            cur += word;
        }
        return k;
    }
}
