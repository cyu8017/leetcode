<?php
// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

class Solution {
    function finalPositionOfSnake($n, $commands) {
        $x = 0;
        $y = 0;
        foreach ($commands as $c) {
            if ($c[0] === 'U') $x--;
            else if ($c[0] === 'D') $x++;
            else if ($c[0] === 'L') $y--;
            else if ($c[0] === 'R') $y++;
        }
        return $x * $n + $y;
    }
}
