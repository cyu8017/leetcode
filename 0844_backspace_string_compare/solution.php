<?php
// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function backspaceCompare($s, $t) {
        $build = function($text) {
            $stack = [];
            $n = strlen($text);
            for ($i = 0; $i < $n; $i++) {
                $ch = $text[$i];
                if ($ch === '#') {
                    if (count($stack)) array_pop($stack);
                } else {
                    $stack[] = $ch;
                }
            }
            return implode('', $stack);
        };
        return $build($s) === $build($t);
    }
}
