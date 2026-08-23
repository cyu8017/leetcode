// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

public class Solution {
    bool Equal(int[] a, int as_, int ae, int[] b, int bs, int be) {
        if (ae - as_ != be - bs) return false;
        for (int i = 0; i < ae - as_; i++) if (a[as_ + i] != b[bs + i]) return false;
        return true;
    }

    public int BeautifulSplits(int[] nums) {
        int n = nums.Length;
        int ans = 0;
        for (int i = 1; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                bool ok = false;
                if (i <= j - i && Equal(nums, 0, i, nums, i, i + i)) ok = true;
                if (!ok && j - i <= n - j && Equal(nums, i, j, nums, j, j + (j - i))) ok = true;
                if (ok) ans++;
            }
        }
        return ans;
    }
}
