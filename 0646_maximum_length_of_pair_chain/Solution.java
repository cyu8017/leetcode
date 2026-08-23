// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

import java.util.Arrays;

class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[1], b[1]));
        int length = 0;
        int currentEnd = Integer.MIN_VALUE;
        for (int[] pair : pairs) {
            if (pair[0] > currentEnd) {
                ++length;
                currentEnd = pair[1];
            }
        }
        return length;
    }
}
