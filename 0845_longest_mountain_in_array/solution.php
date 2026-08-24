<?php
// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function longestMountain($arr) {
        $n = count($arr);
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            if ($j + 1 < $n && $arr[$j] < $arr[$j + 1]) {
                while ($j + 1 < $n && $arr[$j] < $arr[$j + 1]) $j++;
                if ($j + 1 < $n && $arr[$j] > $arr[$j + 1]) {
                    while ($j + 1 < $n && $arr[$j] > $arr[$j + 1]) $j++;
                    $ans = max($ans, $j - $i + 1);
                    $i = $j;
                    continue;
                }
            }
            $i++;
        }
        return $ans;
    }
}
