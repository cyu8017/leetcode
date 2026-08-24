<?php
// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution {
    function similarPairs($words) {
        $freq = [];
        $ans = 0;
        foreach ($words as $w) {
            $mask = 0;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) $mask |= 1 << (ord($w[$i]) - 97);
            $ans += isset($freq[$mask]) ? $freq[$mask] : 0;
            if (!isset($freq[$mask])) $freq[$mask] = 0;
            $freq[$mask]++;
        }
        return $ans;
    }
}
