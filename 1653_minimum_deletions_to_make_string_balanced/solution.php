<?php
// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution {
    function minimumDeletions($s) {
        $b = 0;
        $ans = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === "b") $b++;
            else $ans = min($ans + 1, $b);
        }
        return $ans;
    }
}
