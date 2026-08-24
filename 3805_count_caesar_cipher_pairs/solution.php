<?php
// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

class Solution {
    function countPairs($words) {
        $cnt = [];
        foreach ($words as $word) {
            $s = str_split($word);
            $k = ord('z') - ord($s[0]);
            for ($i = 1; $i < count($s); $i++) {
                $s[$i] = chr(97 + (ord($s[$i]) - 97 + $k) % 26);
            }
            $s[0] = 'z';
            $key = implode('', $s);
            if (!isset($cnt[$key])) $cnt[$key] = 0;
            $cnt[$key]++;
        }
        $ans = 0;
        foreach ($cnt as $v) $ans += $v * ($v - 1) / 2;
        return $ans;
    }
}
