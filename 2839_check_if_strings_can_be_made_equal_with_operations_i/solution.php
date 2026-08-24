<?php
// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution {
    function canBeEqual($s1, $s2) {
        $a = [$s1[0], $s1[2]];
        $b = [$s2[0], $s2[2]];
        $c = [$s1[1], $s1[3]];
        $d = [$s2[1], $s2[3]];
        sort($a);
        sort($b);
        sort($c);
        sort($d);
        return $a === $b && $c === $d;
    }
}
