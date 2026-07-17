<?php
// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function longestBeautifulSubstring($word) {
        $vowels = 'aeiou';
        $best = 0;
        $n = strlen($word);

        for ($start = 0; $start < $n; $start++) {
            if ($word[$start] !== 'a') {
                continue;
            }

            $counts = [0, 0, 0, 0, 0];
            for ($end = $start; $end < $n; $end++) {
                $current = $word[$end];
                if ($end > $start && $current < $word[$end - 1]) {
                    break;
                }

                $idx = strpos($vowels, $current);
                $counts[$idx]++;
                if ($idx > 0 && $counts[$idx - 1] === 0) {
                    break;
                }
                if ($counts[0] > 0 && $counts[1] > 0 && $counts[2] > 0 && $counts[3] > 0 && $counts[4] > 0) {
                    $best = max($best, $end - $start + 1);
                }
            }
        }

        return $best;
    }
}
