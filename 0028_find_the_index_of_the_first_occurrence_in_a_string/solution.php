<?php
// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution {
    /**
     * @param String $haystack
     * @param String $needle
     * @return Integer
     */
    function strStr($haystack, $needle) {
        if ($needle === '') {
            return 0;
        }

        $needleLen = strlen($needle);
        $haystackLen = strlen($haystack);
        for ($i = 0; $i <= $haystackLen - $needleLen; $i++) {
            if (substr($haystack, $i, $needleLen) === $needle) {
                return $i;
            }
        }

        return -1;
    }
}
