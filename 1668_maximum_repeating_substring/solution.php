<?php
// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

class Solution {
    function maxRepeating($sequence, $word) {
        $k = 0;
        while (strpos($sequence, str_repeat($word, $k + 1)) !== false) $k++;
        return $k;
    }
}
