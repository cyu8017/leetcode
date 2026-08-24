<?php
// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

class Solution {
    function secondsToRemoveOccurrences($s) {
        $ans = 0;
        $zeros = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') $zeros++;
            elseif ($zeros > 0) $ans = max($ans + 1, $zeros);
        }
        return $ans;
    }
}
