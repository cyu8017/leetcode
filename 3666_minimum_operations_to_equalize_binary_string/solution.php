<?php
// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

class Solution {
    function minOperations($s, $k) {
        $n = strlen($s);
        $ts = [[], []];
        for ($i = 0; $i <= $n; $i++) $ts[$i % 2][$i] = true;
        $cnt0 = 0;
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '0') $cnt0++;
        unset($ts[$cnt0 % 2][$cnt0]);
        $q = [$cnt0];
        $ans = 0;
        while ($q) {
            $nq = [];
            foreach ($q as $cur) {
                if ($cur === 0) return $ans;
                $l = $cur + $k - 2 * min($cur, $k);
                $r = $cur + $k - 2 * max($k - $n + $cur, 0);
                $t = &$ts[$l % 2];
                $sorted = array_keys($t);
                sort($sorted);
                foreach ($sorted as $it) {
                    if ($it < $l) continue;
                    if ($it > $r) break;
                    $nq[] = $it;
                    unset($t[$it]);
                }
                unset($t);
            }
            $q = $nq;
            $ans++;
        }
        return -1;
    }
}
