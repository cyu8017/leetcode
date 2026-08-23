// LeetCode 0347 - Top K Frequent Elements

// https://leetcode.com/problems/top-k-frequent-elements/



import java.util.ArrayList;

import java.util.HashMap;

import java.util.List;

import java.util.Map;



class Solution {

    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> counts = new HashMap<>();

        for (int num : nums) {

            counts.put(num, counts.getOrDefault(num, 0) + 1);

        }



        List<Integer>[] buckets = new ArrayList[nums.length + 1];

        for (int index = 0; index < buckets.length; index++) {

            buckets[index] = new ArrayList<>();

        }



        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {

            buckets[entry.getValue()].add(entry.getKey());

        }



        int[] result = new int[k];

        int writeIndex = 0;

        for (int index = buckets.length - 1; index >= 0; index--) {

            for (int value : buckets[index]) {

                result[writeIndex++] = value;

                if (writeIndex == k) {

                    return result;

                }

            }

        }



        return result;

    }

}
