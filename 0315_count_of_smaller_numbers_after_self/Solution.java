// LeetCode 0315 - Count of Smaller Numbers After Self

// https://leetcode.com/problems/count-of-smaller-numbers-after-self/



import java.util.ArrayList;

import java.util.List;



class Solution {

    public List<Integer> countSmaller(int[] nums) {

        List<Integer> sortedNums = new ArrayList<>();

        List<Integer> result = new ArrayList<>();

        for (int index = nums.length - 1; index >= 0; index--) {

            int num = nums[index];

            int position = lowerBound(sortedNums, num);

            result.add(position);

            sortedNums.add(position, num);

        }

        java.util.Collections.reverse(result);

        return result;

    }



    private int lowerBound(List<Integer> list, int target) {

        int left = 0;

        int right = list.size();

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (list.get(mid) < target) {

                left = mid + 1;

            } else {

                right = mid;

            }

        }

        return left;

    }

}

