<?php
// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

class Solution {
    function reversePrefix($s, $k) {
        $arr = str_split($s);
        for ($i = 0, $j = $k - 1; $i < $j; $i++, $j--) {
            $t = $arr[$i]; $arr[$i] = $arr[$j]; $arr[$j] = $t;
        }
        return implode('', $arr);
    }
}
