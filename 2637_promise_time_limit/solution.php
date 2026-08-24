<?php
// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

class Solution {
    function timeLimit($fn, $t) {
        return function(...$args) use ($fn, $t) {
            $start = microtime(true);
            $res = $fn(...$args);
            if ((microtime(true) - $start) * 1000 > $t) {
                throw new Exception("Time Limit Exceeded");
            }
            return $res;
        };
    }
}
