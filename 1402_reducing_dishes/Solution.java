// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

import java.util.*;

class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        Arrays.sort(satisfaction); Array.Reverse(satisfaction);
        int total = 0, answer = 0;
        for (int value : satisfaction) {
            if (total + value <= 0) break;
            total += value; answer += total;
        }
        return answer;
    }
}
