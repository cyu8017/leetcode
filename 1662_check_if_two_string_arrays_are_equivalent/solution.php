<?php
// LeetCode 1662 - Check If Two String Arrays are Equivalent
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution {
    function arrayStringsAreEqual($word1, $word2) {
        return implode("", $word1) === implode("", $word2);
    }
}
