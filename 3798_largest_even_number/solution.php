<?php
// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

class Solution {
    function largestEven($s) {
        while (strlen($s) > 0 && $s[strlen($s) - 1] === '1') $s = substr($s, 0, strlen($s) - 1);
        return $s;
    }
}
