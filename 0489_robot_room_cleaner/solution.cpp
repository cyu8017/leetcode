// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

#include <set>
#include <tuple>

class Solution {
    std::set<std::tuple<int, int, int>> visited_;
    static constexpr int directions_[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    void backtrack(Robot& robot, int row, int col, int direction) {
        robot.clean();
        for (int step = 0; step < 4; ++step) {
            const int nextDirection = (direction + step) % 4;
            const int nextRow = row + directions_[nextDirection][0];
            const int nextCol = col + directions_[nextDirection][1];
            if (visited_.count({nextRow, nextCol, nextDirection}) == 0 && robot.move()) {
                visited_.insert({nextRow, nextCol, nextDirection});
                backtrack(robot, nextRow, nextCol, nextDirection);
                robot.turnRight();
                robot.turnRight();
                robot.move();
                robot.turnRight();
                robot.turnRight();
            }
            robot.turnRight();
        }
    }

public:
    void cleanRoom(Robot& robot) {
        visited_.insert({0, 0, 0});
        backtrack(robot, 0, 0, 0);
    }
};
