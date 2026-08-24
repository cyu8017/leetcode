<?php
// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $batteries
     * @return Integer
     */
    function maxRunTime($n, $batteries) {
        $sum = 0;
        foreach ($batteries as $b) $sum += $b;
        $lo = 1;
        $hi = intdiv($sum, $n);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            $need = 0;
            foreach ($batteries as $b) $need += min($b, $mid);
            if ($need >= $mid * $n) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
