<?php
// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

class Solution {
    function cancellable($generator) {
        $cancelled = false;
        $cancel = function() use (&$cancelled) { $cancelled = true; };
        $run = function() use ($generator, &$cancelled) {
            if ($generator instanceof Generator) {
                $next = $generator->current();
                while ($generator->valid()) {
                    if ($cancelled) {
                        $generator->throw(new Exception("Cancelled"));
                        continue;
                    }
                    $generator->send($next);
                    $next = $generator->current();
                }
                return $generator->getReturn();
            }
            return $generator;
        };
        return [$cancel, $run];
    }
}
