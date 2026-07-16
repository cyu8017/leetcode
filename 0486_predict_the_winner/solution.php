<?php
// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

class Solution {
    /**
     * @param int[] $nums
     * @return bool
     */
    function predictTheWinner($nums) {
        return $this->predict_the_winner($nums);
    }

    /**
     * @param int[] $nums
     * @return bool
     */
    function predict_the_winner($nums) {
        $n = count($nums);
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            $dp[$i][$i] = $nums[$i];
        }
        for ($length = 2; $length <= $n; $length++) {
            for ($left = 0; $left <= $n - $length; $left++) {
                $right = $left + $length - 1;
                $dp[$left][$right] = max(
                    $nums[$left] - $dp[$left + 1][$right],
                    $nums[$right] - $dp[$left][$right - 1]
                );
            }
        }
        return $dp[0][$n - 1] >= 0;
    }
}
