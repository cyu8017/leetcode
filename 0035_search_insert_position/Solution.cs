// LeetCode 0035 - Search Insert Position
// https://leetcode.com/problems/search-insert-position/

public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.Length;

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
