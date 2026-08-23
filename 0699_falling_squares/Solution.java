// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

import java.util.*;

class Solution {
    public List<Integer> fallingSquares(int[][] positions) {
        List<int[]> intervals = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();
        int maxHeight = 0;
        for (int[] pos : positions) {
            int left = pos[0], side = pos[1], right = left + side, bas = 0;
            for (int[] it : intervals) {
                if (it[1] > left && it[0] < right) bas = Math.max(bas, it[2]);
            }
            int height = bas + side;
            intervals.add(new int[] {left, right, height});
            maxHeight = Math.max(maxHeight, height);
            answer.add(maxHeight);
        }
        return answer;
    }
}
