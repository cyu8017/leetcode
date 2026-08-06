<?php
class Solution {
    function ways($pizza, $k) {
        $mod = 1000000007;
        $rows = count($pizza);
        $cols = strlen($pizza[0]);
        $apples = array_fill(0, $rows + 1, array_fill(0, $cols + 1, 0));
        for ($r = $rows - 1; $r >= 0; $r--) {
            for ($c = $cols - 1; $c >= 0; $c--) {
                $apples[$r][$c] = ($pizza[$r][$c] === "A" ? 1 : 0) + $apples[$r + 1][$c] + $apples[$r][$c + 1] - $apples[$r + 1][$c + 1];
            }
        }
        $dp = [];
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) $dp[$r][$c] = $apples[$r][$c] ? 1 : 0;
        }
        for ($cut = 1; $cut < $k; $cut++) {
            $nxt = array_fill(0, $rows, array_fill(0, $cols, 0));
            for ($r = 0; $r < $rows; $r++) {
                for ($c = 0; $c < $cols; $c++) {
                    for ($nr = $r + 1; $nr < $rows; $nr++) {
                        if ($apples[$r][$c] > $apples[$nr][$c]) $nxt[$r][$c] += $dp[$nr][$c];
                    }
                    for ($nc = $c + 1; $nc < $cols; $nc++) {
                        if ($apples[$r][$c] > $apples[$r][$nc]) $nxt[$r][$c] += $dp[$r][$nc];
                    }
                    $nxt[$r][$c] %= $mod;
                }
            }
            $dp = $nxt;
        }
        return $dp[0][0];
    }
}
