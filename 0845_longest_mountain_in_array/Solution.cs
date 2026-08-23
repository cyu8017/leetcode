// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

using System;

public class Solution {
    public int LongestMountain(int[] arr) {
        int n = arr.Length, ans = 0, i = 0;
        while (i < n) {
            int j = i;
            if (j + 1 < n && arr[j] < arr[j + 1]) {
                while (j + 1 < n && arr[j] < arr[j + 1]) j++;
                if (j + 1 < n && arr[j] > arr[j + 1]) {
                    while (j + 1 < n && arr[j] > arr[j + 1]) j++;
                    ans = Math.Max(ans, j - i + 1);
                    i = j;
                    continue;
                }
            }
            i++;
        }
        return ans;
    }
}
