<?php
// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

class Solution {
    function promisify($fn) {
        return function(...$args) use ($fn) {
            $err = null;
            $result = null;
            $fn(function($e, $r = null) use (&$err, &$result) {
                $err = $e;
                $result = $r;
            }, ...$args);
            if ($err) throw new Exception(is_string($err) ? $err : json_encode($err));
            return $result;
        };
    }
}
