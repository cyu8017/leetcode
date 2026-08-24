<?php
// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

class Solution {
    function minCost($arr, $brr, $k) {
        $noSwap = 0;
        for ($i = 0; $i < count($arr); $i++) $noSwap += abs($arr[$i] - $brr[$i]);
        $a2 = $arr;
        $b2 = $brr;
        sort($a2);
        sort($b2);
        $withSwap = $k;
        for ($i = 0; $i < count($a2); $i++) $withSwap += abs($a2[$i] - $b2[$i]);
        return $noSwap < $withSwap ? $noSwap : $withSwap;
    }
}
