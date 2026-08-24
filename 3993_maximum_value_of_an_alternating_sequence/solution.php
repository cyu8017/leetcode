<?php
// LeetCode 3993 - Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

class Solution {
    function maximumValue($n, $s, $m) {
        if ($n == 1) return $s;
        return $s + intdiv($n, 2) * ($m - 1) + 1;
    }
}
