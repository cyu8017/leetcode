<?php
// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subsetXORSum($nums) {
        $bits = 0;
        foreach ($nums as $num) {
            $bits |= $num;
        }

        $total = 0;
        $bit = 1;
        while ($bit <= $bits) {
            if ($bits & $bit) {
                $total += $bit;
            }
            $bit <<= 1;
        }

        return $total << (count($nums) - 1);
    }
}
