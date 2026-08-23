// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution {
    static int Popcount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }

    public boolean canSortArray(int[] nums) {
        int preMx = 0;
        int i = 0, n = nums.length;
        while (i < n) {
            int cnt = Popcount(nums[i]);
            int j = i + 1;
            int mi = nums[i], mx = nums[i];
            while (j < n && Popcount(nums[j]) == cnt) {
                mi = Math.min(mi, nums[j]);
                mx = Math.max(mx, nums[j]);
                j++;
            }
            if (preMx > mi) return false;
            preMx = mx;
            i = j;
        }
        return true;
    }
}
