<?php
// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

class Solution {
    function sumImbalanceNumbers($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            $sorted = [];
            $imbalance = 0;
            for ($j = $i; $j < $n; $j++) {
                $x = $nums[$j];
                if (!isset($seen[$x])) {
                    $seen[$x] = true;
                    $lo = 0;
                    $hi = count($sorted);
                    while ($lo < $hi) {
                        $mid = ($lo + $hi) >> 1;
                        if ($sorted[$mid] < $x) $lo = $mid + 1;
                        else $hi = $mid;
                    }
                    $idx = $lo;
                    $next = $idx < count($sorted) ? $sorted[$idx] : null;
                    $prev = $idx > 0 ? $sorted[$idx - 1] : null;
                    if ($prev !== null && $x - $prev !== 1) $imbalance++;
                    if ($next !== null && $next - $x !== 1) $imbalance++;
                    if ($prev !== null && $next !== null && $next - $prev > 1) $imbalance--;
                    array_splice($sorted, $idx, 0, [$x]);
                }
                $ans += $imbalance;
            }
        }
        return $ans;
    }
}
