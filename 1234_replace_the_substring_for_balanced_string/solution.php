<?php
// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function balancedString($s) {
        $count = array_count_values(str_split($s));
        foreach (['Q','W','E','R'] as $c) if (!isset($count[$c])) $count[$c] = 0;
        $limit = intdiv(strlen($s), 4);
        $n = strlen($s);
        $left = 0;
        $answer = $n;
        for ($right = 0; $right < $n; $right++) {
            $count[$s[$right]]--;
            while ($left < $n && $count['Q'] <= $limit && $count['W'] <= $limit
                && $count['E'] <= $limit && $count['R'] <= $limit) {
                $answer = min($answer, $right - $left + 1);
                $count[$s[$left]]++;
                $left++;
            }
        }
        return $answer;
    }
}
