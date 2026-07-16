// LeetCode 0075 - Sort Colors
// https://leetcode.com/problems/sort-colors/

public class Solution {
    public void SortColors(int[] nums) {
        int low = 0;
        int mid = 0;
        int high = nums.Length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                (nums[low], nums[mid]) = (nums[mid], nums[low]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                (nums[mid], nums[high]) = (nums[high], nums[mid]);
                high--;
            }
        }
    }
}
