<?php
// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

class Solution {
    function cancellable($fn, $args, $t) {
        $fn(...$args);
        $cancelled = false;
        return function() use (&$cancelled) {
            $cancelled = true;
        };
    }
}
