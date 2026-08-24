<?php
// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

class Solution {
    function minStartingIndex($s, $pattern) {
        $n = strlen($s);
        $m = strlen($pattern);
        for ($i = 0; $i + $m <= $n; $i++) {
            $diff = 0;
            for ($j = 0; $j < $m; $j++) {
                if ($s[$i + $j] !== $pattern[$j]) {
                    $diff++;
                    if ($diff > 1) break;
                }
            }
            if ($diff <= 1) return $i;
        }
        return -1;
    }
}
