// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

using System;

public class Solution {
    public int GetMaxLen(int[] nums) {
        int positive = 0, negative = 0, answer = 0;
        foreach (int x in nums) {
            if (x == 0) { positive = negative = 0; }
            else if (x > 0) {
                positive++;
                negative = negative > 0 ? negative + 1 : 0;
            } else {
                int newPos = negative > 0 ? negative + 1 : 0;
                negative = positive + 1;
                positive = newPos;
            }
            answer = Math.Max(answer, positive);
        }
        return answer;
    }
}
