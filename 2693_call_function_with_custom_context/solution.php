<?php
// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

class Solution {
    function callPolyfill($fn, $obj, ...$args) {
        if ($fn instanceof Closure) {
            return $fn->call((object)$obj, ...$args);
        }
        return $fn(...$args);
    }
}
