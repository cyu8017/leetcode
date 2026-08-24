<?php
// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

class Solution {
    function goodSubsetofBinaryMatrix($grid) {
        $n = count($grid[0]);
        $first = [];
        for ($i = 0; $i < count($grid); $i++) {
            $mask = 0;
            for ($j = 0; $j < $n; $j++) if ($grid[$i][$j] === 1) $mask |= 1 << $j;
            if ($mask === 0) return [$i];
            foreach ($first as $pm => $idx) {
                if (($pm & $mask) === 0) {
                    return $idx < $i ? [$idx, $i] : [$i, $idx];
                }
            }
            if (!array_key_exists($mask, $first)) $first[$mask] = $i;
        }
        return [];
    }
}
