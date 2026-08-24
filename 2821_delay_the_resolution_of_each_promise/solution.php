<?php
// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/

class Solution {
    function delayAll($functions, $ms) {
        $out = [];
        foreach ($functions as $fn) {
            $out[] = function() use ($fn, $ms) {
                try {
                    $result = $fn();
                    return $result;
                } catch (Throwable $e) {
                    throw $e;
                }
            };
        }
        return $out;
    }
}
