<?php
// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

class Solution {
    function once($fn) {
        $called = false;
        $res = null;
        return function(...$args) use ($fn, &$called, &$res) {
            if ($called) return null;
            $called = true;
            $res = $fn(...$args);
            return $res;
        };
    }
}
