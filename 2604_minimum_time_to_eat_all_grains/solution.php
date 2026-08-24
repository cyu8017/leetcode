<?php
// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

class Solution {
    function minimumTime($hens, $grains) {
        sort($hens);
        sort($grains);
        $ok = function($t) use ($hens, $grains) {
            $j = 0;
            $m = count($grains);
            foreach ($hens as $h) {
                if ($j >= $m) return true;
                if ($grains[$j] >= $h) {
                    while ($j < $m && $grains[$j] - $h <= $t) $j++;
                } else {
                    if ($h - $grains[$j] > $t) return false;
                    $left = $h - $grains[$j];
                    $maxRight1 = $t - 2 * $left;
                    $maxRight2 = intdiv($t - $left, 2);
                    $reach = $h;
                    if ($maxRight1 > $maxRight2) {
                        if ($maxRight1 > 0) $reach = $h + $maxRight1;
                    } else {
                        if ($maxRight2 > 0) $reach = $h + $maxRight2;
                    }
                    while ($j < $m && $grains[$j] <= $reach) $j++;
                }
            }
            return $j >= $m;
        };
        $lo = 0;
        $hi = 2000000000;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
