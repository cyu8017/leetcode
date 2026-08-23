// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

using System;

public class Solution {
    public int MaxChunksToSorted(int[] arr) {
        int chunks = 0, maxSoFar = 0;
        for (int i = 0; i < arr.Length; i++) {
            maxSoFar = Math.Max(maxSoFar, arr[i]);
            if (maxSoFar == i) chunks++;
        }
        return chunks;
    }
}
