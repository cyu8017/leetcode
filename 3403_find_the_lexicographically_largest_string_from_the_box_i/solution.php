<?php
// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

class Solution {
    function answerString($word, $numFriends) {
        if ($numFriends === 1) return $word;
        $n = strlen($word);
        $maxLen = $n - ($numFriends - 1);
        $ans = "";
        for ($i = 0; $i < $n; $i++) {
            $end = $i + $maxLen;
            if ($end > $n) $end = $n;
            $cand = substr($word, $i, $end - $i);
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
