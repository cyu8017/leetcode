<?php
// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution {
    /**
     * @param String $s
     * @param Integer $n
     * @return Boolean
     */
    function queryString($s, $n) {
        for ($i = $n; $i > intdiv($n, 2); $i--) {
            if (strpos($s, decbin($i)) === false) {
                return false;
            }
        }
        return true;
    }
}
