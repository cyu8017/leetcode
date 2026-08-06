<?php

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numOfWays($nums) {
        $MOD = 1000000007;
        $n = count($nums);
        $choose = array_fill(0, $n + 1, array_fill(0, $n + 1, 0));
        for ($i = 0; $i <= $n; $i++) {
            $choose[$i][0] = 1;
            $choose[$i][$i] = 1;
            for ($j = 1; $j < $i; $j++) {
                $choose[$i][$j] = ($choose[$i - 1][$j - 1] + $choose[$i - 1][$j]) % $MOD;
            }
        }

        $ways = function ($values) use (&$ways, &$choose, $MOD) {
            $len = count($values);
            if ($len < 3) {
                return 1;
            }
            $left = [];
            $right = [];
            for ($i = 1; $i < $len; $i++) {
                if ($values[$i] < $values[0]) {
                    $left[] = $values[$i];
                } else {
                    $right[] = $values[$i];
                }
            }
            return $choose[$len - 1][count($left)] * $ways($left) % $MOD * $ways($right) % $MOD;
        };

        return ($ways($nums) - 1 + $MOD) % $MOD;
    }
}
