// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution {
    public int[] constructArray(int n, int k) {
        int[] res = new int[n];
        int idx = 0;
        for (int i = 1; i <= n - k; ++i) {
            res[idx++] = i;
        }
        int left = n - k + 1;
        int right = n;
        boolean takeHigh = true;
        while (left <= right) {
            if (takeHigh) {
                res[idx++] = right--;
            } else {
                res[idx++] = left++;
            }
            takeHigh = !takeHigh;
        }
        return res;
    }
}
