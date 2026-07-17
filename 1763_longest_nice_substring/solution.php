<?php
// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function longestNiceSubstring($s) {
        $n = strlen($s);
        $bestStart = 0;
        $bestLen = 0;
        for ($i = 0; $i < $n; $i++) {
            $lower = 0;
            $upper = 0;
            for ($j = $i; $j < $n; $j++) {
                $code = ord($s[$j]);
                if ($code >= 97) {
                    $lower |= 1 << ($code - 97);
                } else {
                    $upper |= 1 << ($code - 65);
                }
                if ($lower === $upper && $j - $i + 1 > $bestLen) {
                    $bestStart = $i;
                    $bestLen = $j - $i + 1;
                }
            }
        }
        return substr($s, $bestStart, $bestLen);
    }
}
