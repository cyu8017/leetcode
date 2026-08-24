<?php
// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

class Solution {
    function minFlips($s) {
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '1') $ones++;
        $answer = $ones;
        if ($ones > 0) $answer = $ones - 1;
        $zeros = $n - $ones;
        $answer = min($answer, $zeros);
        if ($n >= 2) {
            $cost = 0;
            for ($i = 0; $i < $n; $i++) {
                $want = ($i === 0 || $i === $n - 1) ? '1' : '0';
                if ($s[$i] !== $want) $cost++;
            }
            $answer = min($answer, $cost);
        }
        return $answer;
    }
}
