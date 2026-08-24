<?php
// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function equalDigitFrequency($s) {
        $n = strlen($s);
        $seen = [];
        for ($i = 0; $i < $n; $i++) {
            $freq = array_fill(0, 10, 0);
            $maxf = 0;
            $kinds = 0;
            for ($j = $i; $j < $n; $j++) {
                $d = ord($s[$j]) - 48;
                if ($freq[$d] === 0) $kinds++;
                $freq[$d]++;
                $maxf = max($maxf, $freq[$d]);
                if ($maxf * $kinds === $j - $i + 1) $seen[substr($s, $i, $j - $i + 1)] = true;
            }
        }
        return count($seen);
    }
}
