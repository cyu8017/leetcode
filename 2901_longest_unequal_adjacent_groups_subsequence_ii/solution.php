<?php
// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

class Solution {
    function getWordsInLongestSubsequence($words, $groups) {
        $n = count($words);
        $dp = array_fill(0, $n, 1);
        $prev = array_fill(0, $n, -1);
        $best = 1;
        $bestI = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ($groups[$i] !== $groups[$j] && $this->hamming($words[$i], $words[$j]) === 1 && $dp[$j] + 1 > $dp[$i]) {
                    $dp[$i] = $dp[$j] + 1;
                    $prev[$i] = $j;
                }
            }
            if ($dp[$i] > $best) {
                $best = $dp[$i];
                $bestI = $i;
            }
        }
        $path = [];
        for ($i = $bestI; $i !== -1; $i = $prev[$i]) $path[] = $words[$i];
        return array_reverse($path);
    }

    private function hamming($a, $b) {
        if (strlen($a) !== strlen($b)) return 100;
        $d = 0;
        $n = strlen($a);
        for ($i = 0; $i < $n; $i++) if ($a[$i] !== $b[$i]) $d++;
        return $d;
    }
}
