<?php
// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

class Solution {
    /**
     * @param String $s
     * @param String[] $words
     * @return Integer
     */
    function numMatchingSubseq($s, $words) {
        $waiting = array_fill(0, 26, []);
        $wn = count($words);
        for ($i = 0; $i < $wn; $i++) {
            $w = $words[$i];
            $waiting[ord($w[0]) - 97][] = [$i, 0];
        }
        $ans = 0;
        $n = strlen($s);
        for ($si = 0; $si < $n; $si++) {
            $ch = $s[$si];
            $idxc = ord($ch) - 97;
            $cur = $waiting[$idxc];
            $waiting[$idxc] = [];
            foreach ($cur as $pair) {
                $wi = $pair[0];
                $idx = $pair[1] + 1;
                if ($idx === strlen($words[$wi])) $ans++;
                else $waiting[ord($words[$wi][$idx]) - 97][] = [$wi, $idx];
            }
        }
        return $ans;
    }
}
