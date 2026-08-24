<?php
// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

class Solution {
    /**
     * @param String $paragraph
     * @param String[] $banned
     * @return String
     */
    function mostCommonWord($paragraph, $banned) {
        $bannedSet = [];
        foreach ($banned as $b) $bannedSet[$b] = true;
        $counts = [];
        $word = "";
        $best = "";
        $bestCount = 0;
        $n = strlen($paragraph);
        for ($i = 0; $i <= $n; $i++) {
            $ch = $i < $n ? $paragraph[$i] : ' ';
            if (ctype_alpha($ch)) {
                $word .= strtolower($ch);
            } elseif (strlen($word) > 0) {
                $w = $word;
                $word = "";
                if (!isset($bannedSet[$w])) {
                    $c = ($counts[$w] ?? 0) + 1;
                    $counts[$w] = $c;
                    if ($c > $bestCount) {
                        $bestCount = $c;
                        $best = $w;
                    }
                }
            }
        }
        return $best;
    }
}
