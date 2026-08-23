// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

class Solution {
    private boolean equal(int[] a, int as, int ae, int[] b, int bs, int be) {
        if (ae - as != be - bs) return false;
        for (int i = 0; i < ae - as; i++) if (a[as + i] != b[bs + i]) return false;
        return true;
    }

    public int beautifulSplits(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int i = 1; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                boolean ok = false;
                if (i <= j - i && equal(nums, 0, i, nums, i, i + i)) ok = true;
                if (!ok && j - i <= n - j && equal(nums, i, j, nums, j, j + (j - i))) ok = true;
                if (ok) ans++;
            }
        }
        return ans;
    }
}
