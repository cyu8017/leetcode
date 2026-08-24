<?php
// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution {
    function minimumPushes($word) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) $cnt[ord($word[$i]) - 97]++;
        sort($cnt);
        $ans = 0;
        for ($i = 0; $i < 26; $i++) $ans += (intdiv($i, 8) + 1) * $cnt[26 - $i - 1];
        return $ans;
    }
}
