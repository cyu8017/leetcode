// LeetCode 0373 - Find K Pairs with Smallest Sums

// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/



import java.util.ArrayList;

import java.util.List;

import java.util.PriorityQueue;



class Solution {

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {

        List<List<Integer>> result = new ArrayList<>();

        if (nums1.length == 0 || nums2.length == 0 || k == 0) {

            return result;

        }



        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));



        for (int index = 0; index < Math.min(nums1.length, k); index++) {

            heap.offer(new int[] { nums1[index] + nums2[0], index, 0 });

        }



        while (!heap.isEmpty() && result.size() < k) {

            int[] current = heap.poll();

            int index1 = current[1];

            int index2 = current[2];

            result.add(List.of(nums1[index1], nums2[index2]));

            if (index2 + 1 < nums2.length) {

                heap.offer(new int[] { nums1[index1] + nums2[index2 + 1], index1, index2 + 1 });

            }

        }



        return result;

    }

}
