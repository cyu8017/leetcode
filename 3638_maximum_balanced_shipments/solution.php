<?php
// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

class Solution {
    function maxBalancedShipments($weight) {
        $ans = 0;
        $mx = 0;
        foreach ($weight as $x) {
            $mx = max($mx, $x);
            if ($x < $mx) {
                $ans++;
                $mx = 0;
            }
        }
        return $ans;
    }
}
