<?php
// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

class Solution {
    function minOperations($initial, $target) {
        $m = strlen($initial);
        $n = strlen($target);
        $f = [];
        for ($i = 0; $i <= $m; $i++) $f[] = array_fill(0, $n + 1, 0);
        $mx = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($initial[$i] === $target[$j]) {
                    $f[$i + 1][$j + 1] = $f[$i][$j] + 1;
                    $mx = max($mx, $f[$i + 1][$j + 1]);
                }
            }
        }
        return $m + $n - 2 * $mx;
    }
}
