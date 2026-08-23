// LeetCode 1574 - Shortest Subarray to be Removed to Make Array Sorted
// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

using System;

public class Solution {
    public int FindLengthOfShortestSubarray(int[] arr) {
        int n = arr.Length;
        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) right--;
        if (right == 0) return 0;
        int answer = right, left = 0;
        while (true) {
            while (right < n && arr[right] < arr[left]) right++;
            answer = Math.Min(answer, right - left - 1);
            left++;
            if (left >= n || arr[left - 1] > arr[left]) break;
        }
        return answer;
    }
}
