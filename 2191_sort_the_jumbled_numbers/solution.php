<?php
// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution {
    /**
     * @param Integer[] $mapping
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortJumbled($mapping, $nums) {
        $mapVal = function($x) use ($mapping) {
            if ($x === 0) return $mapping[0];
            $digits = [];
            while ($x > 0) {
                $digits[] = $x % 10;
                $x = intdiv($x, 10);
            }
            $res = 0;
            for ($i = count($digits) - 1; $i >= 0; $i--)
                $res = $res * 10 + $mapping[$digits[$i]];
            return $res;
        };
        $n = count($nums);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$mapVal($nums[$i]), $i, $nums[$i]];
        usort($arr, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
        $ans = [];
        foreach ($arr as $x) $ans[] = $x[2];
        return $ans;
    }
}
