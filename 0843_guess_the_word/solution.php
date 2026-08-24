<?php
// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

class Solution {
    /**
     * @param String[] $words
     * @param Master $master
     * @return NULL
     */
    function findSecretWord($words, $master) {
        $match = function($a, $b) {
            $m = 0;
            $len = strlen($a);
            for ($i = 0; $i < $len; $i++) if ($a[$i] === $b[$i]) $m++;
            return $m;
        };
        $candidates = $words;
        while (count($candidates)) {
            $best = $candidates[0];
            $bestWorst = count($candidates) + 1;
            foreach ($candidates as $w) {
                $buckets = array_fill(0, 7, 0);
                foreach ($candidates as $c) $buckets[$match($w, $c)]++;
                $worst = 0;
                foreach ($buckets as $b) $worst = max($worst, $b);
                if ($worst < $bestWorst) {
                    $bestWorst = $worst;
                    $best = $w;
                }
            }
            $score = $master->guess($best);
            if ($score === 6) return;
            $next = [];
            foreach ($candidates as $c) {
                if ($match($c, $best) === $score) $next[] = $c;
            }
            $candidates = $next;
        }
    }
}
