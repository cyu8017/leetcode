// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        int maxLeft = 0;
        for (int pos : left) {
            maxLeft = Math.max(maxLeft, pos);
        }
        int minRight = n;
        for (int pos : right) {
            minRight = Math.min(minRight, pos);
        }
        return Math.max(maxLeft, n - minRight);
    }
}
