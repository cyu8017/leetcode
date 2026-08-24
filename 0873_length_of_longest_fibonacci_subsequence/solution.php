<?php
// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function lenLongestFibSubseq($arr) {
        $n = count($arr);
        $index = [];
        for ($i = 0; $i < $n; $i++) $index[$arr[$i]] = $i;
        $dp = array_fill(0, $n, array_fill(0, $n, 2));
        $ans = 0;
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $j; $i++) {
                $need = $arr[$j] - $arr[$i];
                if (isset($index[$need])) {
                    $k = $index[$need];
                    if ($k < $i) {
                        $dp[$i][$j] = $dp[$k][$i] + 1;
                        $ans = max($ans, $dp[$i][$j]);
                    }
                }
            }
        }
        return $ans >= 3 ? $ans : 0;
    }
}
