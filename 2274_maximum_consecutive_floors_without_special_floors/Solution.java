// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

import java.util.Arrays;

class Solution {
    public int maxConsecutive(int bottom, int top, int[] special) {
        Arrays.sort(special);
        int ans = special[0] - bottom;
        for (int i = 1; i < special.length; i++)
            ans = Math.max(ans, special[i] - special[i - 1] - 1);
        ans = Math.max(ans, top - special[special.length - 1]);
        return ans;
    }
}
