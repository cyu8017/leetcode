// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

public class Solution {
    public int[] ResultArray(int[] nums, int k, int[][] queries) {
        int n = nums.Length;
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int idx = queries[qi][0], val = queries[qi][1], start = queries[qi][2], x = queries[qi][3];
            nums[idx] = val;
            int prod = 1, cnt = 0;
            for (int i = start; i < n; i++) {
                prod = prod * (nums[i] % k) % k;
                if (prod == x) cnt++;
            }
            ans[qi] = cnt;
        }
        return ans;
    }
}
