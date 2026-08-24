<?php
// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

class Solution {
    function calPoints($operations) {
        $stack = [];
        foreach ($operations as $op) {
            if ($op === 'C') array_pop($stack);
            else if ($op === 'D') $stack[] = $stack[count($stack) - 1] * 2;
            else if ($op === '+') $stack[] = $stack[count($stack) - 1] + $stack[count($stack) - 2];
            else $stack[] = intval($op, 10);
        }
        $total = 0;
        foreach ($stack as $value) $total += $value;
        return $total;
    }
}
