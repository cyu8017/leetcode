// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

import java.util.*;

class Solution {
    public int getMaxLen(int[] nums) {
        int positive = 0;
        int negative = 0;
        int answer = 0;
        for (int x : nums) {
            if (x == 0) {
                positive = 0;
                negative = 0;
            } else if (x > 0) {
                positive++;
                negative = negative == 0 ? 0 : negative + 1;
            } else {
                int nextPositive = negative == 0 ? 0 : negative + 1;
                negative = positive + 1;
                positive = nextPositive;
            }
            answer = Math.max(answer, positive);
        }
        return answer;
    }
}
