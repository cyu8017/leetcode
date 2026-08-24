// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        int even = 0, odd = 1;
        for (int x : nums) {
            if (x % 2 == 0) { ans[even] = x; even += 2; }
            else { ans[odd] = x; odd += 2; }
        }
        return ans;
    }
}
