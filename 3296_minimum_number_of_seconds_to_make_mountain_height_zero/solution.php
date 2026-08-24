<?php
// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

class Solution {
    function ok($t, $mountainHeight, $workerTimes) {
        $total = 0;
        foreach ($workerTimes as $w) {
            $l = 0;
            $h = $mountainHeight;
            while ($l < $h) {
                $mid = intdiv($l + $h + 1, 2);
                if ($w * $mid * ($mid + 1) / 2 <= $t) $l = $mid;
                else $h = $mid - 1;
            }
            $total += $l;
            if ($total >= $mountainHeight) return true;
        }
        return $total >= $mountainHeight;
    }

    function minNumberOfSeconds($mountainHeight, $workerTimes) {
        $lo = 0;
        $hi = 1e18;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->ok($mid, $mountainHeight, $workerTimes)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
