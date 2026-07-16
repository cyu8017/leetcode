// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

class Solution {
    public int[] grayCode(int n) {
        int size = 1 << n;
        int[] result = new int[size];
        for (int i = 0; i < size; i++) {
            result[i] = i ^ (i >> 1);
        }
        return result;
    }
}
