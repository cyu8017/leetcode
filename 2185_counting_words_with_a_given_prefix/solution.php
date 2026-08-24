<?php
// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution {
    /**
     * @param String[] $words
     * @param String $pref
     * @return Integer
     */
    function prefixCount($words, $pref) {
        $ans = 0;
        $plen = strlen($pref);
        foreach ($words as $w) {
            if (strlen($w) >= $plen && substr($w, 0, $plen) === $pref) $ans++;
        }
        return $ans;
    }
}
