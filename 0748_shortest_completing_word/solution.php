<?php
// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

class Solution {
    function shortestCompletingWord($licensePlate, $words) {
        $need = array_fill(0, 26, 0);
        $plen = strlen($licensePlate);
        for ($i = 0; $i < $plen; $i++) {
            $lower = strtolower($licensePlate[$i]);
            if ($lower >= 'a' && $lower <= 'z') $need[ord($lower) - 97]++;
        }
        $best = '';
        foreach ($words as $word) {
            $counts = array_fill(0, 26, 0);
            $wlen = strlen($word);
            for ($i = 0; $i < $wlen; $i++) $counts[ord($word[$i]) - 97]++;
            $ok = true;
            for ($i = 0; $i < 26; $i++) if ($counts[$i] < $need[$i]) { $ok = false; break; }
            if ($ok && (strlen($best) === 0 || $wlen < strlen($best))) $best = $word;
        }
        return $best;
    }
}
