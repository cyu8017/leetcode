<?php
// LeetCode 0186 - Reverse Words in a String II
// https://leetcode.com/problems/reverse-words-in-a-string-ii/

class Solution {
    /**
     * @param String[] $s
     * @return NULL
     */
    function reverseWords(&$s) {
        $this->reverseRange($s, 0, count($s) - 1);
        $start = 0;

        for ($end = 0; $end <= count($s); $end++) {
            if ($end === count($s) || $s[$end] === ' ') {
                $this->reverseRange($s, $start, $end - 1);
                $start = $end + 1;
            }
        }
    }

    private function reverseRange(&$chars, $left, $right) {
        while ($left < $right) {
            [$chars[$left], $chars[$right]] = [$chars[$right], $chars[$left]];
            $left++;
            $right--;
        }
    }
}
