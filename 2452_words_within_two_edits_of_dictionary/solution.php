<?php
// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution {
    function twoEditWords($queries, $dictionary) {
        $ans = [];
        foreach ($queries as $q) {
            $ok = false;
            $ql = strlen($q);
            foreach ($dictionary as $d) {
                $diff = 0;
                for ($i = 0; $i < $ql; $i++) {
                    if ($q[$i] !== $d[$i]) {
                        if (++$diff > 2) break;
                    }
                }
                if ($diff <= 2) { $ok = true; break; }
            }
            if ($ok) $ans[] = $q;
        }
        return $ans;
    }
}
