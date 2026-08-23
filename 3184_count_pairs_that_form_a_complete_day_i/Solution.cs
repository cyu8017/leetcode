// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

public class Solution {
    public int CountCompleteDayPairs(int[] hours) {
        int[] cnt = new int[24];
        int ans = 0;
        foreach (int x in hours) {
            ans += cnt[(24 - x % 24) % 24];
            cnt[x % 24]++;
        }
        return ans;
    }
}
