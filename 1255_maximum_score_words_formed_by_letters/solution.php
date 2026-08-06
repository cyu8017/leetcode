<?php
// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution {
    /**
     * @param String[] $words
     * @param String[] $letters
     * @param Integer[] $score
     * @return Integer
     */
    function maxScoreWords($words, $letters, $score) {
        $available = array_count_values($letters);
        $counts = [];
        $values = [];
        foreach ($words as $word) {
            $counts[] = array_count_values(str_split($word));
            $v = 0;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) $v += $score[ord($word[$i]) - 97];
            $values[] = $v;
        }
        $dfs = function ($i) use (&$dfs, &$available, $counts, $values, $words) {
            if ($i === count($words)) return 0;
            $best = $dfs($i + 1);
            $ok = true;
            foreach ($counts[$i] as $ch => $need) {
                if (($available[$ch] ?? 0) < $need) { $ok = false; break; }
            }
            if ($ok) {
                foreach ($counts[$i] as $ch => $need) $available[$ch] -= $need;
                $best = max($best, $values[$i] + $dfs($i + 1));
                foreach ($counts[$i] as $ch => $need) $available[$ch] += $need;
            }
            return $best;
        };
        return $dfs(0);
    }
}
