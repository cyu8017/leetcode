<?php
// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/

class Solution {
    function judgeCircle($moves) {
        $x = 0;
        $y = 0;
        $n = strlen($moves);
        for ($i = 0; $i < $n; ++$i) {
            $move = $moves[$i];
            if ($move === "U") ++$y;
            elseif ($move === "D") --$y;
            elseif ($move === "L") --$x;
            elseif ($move === "R") ++$x;
        }
        return $x === 0 && $y === 0;
    }
}
