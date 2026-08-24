<?php
// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

class Solution {
    function minCapability($nums, $k) {
        $lo = min($nums);
        $hi = max($nums);
        $ok = function($cap) use ($nums, $k) {
            $cnt = 0;
            $n = count($nums);
            for ($i = 0; $i < $n; ) {
                if ($nums[$i] <= $cap) {
                    $cnt++;
                    $i += 2;
                } else $i++;
            }
            return $cnt >= $k;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
