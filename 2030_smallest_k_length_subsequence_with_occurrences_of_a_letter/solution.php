<?php
// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @param String $letter
     * @param Integer $repetition
     * @return String
     */
    function smallestSubsequence($s, $k, $letter, $repetition) {
        $n = strlen($s);
        $remainLetter = 0;
        for ($i = 0; $i < $n; $i++) if ($s[$i] === $letter) $remainLetter++;
        $stack = "";
        $inStackLetter = 0;
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            while (strlen($stack) > 0 && $ch < $stack[strlen($stack) - 1] && strlen($stack) + $n - $i > $k) {
                $top = $stack[strlen($stack) - 1];
                if ($top === $letter) {
                    if ($inStackLetter + $remainLetter - 1 < $repetition) break;
                    $inStackLetter--;
                }
                $stack = substr($stack, 0, -1);
            }
            if (strlen($stack) < $k) {
                if ($ch === $letter) { $stack .= $ch; $inStackLetter++; }
                else if ($k - strlen($stack) > $repetition - $inStackLetter) $stack .= $ch;
            }
            if ($ch === $letter) $remainLetter--;
        }
        return $stack;
    }
}
