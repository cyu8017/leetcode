<?php
// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

class Solution {
    /**
     * @param Integer $n
     * @return Float
     */
    function soupServings($n) {
        if ($n >= 4800) return 1.0;
        $units = intdiv($n + 24, 25);
        $memo = [];
        $dp = function($a, $b) use (&$dp, &$memo) {
            if ($a <= 0 && $b <= 0) return 0.5;
            if ($a <= 0) return 1.0;
            if ($b <= 0) return 0.0;
            $key = ($a << 16) | $b;
            if (isset($memo[$key])) return $memo[$key];
            $val = 0.25 * ($dp($a - 4, $b) + $dp($a - 3, $b - 1) + $dp($a - 2, $b - 2) + $dp($a - 1, $b - 3));
            $memo[$key] = $val;
            return $val;
        };
        return $dp($units, $units);
    }
}
