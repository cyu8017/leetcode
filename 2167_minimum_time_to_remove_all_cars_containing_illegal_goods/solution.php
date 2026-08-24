<?php
// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minimumTime($s) {
        $n = strlen($s);
        $left = array_fill(0, $n, 0);
        if ($s[0] === '1') $left[0] = 1;
        for ($i = 1; $i < $n; $i++) {
            $left[$i] = $left[$i - 1];
            if ($s[$i] === '1') $left[$i] = min($i + 1, $left[$i - 1] + 2);
        }
        $ans = $left[$n - 1];
        $right = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === '1') $right = min($n - $i, $right + 2);
            $leftCost = $i > 0 ? $left[$i - 1] : 0;
            $ans = min($ans, $leftCost + $right);
        }
        return $ans;
    }
}
