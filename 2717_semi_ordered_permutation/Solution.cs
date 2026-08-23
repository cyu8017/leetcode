// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

public class Solution {
    public int SemiOrderedPermutation(int[] nums) {
        int n = nums.Length, p1 = 0, pn = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) p1 = i;
            if (nums[i] == n) pn = i;
        }
        int ans = p1 + (n - 1 - pn);
        if (p1 > pn) ans--;
        return ans;
    }
}
