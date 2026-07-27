<?php
// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Float
     */
    function trimMean($arr) {
        sort($arr);
        $n = count($arr);
        $k = intdiv($n, 20);
        $sum = 0;
        for ($i = $k; $i < $n - $k; $i++) {
            $sum += $arr[$i];
        }
        return $sum / ($n - 2 * $k);
    }
}
