// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

import java.util.*;

class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        Integer[] sorted1 = new Integer[nums1.length];
        for (int i = 0; i < nums1.length; i++) sorted1[i] = nums1[i];
        Arrays.sort(sorted1);
        Deque<Integer> dq = new ArrayDeque<>(Arrays.asList(sorted1));
        int[] ans = new int[nums1.length];
        int[][] indexed = new int[nums2.length][2];
        for (int i = 0; i < nums2.length; i++) {
            indexed[i][0] = nums2[i];
            indexed[i][1] = i;
        }
        Arrays.sort(indexed, (a, b) -> Integer.compare(b[0], a[0]));
        for (int[] pair : indexed) {
            int val = pair[0], i = pair[1];
            if (dq.peekLast() > val) ans[i] = dq.pollLast();
            else ans[i] = dq.pollFirst();
        }
        return ans;
    }
}
