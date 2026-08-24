<?php
// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution {
    function divisibilityArray($word, $m) {
        $n = strlen($word);
        $ans = array_fill(0, $n, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur = ($cur * 10 + (ord($word[$i]) - 48)) % $m;
            if ($cur === 0) $ans[$i] = 1;
        }
        return $ans;
    }
}
