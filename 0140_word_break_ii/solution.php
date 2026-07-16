<?php

class Solution {
    function wordBreak($s, $wordDict) {
        $words = array_fill_keys($wordDict, true);
        $n = strlen($s);
        $memo = [];

        $dfs = function ($start) use (&$dfs, &$memo, $s, $n, $words) {
            if ($start === $n) {
                return [""];
            }
            if (isset($memo[$start])) {
                return $memo[$start];
            }

            $sentences = [];
            for ($end = $start + 1; $end <= $n; $end++) {
                $word = substr($s, $start, $end - $start);
                if (!isset($words[$word])) {
                    continue;
                }
                foreach ($dfs($end) as $tail) {
                    $sentences[] = $tail === "" ? $word : "$word $tail";
                }
            }
            return $memo[$start] = $sentences;
        };

        return $dfs(0);
    }
}