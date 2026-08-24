<?php
// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

class Solution {
    function resultArray($nums, $k, $queries) {
        $n = count($nums);
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $idx = $queries[$qi][0];
            $val = $queries[$qi][1];
            $start = $queries[$qi][2];
            $x = $queries[$qi][3];
            $nums[$idx] = $val;
            $prod = 1;
            $cnt = 0;
            for ($i = $start; $i < $n; $i++) {
                $prod = $prod * ($nums[$i] % $k) % $k;
                if ($prod === $x) $cnt++;
            }
            $ans[$qi] = $cnt;
        }
        return $ans;
    }
}
