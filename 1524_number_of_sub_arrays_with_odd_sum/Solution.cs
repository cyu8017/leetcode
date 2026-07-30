// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

public class Solution {
    public int NumOfSubarrays(int[] arr) {
        int[] counts = { 1, 0 };
        int parity = 0;
        long answer = 0;
        foreach (int value in arr) {
            parity ^= value & 1;
            answer += counts[parity ^ 1];
            counts[parity]++;
        }
        return (int)(answer % 1000000007);
    }
}
