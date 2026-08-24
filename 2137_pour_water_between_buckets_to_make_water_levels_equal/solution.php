<?php
// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

class Solution {
    /**
     * @param Integer[] $buckets
     * @param Integer $loss
     * @return Float
     */
    function equalizeWater($buckets, $loss) {
        $lo = 0.0;
        $hi = 0.0;
        foreach ($buckets as $b) $hi = max($hi, $b);
        for ($iter = 0; $iter < 60; $iter++) {
            $mid = ($lo + $hi) / 2.0;
            $have = 0.0;
            $need = 0.0;
            foreach ($buckets as $b) {
                if ($b >= $mid) $have += $b - $mid;
                else $need += $mid - $b;
            }
            if ($have * (1.0 - $loss / 100.0) >= $need) $lo = $mid;
            else $hi = $mid;
        }
        return $lo;
    }
}
