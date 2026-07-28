// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

public class Solution {
    public bool IsRobotBounded(string instructions) {
        int x = 0, y = 0, dx = 0, dy = 1;
        foreach (char ch in instructions) {
            if (ch == 'G') { x += dx; y += dy; }
            else if (ch == 'L') { int t = dx; dx = -dy; dy = t; }
            else { int t = dx; dx = dy; dy = -t; }
        }
        return (x == 0 && y == 0) || !(dx == 0 && dy == 1);
    }
}
