// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

class Solution {
    public int minimumTimeToInitialState(String word, int k) {
        int n = word.length();
        for (int i = k; i < n; i += k)
            if (word.substring(i).equals(word.substring(0, n - i))) return i / k;
        return (n + k - 1) / k;
    }
}
