<?php
// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

class Solution {
    function minDeletion($s, $k) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        sort($cnt);
        $ans = 0;
        for ($i = 0; $i + $k < 26; $i++) $ans += $cnt[$i];
        return $ans;
    }
}
