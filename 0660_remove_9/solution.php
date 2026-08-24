<?php
// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/

class Solution {
    function newInteger($n) {
        $result = 0;
        $base = 1;
        while ($n > 0) {
            $result += ($n % 9) * $base;
            $n = intdiv($n, 9);
            $base *= 10;
        }
        return $result;
    }
}
