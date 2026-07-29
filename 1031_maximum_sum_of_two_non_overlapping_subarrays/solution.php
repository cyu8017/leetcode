<?php
// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $firstLen
     * @param Integer $secondLen
     * @return Integer
     */
    function maxSumTwoNoOverlap($nums, $firstLen, $secondLen) {
        $prefix = [0];
        foreach ($nums as $x) {
            $prefix[] = end($prefix) + $x;
        }

        $best = function ($a, $b) use ($prefix) {
            $bestA = $ans = 0;
            $len = count($prefix);
            for ($i = $a + $b; $i < $len; $i++) {
                $bestA = max($bestA, $prefix[$i - $b] - $prefix[$i - $b - $a]);
                $ans = max($ans, $bestA + $prefix[$i] - $prefix[$i - $b]);
            }
            return $ans;
        };

        return max($best($firstLen, $secondLen), $best($secondLen, $firstLen));
    }
}
