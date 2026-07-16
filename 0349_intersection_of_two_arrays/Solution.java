// LeetCode 0349 - Intersection of Two Arrays

// https://leetcode.com/problems/intersection-of-two-arrays/



import java.util.HashSet;

import java.util.Set;



class Solution {

    public int[] intersection(int[] nums1, int[] nums2) {

        Set<Integer> set1 = new HashSet<>();

        for (int num : nums1) {

            set1.add(num);

        }



        Set<Integer> set2 = new HashSet<>();

        for (int num : nums2) {

            set2.add(num);

        }



        set1.retainAll(set2);



        int[] result = new int[set1.size()];

        int index = 0;

        for (int num : set1) {

            result[index++] = num;

        }

        return result;

    }

}
