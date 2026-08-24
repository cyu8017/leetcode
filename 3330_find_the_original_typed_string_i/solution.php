<?php
// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution {
    function possibleStringCount($word) {
        $ans = 1;
        $n = strlen($word);
        for ($i = 1; $i < $n; $i++) {
            if ($word[$i] === $word[$i - 1]) $ans++;
        }
        return $ans;
    }
}
