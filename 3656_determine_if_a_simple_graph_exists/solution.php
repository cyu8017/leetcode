<?php
// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

class Solution {
    function simpleGraphExists($degrees) {
        $n = count($degrees);
        $d = $degrees;
        rsort($d);
        $sum = 0;
        foreach ($d as $x) {
            if ($x < 0 || $x >= $n) return false;
            $sum += $x;
        }
        if ($sum % 2 === 1) return false;
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $d[$i];
        for ($k = 1; $k <= $n; $k++) {
            $right = 0;
            for ($i = $k; $i < $n; $i++) $right += $d[$i] < $k ? $d[$i] : $k;
            if ($prefix[$k] > $k * ($k - 1) + $right) return false;
        }
        return true;
    }
}
