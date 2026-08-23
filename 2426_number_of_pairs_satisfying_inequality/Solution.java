// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution {
    private int[] arr, tmp;

    public long numberOfPairs(int[] nums1, int[] nums2, int diff) {
        int n = nums1.length;
        arr = new int[n];
        tmp = new int[n];
        for (int i = 0; i < n; i++) arr[i] = nums1[i] - nums2[i];
        return mergeCount(0, n, diff);
    }

    private long mergeCount(int l, int r, int diff) {
        if (r - l <= 1) return 0;
        int m = (l + r) / 2;
        long ans = MergeCount(l, m, diff) + MergeCount(m, r, diff);
        int j = m;
        for (int i = l; i < m; i++) {
            while (j < r && arr[j] < arr[i] - diff) j++;
            ans += r - j;
        }
        int p = l, q = m, i2 = l;
        while (p < m && q < r) {
            if (arr[p] <= arr[q]) tmp[i2++] = arr[p++];
            else tmp[i2++] = arr[q++];
        }
        while (p < m) tmp[i2++] = arr[p++];
        while (q < r) tmp[i2++] = arr[q++];
        for (int t = l; t < r; t++) arr[t] = tmp[t];
        return ans;
    }
}
