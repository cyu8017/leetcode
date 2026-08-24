<?php
// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

class Solution {
    function countGoodIntegers($n, $k) {
        $half = intdiv($n + 1, 2);
        $start = 1;
        for ($i = 1; $i < $half; $i++) $start *= 10;
        $end = $start * 10;
        $seen = [];
        $ans = 0;
        $fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) $fact[$i] = $fact[$i - 1] * $i;
        for ($h = $start; $h < $end; $h++) {
            $s = (string)$h;
            $pal = $s;
            $revStart = strlen($s) - 1;
            if ($n % 2 === 1) $revStart--;
            for ($i = $revStart; $i >= 0; $i--) $pal .= $s[$i];
            if (intval($pal) % $k !== 0) continue;
            $charsArr = str_split($pal);
            sort($charsArr);
            $chars = implode('', $charsArr);
            if (isset($seen[$chars])) continue;
            $seen[$chars] = true;
            $cnt = array_fill(0, 10, 0);
            $clen = strlen($chars);
            for ($i = 0; $i < $clen; $i++) $cnt[ord($chars[$i]) - 48]++;
            $total = $fact[$n];
            foreach ($cnt as $c) $total = intdiv($total, $fact[$c]);
            if ($cnt[0] > 0) {
                $bad = $fact[$n - 1];
                $cnt[0]--;
                foreach ($cnt as $c) $bad = intdiv($bad, $fact[$c]);
                $cnt[0]++;
                $total -= $bad;
            }
            $ans += $total;
        }
        return $ans;
    }
}
