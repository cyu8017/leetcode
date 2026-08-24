<?php
// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution {
    function fullBloomFlowers($flowers, $people) {
        $start = [];
        $end = [];
        foreach ($flowers as $f) { $start[] = $f[0]; $end[] = $f[1]; }
        sort($start);
        sort($end);
        $upperBound = function($a, $t) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] <= $t) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $lowerBound = function($a, $t) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $t) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = array_fill(0, count($people), 0);
        for ($i = 0; $i < count($people); $i++) {
            $t = $people[$i];
            $ans[$i] = $upperBound($start, $t) - $lowerBound($end, $t);
        }
        return $ans;
    }
}
