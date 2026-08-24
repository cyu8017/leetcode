<?php
// LeetCode 3823 - Reverse Letters Then Special Characters in a String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution {
    function reverseByType($s) {
        $a = [];
        $b = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (($c >= 'A' && $c <= 'Z') || ($c >= 'a' && $c <= 'z')) $a[] = $c;
            else $b[] = $c;
        }
        $j = count($a);
        $k = count($b);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = $s[$i];
        for ($i = 0; $i < $n; $i++) {
            if (($arr[$i] >= 'A' && $arr[$i] <= 'Z') || ($arr[$i] >= 'a' && $arr[$i] <= 'z')) $arr[$i] = $a[--$j];
            else $arr[$i] = $b[--$k];
        }
        return implode('', $arr);
    }
}
