<?php
// LeetCode 3799 - Word Squares II
// https://leetcode.com/problems/word-squares-ii/

class Solution {
    function wordSquares($words) {
        sort($words);
        $n = count($words);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $top = $words[$i];
            for ($j = 0; $j < $n; $j++) {
                if ($j === $i) continue;
                $left = $words[$j];
                for ($k = 0; $k < $n; $k++) {
                    if ($k === $j || $k === $i) continue;
                    $right = $words[$k];
                    for ($h = 0; $h < $n; $h++) {
                        if ($h === $k || $h === $j || $h === $i) continue;
                        $bottom = $words[$h];
                        if ($top[0] === $left[0] && $top[3] === $right[0] &&
                            $bottom[0] === $left[3] && $bottom[3] === $right[3]) {
                            $ans[] = [$top, $left, $right, $bottom];
                        }
                    }
                }
            }
        }
        return $ans;
    }
}
