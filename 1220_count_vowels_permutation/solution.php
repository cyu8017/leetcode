<?php
// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function countVowelPermutation($n) {
        $mod = 1000000007;
        $a = $e = $i = $o = $u = 1;
        for ($t = 1; $t < $n; $t++) {
            [$a, $e, $i, $o, $u] = [
                ($e + $i + $u) % $mod,
                ($a + $i) % $mod,
                ($e + $o) % $mod,
                $i,
                ($i + $o) % $mod
            ];
        }
        return ($a + $e + $i + $o + $u) % $mod;
    }
}
