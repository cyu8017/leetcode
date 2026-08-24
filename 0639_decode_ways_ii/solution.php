<?php
// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

class Solution {
    function numDecodings($s) {
        $mod = 1000000007;
        $one = function($ch) {
            if ($ch === "*") return 9;
            if ($ch === "0") return 0;
            return 1;
        };
        $two = function($a, $b) {
            if ($a === "*" && $b === "*") return 15;
            if ($a === "*") return $b <= "6" ? 2 : 1;
            if ($b === "*") {
                if ($a === "1") return 9;
                if ($a === "2") return 6;
                return 0;
            }
            $value = (ord($a) - 48) * 10 + (ord($b) - 48);
            return $value >= 10 && $value <= 26 ? 1 : 0;
        };
        $prev2 = 1;
        $prev1 = $one($s[0]);
        for ($i = 1; $i < strlen($s); ++$i) {
            $cur = ($one($s[$i]) * $prev1 + $two($s[$i - 1], $s[$i]) * $prev2) % $mod;
            $prev2 = $prev1;
            $prev1 = $cur;
        }
        return $prev1;
    }
}
