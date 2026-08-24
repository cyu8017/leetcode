<?php
// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

class Solution {
    function countRectangles($rectangles, $points) {
        $byH = [];
        for ($h = 0; $h <= 100; $h++) $byH[$h] = [];
        foreach ($rectangles as $r) $byH[$r[1]][] = $r[0];
        for ($h = 1; $h <= 100; $h++) sort($byH[$h]);
        $ans = array_fill(0, count($points), 0);
        for ($i = 0; $i < count($points); $i++) {
            $x = $points[$i][0];
            $y = $points[$i][1];
            $cnt = 0;
            for ($h = $y; $h <= 100; $h++) {
                $xs = $byH[$h];
                $lo = 0;
                $hi = count($xs);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($xs[$mid] < $x) $lo = $mid + 1;
                    else $hi = $mid;
                }
                $cnt += count($xs) - $lo;
            }
            $ans[$i] = $cnt;
        }
        return $ans;
    }
}
