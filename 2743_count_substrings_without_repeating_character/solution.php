<?php
// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

class Solution {
    function numberOfSpecialSubstrings($s) {
        $n = strlen($s);
        $ans = 0;
        $left = 0;
        $cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            $cnt[$c]++;
            while ($cnt[$c] > 1) {
                $cnt[ord($s[$left]) - 97]--;
                $left++;
            }
            $ans += $i - $left + 1;
        }
        return $ans;
    }
}
