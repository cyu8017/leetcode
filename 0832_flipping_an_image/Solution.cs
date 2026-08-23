// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

using System;

public class Solution {
    public int[][] FlipAndInvertImage(int[][] image) {
        foreach (var row in image) {
            Array.Reverse(row);
            for (int i = 0; i < row.Length; i++) row[i] = 1 - row[i];
        }
        return image;
    }
}
