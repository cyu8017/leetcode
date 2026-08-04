// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

class Solution {
    public int missingNumber(int[] arr) {
        int diff = (arr[arr.length - 1] - arr[0]) / arr.length;
        for (int i = 1; i < arr.length; i++) {
            int expected = arr[0] + i * diff;
            if (arr[i] != expected) return expected;
        }
        return arr[0];
    }
}

