<?php
// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function getDistances($arr) {
        $n = count($arr);
        $pos = [];
        for ($i = 0; $i < $n; $i++) {
            if (!isset($pos[$arr[$i]])) $pos[$arr[$i]] = [];
            $pos[$arr[$i]][] = $i;
        }
        $ans = array_fill(0, $n, 0);
        foreach ($pos as $idxs) {
            $m = count($idxs);
            $pref = array_fill(0, $m + 1, 0);
            for ($i = 0; $i < $m; $i++) $pref[$i + 1] = $pref[$i] + $idxs[$i];
            for ($i = 0; $i < $m; $i++) {
                $left = $i * $idxs[$i] - $pref[$i];
                $right = ($pref[$m] - $pref[$i + 1]) - ($m - $i - 1) * $idxs[$i];
                $ans[$idxs[$i]] = $left + $right;
            }
        }
        return $ans;
    }
}
