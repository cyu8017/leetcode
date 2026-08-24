<?php
// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

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
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $ans = 1;
        $candidates = [];
        $seen = [];
        foreach ($nums as $x) {
            foreach ([$x - $k, $x, $x + $k] as $t) {
                if (!isset($seen[$t])) { $seen[$t] = true; $candidates[] = $t; }
            }
        }
        foreach ($candidates as $t) {
            $lo = $this->lowerBound($nums, $t - $k);
            $hi = $this->upperBound($nums, $t + $k);
            $can = $hi - $lo;
            $f = $freq[$t] ?? 0;
            $use = min($can, $f + $numOperations);
            if ($use > $ans) $ans = $use;
        }
        return $ans;
    }
}
