// LeetCode 0350 - Intersection of Two Arrays II

// https://leetcode.com/problems/intersection-of-two-arrays-ii/



import java.util.ArrayList;

import java.util.HashMap;

import java.util.List;

import java.util.Map;



class Solution {

    public int[] intersect(int[] nums1, int[] nums2) {

        Map<Integer, Integer> counts = new HashMap<>();

        for (int num : nums1) {

            counts.put(num, counts.getOrDefault(num, 0) + 1);

        }



        List<Integer> result = new ArrayList<>();

        for (int num : nums2) {

            int count = counts.getOrDefault(num, 0);

            if (count > 0) {

                result.add(num);

                counts.put(num, count - 1);

            }

        }



        int[] output = new int[result.size()];

        for (int index = 0; index < result.size(); index++) {

            output[index] = result.get(index);

        }

        return output;

    }

}
