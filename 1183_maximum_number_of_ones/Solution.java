// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

import java.util.*;

class Solution {
    public int maximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
        List<Integer> counts = new ArrayList<>();
        for (int r = 0; r < sideLength; r++) {
            for (int c = 0; c < sideLength; c++) {
                int rows = (height - r + sideLength - 1) / sideLength;
                int cols = (width - c + sideLength - 1) / sideLength;
                counts.add(rows * cols);
            }
        }
        counts.sort(Collections.reverseOrder());
        int ans = 0;
        for (int i = 0; i < maxOnes && i < counts.size(); i++) ans += counts.get(i);
        return ans;
    }
}
