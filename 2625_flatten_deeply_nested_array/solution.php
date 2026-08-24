<?php
// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

class Solution {
    function flat($arr, $n) {
        $res = [];
        $dfs = function($a, $depth) use (&$dfs, &$res, $n) {
            foreach ($a as $x) {
                if (is_array($x) && $depth < $n) $dfs($x, $depth + 1);
                else $res[] = $x;
            }
        };
        $dfs($arr, 0);
        return $res;
    }
}
