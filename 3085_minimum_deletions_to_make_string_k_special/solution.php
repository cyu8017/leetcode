<?php
// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

class Solution {
    function minimumDeletions($word, $k) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) $freq[ord($word[$i]) - 97]++;
        $nums = [];
        foreach ($freq as $v) if ($v > 0) $nums[] = $v;
        $ans = $n;
        for ($i = 0; $i <= $n; $i++) {
            $cur = 0;
            foreach ($nums as $x) {
                if ($x < $i) $cur += $x;
                else if ($x > $i + $k) $cur += $x - $i - $k;
            }
            $ans = min($ans, $cur);
        }
        return $ans;
    }
}
