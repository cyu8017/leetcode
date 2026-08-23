// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int even = 0;
        for (int x : nums) if (x % 2 == 0) even += x;
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int val = queries[qi][0], i = queries[qi][1];
            if (nums[i] % 2 == 0) even -= nums[i];
            nums[i] += val;
            if (nums[i] % 2 == 0) even += nums[i];
            ans[qi] = even;
        }
        return ans;
    }
}
