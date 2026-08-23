// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

import java.util.*;

class Solution {
    public int[][] chunk(int[] arr, int size) {
        List<int[]> ans = new ArrayList<>();
        for (int i = 0; i < arr.length; i += size) {
            int end = Math.min(arr.length, i + size);
            ans.add(Arrays.copyOfRange(arr, i, end));
        }
        return ans.toArray(new int[0][]);
    }
}
