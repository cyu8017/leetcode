<?php
// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

class Solution {
    function mirrorFrequency($s) {
        $freq = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $freq[$c] = ($freq[$c] ?? 0) + 1;
        }
        $ans = 0;
        $vis = [];
        foreach ($freq as $c => $v) {
            if ($c >= 'a' && $c <= 'z') $m = chr(97 + 25 - (ord($c) - 97));
            else $m = chr(48 + (9 - (ord($c) - 48)));
            if (($vis[$m] ?? false) === true) continue;
            $vis[$c] = true;
            $mv = $freq[$m] ?? 0;
            $ans += abs($v - $mv);
        }
        return $ans;
    }
}
