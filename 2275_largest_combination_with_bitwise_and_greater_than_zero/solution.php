<?php
// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution {
    function largestCombination($candidates) {
        $ans = 0;
        for ($bit = 0; $bit < 24; $bit++) {
            $cnt = 0;
            foreach ($candidates as $x) if ((($x >> $bit) & 1) !== 0) $cnt++;
            $ans = max($ans, $cnt);
        }
        return $ans;
    }
}
