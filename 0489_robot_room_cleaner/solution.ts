// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

interface Robot {
    move(): boolean;
    turnLeft(): void;
    turnRight(): void;
    clean(): void;
}

export class Solution {
    cleanRoom(robot: Robot): void {
        const visited = new Set<string>();
        const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];

        const backtrack = (row: number, col: number, direction: number): void => {
            robot.clean();
            for (let step = 0; step < 4; step += 1) {
                const d = (direction + step) % 4;
                const [dr, dc] = directions[d];
                const nextRow = row + dr;
                const nextCol = col + dc;
                const key = `${nextRow},${nextCol},${d}`;
                if (!visited.has(key) && robot.move()) {
                    visited.add(key);
                    backtrack(nextRow, nextCol, d);
                    robot.turnRight();
                    robot.turnRight();
                    robot.move();
                    robot.turnRight();
                    robot.turnRight();
                }
                robot.turnRight();
            }
        };

        visited.add("0,0,0");
        backtrack(0, 0, 0);
    }
}
