// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution {
    public int minimumPushes(String word) {
        int n = word.length(), ans = 0, k = 1;
        for (int i = 0; i < n / 8; i++) {
            ans += k * 8;
            k++;
        }
        ans += k * (n % 8);
        return ans;
    }
}
