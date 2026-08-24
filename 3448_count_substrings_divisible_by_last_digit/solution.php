<?php
// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

class Solution {
    function countSubstrings($s) {
        $ans = 0;
        $n = strlen($s);
        for ($r = 0; $r < $n; $r++) {
            $last = ord($s[$r]) - 48;
            if ($last === 0) continue;
            $mod = 0;
            $p = 1 % $last;
            for ($l = $r; $l >= 0; $l--) {
                $mod = ($mod + (ord($s[$l]) - 48) * $p) % $last;
                $p = ($p * 10) % $last;
                if ($mod === 0) $ans++;
            }
        }
        return $ans;
    }
}
