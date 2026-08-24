<?php
// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution {
    function longestCommonPrefix($arr1, $arr2) {
        $s = [];
        foreach ($arr1 as $x0) {
            for ($x = $x0; $x > 0; $x = intdiv($x, 10)) $s[$x] = true;
        }
        $mx = 0;
        foreach ($arr2 as $x0) {
            for ($x = $x0; $x > 0; $x = intdiv($x, 10)) {
                if (isset($s[$x])) {
                    $mx = max($mx, $x);
                    break;
                }
            }
        }
        return $mx > 0 ? strlen((string)$mx) : 0;
    }
}
