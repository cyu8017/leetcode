// LeetCode 0347 - Top K Frequent Elements

// https://leetcode.com/problems/top-k-frequent-elements/



using System.Collections.Generic;



public class Solution {

    public int[] TopKFrequent(int[] nums, int k) {

        Dictionary<int, int> counts = new();

        foreach (int num in nums) {

            counts[num] = counts.GetValueOrDefault(num) + 1;

        }



        List<int>[] buckets = new List<int>[nums.Length + 1];

        for (int index = 0; index < buckets.Length; index++) {

            buckets[index] = new List<int>();

        }



        foreach (KeyValuePair<int, int> entry in counts) {

            buckets[entry.Value].Add(entry.Key);

        }



        int[] result = new int[k];

        int writeIndex = 0;

        for (int index = buckets.Length - 1; index >= 0; index--) {

            foreach (int value in buckets[index]) {

                result[writeIndex++] = value;

                if (writeIndex == k) {

                    return result;

                }

            }

        }



        return result;

    }

}
