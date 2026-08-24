<?php
// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

class Solution {
    /**
     * @param String $word
     * @param String $ch
     * @return String
     */
    function reversePrefix($word, $ch) {
        $pos = strpos($word, $ch);
        if ($pos === false) return $word;
        $arr = str_split($word);
        for ($l = 0, $r = $pos; $l < $r; $l++, $r--) {
            $tmp = $arr[$l];
            $arr[$l] = $arr[$r];
            $arr[$r] = $tmp;
        }
        return implode('', $arr);
    }
}
