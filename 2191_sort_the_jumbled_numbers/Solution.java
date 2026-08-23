// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

import java.util.*;

class Solution {
    private int mapVal(int[] mapping, int x) {
        if (x == 0) return mapping[0];
        List<Integer> digits = new ArrayList<>();
        while (x > 0) { digits.add(x % 10); x /= 10; }
        int res = 0;
        for (int i = digits.size() - 1; i >= 0; i--)
            res = res * 10 + mapping[digits.get(i)];
        return res;
    }

    public int[] sortJumbled(int[] mapping, int[] nums) {
        int n = nums.length;
        int[][] arr = new int[n][3];
        for (int i = 0; i < n; i++) {
            arr[i][0] = mapVal(mapping, nums[i]);
            arr[i][1] = i;
            arr[i][2] = nums[i];
        }
        Arrays.sort(arr, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = arr[i][2];
        return ans;
    }
}
