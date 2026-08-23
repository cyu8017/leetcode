// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

public class Solution {
    public int FindSmallestInteger(int[] nums, int value) {
        int[] cnt = new int[value];
        foreach (int x in nums) {
            int r = x % value;
            if (r < 0) r += value;
            cnt[r]++;
        }
        int mex = 0;
        while (cnt[mex % value] > 0) {
            cnt[mex % value]--;
            mex++;
        }
        return mex;
    }
}
