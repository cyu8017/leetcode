// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

class Solution {
    public void duplicateZeros(int[] arr) {
        int zeros = 0;
        for (int x : arr) {
            if (x == 0) {
                zeros++;
            }
        }
        int n = arr.length;
        for (int i = n - 1; i >= 0; i--) {
            if (i + zeros < n) {
                arr[i + zeros] = arr[i];
            }
            if (arr[i] == 0) {
                zeros--;
                if (i + zeros < n) {
                    arr[i + zeros] = 0;
                }
            }
        }
    }
}
