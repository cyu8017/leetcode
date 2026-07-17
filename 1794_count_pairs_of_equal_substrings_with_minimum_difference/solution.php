<?php
// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

class Solution {
    /**
     * @param String $firstString
     * @param String $secondString
     * @return Integer
     */
    function countQuadruples($firstString, $secondString) {
        $first = [];
        $lastF = [];
        $lastS = [];
        $n1 = strlen($firstString);
        $n2 = strlen($secondString);
        for ($i = 0; $i < $n1; $i++) {
            $ch = $firstString[$i];
            if (!isset($first[$ch])) $first[$ch] = $i;
            $lastF[$ch] = $i;
        }
        for ($i = 0; $i < $n2; $i++) {
            $lastS[$secondString[$i]] = $i;
        }
        $best = PHP_INT_MAX;
        foreach ($first as $ch => $idx) {
            if (isset($lastS[$ch])) {
                $best = min($best, $lastF[$ch] - $lastS[$ch]);
            }
        }
        if ($best === PHP_INT_MAX) return 0;
        $ans = 0;
        foreach ($first as $ch => $idx) {
            if (!isset($lastS[$ch]) || $lastF[$ch] - $lastS[$ch] !== $best) continue;
            $iCount = 0;
            for ($k = $first[$ch]; $k <= $lastF[$ch]; $k++) {
                if ($firstString[$k] === $ch) $iCount++;
            }
            $aCount = 0;
            for ($k = 0; $k <= $lastS[$ch]; $k++) {
                if ($secondString[$k] === $ch) $aCount++;
            }
            $ans += $iCount * $aCount;
        }
        return $ans;
    }
}
