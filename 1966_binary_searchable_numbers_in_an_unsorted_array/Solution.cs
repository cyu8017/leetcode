// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

using System.Linq;

public class Solution {
    public int BinarySearchableNumbers(int[] nums) {
        int n = nums.Length;
        var ok = new int[n];
        for (int i = 0; i < n; i++) ok[i] = 1;
        int mx = int.MinValue, mi = int.MaxValue;
        for (int i = 0; i < n; i++) {
            if (nums[i] < mx) ok[i] = 0;
            else mx = nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] > mi) ok[i] = 0;
            else mi = nums[i];
        }
        return ok.Sum();
    }
}