<?php
// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution {
    /**
     * @param String $s
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function maximumGain($s, $x, $y) {
        if ($x >= $y) {
            [$rest, $first] = $this->remove($s, 'a', 'b', $x);
            [, $second] = $this->remove($rest, 'b', 'a', $y);
        } else {
            [$rest, $first] = $this->remove($s, 'b', 'a', $y);
            [, $second] = $this->remove($rest, 'a', 'b', $x);
        }
        return $first + $second;
    }

    private function remove($text, $open, $close, $score) {
        $stack = [];
        $gained = 0;
        $len = strlen($text);
        for ($i = 0; $i < $len; $i++) {
            $ch = $text[$i];
            if (!empty($stack) && end($stack) === $open && $ch === $close) {
                array_pop($stack);
                $gained += $score;
            } else {
                $stack[] = $ch;
            }
        }
        return [implode('', $stack), $gained];
    }
}
