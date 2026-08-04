// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        int threshold = n / 4;
        for (int idx : new int[] {n / 4, n / 2, 3 * n / 4}) {
            int value = arr[idx];
            int count = 0;
            for (int x : arr) if (x == value) count++;
            if (count > threshold) return value;
        }
        return arr[0];
    }
}
