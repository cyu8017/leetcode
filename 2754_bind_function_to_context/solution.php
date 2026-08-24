<?php
// LeetCode 2754 - Bind Function to Context
// https://leetcode.com/problems/bind-function-to-context/

class Solution {
    function bindPolyfill($fn, $obj) {
        return function(...$args) use ($fn, $obj) {
            if (is_callable($fn)) {
                return $fn($obj, ...$args);
            }
            return null;
        };
    }
}
