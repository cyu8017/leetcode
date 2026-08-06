<?php
class Solution {
    function numberOfArrays($s, $k) {
        $mod = 1000000007;
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, 0);
        $dp[$n] = 1;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === "0") continue;
            $value = 0;
            for ($j = $i; $j < $n; $j++) {
                $value = $value * 10 + intval($s[$j]);
                if ($value > $k) break;
                $dp[$i] = ($dp[$i] + $dp[$j + 1]) % $mod;
            }
        }
        return $dp[0];
    }
}
