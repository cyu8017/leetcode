// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

public class Solution {
    public int FindKthPositive(int[] arr, int k) {
        int left = 0, right = arr.Length;
        while (left < right) {
            int middle = (left + right) / 2;
            if (arr[middle] - middle - 1 < k) left = middle + 1;
            else right = middle;
        }
        return left + k;
    }
}
