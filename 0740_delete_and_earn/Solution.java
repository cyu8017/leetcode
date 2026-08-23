// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

class Solution {
    public int deleteAndEarn(int[] nums) {
        if (nums.length == 0) return 0;
        int maxNum = 0;
        for (int num : nums) maxNum = Math.max(maxNum, num);
        int[] points = new int[maxNum + 1];
        for (int num : nums) points[num] += num;
        int take = 0, skip = 0;
        for (int value : points) {
            int newTake = skip + value;
            int newSkip = Math.max(skip, take);
            take = newTake;
            skip = newSkip;
        }
        return Math.max(take, skip);
    }
}
