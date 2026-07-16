// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

using System.Collections.Generic;

public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        List<int> result = new List<int>();
        foreach (int number in nums) {
            int index = System.Math.Abs(number) - 1;
            if (nums[index] < 0) {
                result.Add(System.Math.Abs(number));
            } else {
                nums[index] = -nums[index];
            }
        }
        return result;
    }
}
