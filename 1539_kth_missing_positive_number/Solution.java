// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

class Solution {
    public int findKthPositive(int[] arr, int k) {
        int left = 0;
        int right = arr.length;
        while (left < right) {
            int middle = left + (right - left) / 2;
            if (arr[middle] - middle - 1 < k) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return left + k;
    }
}
