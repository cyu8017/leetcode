<?php
// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

class Solution {
    function minOperations($nums, $x, $y) {
        $lo = 0;
        $hi = 0;
        foreach ($nums as $v) {
            $hi = max($hi, (int)ceil($v / $y));
            $hi = max($hi, (int)ceil($v / $x));
        }
        $hi += count($nums);
        $ok = function($ops) use ($nums, $x, $y) {
            $extra = 0;
            foreach ($nums as $v) {
                $remain = $v - $ops * $y;
                if ($remain > 0) $extra += (int)ceil($remain / ($x - $y));
            }
            return $extra <= $ops;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
