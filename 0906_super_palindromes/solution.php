<?php
// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

class Solution {
    function superpalindromesInRange($left, $right) {
        $L = (int)$left;
        $R = (int)$right;
        $isPal = function ($x) {
            $s = strval($x);
            $n = strlen($s);
            for ($i = 0; $i < intdiv($n, 2); $i++) {
                if ($s[$i] !== $s[$n - 1 - $i]) return false;
            }
            return true;
        };
        $ans = 0;
        for ($k = 1; $k <= 100000; $k++) {
            $s = strval($k);
            $pal = (int)($s . strrev($s));
            if ($pal > 1000000000) break;
            $sq = $pal * $pal;
            if ($sq > $R) break;
            if ($sq >= $L && $isPal($sq)) $ans++;
        }
        for ($k = 1; $k <= 100000; $k++) {
            $s = strval($k);
            $pal = (int)($s . strrev(substr($s, 0, -1)));
            if ($pal > 1000000000) break;
            $sq = $pal * $pal;
            if ($sq > $R) break;
            if ($sq >= $L && $isPal($sq)) $ans++;
        }
        return $ans;
    }
}
