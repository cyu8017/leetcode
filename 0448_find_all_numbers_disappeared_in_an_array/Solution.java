// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int number : nums) {
            int index = Math.abs(number) - 1;
            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int index = 0; index < nums.length; index++) {
            if (nums[index] > 0) {
                result.add(index + 1);
            }
        }
        return result;
    }
}
