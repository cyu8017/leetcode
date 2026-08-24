<?php
// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

class Solution {
    function ok($removeFirst, $source, $pattern, $targetIndices, $n) {
        $mark = array_fill(0, $n, false);
        for ($i = 0; $i < $removeFirst; $i++) $mark[$targetIndices[$i]] = true;
        $j = 0;
        $m = strlen($pattern);
        for ($i = 0; $i < $n && $j < $m; $i++) {
            if ($mark[$i]) continue;
            if ($source[$i] === $pattern[$j]) $j++;
        }
        return $j === $m;
    }

    function maxRemovals($source, $pattern, $targetIndices) {
        $n = strlen($source);
        $lo = 0;
        $hi = count($targetIndices);
        while ($lo < $hi) {
            $mid = ($lo + $hi + 1) >> 1;
            if ($this->ok($mid, $source, $pattern, $targetIndices, $n)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
