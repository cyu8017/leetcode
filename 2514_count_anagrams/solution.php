<?php
// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

class Solution {
    function countAnagrams($s) {
        $MOD = 1000000007;
        $modPow = function ($a, $e) use ($MOD) {
            $res = 1;
            $a %= $MOD;
            while ($e > 0) {
                if ($e & 1) $res = ($res * $a) % $MOD;
                $a = ($a * $a) % $MOD;
                $e >>= 1;
            }
            return $res;
        };
        $trimmed = trim($s);
        $words = $trimmed === '' ? [] : preg_split('/\s+/', $trimmed);
        $maxN = 0;
        foreach ($words as $w) if (strlen($w) > $maxN) $maxN = strlen($w);
        $fact = array_fill(0, $maxN + 1, 0);
        $invFact = array_fill(0, $maxN + 1, 0);
        $fact[0] = 1;
        for ($i = 1; $i <= $maxN; $i++) $fact[$i] = ($fact[$i - 1] * $i) % $MOD;
        $invFact[$maxN] = $modPow($fact[$maxN], $MOD - 2);
        for ($i = $maxN; $i > 0; $i--) $invFact[$i - 1] = ($invFact[$i] * $i) % $MOD;
        $ans = 1;
        foreach ($words as $word) {
            $cnt = array_fill(0, 26, 0);
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) $cnt[ord($word[$i]) - 97]++;
            $cur = $fact[$len];
            foreach ($cnt as $c) $cur = ($cur * $invFact[$c]) % $MOD;
            $ans = ($ans * $cur) % $MOD;
        }
        return $ans;
    }
}
