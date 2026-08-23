// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

public class Solution {
    public bool CarPooling(int[][] trips, int capacity) {
        int[] diff = new int[1001];
        foreach (var trip in trips) {
            diff[trip[1]] += trip[0];
            diff[trip[2]] -= trip[0];
        }
        int cur = 0;
        foreach (int x in diff) {
            cur += x;
            if (cur > capacity) {
                return false;
            }
        }
        return true;
    }
}
