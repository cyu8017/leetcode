// LeetCode 0315 - Count of Smaller Numbers After Self

// https://leetcode.com/problems/count-of-smaller-numbers-after-self/



using System.Collections.Generic;



public class Solution {

    public IList<int> CountSmaller(int[] nums) {

        List<int> sortedNums = new();

        List<int> result = new();

        for (int index = nums.Length - 1; index >= 0; index--) {

            int num = nums[index];

            int position = LowerBound(sortedNums, num);

            result.Add(position);

            sortedNums.Insert(position, num);

        }

        result.Reverse();

        return result;

    }



    private int LowerBound(List<int> list, int target) {

        int left = 0;

        int right = list.Count;

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (list[mid] < target) {

                left = mid + 1;

            } else {

                right = mid;

            }

        }

        return left;

    }

}

