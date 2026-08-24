<?php
// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

class Solution {
    function maxFrequencyScore($nums, $k) {
        $MOD = 1000000007;
        $modPow = function($a, $e) use ($MOD) {
            $res = 1;
            $a %= $MOD;
            while ($e > 0) {
                if ($e & 1) $res = $res * $a % $MOD;
                $a = $a * $a % $MOD;
                $e >>= 1;
            }
            return $res;
        };
        $freq = [];
        $add = function($score, $x) use (&$freq, $modPow, $MOD) {
            $c = $freq[$x] ?? 0;
            if ($c > 0) $score = ($score - $modPow($x, $c) + $MOD) % $MOD;
            $freq[$x] = $c + 1;
            return ($score + $modPow($x, $c + 1)) % $MOD;
        };
        $remove = function($score, $x) use (&$freq, $modPow, $MOD) {
            $c = $freq[$x];
            $score = ($score - $modPow($x, $c) + $MOD) % $MOD;
            if ($c === 1) unset($freq[$x]);
            else {
                $freq[$x] = $c - 1;
                $score = ($score + $modPow($x, $c - 1)) % $MOD;
            }
            return $score;
        };
        $score = 0;
        $best = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $score = $add($score, $nums[$i]);
            if ($i >= $k) $score = $remove($score, $nums[$i - $k]);
            if ($i >= $k - 1 && $score > $best) $best = $score;
        }
        return $best;
    }
}
