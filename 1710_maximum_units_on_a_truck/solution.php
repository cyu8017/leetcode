<?php
// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution {
    /**
     * @param Integer[][] $boxTypes
     * @param Integer $truckSize
     * @return Integer
     */
    function maximumUnits($boxTypes, $truckSize) {
        usort($boxTypes, function ($a, $b) {
            return $b[1] <=> $a[1];
        });
        $total = 0;
        foreach ($boxTypes as [$count, $units]) {
            $take = min($count, $truckSize);
            $total += $take * $units;
            $truckSize -= $take;
            if ($truckSize === 0) {
                break;
            }
        }
        return $total;
    }
}
