<?php
// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

class Solution {
    function countGoodIntegers($l, $r, $k) {
        return $this->countBound($r, $k) - $this->countBound($l - 1, $k);
    }

    private function countBound($bound, $k) {
        if ($bound <= 0) return 0;
        $digits = strval($bound);
        $memo = [];
        return $this->dfs(0, 0, false, true, $digits, $k, $memo);
    }

    private function dfs($position, $previous, $started, $tight, $digits, $k, &$memo) {
        if ($position === strlen($digits)) return $started ? 1 : 0;
        $key = $position . "," . $previous . "," . ($started ? 1 : 0);
        if (!$tight && isset($memo[$key])) return $memo[$key];
        $limit = $tight ? intval($digits[$position]) : 9;
        $result = 0;
        for ($digit = 0; $digit <= $limit; $digit++) {
            $nextStarted = $started || $digit !== 0;
            if ($started && abs($previous - $digit) > $k) continue;
            $nextPrevious = $nextStarted ? $digit : $previous;
            $result += $this->dfs($position + 1, $nextPrevious, $nextStarted, $tight && $digit === $limit, $digits, $k, $memo);
        }
        if (!$tight) $memo[$key] = $result;
        return $result;
    }
}
