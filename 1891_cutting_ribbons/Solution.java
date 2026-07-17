// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

class Solution {
    public int maxLength(int[] ribbons, int k) {
        int lo = 1;
        int hi = max(ribbons);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(ribbons, mid, k)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return can(ribbons, lo, k) ? lo : 0;
    }

    private boolean can(int[] ribbons, int length, int k) {
        int count = 0;
        for (int ribbon : ribbons) {
            count += ribbon / length;
        }
        return count >= k;
    }

    private int max(int[] values) {
        int result = values[0];
        for (int value : values) {
            result = Math.max(result, value);
        }
        return result;
    }
}
