// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    int f(int x) {
        int s = 0;
        while (x != 0) { s += x % 10; x /= 10; }
        return s;
    }

    public int minSwaps(int[] nums) {
        int n = nums.length;
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) arr[i] = new int[] {f(nums[i]), nums[i]};
        Arrays.sort(arr, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        Map<Integer, Integer> d = new HashMap<>();
        for (int i = 0; i < n; i++) d.put(arr[i][1], i);
        boolean[] vis = new boolean[n];
        int ans = n;
        for (int i = 0; i < n; i++) {
            if (!vis[i]) {
                ans--;
                int j = i;
                while (!vis[j]) {
                    vis[j] = true;
                    j = d.get(nums[j]);
                }
            }
        }
        return ans;
    }
}
