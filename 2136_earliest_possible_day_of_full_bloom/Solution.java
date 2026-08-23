// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

import java.util.Arrays;

class Solution {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(growTime[b], growTime[a]));
        int day = 0, ans = 0;
        for (int i : idx) {
            day += plantTime[i];
            ans = Math.max(ans, day + growTime[i]);
        }
        return ans;
    }
}
