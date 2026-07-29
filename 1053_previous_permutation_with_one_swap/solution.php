<?php
// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function prevPermOpt1($arr) {
        $n = count($arr);
        $i = $n - 2;
        while ($i >= 0 && $arr[$i] <= $arr[$i + 1]) {
            $i--;
        }
        if ($i < 0) {
            return $arr;
        }
        $j = $n - 1;
        while ($arr[$j] >= $arr[$i] || $arr[$j] === $arr[$j - 1]) {
            $j--;
        }
        $tmp = $arr[$i];
        $arr[$i] = $arr[$j];
        $arr[$j] = $tmp;
        return $arr;
    }
}
