<?php
// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution {
    /**
     * @param String[] $words
     * @return Boolean
     */
    function makeEqual($words) {
        $counts = [];
        foreach ($words as $word) {
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $ch = $word[$i];
                $counts[$ch] = ($counts[$ch] ?? 0) + 1;
            }
        }
        $n = count($words);
        foreach ($counts as $total) {
            if ($total % $n !== 0) {
                return false;
            }
        }
        return true;
    }
}
