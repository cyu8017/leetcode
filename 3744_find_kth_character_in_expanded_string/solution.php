<?php
// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

class Solution {
    function kthCharacter($s, $k) {
        $words = preg_split('/\s+/', trim($s));
        foreach ($words as $w) {
            $m = (1 + strlen($w)) * strlen($w) / 2;
            if ($k == $m) return ' ';
            if ($k > $m) {
                $k -= $m + 1;
            } else {
                $cur = 0;
                for ($i = 0; ; $i++) {
                    $cur += $i + 1;
                    if ($k < $cur) return $w[$i];
                }
            }
        }
        return ' ';
    }
}
