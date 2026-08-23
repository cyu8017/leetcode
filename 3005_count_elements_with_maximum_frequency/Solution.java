// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] cnt = new int[101];
        for (int x : nums) cnt[x]++;
        int mx = -1, ans = 0;
        for (int x : cnt) {
            if (mx < x) {
                mx = x;
                ans = x;
            } else if (mx == x) {
                ans += x;
            }
        }
        return ans;
    }
}
