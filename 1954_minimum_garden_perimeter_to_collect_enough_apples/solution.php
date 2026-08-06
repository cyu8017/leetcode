<?php
class Solution {
    /**
     * @param Integer $neededApples
     * @return Integer
     */
    function minimumPerimeter($neededApples) {
        $lo = 1;
        $hi = 100000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $apples = 2 * $mid * ($mid + 1) * (2 * $mid + 1);
            if ($apples >= $neededApples) {
                $hi = $mid;
            } else {
                $lo = $mid + 1;
            }
        }
        return 8 * $lo;
    }
}
