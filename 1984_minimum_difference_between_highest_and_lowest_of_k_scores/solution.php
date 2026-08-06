<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minimumDifference($nums, $k) {
        sort($nums);
        $best = PHP_INT_MAX;
        $n = count($nums);
        for ($i = 0; $i <= $n - $k; $i++) {
            $best = min($best, $nums[$i + $k - 1] - $nums[$i]);
        }
        return $best;
    }
}
