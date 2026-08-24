<?php
// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

class Solution {
    function cancellable($fn, $args, $t) {
        $cancelled = false;
        $run = function() use ($fn, $args, &$cancelled) {
            if (!$cancelled) $fn(...$args);
        };
        return function() use (&$cancelled) {
            $cancelled = true;
        };
    }
}
