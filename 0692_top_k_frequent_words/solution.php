<?php
// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

class Solution {
    function topKFrequent($words, $k) {
        $counts = [];
        foreach ($words as $word) $counts[$word] = ($counts[$word] ?? 0) + 1;
        $ordered = array_keys($counts);
        usort($ordered, function ($a, $b) use ($counts) {
            $ca = $counts[$a];
            $cb = $counts[$b];
            if ($ca !== $cb) return $cb - $ca;
            return $a < $b ? -1 : ($a > $b ? 1 : 0);
        });
        return array_slice($ordered, 0, $k);
    }
}
