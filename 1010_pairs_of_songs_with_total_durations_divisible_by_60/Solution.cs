// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

public class Solution {
    public int NumPairsDivisibleBy60(int[] time) {
        var count = new int[60];
        int ans = 0;
        foreach (int t in time) {
            ans += count[(60 - t % 60) % 60];
            count[t % 60]++;
        }
        return ans;
    }
}
