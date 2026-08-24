<?php
// LeetCode 0072 - Edit Distance
// https://leetcode.com/problems/edit-distance/

class Solution {
    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function minDistance($word1, $word2) {
        $m = strlen($word1);
        $n = strlen($word2);
        $prev = range(0, $n);
        $curr = array_fill(0, $n + 1, 0);

        for ($i = 1; $i <= $m; $i++) {
            $curr[0] = $i;
            for ($j = 1; $j <= $n; $j++) {
                if ($word1[$i - 1] === $word2[$j - 1]) {
                    $curr[$j] = $prev[$j - 1];
                } else {
                    $curr[$j] = 1 + min($prev[$j], $curr[$j - 1], $prev[$j - 1]);
                }
            }
            $tmp = $prev;
            $prev = $curr;
            $curr = $tmp;
        }

        return $prev[$n];
    }
}
