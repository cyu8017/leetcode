<?php
// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

class Solution {
    function createCounter($init) {
        $cur = $init;
        return [
            'increment' => function() use (&$cur) { return ++$cur; },
            'decrement' => function() use (&$cur) { return --$cur; },
            'reset' => function() use ($init, &$cur) { $cur = $init; return $cur; },
        ];
    }
}
