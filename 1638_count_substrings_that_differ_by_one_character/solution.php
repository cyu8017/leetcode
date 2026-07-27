<?php
// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function countSubstrings($s, $t) {
        $ans = 0;
        $ns = strlen($s);
        $nt = strlen($t);
        for ($i = 0; $i < $ns; $i++) {
            for ($j = 0; $j < $nt; $j++) {
                $diff = 0;
                $limit = min($ns - $i, $nt - $j);
                for ($k = 0; $k < $limit; $k++) {
                    if ($s[$i + $k] !== $t[$j + $k]) {
                        $diff++;
                    }
                    if ($diff === 1) {
                        $ans++;
                    } elseif ($diff > 1) {
                        break;
                    }
                }
            }
        }
        return $ans;
    }
}
