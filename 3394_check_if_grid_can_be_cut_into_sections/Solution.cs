// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

using System;

public class Solution {
    bool CheckCut(int[][] rects, int axis) {
        var arr = new (int a, int b)[rects.Length];
        for (int i = 0; i < rects.Length; i++) {
            if (axis == 0) arr[i] = (rects[i][0], rects[i][2]);
            else arr[i] = (rects[i][1], rects[i][3]);
        }
        Array.Sort(arr, (x, y) => {
            if (x.a == y.a) return x.b.CompareTo(y.b);
            return x.a.CompareTo(y.a);
        });
        int cuts = 0;
        int end = arr[0].b;
        for (int i = 1; i < arr.Length; i++) {
            if (arr[i].a >= end) {
                cuts++;
                end = arr[i].b;
                if (cuts >= 2) return true;
            } else if (arr[i].b > end) {
                end = arr[i].b;
            }
        }
        return false;
    }

    public bool CheckValidCuts(int n, int[][] rectangles) {
        return CheckCut(rectangles, 0) || CheckCut(rectangles, 1);
    }
}
