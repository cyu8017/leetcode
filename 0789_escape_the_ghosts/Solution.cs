// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

using System;

public class Solution {
    public bool EscapeGhosts(int[][] ghosts, int[] target) {
        int targetDist = Math.Abs(target[0]) + Math.Abs(target[1]);
        foreach (var ghost in ghosts) {
            if (Math.Abs(ghost[0] - target[0]) + Math.Abs(ghost[1] - target[1]) <= targetDist) return false;
        }
        return true;
    }
}
