<?php
// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function minTimeToType($word) {
        $cur = 'a';
        $ans = 0;
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $ch = $word[$i];
            $d = abs(ord($ch) - ord($cur));
            $ans += min($d, 26 - $d) + 1;
            $cur = $ch;
        }
        return $ans;
    }
}
