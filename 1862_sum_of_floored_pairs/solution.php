<?php
// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfFlooredPairs($nums) {
        $mod = 1000000007;
        $maxVal = max($nums);
        $count = array_fill(0, $maxVal + 1, 0);
        foreach ($nums as $num) {
            $count[$num]++;
        }

        $prefix = array_fill(0, $maxVal + 1, 0);
        $prefix[0] = $count[0];
        for ($value = 1; $value <= $maxVal; $value++) {
            $prefix[$value] = $prefix[$value - 1] + $count[$value];
        }

        $answer = 0;
        for ($divisor = 1; $divisor <= $maxVal; $divisor++) {
            if ($count[$divisor] === 0) {
                continue;
            }
            $quotient = 1;
            while ($quotient * $divisor <= $maxVal) {
                $low = $quotient * $divisor;
                $high = min(($quotient + 1) * $divisor - 1, $maxVal);
                $matches = $prefix[$high] - ($low ? $prefix[$low - 1] : 0);
                $answer = ($answer + $count[$divisor] * $matches * $quotient) % $mod;
                $quotient++;
            }
        }

        return $answer;
    }
}
