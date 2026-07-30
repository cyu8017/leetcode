// LeetCode 1437 - Check If All 1s Are At Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int previous = -k - 1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                if (i - previous <= k) return false;
                previous = i;
            }
        }
        return true;
    }
}
