<?php
// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

class Solution {
    /**
     * @param Integer[][] $towers
     * @param Integer $radius
     * @return Integer[]
     */
    function bestCoordinate($towers, $radius) {
        $best = [0, 0];
        $quality = -1;
        for ($x = 0; $x <= 50; $x++) {
            for ($y = 0; $y <= 50; $y++) {
                $q = 0;
                foreach ($towers as $t) {
                    $d = hypot($x - $t[0], $y - $t[1]);
                    if ($d <= $radius) {
                        $q += intval($t[2] / (1 + $d));
                    }
                }
                if ($q > $quality) {
                    $quality = $q;
                    $best = [$x, $y];
                }
            }
        }
        return $best;
    }
}
