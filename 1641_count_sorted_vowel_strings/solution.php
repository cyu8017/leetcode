<?php
// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution {
    private function comb($n, $k) {
        if ($k < 0 || $k > $n) {
            return 0;
        }
        $k = min($k, $n - $k);
        $res = 1;
        for ($i = 1; $i <= $k; $i++) {
            $res = intdiv($res * ($n - $k + $i), $i);
        }
        return $res;
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function countVowelStrings($n) {
        return $this->comb($n + 4, 4);
    }
}
