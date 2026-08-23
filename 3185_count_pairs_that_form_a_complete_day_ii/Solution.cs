// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

public class Solution {
    public long CountCompleteDayPairs(int[] hours) {
        int[] cnt = new int[24];
        long ans = 0;
        foreach (int x in hours) {
            ans += cnt[(24 - x % 24) % 24];
            cnt[x % 24]++;
        }
        return ans;
    }
}
