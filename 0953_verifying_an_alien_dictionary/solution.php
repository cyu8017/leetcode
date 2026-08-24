<?php
// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution {
    function isAlienSorted($words, $order) {
        $rank = array_fill(0, 26, 0);
        for ($i = 0; $i < 26; $i++) $rank[ord($order[$i]) - 97] = $i;
        $lessEq = function ($a, $b) use ($rank) {
            $n = min(strlen($a), strlen($b));
            for ($i = 0; $i < $n; $i++) {
                $ra = $rank[ord($a[$i]) - 97];
                $rb = $rank[ord($b[$i]) - 97];
                if ($ra !== $rb) return $ra < $rb;
            }
            return strlen($a) <= strlen($b);
        };
        $nw = count($words);
        for ($i = 0; $i + 1 < $nw; $i++) {
            if (!$lessEq($words[$i], $words[$i + 1])) return false;
        }
        return true;
    }
}
