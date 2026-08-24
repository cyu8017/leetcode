<?php
// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

class Solution {
    /**
     * @param String $path
     * @return String
     */
    function simplifyPath($path) {
        $stack = [];

        foreach (explode('/', $path) as $part) {
            if ($part === '' || $part === '.') {
                continue;
            }
            if ($part === '..') {
                if (!empty($stack)) {
                    array_pop($stack);
                }
            } else {
                $stack[] = $part;
            }
        }

        return '/' . implode('/', $stack);
    }
}
