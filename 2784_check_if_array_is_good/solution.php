<?php
// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

class Solution {
    function isGood($nums) {
        $n = count($nums) - 1;
        if ($n < 1) return false;
        $freq = array_fill(0, $n + 1, 0);
        foreach ($nums as $v) {
            if ($v < 1 || $v > $n) return false;
            $freq[$v]++;
        }
        for ($i = 1; $i < $n; $i++) if ($freq[$i] !== 1) return false;
        return $freq[$n] === 2;
    }
}
