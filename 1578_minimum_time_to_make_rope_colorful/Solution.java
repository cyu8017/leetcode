// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

import java.util.*;

class Solution {
    public int minCost(String colors, int[] neededTime) {
        int answer = 0;
        int maximum = 0;
        for (int i = 0; i < neededTime.length; i++) {
            if (i > 0 && colors.charAt(i) != colors.charAt(i - 1)) {
                maximum = 0;
            }
            answer += Math.min(maximum, neededTime[i]);
            maximum = Math.max(maximum, neededTime[i]);
        }
        return answer;
    }
}
