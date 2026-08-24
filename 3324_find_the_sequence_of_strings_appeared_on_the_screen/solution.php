<?php
// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

class Solution {
    function stringSequence($target) {
        $ans = [];
        $cur = '';
        $n = strlen($target);
        for ($p = 0; $p < $n; $p++) {
            $ch = $target[$p];
            $cur .= 'a';
            $ans[] = $cur;
            while ($cur[strlen($cur) - 1] !== $ch) {
                $last = chr(ord($cur[strlen($cur) - 1]) + 1);
                $cur = substr($cur, 0, -1) . $last;
                $ans[] = $cur;
            }
        }
        return $ans;
    }
}
