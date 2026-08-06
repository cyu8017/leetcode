<?php
// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumDivThree($nums) {
        $impossible = -1000000000000000000;
        $dp = [0, $impossible, $impossible];
        foreach ($nums as $value) {
            $old = $dp;
            foreach ($old as $total) {
                if ($total === $impossible) continue;
                $remainder = ($total + $value) % 3;
                $dp[$remainder] = max($dp[$remainder], $total + $value);
            }
        }
        return $dp[0];
    }
}
