<?php
// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution {
    function removeOccurrences($s, $part) {
        $stack = [];
        $m = strlen($part);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $stack[] = $s[$i];
            if (count($stack) >= $m && implode('', array_slice($stack, -$m)) === $part) {
                array_splice($stack, -$m);
            }
        }
        return implode('', $stack);
    }
}
