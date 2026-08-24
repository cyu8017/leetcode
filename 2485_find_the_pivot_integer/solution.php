<?php
// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

class Solution {
    function pivotInteger($n) {
        $total = intdiv($n * ($n + 1), 2);
        $sum = 0;
        for ($x = 1; $x <= $n; $x++) {
            $sum += $x;
            if ($sum === $total - $sum + $x) return $x;
        }
        return -1;
    }
}
