<?php
// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

class Solution {
    function cycleGenerator($arr, $steps, $startIndex) {
        $i = $startIndex;
        $n = count($arr);
        $out = [$arr[$i]];
        foreach ($steps as $jump) {
            $i = (($i + $jump) % $n + $n) % $n;
            $out[] = $arr[$i];
        }
        return $out;
    }
}
