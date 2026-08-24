<?php
// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

class Solution {
    function makeAntiPalindrome($s) {
        $arr = str_split($s);
        sort($arr);
        $n = count($arr);
        $m = intdiv($n, 2);
        if ($arr[$m] === $arr[$m - 1]) {
            $i = $m;
            while ($i < $n && $arr[$i] === $arr[$i - 1]) $i++;
            for ($j = $m; $j < $n && $arr[$j] === $arr[$n - $j - 1]; $i++, $j++) {
                if ($i >= $n) return "-1";
                $tmp = $arr[$i]; $arr[$i] = $arr[$j]; $arr[$j] = $tmp;
            }
        }
        return implode("", $arr);
    }
}
