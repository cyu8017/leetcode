<?php
// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

class Solution {
    function reformatNumber($number) {
        $s = preg_replace('/\D+/', '', $number);
        $out = [];
        while (strlen($s) > 4) {
            $out[] = substr($s, 0, 3);
            $s = substr($s, 3);
        }
        if (strlen($s) === 4) {
            $out[] = substr($s, 0, 2);
            $out[] = substr($s, 2);
        } elseif ($s !== "") {
            $out[] = $s;
        }
        return implode("-", $out);
    }
}
