<?php
// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

class Solution {
    function bestHand($ranks, $suits) {
        if ($suits[0] === $suits[1] && $suits[1] === $suits[2] && $suits[2] === $suits[3] && $suits[3] === $suits[4])
            return "Flush";
        $cnt = [];
        $best = 0;
        foreach ($ranks as $r) {
            $c = ($cnt[$r] ?? 0) + 1;
            $cnt[$r] = $c;
            $best = max($best, $c);
        }
        if ($best >= 3) return "Three of a Kind";
        if ($best === 2) return "Pair";
        return "High Card";
    }
}
