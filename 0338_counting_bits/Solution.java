// LeetCode 0338 - Counting Bits

// https://leetcode.com/problems/counting-bits/



class Solution {

    public int[] countBits(int n) {

        int[] result = new int[n + 1];

        for (int index = 1; index <= n; index++) {

            result[index] = result[index & (index - 1)] + 1;

        }

        return result;

    }

}
