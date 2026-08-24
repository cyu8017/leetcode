<?php
// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

class Solution {
    function throttle($fn, $t) {
        $last = -INF;
        $pending = null;
        return function(...$args) use ($fn, $t, &$last, &$pending) {
            $now = (int)round(microtime(true) * 1000);
            $remaining = $t - ($now - $last);
            if ($remaining <= 0) {
                $last = $now;
                $pending = null;
                return $fn(...$args);
            }
            $pending = $args;
            return null;
        };
    }
}
