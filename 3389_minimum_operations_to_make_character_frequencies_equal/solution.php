<?php
// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

class Solution {
    function makeStringGood($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $ans = $n;
        for ($t = 1; $t <= $n; $t++) {
            $pool = 0;
            for ($i = 0; $i < 26; $i++) if ($freq[$i] > $t) $pool += $freq[$i] - $t;
            $deficit = 0;
            for ($i = 0; $i < 26; $i++) if ($freq[$i] < $t) $deficit += $t - $freq[$i];
            $ops = max($pool, $deficit);
            if ($ops < $ans) $ans = $ops;
        }
        if ($n < $ans) $ans = $n;
        return $ans;
    }
}
