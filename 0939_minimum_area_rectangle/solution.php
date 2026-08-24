<?php
// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

class Solution {
    function minAreaRect($points) {
        $set = [];
        foreach ($points as $p) $set[$p[0] . "," . $p[1]] = true;
        $ans = PHP_INT_MAX;
        $n = count($points);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                [$x1, $y1] = $points[$i];
                [$x2, $y2] = $points[$j];
                if ($x1 === $x2 || $y1 === $y2) continue;
                if (isset($set[$x1 . "," . $y2]) && isset($set[$x2 . "," . $y1])) {
                    $ans = min($ans, abs($x1 - $x2) * abs($y1 - $y2));
                }
            }
        }
        return $ans === PHP_INT_MAX ? 0 : $ans;
    }
}
