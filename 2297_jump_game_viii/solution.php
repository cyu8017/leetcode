<?php
// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

class Solution {
    function solve($nums, $costs) {
        $n = count($nums);
        $INF = PHP_INT_MAX / 4;
        $dp = array_fill(0, $n, $INF);
        $dp[0] = 0;
        $stack1 = [];
        $stack2 = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($stack1) && $nums[$stack1[count($stack1) - 1]] <= $nums[$i]) {
                $j = array_pop($stack1);
                $dp[$i] = min($dp[$i], $dp[$j] + $costs[$i]);
            }
            while (count($stack2) && $nums[$stack2[count($stack2) - 1]] > $nums[$i]) {
                $j = array_pop($stack2);
                $dp[$i] = min($dp[$i], $dp[$j] + $costs[$i]);
            }
            if (count($stack1)) $dp[$i] = min($dp[$i], $dp[$stack1[count($stack1) - 1]] + $costs[$i]);
            if (count($stack2)) $dp[$i] = min($dp[$i], $dp[$stack2[count($stack2) - 1]] + $costs[$i]);
            $stack1[] = $i;
            $stack2[] = $i;
        }
        return $dp[$n - 1];
    }
}
