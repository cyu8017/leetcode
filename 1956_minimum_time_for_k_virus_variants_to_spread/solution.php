<?php
class Solution {
    /**
     * @param Integer[][] $points
     * @param Integer $k
     * @return Integer
     */
    function minDayskVariants($points, $k) {
        $ans = PHP_INT_MAX;
        for ($x = 1; $x <= 100; $x++) {
            for ($y = 1; $y <= 100; $y++) {
                $dists = [];
                foreach ($points as $p) {
                    $dists[] = abs($p[0] - $x) + abs($p[1] - $y);
                }
                sort($dists);
                $ans = min($ans, $dists[$k - 1]);
            }
        }
        return $ans;
    }
}
