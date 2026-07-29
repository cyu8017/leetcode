<?php
// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

class Solution {
    /**
     * @param String $instructions
     * @return Boolean
     */
    function isRobotBounded($instructions) {
        $x = $y = 0;
        $dx = 0;
        $dy = 1;
        $n = strlen($instructions);
        for ($i = 0; $i < $n; $i++) {
            $ch = $instructions[$i];
            if ($ch === 'G') {
                $x += $dx;
                $y += $dy;
            } elseif ($ch === 'L') {
                $tmp = $dx;
                $dx = -$dy;
                $dy = $tmp;
            } else {
                $tmp = $dx;
                $dx = $dy;
                $dy = -$tmp;
            }
        }
        return ($x === 0 && $y === 0) || !($dx === 0 && $dy === 1);
    }
}
