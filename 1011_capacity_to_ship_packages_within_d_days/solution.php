<?php
// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution {
    /**
     * @param Integer[] $weights
     * @param Integer $days
     * @return Integer
     */
    function shipWithinDays($weights, $days) {
        $lo = max($weights);
        $hi = array_sum($weights);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $need = 1;
            $cur = 0;
            foreach ($weights as $w) {
                if ($cur + $w > $mid) {
                    $need++;
                    $cur = 0;
                }
                $cur += $w;
            }
            if ($need <= $days) {
                $hi = $mid;
            } else {
                $lo = $mid + 1;
            }
        }
        return $lo;
    }
}
