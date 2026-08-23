// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

import java.util.PriorityQueue;

class Solution {
    private long modPow(long a, long e, long mod) {
        long r = 1;
        a %= mod;
        while (e > 0) {
            if ((e & 1) != 0) {
                r = r * a % mod;
            }
            a = a * a % mod;
            e >>= 1;
        }
        return r;
    }

    public int[] getFinalState(int[] nums, int k, int multiplier) {
        final int mod = 1000000007;
        if (multiplier == 1) {
            return nums;
        }
        PriorityQueue<int[]> h = new PriorityQueue<>((a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        int maxV = 0;
        for (int i = 0; i < nums.length; i++) {
            h.offer(new int[] {nums[i], i});
            if (nums[i] > maxV) {
                maxV = nums[i];
            }
        }
        while (k > 0 && !h.isEmpty()) {
            int[] cur = h.poll();
            int v = cur[0], i = cur[1];
            if ((long) v * multiplier > maxV && k >= nums.length) {
                h.offer(new int[] {v, i});
                break;
            }
            int nv = v * multiplier;
            nums[i] = nv;
            if (nv > maxV) {
                maxV = nv;
            }
            h.offer(new int[] {nv, i});
            k--;
        }
        if (k > 0) {
            int n = nums.length;
            int full = k / n, rem = k % n;
            long powFull = modPow(multiplier, full, mod);
            for (int i = 0; i < n; i++) {
                nums[i] = (int) ((long) nums[i] * powFull % mod);
            }
            PriorityQueue<int[]> hh = new PriorityQueue<>((a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
            for (int i = 0; i < n; i++) {
                hh.offer(new int[] {nums[i], i});
            }
            for (int t = 0; t < rem; t++) {
                int[] cur = hh.poll();
                int v = (int) ((long) cur[0] * multiplier % mod);
                int i = cur[1];
                nums[i] = v;
                hh.offer(new int[] {v, i});
            }
            for (int i = 0; i < n; i++) {
                nums[i] %= mod;
            }
        } else {
            for (int i = 0; i < nums.length; i++) {
                nums[i] %= mod;
            }
        }
        return nums;
    }
}
