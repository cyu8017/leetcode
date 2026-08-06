<?php
// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution {
    /**
     * @param Integer[] $data
     * @return Integer
     */
    function minSwaps($data) {
        $ones = array_sum($data);
        if ($ones <= 1) return 0;
        $cur = array_sum(array_slice($data, 0, $ones));
        $best = $cur;
        $n = count($data);
        for ($i = $ones; $i < $n; $i++) {
            $cur += $data[$i] - $data[$i - $ones];
            $best = max($best, $cur);
        }
        return $ones - $best;
    }
}
