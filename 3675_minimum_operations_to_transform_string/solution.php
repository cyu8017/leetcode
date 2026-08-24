<?php
// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

class Solution {
    function minOperations($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c !== 'a') $ans = max($ans, 26 - (ord($c) - 97));
        }
        return $ans;
    }
}
