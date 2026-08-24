<?php
// LeetCode 3025 - Find the Number of Ways to Place People I
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

class Solution {
    function numberOfPairs($points) {
        usort($points, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $b[1] <=> $a[1];
        });
        $ans = 0;
        $n = count($points);
        for ($i = 0; $i < $n; $i++) {
            $y1 = $points[$i][1];
            $maxY = PHP_INT_MIN;
            for ($j = $i + 1; $j < $n; $j++) {
                $y2 = $points[$j][1];
                if ($maxY < $y2 && $y2 <= $y1) {
                    $maxY = $y2;
                    $ans++;
                }
            }
        }
        return $ans;
    }
}
