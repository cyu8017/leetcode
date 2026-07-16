<?php
// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

class Solution {
    /**
     * @param object $robot
     * @return void
     */
    function cleanRoom($robot) {
        $this->clean_room($robot);
    }

    /**
     * @param object $robot
     * @return void
     */
    function clean_room($robot) {
        $visited = [];
        $directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];

        $backtrack = function (int $row, int $col, int $direction) use (
            &$backtrack,
            &$visited,
            $directions,
            $robot
        ): void {
            $robot->clean();
            for ($step = 0; $step < 4; $step++) {
                $d = ($direction + $step) % 4;
                [$dr, $dc] = $directions[$d];
                $nextRow = $row + $dr;
                $nextCol = $col + $dc;
                $key = "{$nextRow},{$nextCol},{$d}";
                if (!isset($visited[$key]) && $robot->move()) {
                    $visited[$key] = true;
                    $backtrack($nextRow, $nextCol, $d);
                    $robot->turnRight();
                    $robot->turnRight();
                    $robot->move();
                    $robot->turnRight();
                    $robot->turnRight();
                }
                $robot->turnRight();
            }
        };

        $visited['0,0,0'] = true;
        $backtrack(0, 0, 0);
    }
}
