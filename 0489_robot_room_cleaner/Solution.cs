// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

public interface Robot {
    bool Move();
    void TurnLeft();
    void TurnRight();
    void Clean();
}

public class Solution {
    private readonly int[][] directions = new int[][] { new[] { -1, 0 }, new[] { 0, 1 }, new[] { 1, 0 }, new[] { 0, -1 } };
    private readonly HashSet<string> visited = new();

    public void CleanRoom(Robot robot) {
        visited.Add("0,0,0");
        Backtrack(robot, 0, 0, 0);
    }

    private void Backtrack(Robot robot, int row, int col, int direction) {
        robot.Clean();
        for (int step = 0; step < 4; step++) {
            int d = (direction + step) % 4;
            int nextRow = row + directions[d][0];
            int nextCol = col + directions[d][1];
            string key = $"{nextRow},{nextCol},{d}";
            if (!visited.Contains(key) && robot.Move()) {
                visited.Add(key);
                Backtrack(robot, nextRow, nextCol, d);
                robot.TurnRight();
                robot.TurnRight();
                robot.Move();
                robot.TurnRight();
                robot.TurnRight();
            }
            robot.TurnRight();
        }
    }
}
