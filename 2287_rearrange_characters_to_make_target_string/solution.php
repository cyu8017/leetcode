<?php
// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution {
    function rearrangeCharacters($s, $target) {
        $sc = array_fill(0, 26, 0);
        $tc = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $sc[ord($s[$i]) - 97]++;
        $tn = strlen($target);
        for ($i = 0; $i < $tn; $i++) $tc[ord($target[$i]) - 97]++;
        $ans = PHP_INT_MAX;
        for ($i = 0; $i < 26; $i++) {
            if ($tc[$i] === 0) continue;
            $ans = min($ans, intdiv($sc[$i], $tc[$i]));
        }
        return $ans;
    }
}
