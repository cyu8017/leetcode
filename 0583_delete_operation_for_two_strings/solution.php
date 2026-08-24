<?php
// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution {
    function minDistance($word1, $word2) {
        $m = strlen($word1);
        $n = strlen($word2);
        $prev = array_fill(0, $n + 1, 0);
        $curr = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $m; ++$i) {
            for ($j = 1; $j <= $n; ++$j) {
                if ($word1[$i - 1] === $word2[$j - 1]) $curr[$j] = $prev[$j - 1] + 1;
                else $curr[$j] = max($prev[$j], $curr[$j - 1]);
            }
            $tmp = $prev; $prev = $curr; $curr = $tmp;
            $curr = array_fill(0, $n + 1, 0);
        }
        return $m + $n - 2 * $prev[$n];
    }
}
