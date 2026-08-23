// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

public class Solution {
    public int[] SortArrayByParityII(int[] nums) {
        int n = nums.Length;
        int[] ans = new int[n];
        int even = 0, odd = 1;
        foreach (int x in nums) {
            if (x % 2 == 0) { ans[even] = x; even += 2; }
            else { ans[odd] = x; odd += 2; }
        }
        return ans;
    }
}
