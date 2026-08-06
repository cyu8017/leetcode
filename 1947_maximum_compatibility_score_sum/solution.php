<?php

class Solution {
    /**
     * @param Integer[][] $students
     * @param Integer[][] $mentors
     * @return Integer
     */
    function maxCompatibilitySum($students, $mentors) {
        $m = count($students);
        $score = array_fill(0, $m, array_fill(0, $m, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $s = 0;
                $len = count($students[$i]);
                for ($k = 0; $k < $len; $k++) {
                    if ($students[$i][$k] === $mentors[$j][$k]) {
                        $s++;
                    }
                }
                $score[$i][$j] = $s;
            }
        }

        $memo = [];
        $dp = function ($i, $mask) use (&$dp, &$memo, $m, &$score) {
            if ($i === $m) {
                return 0;
            }
            $key = $i . ',' . $mask;
            if (isset($memo[$key])) {
                return $memo[$key];
            }
            $best = 0;
            for ($j = 0; $j < $m; $j++) {
                if (($mask & (1 << $j)) === 0) {
                    $best = max($best, $score[$i][$j] + $dp($i + 1, $mask | (1 << $j)));
                }
            }
            return $memo[$key] = $best;
        };

        return $dp(0, 0);
    }
}
