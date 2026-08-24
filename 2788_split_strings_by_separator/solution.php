<?php
// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

class Solution {
    function splitWordsBySeparator($words, $separator) {
        $ans = [];
        foreach ($words as $w) {
            $start = 0;
            $len = strlen($w);
            for ($i = 0; $i <= $len; $i++) {
                if ($i === $len || $w[$i] === $separator) {
                    if ($i > $start) $ans[] = substr($w, $start, $i - $start);
                    $start = $i + 1;
                }
            }
        }
        return $ans;
    }
}
