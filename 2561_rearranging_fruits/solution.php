<?php
// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

class Solution {
    function minCost($basket1, $basket2) {
        $freq = [];
        $mn = PHP_INT_MAX;
        foreach ($basket1 as $x) {
            $freq[$x] = ($freq[$x] ?? 0) + 1;
            if ($x < $mn) $mn = $x;
        }
        foreach ($basket2 as $x) {
            $freq[$x] = ($freq[$x] ?? 0) - 1;
            if ($x < $mn) $mn = $x;
        }
        $extra = [];
        foreach ($freq as $k => $v) {
            if ($v % 2 !== 0) return -1;
            $times = intdiv(abs($v), 2);
            for ($i = 0; $i < $times; $i++) $extra[] = $k;
        }
        sort($extra);
        $ans = 0;
        $half = intdiv(count($extra), 2);
        for ($i = 0; $i < $half; $i++) {
            $ans += min($extra[$i], 2 * $mn);
        }
        return $ans;
    }
}
