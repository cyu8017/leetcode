// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int n = nums.length;
        int[] left = lis(nums);
        int[] reversed = new int[n];
        for (int i = 0; i < n; i++) {
            reversed[i] = nums[n - 1 - i];
        }
        int[] rightRev = lis(reversed);
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            right[i] = rightRev[n - 1 - i];
        }
        int best = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] > 1 && right[i] > 1) {
                best = Math.max(best, left[i] + right[i] - 1);
            }
        }
        return n - best;
    }

    private int[] lis(int[] a) {
        List<Integer> tails = new ArrayList<>();
        int[] out = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            int x = a[i];
            int idx = Collections.binarySearch(tails, x);
            if (idx < 0) {
                idx = -idx - 1;
            }
            if (idx == tails.size()) {
                tails.add(x);
            } else {
                tails.set(idx, x);
            }
            out[i] = idx + 1;
        }
        return out;
    }
}
