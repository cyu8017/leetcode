<?php
// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

class Solution {
    function validateStackSequences($pushed, $popped) {
        $stack = [];
        $j = 0;
        foreach ($pushed as $x) {
            $stack[] = $x;
            while ($stack && $stack[count($stack) - 1] === $popped[$j]) {
                array_pop($stack);
                $j++;
            }
        }
        return count($stack) === 0;
    }
}
