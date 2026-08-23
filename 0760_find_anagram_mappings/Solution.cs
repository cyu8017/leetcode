// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

using System.Collections.Generic;

public class Solution {
    public int[] AnagramMappings(int[] nums1, int[] nums2) {
        var positions = new Dictionary<int, Queue<int>>();
        for (int i = 0; i < nums2.Length; i++) {
            if (!positions.ContainsKey(nums2[i])) positions[nums2[i]] = new Queue<int>();
            positions[nums2[i]].Enqueue(i);
        }
        int[] result = new int[nums1.Length];
        for (int i = 0; i < nums1.Length; i++) result[i] = positions[nums1[i]].Dequeue();
        return result;
    }
}
