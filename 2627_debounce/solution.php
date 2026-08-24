<?php
// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

class Solution {
    function debounce($fn, $t) {
        $timer = null;
        return function(...$args) use ($fn, $t, &$timer) {
            $timer = ['args' => $args, 't' => $t];
            return $fn(...$args);
        };
    }
}
