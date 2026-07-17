<?php
// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $goal
     * @return Integer
     */
    function minAbsDifference($nums, $goal) {
        $n = count($nums);
        $left = array_slice($nums, 0, intdiv($n, 2));
        $right = array_slice($nums, intdiv($n, 2));

        $sums = function ($arr) {
            $vals = [0];
            foreach ($arr as $x) {
                $size = count($vals);
                for ($i = 0; $i < $size; $i++) {
                    $vals[] = $vals[$i] + $x;
                }
            }
            sort($vals);
            return $vals;
        };

        $a = $sums($left);
        $b = $sums($right);
        $best = PHP_INT_MAX;
        $j = count($b) - 1;
        foreach ($a as $x) {
            while ($j > 0 && abs($x + $b[$j] - $goal) >= abs($x + $b[$j - 1] - $goal)) {
                $j--;
            }
            $best = min($best, abs($x + $b[$j] - $goal));
        }
        return $best;
    }
}
