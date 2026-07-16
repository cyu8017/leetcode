<?php
// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution {
    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function findLUSlength($a, $b) {
        return $this->find_luslength($a, $b);
    }

    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function find_luslength($a, $b) {
        return $a !== $b ? max(strlen($a), strlen($b)) : -1;
    }
}
