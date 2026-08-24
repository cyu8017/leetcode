<?php
// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution {
    function maximumLengthSubstring($s) {
        $l = 0;
        $ans = 0;
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($r = 0; $r < $n; $r++) {
            $idx = ord($s[$r]) - 97;
            $cnt[$idx]++;
            while ($cnt[$idx] > 2) {
                $cnt[ord($s[$l]) - 97]--;
                $l++;
            }
            $ans = max($ans, $r - $l + 1);
        }
        return $ans;
    }
}
