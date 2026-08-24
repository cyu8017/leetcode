<?php
// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

class Solution {
    function maxPrice($items, $capacity) {
        usort($items, function($a, $b) {
            return $b[0] / $b[1] <=> $a[0] / $a[1];
        });
        $ans = 0.0;
        $remain = $capacity;
        foreach ($items as $it) {
            $price = $it[0];
            $weight = $it[1];
            if ($remain >= $weight) {
                $ans += $price;
                $remain -= $weight;
            } else {
                $ans += $price * $remain / $weight;
                $remain = 0;
                break;
            }
        }
        if ($remain > 0) return -1;
        return $ans;
    }
}
