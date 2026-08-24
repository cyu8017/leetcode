<?php
// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution {
    function countPrefixSuffixPairs($words) {
        $ans = 0;
        $n = count($words);
        for ($i = 0; $i < $n; $i++) {
            $s = $words[$i];
            for ($j = $i + 1; $j < $n; $j++) {
                $t = $words[$j];
                if (strlen($t) >= strlen($s) && strncmp($t, $s, strlen($s)) === 0 && substr($t, -strlen($s)) === $s) {
                    $ans++;
                }
            }
        }
        return $ans;
    }
}
