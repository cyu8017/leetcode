// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

using System.Collections.Generic;
public class Solution {
    public bool IsPathCrossing(string path) {
        int x = 0, y = 0;
        var seen = new HashSet<(int,int)> { (0, 0) };
        foreach (char c in path) {
            if (c == 'N') y++; else if (c == 'S') y--; else if (c == 'E') x++; else x--;
            if (!seen.Add((x, y))) return true;
        }
        return false;
    }
}
