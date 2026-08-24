<?php
// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function areNumbersAscending($s) {
        $prev = -1;
        foreach (explode(" ", $s) as $tok) {
            if ($tok === "") continue;
            if ($tok[0] >= '0' && $tok[0] <= '9') {
                $v = intval($tok);
                if ($v <= $prev) return false;
                $prev = $v;
            }
        }
        return true;
    }
}
