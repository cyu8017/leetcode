<?php
// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

class Solution {
    function memoize($fn) {
        $cache = [];
        return function($x) use ($fn, &$cache) {
            $k = is_scalar($x) ? (string)$x : serialize($x);
            if (array_key_exists($k, $cache)) return $cache[$k];
            $r = $fn($x);
            $cache[$k] = $r;
            return $r;
        };
    }
}
