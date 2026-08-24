<?php
// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution {
    function countPrefixes($words, $s) {
        $ans = 0;
        foreach ($words as $w)
            if (strlen($w) <= strlen($s) && strncmp($s, $w, strlen($w)) === 0) $ans++;
        return $ans;
    }
}
