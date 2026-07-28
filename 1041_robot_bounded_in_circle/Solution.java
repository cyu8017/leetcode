// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0, dx = 0, dy = 1;
        for (char ch : instructions.toCharArray()) {
            if (ch == 'G') {
                x += dx;
                y += dy;
            } else if (ch == 'L') {
                int tmp = dx;
                dx = -dy;
                dy = tmp;
            } else {
                int tmp = dx;
                dx = dy;
                dy = -tmp;
            }
        }
        return (x == 0 && y == 0) || !(dx == 0 && dy == 1);
    }
}
