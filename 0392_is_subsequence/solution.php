<?php
// LeetCode 0392 - Is Subsequence
// https://leetcode.com/problems/is-subsequence/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isSubsequence($s, $t) {
        return $this->is_subsequence($s, $t);
    }

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function is_subsequence($s, $t) {
        $index = 0;
        $length = strlen($s);
        $tLength = strlen($t);
        for ($position = 0; $position < $tLength; $position++) {
            if ($index < $length && $s[$index] === $t[$position]) {
                $index++;
            }
        }
        return $index === $length;
    }
}
