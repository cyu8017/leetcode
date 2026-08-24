<?php
// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution {
    /**
     * @param Integer[] $changed
     * @return Integer[]
     */
    function findOriginalArray($changed) {
        if (count($changed) % 2 !== 0) return [];
        sort($changed);
        $freq = [];
        foreach ($changed as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $ans = [];
        foreach ($changed as $x) {
            if (($freq[$x] ?? 0) === 0) continue;
            $freq[$x]--;
            if (($freq[2 * $x] ?? 0) === 0) return [];
            $freq[2 * $x]--;
            $ans[] = $x;
        }
        return $ans;
    }
}
