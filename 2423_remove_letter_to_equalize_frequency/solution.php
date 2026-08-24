<?php
// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution {
    function equalFrequency($word) {
        $n = strlen($word);
        for ($skip = 0; $skip < $n; $skip++) {
            $cnt = array_fill(0, 26, 0);
            for ($i = 0; $i < $n; $i++) {
                if ($i === $skip) continue;
                $cnt[ord($word[$i]) - 97]++;
            }
            $freq = [];
            foreach ($cnt as $c) {
                if ($c > 0) {
                    if (!isset($freq[$c])) $freq[$c] = 0;
                    $freq[$c]++;
                }
            }
            if (count($freq) === 1) return true;
        }
        return false;
    }
}
