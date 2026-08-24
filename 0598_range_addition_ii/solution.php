<?php
// LeetCode 0598 - Range Addition II
// https://leetcode.com/problems/range-addition-ii/

class Solution {
    function maxCount($m, $n, $ops) {
        foreach ($ops as $op) {
            $m = min($m, $op[0]);
            $n = min($n, $op[1]);
        }
        return $m * $n;
    }
}
