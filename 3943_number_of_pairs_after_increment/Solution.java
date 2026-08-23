// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long[] numberOfPairs(int[] nums1, int[] nums2, int[][] queries) {
        final int blockSize = 225;
        int n = nums2.length;
        int blocks = (n + blockSize - 1) / blockSize;
        int[] lazy = new int[blocks];
        Map<Integer, Integer>[] freq = new HashMap[blocks];
        for (int b = 0; b < blocks; b++) {
            freq[b] = new HashMap<>();
            rebuild(freq, nums2, b, blockSize, n);
        }
        Map<Integer, Integer> fixed = new HashMap<>();
        for (int x : nums1) fixed.put(x, fixed.getOrDefault(x, 0) + 1);
        java.util.List<Long> answer = new java.util.ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) {
                int l = q[1], r = q[2], delta = q[3];
                int first = l / blockSize, last = r / blockSize;
                if (first == last) {
                    push(lazy, nums2, first, blockSize, n);
                    for (int i = l; i <= r; i++) nums2[i] += delta;
                    rebuild(freq, nums2, first, blockSize, n);
                    continue;
                }
                push(lazy, nums2, first, blockSize, n);
                for (int i = l; i < (first + 1) * blockSize; i++) nums2[i] += delta;
                rebuild(freq, nums2, first, blockSize, n);
                push(lazy, nums2, last, blockSize, n);
                for (int i = last * blockSize; i <= r; i++) nums2[i] += delta;
                rebuild(freq, nums2, last, blockSize, n);
                for (int b = first + 1; b < last; b++) lazy[b] += delta;
            } else {
                long total = 0;
                for (Map.Entry<Integer, Integer> e : fixed.entrySet()) {
                    int a = e.getKey(), countA = e.getValue();
                    int target = q[1] - a;
                    for (int b = 0; b < blocks; b++) {
                        Integer c = freq[b].get(target - lazy[b]);
                        if (c != null) total += (long) countA * c;
                    }
                }
                answer.add(total);
            }
        }
        long[] out = new long[answer.size()];
        for (int i = 0; i < out.length; i++) out[i] = answer.get(i);
        return out;
    }

    private void rebuild(Map<Integer, Integer>[] freq, int[] nums2, int b, int blockSize, int n) {
        freq[b].clear();
        int end = Math.min((b + 1) * blockSize, n);
        for (int i = b * blockSize; i < end; i++) freq[b].put(nums2[i], freq[b].getOrDefault(nums2[i], 0) + 1);
    }

    private void push(int[] lazy, int[] nums2, int b, int blockSize, int n) {
        if (lazy[b] != 0) {
            int end = Math.min((b + 1) * blockSize, n);
            for (int i = b * blockSize; i < end; i++) nums2[i] += lazy[b];
            lazy[b] = 0;
        }
    }
}
