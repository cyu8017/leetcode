<?php
// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

class Solution {
    function maxPointsInsideSquare($points, $s) {
        $g = [];
        $keys = [];
        for ($i = 0; $i < count($points); $i++) {
            $key = max(abs($points[$i][0]), abs($points[$i][1]));
            if (!isset($g[$key])) {
                $g[$key] = [];
                $lo = 0;
                $hi = count($keys);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($keys[$mid] < $key) $lo = $mid + 1;
                    else $hi = $mid;
                }
                array_splice($keys, $lo, 0, [$key]);
            }
            $g[$key][] = $i;
        }
        $vis = array_fill(0, 26, false);
        $ans = 0;
        foreach ($keys as $key) {
            $list = $g[$key];
            foreach ($list as $i) {
                $j = ord($s[$i]) - 97;
                if ($vis[$j]) return $ans;
                $vis[$j] = true;
            }
            $ans += count($list);
        }
        return $ans;
    }
}
