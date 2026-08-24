<?php
// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution {
    function deckRevealedIncreasing($deck) {
        sort($deck);
        $n = count($deck);
        $idx = range(0, $n - 1);
        $ans = array_fill(0, $n, 0);
        foreach ($deck as $card) {
            $ans[array_shift($idx)] = $card;
            if ($idx) $idx[] = array_shift($idx);
        }
        return $ans;
    }
}
