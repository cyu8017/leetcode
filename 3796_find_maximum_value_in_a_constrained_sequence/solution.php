<?php
// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

class Solution {
    function maxValue($n, $restrictions, $diff) {
        $INF = intdiv(2147483647, 4);
        $bound = array_fill(0, $n, $INF);
        $bound[0] = 0;
        foreach ($restrictions as $r) $bound[$r[0]] = $r[1];
        for ($i = 1; $i < $n; $i++) $bound[$i] = min($bound[$i], $bound[$i - 1] + $diff[$i - 1]);
        for ($i = $n - 2; $i >= 0; $i--) $bound[$i] = min($bound[$i], $bound[$i + 1] + $diff[$i]);
        $ans = $bound[0];
        for ($i = 1; $i < $n; $i++) $ans = max($ans, $bound[$i]);
        return $ans;
    }
}
