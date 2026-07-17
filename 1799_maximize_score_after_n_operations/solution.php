<?php
// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxScore($nums) {
        $n = count($nums);
        $full = (1 << $n) - 1;
        $memo = [];

        $gcd = function ($a, $b) use (&$gcd) {
            return $b === 0 ? $a : $gcd($b, $a % $b);
        };

        $dp = function ($mask) use (&$dp, &$memo, $nums, $n, $full, $gcd) {
            if ($mask === $full) return 0;
            if (isset($memo[$mask])) return $memo[$mask];
            $step = intdiv(substr_count(decbin($mask), '1'), 2) + 1;
            $best = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($mask >> $i & 1) continue;
                for ($j = $i + 1; $j < $n; $j++) {
                    if ($mask >> $j & 1) continue;
                    $score = $step * $gcd($nums[$i], $nums[$j]) + $dp($mask | (1 << $i) | (1 << $j));
                    if ($score > $best) $best = $score;
                }
            }
            $memo[$mask] = $best;
            return $best;
        };

        return $dp(0);
    }
}
