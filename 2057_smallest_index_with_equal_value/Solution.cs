// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

public class Solution {
    public int SmallestEqual(int[] nums) {
        for (int i = 0; i < nums.Length; i++)
            if (i % 10 == nums[i]) return i;
        return -1;
    }
}
