<?php
// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

class Solution {
    function totalReplacements($ranks) {
        $ans = 0;
        $cur = $ranks[0];
        foreach ($ranks as $x) {
            if ($x < $cur) {
                $cur = $x;
                $ans++;
            }
        }
        return $ans;
    }
}
