<?php
// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

class Solution {
    function minCuttingCost($n, $m, $k) {
        $x = max($n, $m);
        if ($x <= $k) return 0;
        return $k * ($x - $k);
    }
}
