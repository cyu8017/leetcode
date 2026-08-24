<?php
// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution {
    function garbageCollection($garbage, $travel) {
        $ans = 0;
        $lastM = 0;
        $lastP = 0;
        $lastG = 0;
        $gn = count($garbage);
        for ($i = 0; $i < $gn; $i++) {
            $ans += strlen($garbage[$i]);
            $len = strlen($garbage[$i]);
            for ($j = 0; $j < $len; $j++) {
                $c = $garbage[$i][$j];
                if ($c === 'M') $lastM = $i;
                elseif ($c === 'P') $lastP = $i;
                else $lastG = $i;
            }
        }
        $tn = count($travel);
        $pref = array_fill(0, $tn + 1, 0);
        for ($i = 0; $i < $tn; $i++) $pref[$i + 1] = $pref[$i] + $travel[$i];
        $ans += $pref[$lastM] + $pref[$lastP] + $pref[$lastG];
        return $ans;
    }
}
