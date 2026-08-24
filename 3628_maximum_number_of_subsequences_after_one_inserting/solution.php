<?php
// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

class Solution {
    function numOfSubsequences($s) {
        $calc = function($str, $t) {
            $cnt = 0;
            $a = 0;
            $n = strlen($str);
            for ($i = 0; $i < $n; $i++) {
                $c = $str[$i];
                if ($c === $t[1]) $cnt += $a;
                if ($c === $t[0]) $a++;
            }
            return $cnt;
        };
        $l = 0;
        $r = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === 'T') $r++;
        $ans = 0;
        $mx = 0;
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === 'T') $r--;
            if ($c === 'C') $ans += $l * $r;
            if ($c === 'L') $l++;
            $mx = max($mx, $l * $r);
        }
        $mx = max($mx, max($calc($s, 'LC'), $calc($s, 'CT')));
        return $ans + $mx;
    }
}
