// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

using System.Collections.Generic;

public class Solution {
    public IList<int> FindDisappearedNumbers(int[] nums) {
        foreach (int number in nums) {
            int index = System.Math.Abs(number) - 1;
            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }

        List<int> result = new List<int>();
        for (int index = 0; index < nums.Length; index++) {
            if (nums[index] > 0) {
                result.Add(index + 1);
            }
        }
        return result;
    }
}
