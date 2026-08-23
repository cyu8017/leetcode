// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

import java.util.*;

class Solution {
    public int[] anagramMappings(int[] nums1, int[] nums2) {
        Map<Integer, Queue<Integer>> positions = new HashMap<>();
        for (int i = 0; i < nums2.length; i++) {
            positions.computeIfAbsent(nums2[i], k -> new ArrayDeque<>()).offer(i);
        }
        int[] result = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) result[i] = positions.get(nums1[i]).poll();
        return result;
    }
}
