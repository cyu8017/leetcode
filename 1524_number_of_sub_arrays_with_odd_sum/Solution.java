// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution {
    private static final int MOD = 1_000_000_007;

    public int numOfSubarrays(int[] arr) {
        int[] counts = {1, 0};
        int parity = 0;
        long answer = 0;
        for (int value : arr) {
            parity ^= value & 1;
            answer += counts[parity ^ 1];
            counts[parity]++;
        }
        return (int) (answer % MOD);
    }
}
