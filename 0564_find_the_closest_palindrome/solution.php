<?php
// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

class Solution {
    function nearestPalindromic($n) {
        $length = strlen($n);
        $number = intval($n);
        $candidates = [];
        $pow10 = function($exp) {
            $value = 1;
            for ($i = 0; $i < $exp; ++$i) $value *= 10;
            return $value;
        };
        $makePalindrome = function($half, $len) {
            $text = strval($half);
            $pal = $text;
            if ($len % 2 === 0) {
                for ($i = strlen($text) - 1; $i >= 0; --$i) $pal .= $text[$i];
            } else {
                for ($i = strlen($text) - 2; $i >= 0; --$i) $pal .= $text[$i];
            }
            return intval($pal);
        };
        $candidates[] = $pow10($length - 1) - 1;
        $candidates[] = $pow10($length) + 1;
        $prefix = intval(substr($n, 0, intdiv($length + 1, 2)));
        for ($half = $prefix - 1; $half <= $prefix + 1; ++$half) {
            $candidates[] = $makePalindrome($half, $length);
        }
        $best = -1;
        $bestDiff = null;
        foreach ($candidates as $candidate) {
            if ($candidate === $number) continue;
            $diff = $candidate > $number ? $candidate - $number : $number - $candidate;
            if ($bestDiff === null || $diff < $bestDiff || ($diff === $bestDiff && $candidate < $best)) {
                $best = $candidate;
                $bestDiff = $diff;
            }
        }
        return strval($best);
    }
}
