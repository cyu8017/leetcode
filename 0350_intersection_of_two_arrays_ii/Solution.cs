// LeetCode 0350 - Intersection of Two Arrays II

// https://leetcode.com/problems/intersection-of-two-arrays-ii/



using System.Collections.Generic;



public class Solution {

    public int[] Intersect(int[] nums1, int[] nums2) {

        Dictionary<int, int> counts = new();

        foreach (int num in nums1) {

            counts[num] = counts.GetValueOrDefault(num) + 1;

        }



        List<int> result = new();

        foreach (int num in nums2) {

            int count = counts.GetValueOrDefault(num);

            if (count > 0) {

                result.Add(num);

                counts[num] = count - 1;

            }

        }



        return result.ToArray();

    }

}
