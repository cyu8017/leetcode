<?php
// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

class Solution {
    function createCounter($n) {
        return function() use (&$n) {
            return $n++;
        };
    }
}
