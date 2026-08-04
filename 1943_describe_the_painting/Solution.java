// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

import java.util.*;

class Solution {
    public List<List<Long>> splitPainting(int[][] segments) {
        TreeMap<Integer, Long> diff = new TreeMap<>();
        for (int[] seg : segments) {
            diff.merge(seg[0], (long) seg[2], Long::sum);
            diff.merge(seg[1], (long) -seg[2], Long::sum);
        }
        List<Integer> points = new ArrayList<>(diff.keySet());
        List<List<Long>> ans = new ArrayList<>();
        long cur = 0;
        for (int i = 0; i < points.size() - 1; i++) {
            cur += diff.get(points.get(i));
            if (cur != 0) ans.add(Arrays.asList((long) points.get(i), (long) points.get(i + 1), cur));
        }
        return ans;
    }
}
