<?php
// LeetCode 3791 - Number of Balanced Integers in a Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

class Solution {
    function countBalanced($low, $high) {
        $BASE = 90;
        $num = '';
        $f = [];
        $initF = function() use (&$f) {
            $f = [];
            for ($i = 0; $i < 20; $i++) $f[$i] = array_fill(0, 181, -1);
        };
        $dfs = function($pos, $diff, $lim) use (&$dfs, &$f, &$num, $BASE) {
            if ($pos >= strlen($num)) return $diff === 0 ? 1 : 0;
            if (!$lim && $f[$pos][$diff + $BASE] !== -1) return $f[$pos][$diff + $BASE];
            $up = $lim ? ord($num[$pos]) - 48 : 9;
            $res = 0;
            for ($i = 0; $i <= $up; $i++) {
                if ($pos % 2 === 0) $res += $dfs($pos + 1, $diff + $i, $lim && $i === $up);
                else $res += $dfs($pos + 1, $diff - $i, $lim && $i === $up);
            }
            if (!$lim) $f[$pos][$diff + $BASE] = $res;
            return $res;
        };
        if ($high < 11) return 0;
        if ($low < 11) $low = 11;
        $num = strval($low - 1);
        $initF();
        $a = $dfs(0, 0, true);
        $num = strval($high);
        $initF();
        $b = $dfs(0, 0, true);
        return $b - $a;
    }
}
