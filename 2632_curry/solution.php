<?php
// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

class Solution {
    function curry($fn) {
        $arity = (new ReflectionFunction($fn instanceof Closure ? $fn : Closure::fromCallable($fn)))->getNumberOfParameters();
        $curried = null;
        $curried = function(...$args) use ($fn, $arity, &$curried) {
            if (count($args) >= $arity) return $fn(...$args);
            return function(...$next) use ($curried, $args) {
                return $curried(...array_merge($args, $next));
            };
        };
        return $curried;
    }
}
