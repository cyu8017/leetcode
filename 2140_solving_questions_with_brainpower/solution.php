<?php
// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution {
    /**
     * @param Integer[][] $questions
     * @return Integer
     */
    function mostPoints($questions) {
        $n = count($questions);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $pts = $questions[$i][0];
            $brain = $questions[$i][1];
            $next = $i + $brain + 1;
            $take = $pts + ($next < $n ? $dp[$next] : 0);
            $dp[$i] = max($dp[$i + 1], $take);
        }
        return $dp[0];
    }
}
