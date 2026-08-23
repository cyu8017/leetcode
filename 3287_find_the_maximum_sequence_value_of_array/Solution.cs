// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

public class Solution {
    public int MaxValue(int[] nums, int k) {
        int n = nums.Length;
        const int MAX = 128;
        bool[,,] left = new bool[n + 1, k + 1, MAX];
        left[0, 0, 0] = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                for (int v = 0; v < MAX; v++) {
                    if (!left[i, j, v]) continue;
                    left[i + 1, j, v] = true;
                    if (j < k) left[i + 1, j + 1, v | nums[i]] = true;
                }
            }
        }
        bool[,,] right = new bool[n + 1, k + 1, MAX];
        right[n, 0, 0] = true;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= k; j++) {
                for (int v = 0; v < MAX; v++) {
                    if (!right[i + 1, j, v]) continue;
                    right[i, j, v] = true;
                    if (j < k) right[i, j + 1, v | nums[i]] = true;
                }
            }
        }
        int ans = 0;
        for (int mid = k; mid + k <= n; mid++) {
            for (int a = 0; a < MAX; a++) {
                if (!left[mid, k, a]) continue;
                for (int b = 0; b < MAX; b++) {
                    if (right[mid, k, b] && (a ^ b) > ans) ans = a ^ b;
                }
            }
        }
        return ans;
    }
}
