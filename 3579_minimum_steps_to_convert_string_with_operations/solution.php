<?php
// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

class Solution {
    private $word1;
    private $word2;

    private function calc($l, $r, $rev) {
        $cnt = [];
        for ($i = 0; $i < 26; $i++) $cnt[$i] = array_fill(0, 26, 0);
        $res = 0;
        for ($i = $l; $i <= $r; $i++) {
            $j = $rev ? $r - ($i - $l) : $i;
            $a = ord($this->word1[$j]) - 97;
            $b = ord($this->word2[$i]) - 97;
            if ($a !== $b) {
                if ($cnt[$b][$a] > 0) $cnt[$b][$a]--;
                else {
                    $cnt[$a][$b]++;
                    $res++;
                }
            }
        }
        return $res;
    }

    function minOperations($word1, $word2) {
        $this->word1 = $word1;
        $this->word2 = $word2;
        $n = strlen($word1);
        $f = array_fill(0, $n + 1, intdiv(2147483647, 2));
        $f[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                $a = $this->calc($j, $i - 1, false);
                $b = 1 + $this->calc($j, $i - 1, true);
                $f[$i] = min($f[$i], $f[$j] + min($a, $b));
            }
        }
        return $f[$n];
    }
}
