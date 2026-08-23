// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

public class Solution {
    public int FindUnsortedSubarray(int[] nums) {
        int n = nums.Length;
        int left = -1, right = -2;
        int maxSeen = nums[0], minSeen = nums[n - 1];
        for (int i = 0; i < n; ++i) {
            if (nums[i] > maxSeen) maxSeen = nums[i];
            if (nums[i] < maxSeen) right = i;
            int j = n - 1 - i;
            if (nums[j] < minSeen) minSeen = nums[j];
            if (nums[j] > minSeen) left = j;
        }
        return right - left + 1;
    }
}
