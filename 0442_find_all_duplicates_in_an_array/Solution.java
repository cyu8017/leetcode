// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();
        for (int number : nums) {
            int index = Math.abs(number) - 1;
            if (nums[index] < 0) {
                result.add(Math.abs(number));
            } else {
                nums[index] = -nums[index];
            }
        }
        return result;
    }
}
