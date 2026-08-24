<?php
// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

class Solution {
    function unmarkedSumArray($nums, $queries) {
        $n = count($nums);
        $s = 0;
        foreach ($nums as $x) $s += $x;
        $mark = array_fill(0, $n, false);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$nums[$i], $i];
        usort($arr, function ($a, $b) {
            return $a[0] !== $b[0] ? $a[0] <=> $b[0] : $a[1] <=> $b[1];
        });
        $ans = array_fill(0, count($queries), 0);
        $j = 0;
        for ($qi = 0; $qi < count($queries); $qi++) {
            $index = $queries[$qi][0];
            $k = $queries[$qi][1];
            if (!$mark[$index]) {
                $mark[$index] = true;
                $s -= $nums[$index];
            }
            for (; $k > 0 && $j < $n; $j++) {
                if (!$mark[$arr[$j][1]]) {
                    $mark[$arr[$j][1]] = true;
                    $s -= $arr[$j][0];
                    $k--;
                }
            }
            $ans[$qi] = $s;
        }
        return $ans;
    }
}
