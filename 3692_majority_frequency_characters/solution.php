<?php
// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

class Solution {
    function majorityFrequencyGroup($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $f = [];
        for ($i = 0; $i < 26; $i++) {
            if ($cnt[$i] > 0) {
                if (!isset($f[$cnt[$i]])) $f[$cnt[$i]] = '';
                $f[$cnt[$i]] .= chr(97 + $i);
            }
        }
        $mx = 0;
        $mv = 0;
        $ans = '';
        foreach ($f as $v => $cs) {
            if (strlen($cs) > $mx || (strlen($cs) === $mx && $v > $mv)) {
                $mx = strlen($cs);
                $mv = $v;
                $ans = $cs;
            }
        }
        return $ans;
    }
}
