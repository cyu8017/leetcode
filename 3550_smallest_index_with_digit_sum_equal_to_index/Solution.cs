// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

public class Solution {
    public int SmallestIndex(int[] nums) {
        for (int i = 0; i < nums.Length; i++) {
            int x = nums[i], s = 0;
            for (; x > 0; x /= 10) s += x % 10;
            if (s == i) return i;
        }
        return -1;
    }
}
