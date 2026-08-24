<?php
// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

class Solution {
    function firstMatchingIndex($s) {
        $n = strlen($s);
        $lim = intdiv($n, 2) + 1;
        for ($i = 0; $i < $lim; $i++) {
            if ($s[$i] === $s[$n - $i - 1]) return $i;
        }
        return -1;
    }
}
