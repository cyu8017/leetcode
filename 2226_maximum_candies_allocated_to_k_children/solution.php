<?php
// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution {
    function maximumCandies($candies, $k) {
        $mx = 0;
        foreach ($candies as $c) $mx = max($mx, $c);
        $lo = 0;
        $hi = $mx;
        $can = function($mid) use ($candies, $k) {
            if ($mid === 0) return true;
            $cnt = 0;
            foreach ($candies as $c) {
                $cnt += intdiv($c, $mid);
                if ($cnt >= $k) return true;
            }
            return false;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($can($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
