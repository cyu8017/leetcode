<?php
// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution {
    function repeatedCharacter($s) {
        $seen = array_fill(0, 26, false);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $idx = ord($c) - 97;
            if ($seen[$idx]) return $c;
            $seen[$idx] = true;
        }
        return chr(0);
    }
}
