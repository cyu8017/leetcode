<?php
// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution {
    function closeStrings($word1, $word2) {
        if (strlen($word1) !== strlen($word2)) return false;
        $a = array_count_values(str_split($word1));
        $b = array_count_values(str_split($word2));
        $ka = array_keys($a);
        $kb = array_keys($b);
        sort($ka);
        sort($kb);
        if ($ka !== $kb) return false;
        $va = array_values($a);
        $vb = array_values($b);
        sort($va);
        sort($vb);
        return $va === $vb;
    }
}
