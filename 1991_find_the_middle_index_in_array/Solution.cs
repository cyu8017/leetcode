// LeetCode 1991 - Find the Middle Index in Array
// https://leetcode.com/problems/find-the-middle-index-in-array/

using System.Linq;

public class Solution {
    public int FindMiddleIndex(int[] nums) {
        int total = nums.Sum(), left = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (left == total - left - nums[i]) return i;
            left += nums[i];
        }
        return -1;
    }
}