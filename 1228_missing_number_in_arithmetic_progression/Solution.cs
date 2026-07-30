// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

public class Solution {
    public int MissingNumber(int[] arr) {
        int difference = (arr[^1] - arr[0]) / arr.Length;
        for (int i = 1; i < arr.Length; i++) {
            int expected = arr[0] + i * difference;
            if (arr[i] != expected) return expected;
        }
        return arr[0];
    }
}
