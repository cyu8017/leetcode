// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

class Solution {
    public boolean isMiddleElementUnique(int[] nums) {
        int mid = nums[nums.length / 2];
        int cnt = 0;
        for (int x : nums) {
            if (x == mid) cnt++;
        }
        return cnt == 1;
    }
}
