<?php
// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution {
    function reverseWords($s) {
        $chars = str_split($s);
        $n = count($chars);
        $start = 0;
        for ($i = 0; $i <= $n; ++$i) {
            if ($i === $n || $chars[$i] === " ") {
                $left = $start;
                $right = $i - 1;
                while ($left < $right) {
                    $tmp = $chars[$left]; $chars[$left] = $chars[$right]; $chars[$right] = $tmp;
                    ++$left;
                    --$right;
                }
                $start = $i + 1;
            }
        }
        return implode("", $chars);
    }
}
