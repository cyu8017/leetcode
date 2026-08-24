<?php
// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function longestSubsequenceRepeatedK($s, $k) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $chars = "";
        for ($c = 25; $c >= 0; $c--) if ($freq[$c] >= $k) $chars .= chr(97 + $c);
        $isSubseq = function ($t) use ($s, $k) {
            $need = 0;
            $times = 0;
            $tl = strlen($t);
            $sl = strlen($s);
            for ($i = 0; $i < $sl; $i++) {
                if ($s[$i] === $t[$need]) {
                    $need++;
                    if ($need === $tl) {
                        $times++;
                        if ($times === $k) return true;
                        $need = 0;
                    }
                }
            }
            return false;
        };
        $best = "";
        $q = [""];
        $clen = strlen($chars);
        while ($q) {
            $cur = array_shift($q);
            for ($i = 0; $i < $clen; $i++) {
                $nxt = $cur . $chars[$i];
                if ($isSubseq($nxt)) {
                    if (strlen($nxt) > strlen($best) || (strlen($nxt) === strlen($best) && $nxt > $best))
                        $best = $nxt;
                    $q[] = $nxt;
                }
            }
        }
        return $best;
    }
}
