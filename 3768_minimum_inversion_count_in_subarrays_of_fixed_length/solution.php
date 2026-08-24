<?php
// LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

class Solution {
    function minInversionCount($nums, $k) {
        $vals = $nums;
        sort($vals);
        $n = 0;
        for ($i = 0; $i < count($vals); $i++) {
            if ($n === 0 || $vals[$i] !== $vals[$n - 1]) $vals[$n++] = $vals[$i];
        }
        $vals = array_slice($vals, 0, $n);
        $bit = array_fill(0, count($vals) + 1, 0);
        $add = function($i, $delta) use (&$bit) {
            for (; $i < count($bit); $i += $i & -$i) $bit[$i] += $delta;
        };
        $sum = function($i) use (&$bit) {
            $res = 0;
            for (; $i > 0; $i -= $i & -$i) $res += $bit[$i];
            return $res;
        };
        $lowerBound = function($a, $x) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $rank = array_fill(0, count($nums), 0);
        $inv = 0;
        for ($i = 0; $i < count($nums); $i++) {
            $rank[$i] = $lowerBound($vals, $nums[$i]) + 1;
            if ($i < $k) {
                $inv += $i - $sum($rank[$i]);
                $add($rank[$i], 1);
            }
        }
        $best = $inv;
        for ($r = $k; $r < count($nums); $r++) {
            $left = $rank[$r - $k];
            $inv -= $sum($left - 1);
            $add($left, -1);
            $inv += $k - 1 - $sum($rank[$r]);
            $add($rank[$r], 1);
            if ($inv < $best) $best = $inv;
        }
        return $best;
    }
}
