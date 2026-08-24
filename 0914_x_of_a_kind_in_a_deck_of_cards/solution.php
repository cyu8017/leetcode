<?php
// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution {
    function hasGroupsSizeX($deck) {
        $count = [];
        foreach ($deck as $x) $count[$x] = ($count[$x] ?? 0) + 1;
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $g = 0;
        foreach ($count as $c) $g = $gcd($g, $c);
        return $g >= 2;
    }
}
