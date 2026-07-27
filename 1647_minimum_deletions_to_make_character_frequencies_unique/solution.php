<?php
// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minDeletions($s) {
        $freq = array_count_values(str_split($s));
        $used = [];
        $ans = 0;
        foreach ($freq as $x) {
            while ($x && isset($used[$x])) {
                $x--;
                $ans++;
            }
            $used[$x] = true;
        }
        return $ans;
    }
}
