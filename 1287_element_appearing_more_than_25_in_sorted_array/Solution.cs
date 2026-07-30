// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

public class Solution {
    public int FindSpecialInteger(int[] arr) {
        int n = arr.Length;
        int threshold = n / 4;
        foreach (int idx in new[] { n / 4, n / 2, 3 * n / 4 }) {
            int value = arr[idx];
            int count = 0;
            foreach (int x in arr) if (x == value) count++;
            if (count > threshold) return value;
        }
        return arr[0];
    }
}
