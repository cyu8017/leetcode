<?php
// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

class Solution {
    function kthCharacter($k, $operations) {
        $shift = 0;
        $ops = $operations;
        while (count($ops)) {
            $op = array_pop($ops);
            $len = count($ops);
            $half = $len >= 62 ? INF : (1 << $len);
            if ($k > $half) {
                $k = $k - $half;
                if ($op === 1) $shift++;
            }
        }
        return chr(97 + ($shift % 26));
    }
}
