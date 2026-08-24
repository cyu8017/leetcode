<?php
// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

class Solution {
    private function isNonDecreasing($a) {
        $n = count($a);
        for ($i = 1; $i < $n; $i++) if ($a[$i] < $a[$i - 1]) return false;
        return true;
    }

    function minimumPairRemoval($nums) {
        $arr = $nums;
        $ans = 0;
        while (!$this->isNonDecreasing($arr)) {
            $k = 0;
            $s = $arr[0] + $arr[1];
            $n = count($arr);
            for ($i = 1; $i + 1 < $n; $i++) {
                $t = $arr[$i] + $arr[$i + 1];
                if ($s > $t) { $s = $t; $k = $i; }
            }
            $arr[$k] = $s;
            array_splice($arr, $k + 1, 1);
            $ans++;
        }
        return $ans;
    }
}
