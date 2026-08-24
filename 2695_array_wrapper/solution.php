<?php
// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

class ArrayWrapper {
    private $nums;

    function __construct($nums) {
        $this->nums = $nums;
    }

    function valueOf() {
        $s = 0;
        foreach ($this->nums as $x) $s += $x;
        return $s;
    }

    function __toString() {
        return "[" . implode(",", $this->nums) . "]";
    }
}

class Solution {
    function ArrayWrapper($nums) {
        return new ArrayWrapper($nums);
    }
}
