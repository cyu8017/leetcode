// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

public class Solution {
    public int SmallestBalancedIndex(int[] nums) {
        long s = 0, p = 1;
        foreach (int x in nums) s += x;
        for (int i = nums.Length - 1; i >= 0; i--) {
            s -= nums[i];
            if (s == p) return i;
            p *= nums[i];
            if (p >= s) break;
        }
        return -1;
    }
}
