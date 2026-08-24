<?php
// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

class Solution {
    function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] < $x) $lo = $mid + 1; else $hi = $mid;
        }
        return $lo;
    }

    function upperBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] <= $x) $lo = $mid + 1; else $hi = $mid;
        }
        return $lo;
    }

    function maxFrequency($nums, $k, $numOperations) {
        sort($nums);
        $n = count($nums);
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $ans = 1;
        foreach ($freq as $t => $f) {
            $lo = $this->lowerBound($nums, $t - $k);
            $hi = $this->upperBound($nums, $t + $k);
            $can = $hi - $lo;
            $use = min($can, $f + $numOperations);
            if ($use > $ans) $ans = $use;
        }
        $l = 0;
        for ($r = 0; $r < $n; $r++) {
            while ($nums[$r] - $nums[$l] > 2 * $k) $l++;
            $window = min($r - $l + 1, $numOperations);
            if ($window > $ans) $ans = $window;
        }
        return $ans;
    }
}
