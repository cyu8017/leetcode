<?php
// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

class Solution {
    function countDistinct($n) {
        $s = strval($n);
        $m = strlen($s);
        $f = [];
        for ($i = 0; $i < 20; $i++) {
            $f[$i] = [];
            for ($z = 0; $z < 2; $z++) {
                $f[$i][$z] = [];
                for ($l = 0; $l < 2; $l++) $f[$i][$z][$l] = array_fill(0, 2, -1);
            }
        }
        $dfs = function($i, $zero, $lead, $limit) use (&$dfs, &$f, $s, $m) {
            if ($i === $m) return ($zero === 0 && $lead === 0) ? 1 : 0;
            if ($limit === 0 && $f[$i][$zero][$lead][$limit] !== -1) return $f[$i][$zero][$lead][$limit];
            $up = $limit === 1 ? ord($s[$i]) - 48 : 9;
            $ans = 0;
            for ($d = 0; $d <= $up; $d++) {
                $nxtZero = $zero;
                if ($d === 0 && $lead === 0) $nxtZero = 1;
                $nxtLead = ($lead === 1 && $d === 0) ? 1 : 0;
                $nxtLimit = ($limit === 1 && $d === $up) ? 1 : 0;
                $ans += $dfs($i + 1, $nxtZero, $nxtLead, $nxtLimit);
            }
            if ($limit === 0) $f[$i][$zero][$lead][$limit] = $ans;
            return $ans;
        };
        return $dfs(0, 0, 1, 1);
    }
}
