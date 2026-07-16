<?php

class Solution {
    function wordBreak($s, $wordDict) {
        $words = array_fill_keys($wordDict, true);
        $n = strlen($s);
        $canBreak = array_fill(0, $n + 1, false);
        $canBreak[0] = true;

        for ($end = 1; $end <= $n; $end++) {
            for ($start = 0; $start < $end; $start++) {
                if ($canBreak[$start] && isset($words[substr($s, $start, $end - $start)])) {
                    $canBreak[$end] = true;
                    break;
                }
            }
        }
        return $canBreak[$n];
    }
}