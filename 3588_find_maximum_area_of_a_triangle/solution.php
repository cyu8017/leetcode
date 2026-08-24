<?php
// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

class Solution {
    private function calc(&$coords) {
        $mn = 1e9;
        $mx = 0;
        $f = [];
        $g = [];
        foreach ($coords as $c) {
            $x = $c[0];
            $y = $c[1];
            $mn = min($mn, $x);
            $mx = max($mx, $x);
            if (isset($f[$x])) {
                $f[$x] = min($f[$x], $y);
                $g[$x] = max($g[$x], $y);
            } else {
                $f[$x] = $y;
                $g[$x] = $y;
            }
        }
        $ans = 0;
        foreach ($f as $x => $y) {
            $d = $g[$x] - $y;
            $ans = max($ans, $d * max($mx - $x, $x - $mn));
        }
        return $ans;
    }

    function maxArea($coords) {
        $ans = $this->calc($coords);
        foreach ($coords as &$c) {
            $t = $c[0];
            $c[0] = $c[1];
            $c[1] = $t;
        }
        unset($c);
        $ans = max($ans, $this->calc($coords));
        return $ans > 0 ? $ans : -1;
    }
}
