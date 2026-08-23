// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

public class Solution {
    public int MaxFrequencyElements(int[] nums) {
        int[] cnt = new int[101];
        foreach (int x in nums) cnt[x]++;
        int mx = -1, ans = 0;
        foreach (int x in cnt) {
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
