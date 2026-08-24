<?php
// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution {
    function findMissingAndRepeatedValues($grid) {
        $n = count($grid);
        $freq = array_fill(0, $n * $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $freq[$grid[$i][$j]]++;
            }
        }
        $rep = 0;
        $miss = 0;
        for ($i = 1; $i <= $n * $n; $i++) {
            if ($freq[$i] === 2) $rep = $i;
            if ($freq[$i] === 0) $miss = $i;
        }
        return [$rep, $miss];
    }
}
