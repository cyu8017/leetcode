<?php
// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

class Solution {
    function replicate($str, $times) {
        $res = '';
        for ($i = 0; $i < $times; $i++) $res .= $str;
        return $res;
    }
}
