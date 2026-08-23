// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        int[] cnt = new int[101];
        for (int x : nums) {
            cnt[x]++;
            if (cnt[x] >= 3) return false;
        }
        return true;
    }
}
