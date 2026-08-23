// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

public class Solution {
    public bool UniformArray(int[] nums1) {
        int mn = int.MaxValue;
        foreach (int x in nums1) {
            if (x % 2 == 1 && x < mn) mn = x;
        }
        foreach (int x in nums1) {
            if (x % 2 == 0 && mn != int.MaxValue && x < mn) return false;
        }
        return true;
    }
}
