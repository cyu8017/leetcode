// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] diff = new int[1001];
        for (int[] t : trips) {
            diff[t[1]] += t[0];
            diff[t[2]] -= t[0];
        }
        int cur = 0;
        for (int x : diff) {
            cur += x;
            if (cur > capacity) {
                return false;
            }
        }
        return true;
    }
}
