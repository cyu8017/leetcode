<?php
// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function wonderfulSubstrings($word) {
        $count = array_fill(0, 1024, 0);
        $count[0] = 1;
        $mask = 0;
        $ans = 0;
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $mask ^= 1 << (ord($word[$i]) - 97);
            $ans += $count[$mask];
            for ($bit = 0; $bit < 10; $bit++) {
                $ans += $count[$mask ^ (1 << $bit)];
            }
            $count[$mask]++;
        }
        return $ans;
    }
}
