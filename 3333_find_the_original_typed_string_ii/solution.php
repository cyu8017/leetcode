<?php
// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

class Solution {
    function possibleStringCount($word, $k) {
        $mod = 1000000007;
        $groups = [];
        $n = strlen($word);
        for ($i = 0; $i < $n; ) {
            $j = $i;
            while ($j < $n && $word[$j] === $word[$i]) $j++;
            $groups[] = $j - $i;
            $i = $j;
        }
        $total = 1;
        foreach ($groups as $g) $total = $total * $g % $mod;
        if ($k <= count($groups)) return $total;
        $need = $k - 1;
        $dp = array_fill(0, $need, 0);
        $dp[0] = 1;
        foreach ($groups as $g) {
            $ndp = array_fill(0, $need, 0);
            $pref = array_fill(0, $need + 1, 0);
            for ($i = 0; $i < $need; $i++) $pref[$i + 1] = ($pref[$i] + $dp[$i]) % $mod;
            for ($s = 0; $s < $need; $s++) {
                $lo = $s - $g;
                if ($lo < 0) $lo = 0;
                $hi = $s - 1;
                if ($hi >= 0) $ndp[$s] = ($pref[$hi + 1] - $pref[$lo] + $mod) % $mod;
            }
            $dp = $ndp;
        }
        $bad = 0;
        foreach ($dp as $v) $bad = ($bad + $v) % $mod;
        return ($total - $bad + $mod) % $mod;
    }
}
