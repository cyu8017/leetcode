// LeetCode 0373 - Find K Pairs with Smallest Sums

// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/



using System.Collections.Generic;



public class Solution {

    public IList<IList<int>> KSmallestPairs(int[] nums1, int[] nums2, int k) {

        List<IList<int>> result = new();

        if (nums1.Length == 0 || nums2.Length == 0 || k == 0) {

            return result;

        }



        PriorityQueue<(int total, int index1, int index2), int> heap = new();



        for (int index = 0; index < System.Math.Min(nums1.Length, k); index++) {

            heap.Enqueue((nums1[index] + nums2[0], index, 0), nums1[index] + nums2[0]);

        }



        while (heap.Count > 0 && result.Count < k) {

            var (_, index1, index2) = heap.Dequeue();

            result.Add(new List<int> { nums1[index1], nums2[index2] });

            if (index2 + 1 < nums2.Length) {

                int total = nums1[index1] + nums2[index2 + 1];

                heap.Enqueue((total, index1, index2 + 1), total);

            }

        }



        return result;

    }

}
