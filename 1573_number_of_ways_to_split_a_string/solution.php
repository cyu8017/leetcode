<?php

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function numWays($s) {
        $MOD = 1000000007;
        $ones = substr_count($s, '1');
        if ($ones % 3 !== 0) {
            return 0;
        }
        if ($ones === 0) {
            $gaps = strlen($s) - 1;
            return intdiv($gaps * ($gaps - 1), 2) % $MOD;
        }
        $target = intdiv($ones, 3);
        $positions = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '1') {
                $positions[] = $i;
            }
        }
        return ($positions[$target] - $positions[$target - 1])
            * ($positions[2 * $target] - $positions[2 * $target - 1])
            % $MOD;
    }
}
