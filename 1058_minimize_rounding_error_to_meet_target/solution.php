<?php
// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

class Solution {
    /**
     * @param String[] $prices
     * @param Integer $target
     * @return String
     */
    function minimizeError($prices, $target) {
        $floors = 0;
        $fracs = [];
        foreach ($prices as $p) {
            $value = (float)$p;
            $floor = (int)$value;
            $floors += $floor;
            $frac = $value - $floor;
            if ($frac > 1e-9) {
                $fracs[] = $frac;
            }
        }
        $ceilCount = $target - $floors;
        if ($ceilCount < 0 || $ceilCount > count($fracs)) {
            return "-1";
        }
        rsort($fracs);
        $error = 0.0;
        for ($i = 0; $i < count($fracs); $i++) {
            if ($i < $ceilCount) {
                $error += 1 - $fracs[$i];
            } else {
                $error += $fracs[$i];
            }
        }
        return sprintf("%.3f", $error);
    }
}
