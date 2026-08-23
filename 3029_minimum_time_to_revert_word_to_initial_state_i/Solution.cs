// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

public class Solution {
    public int MinimumTimeToInitialState(string word, int k) {
        int n = word.Length;
        for (int i = k; i < n; i += k)
            if (word.Substring(i) == word.Substring(0, n - i)) return i / k;
        return (n + k - 1) / k;
    }
}
