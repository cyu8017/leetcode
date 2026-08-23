// LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

class Solution {
    public int maxDistance(String[] words) {
        int n = words.length, ans = 0;
        for (int i = 0; i < n; i++) {
            if (words[i] != words[0]) ans = Math.max(ans, i + 1);
            if (words[i] != words[n - 1]) ans = Math.max(ans, n - i);
        }
        return ans;
    }
}
