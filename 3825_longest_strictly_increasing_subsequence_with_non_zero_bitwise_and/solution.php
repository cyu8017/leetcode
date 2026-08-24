<?php
// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise AND
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

class Solution {
    function bitLen($x) {
        if ($x === 0) return 0;
        $n = 0;
        while ($x > 0) { $n++; $x >>= 1; }
        return $n;
    }
    function lis($arr) {
        $g = [];
        foreach ($arr as $x) {
            $lo = 0;
            $hi = count($g);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($g[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            if ($lo === count($g)) $g[] = $x;
            else $g[$lo] = $x;
        }
        return count($g);
    }
    function longestSubsequence($nums) {
        $ans = 0;
        $mx = 0;
        foreach ($nums as $x) $mx = max($mx, $x);
        $m = $this->bitLen($mx);
        for ($i = 0; $i < $m; $i++) {
            $arr = [];
            foreach ($nums as $x) {
                if ((($x >> $i) & 1) !== 0) $arr[] = $x;
            }
            $ans = max($ans, $this->lis($arr));
        }
        return $ans;
    }
}
