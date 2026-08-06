<?php
// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function transformArray($arr) {
        while (true) {
            $nxt = $arr;
            $n = count($arr);
            for ($i = 1; $i < $n - 1; $i++) {
                if ($arr[$i] < $arr[$i - 1] && $arr[$i] < $arr[$i + 1]) $nxt[$i]++;
                elseif ($arr[$i] > $arr[$i - 1] && $arr[$i] > $arr[$i + 1]) $nxt[$i]--;
            }
            if ($nxt === $arr) return $arr;
            $arr = $nxt;
        }
    }
}
