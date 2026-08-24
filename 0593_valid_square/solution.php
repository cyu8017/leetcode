<?php
// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

class Solution {
    function validSquare($p1, $p2, $p3, $p4) {
        $distSq = function($a, $b) {
            $dx = $a[0] - $b[0];
            $dy = $a[1] - $b[1];
            return $dx * $dx + $dy * $dy;
        };
        $points = [$p1, $p2, $p3, $p4];
        $distances = [];
        for ($i = 0; $i < 4; ++$i) {
            for ($j = $i + 1; $j < 4; ++$j) $distances[] = $distSq($points[$i], $points[$j]);
        }
        sort($distances);
        return $distances[0] > 0 && $distances[0] === $distances[1] && $distances[1] === $distances[2]
            && $distances[2] === $distances[3] && $distances[4] === $distances[5]
            && $distances[4] === 2 * $distances[0];
    }
}
