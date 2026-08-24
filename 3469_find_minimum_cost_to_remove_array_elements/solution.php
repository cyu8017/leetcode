<?php
// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

class Solution {
    function minCost($nums) {
        $n = count($nums);
        $memo = [];
        $max2 = function($a, $b) { return $a > $b ? $a : $b; };
        $min3 = function($a, $b, $c) { return min($a, min($b, $c)); };
        $dfs = null;
        $dfs = function($i, $prev) use (&$dfs, $n, $nums, &$memo, $max2, $min3) {
            if ($i >= $n) return $prev === -1 ? 0 : $nums[$prev];
            $k = $i . "," . $prev;
            if (isset($memo[$k])) return $memo[$k];
            if ($prev === -1) {
                if ($i + 1 >= $n) $res = $nums[$i];
                else if ($i + 2 >= $n) $res = $max2($nums[$i], $nums[$i + 1]);
                else {
                    $a = $nums[$i]; $b = $nums[$i + 1]; $c = $nums[$i + 2];
                    $res = $min3($max2($b, $c) + $dfs($i + 3, $i), $max2($a, $c) + $dfs($i + 3, $i + 1), $max2($a, $b) + $dfs($i + 3, $i + 2));
                }
            } else {
                if ($i + 1 >= $n) $res = $max2($nums[$prev], $nums[$i]);
                else {
                    $a = $nums[$prev]; $b = $nums[$i]; $c = $nums[$i + 1];
                    $res = $min3($max2($b, $c) + $dfs($i + 2, $prev), $max2($a, $c) + $dfs($i + 2, $i), $max2($a, $b) + $dfs($i + 2, $i + 1));
                }
            }
            $memo[$k] = $res;
            return $res;
        };
        return $dfs(0, -1);
    }
}
