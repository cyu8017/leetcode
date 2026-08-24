<?php
// LeetCode 3801 - Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

class Solution {
    function minMergeCost($lists) {
        $m = count($lists);
        $totalMasks = 1 << $m;
        $merged = array_fill(0, $totalMasks, []);
        $length = array_fill(0, $totalMasks, 0);
        $median = array_fill(0, $totalMasks, 0);
        $trailingZeros = function($bit) {
            $n = 0;
            while (($bit & 1) === 0) { $bit >>= 1; $n++; }
            return $n;
        };
        for ($mask = 1; $mask < $totalMasks; $mask++) {
            $bit = $mask & -$mask;
            $index = $trailingZeros($bit);
            $previous = $merged[$mask ^ $bit];
            $current = $lists[$index];
            $out = [];
            $i = 0;
            $j = 0;
            while ($i < count($previous) || $j < count($current)) {
                if ($j === count($current) || ($i < count($previous) && $previous[$i] <= $current[$j])) {
                    $out[] = $previous[$i++];
                } else {
                    $out[] = $current[$j++];
                }
            }
            $merged[$mask] = $out;
            $length[$mask] = count($out);
            $median[$mask] = $out[intdiv(count($out) - 1, 2)];
        }
        $INF = PHP_INT_MAX;
        $dp = array_fill(0, $totalMasks, 0);
        for ($mask = 1; $mask < $totalMasks; $mask++) {
            if (($mask & ($mask - 1)) === 0) continue;
            $dp[$mask] = $INF;
            $firstBit = $mask & -$mask;
            for ($left = ($mask - 1) & $mask; $left > 0; $left = ($left - 1) & $mask) {
                if (($left & $firstBit) === 0) continue;
                $right = $mask ^ $left;
                if ($right === 0) continue;
                $diff = $median[$left] - $median[$right];
                if ($diff < 0) $diff = -$diff;
                $candidate = $dp[$left] + $dp[$right] + $length[$mask] + $diff;
                if ($candidate < $dp[$mask]) $dp[$mask] = $candidate;
            }
        }
        return $dp[$totalMasks - 1];
    }
}
