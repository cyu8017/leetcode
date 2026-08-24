<?php
// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution {
    /**
     * @param String[] $words1
     * @param String[] $words2
     * @return Integer
     */
    function countWords($words1, $words2) {
        $f1 = [];
        $f2 = [];
        foreach ($words1 as $w) $f1[$w] = ($f1[$w] ?? 0) + 1;
        foreach ($words2 as $w) $f2[$w] = ($f2[$w] ?? 0) + 1;
        $ans = 0;
        foreach ($f1 as $k => $v)
            if ($v === 1 && ($f2[$k] ?? 0) === 1) $ans++;
        return $ans;
    }
}
