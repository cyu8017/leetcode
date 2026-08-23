// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

import java.util.Arrays;

class Solution {
    public long maxRatings(int[][] units) {
        int n = units[0].length;
        if (n == 1) {
            long ans = 0;
            for (var x : units) ans += x[0];
            return ans;
        }
        long answer = 0;
        int mn = Integer.MAX_VALUE, mn2 = Integer.MAX_VALUE;
        for (var x : units) {
            Arrays.sort(x);
            answer += x[1];
            mn2 = Math.min(mn2, x[1]);
            mn = Math.min(mn, x[0]);
        }
        return answer - (mn2 - mn);
    }
}
