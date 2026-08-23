// LeetCode 0396 - Rotate Function

// https://leetcode.com/problems/rotate-function/



using System.Linq;



public class Solution {

    public int MaxRotateFunction(int[] nums) {

        int total = nums.Sum();

        int current = 0;



        for (int index = 0; index < nums.Length; index++) {

            current += index * nums[index];

        }



        int best = current;



        for (int index = nums.Length - 1; index > 0; index--) {

            current += total - nums.Length * nums[index];

            best = int.Max(best, current);

        }



        return best;

    }

}
