<?php
// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function numSquares($n) {
        $squares = [];
        for ($value = 1; $value * $value <= $n; $value++) {
            $squares[] = $value * $value;
        }

        $queue = [[$n, 0]];
        $visited = [$n => true];

        while (!empty($queue)) {
            [$remain, $steps] = array_shift($queue);
            if ($remain === 0) {
                return $steps;
            }
            foreach ($squares as $square) {
                $next = $remain - $square;
                if ($next < 0) {
                    break;
                }
                if (empty($visited[$next])) {
                    $visited[$next] = true;
                    $queue[] = [$next, $steps + 1];
                }
            }
        }
        return 0;
    }
}
