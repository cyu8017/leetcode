<?php
// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

class Solution {
    /**
     * @param Integer[] $stones
     * @return Boolean
     */
    function stoneGameIX($stones) {
        $cnt = [0, 0, 0];
        foreach ($stones as $s) $cnt[$s % 3]++;
        if ($cnt[0] % 2 === 0) return $cnt[1] > 0 && $cnt[2] > 0;
        return abs($cnt[1] - $cnt[2]) > 2;
    }
}
