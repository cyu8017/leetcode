<?php
// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

class Solution {
    /**
     * @param int[] $nums
     * @return int
     */
    function totalHammingDistance($nums) {
        return $this->total_hamming_distance($nums);
    }

    /**
     * @param int[] $nums
     * @return int
     */
    function total_hamming_distance($nums) {
        $total = 0;
        for ($bit = 0; $bit < 32; $bit++) {
            $zeros = 0;
            $ones = 0;
            foreach ($nums as $value) {
                if (($value & (1 << $bit)) !== 0) {
                    $ones++;
                } else {
                    $zeros++;
                }
            }
            $total += $zeros * $ones;
        }
        return $total;
    }
}
