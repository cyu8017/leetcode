<?php
// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxEqualFreq($nums) {
        $count = [];
        $frequencies = [];
        $answer = 0;
        foreach ($nums as $i => $x) {
            $i++;
            $old = $count[$x] ?? 0;
            if ($old) {
                $frequencies[$old]--;
                if ($frequencies[$old] === 0) unset($frequencies[$old]);
            }
            $count[$x] = $old + 1;
            $frequencies[$old + 1] = ($frequencies[$old + 1] ?? 0) + 1;
            $high = max(array_keys($frequencies));
            if ($high === 1
                || ($frequencies[$high] ?? 0) * $high + 1 === $i
                || (($frequencies[$high] ?? 0) === 1 && ($frequencies[$high - 1] ?? 0) * ($high - 1) + $high === $i)) {
                $answer = $i;
            }
        }
        return $answer;
    }
}
