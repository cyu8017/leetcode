<?php
// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

class Solution {
    function minCost($source, $target, $rules, $costs) {
        $n = strlen($source);
        if (strlen($target) != $n) return -1;
        $dp = array_fill(0, $n + 1, 2147483647);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] == 2147483647) continue;
            if ($source[$i] == $target[$i] && $dp[$i] < $dp[$i + 1]) $dp[$i + 1] = $dp[$i];
            for ($j = 0; $j < count($rules); $j++) {
                $p = $rules[$j][0];
                $r = $rules[$j][1];
                $plen = strlen($p);
                if ($i + $plen > $n) continue;
                $c = $costs[$j];
                $ok = true;
                for ($k = 0; $k < $plen; $k++) {
                    if ($r[$k] != $target[$i + $k]) { $ok = false; break; }
                    if ($p[$k] == '*') $c++;
                    else if ($p[$k] != $source[$i + $k]) { $ok = false; break; }
                }
                if ($ok && $dp[$i] <= 2147483647 - $c && $dp[$i] + $c < $dp[$i + $plen]) {
                    $dp[$i + $plen] = $dp[$i] + $c;
                }
            }
        }
        return $dp[$n] == 2147483647 ? -1 : $dp[$n];
    }
}
