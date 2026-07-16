// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

import java.util.HashSet;
import java.util.Set;

class Solution {
    private final int[][] directions = new int[][] {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    private final Set<String> visited = new HashSet<>();

    public void cleanRoom(Robot robot) {
        visited.add("0,0,0");
        backtrack(robot, 0, 0, 0);
    }

    private void backtrack(Robot robot, int row, int col, int direction) {
        robot.clean();
        for (int step = 0; step < 4; step++) {
            int d = (direction + step) % 4;
            int nextRow = row + directions[d][0];
            int nextCol = col + directions[d][1];
            String key = nextRow + "," + nextCol + "," + d;
            if (!visited.contains(key) && robot.move()) {
                visited.add(key);
                backtrack(robot, nextRow, nextCol, d);
                robot.turnRight();
                robot.turnRight();
                robot.move();
                robot.turnRight();
                robot.turnRight();
            }
            robot.turnRight();
        }
    }
}
