// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution {
    public int maxDistToClosest(int[] seats) {
        int n = seats.length, prev = -1, ans = 0;
        for (int i = 0; i < n; i++) {
            if (seats[i] == 1) {
                if (prev == -1) ans = i;
                else ans = Math.max(ans, (i - prev) / 2);
                prev = i;
            }
        }
        return Math.max(ans, n - 1 - prev);
    }
}
