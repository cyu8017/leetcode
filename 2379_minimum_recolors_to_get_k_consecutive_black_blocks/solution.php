<?php
// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution {
    function minimumRecolors($blocks, $k) {
        $white = 0;
        for ($i = 0; $i < $k; $i++) if ($blocks[$i] === 'W') $white++;
        $ans = $white;
        $n = strlen($blocks);
        for ($i = $k; $i < $n; $i++) {
            if ($blocks[$i] === 'W') $white++;
            if ($blocks[$i - $k] === 'W') $white--;
            $ans = min($ans, $white);
        }
        return $ans;
    }
}
