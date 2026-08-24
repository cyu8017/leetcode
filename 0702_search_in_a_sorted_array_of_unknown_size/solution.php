<?php
// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

class Solution {
    function search($reader, $target) {
        if (is_array($reader)) {
            $secret = $reader;
            $reader = new class($secret) {
                private $secret;
                function __construct($secret) { $this->secret = $secret; }
                function get($index) {
                    if ($index < 0 || $index >= count($this->secret)) return 2147483647;
                    return $this->secret[$index];
                }
            };
        }
        $right = 1;
        while ($reader->get($right) < $target) $right <<= 1;
        $left = $right >> 1;
        while ($left <= $right) {
            $mid = $left + intdiv($right - $left, 2);
            $value = $reader->get($mid);
            if ($value === $target) return $mid;
            if ($value > $target) $right = $mid - 1;
            else $left = $mid + 1;
        }
        return -1;
    }
}
