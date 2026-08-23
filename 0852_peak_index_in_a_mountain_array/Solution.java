// LeetCode 0852 - Peak Index in a Mountain Array
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] < arr[mid + 1]) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
