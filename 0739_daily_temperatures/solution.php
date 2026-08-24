<?php
// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

class Solution {
    function dailyTemperatures($temperatures) {
        $n = count($temperatures);
        $answer = array_fill(0, $n, 0);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($stack) > 0 && $temperatures[$stack[count($stack) - 1]] < $temperatures[$i]) {
                $prev = array_pop($stack);
                $answer[$prev] = $i - $prev;
            }
            $stack[] = $i;
        }
        return $answer;
    }
}
