// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

import java.util.Arrays;

class Solution {
    private boolean checkCut(int[][] rects, int axis) {
        int[][] arr = new int[rects.length][2];
        for (int i = 0; i < rects.length; i++) {
            if (axis == 0) {
                arr[i][0] = rects[i][0];
                arr[i][1] = rects[i][2];
            } else {
                arr[i][0] = rects[i][1];
                arr[i][1] = rects[i][3];
            }
        }
        Arrays.sort(arr, (x, y) -> x[0] == y[0] ? Integer.compare(x[1], y[1]) : Integer.compare(x[0], y[0]));
        int cuts = 0;
        int end = arr[0][1];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i][0] >= end) {
                cuts++;
                end = arr[i][1];
                if (cuts >= 2) return true;
            } else if (arr[i][1] > end) {
                end = arr[i][1];
            }
        }
        return false;
    }

    public boolean checkValidCuts(int n, int[][] rectangles) {
        return checkCut(rectangles, 0) || checkCut(rectangles, 1);
    }
}
