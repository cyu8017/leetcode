<?php
// LeetCode 3750 - Minimum Number of Flips to Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution {
    function minimumFlips($n) {
        $x = $n;
        if ($x === 0) $s = "0";
        else {
            $bits = '';
            while ($x > 0) {
                $bits .= chr(48 + ($x & 1));
                $x >>= 1;
            }
            $s = strrev($bits);
        }
        $m = strlen($s);
        $cnt = 0;
        for ($i = 0; $i < intdiv($m, 2); $i++) {
            if ($s[$i] !== $s[$m - $i - 1]) $cnt++;
        }
        return $cnt * 2;
    }
}
