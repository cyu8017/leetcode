<?php
// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maxProduct($s) {
        $n = strlen($s);
        $palLen = function ($mask) use ($s, $n) {
            $chars = "";
            for ($i = 0; $i < $n; $i++)
                if (($mask & (1 << $i)) !== 0) $chars .= $s[$i];
            for ($l = 0, $r = strlen($chars) - 1; $l < $r; $l++, $r--)
                if ($chars[$l] !== $chars[$r]) return 0;
            return strlen($chars);
        };
        $best = 0;
        $total = 1 << $n;
        for ($mask1 = 1; $mask1 < $total; $mask1++) {
            $len1 = $palLen($mask1);
            if ($len1 === 0) continue;
            $remain = ($total - 1) ^ $mask1;
            for ($mask2 = $remain; $mask2 > 0; $mask2 = ($mask2 - 1) & $remain) {
                $len2 = $palLen($mask2);
                if ($len2 > 0 && $len1 * $len2 > $best) $best = $len1 * $len2;
            }
        }
        return $best;
    }
}
