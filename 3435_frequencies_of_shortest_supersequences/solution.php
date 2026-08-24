<?php
// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

class Solution {
    function supersequences($words) {
        $used = array_fill(0, 26, false);
        foreach ($words as $w) {
            $used[ord($w[0]) - 97] = true;
            $used[ord($w[1]) - 97] = true;
        }
        $letters = [];
        for ($i = 0; $i < 26; $i++) if ($used[$i]) $letters[] = $i;
        $m = count($letters);
        $freq = array_fill(0, 26, 0);
        $best = 1e9;
        $bestFreqs = [];
        $dfs = null;
        $dfs = function($i) use (&$dfs, $m, &$letters, &$freq, &$best, &$bestFreqs, $words) {
            if ($i === $m) {
                foreach ($words as $w) {
                    $a = ord($w[0]) - 97;
                    $b = ord($w[1]) - 97;
                    if ($a === $b) {
                        if ($freq[$a] < 2) return;
                    } else if ($freq[$a] < 1 || $freq[$b] < 1) return;
                }
                $sum = 0;
                $f = $freq;
                for ($j = 0; $j < 26; $j++) $sum += $freq[$j];
                if ($sum < $best) {
                    $best = $sum;
                    $bestFreqs = [$f];
                } else if ($sum === $best) $bestFreqs[] = $f;
                return;
            }
            $L = $letters[$i];
            for ($c = 1; $c <= 2; $c++) {
                $freq[$L] = $c;
                $dfs($i + 1);
            }
            $freq[$L] = 0;
        };
        $dfs(0);
        return $bestFreqs;
    }
}
