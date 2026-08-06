<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minSpaceWastedKResizing($nums, $k) {
        $n = count($nums);
        $INF = PHP_INT_MAX;
        $waste = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            $mx = 0;
            $total = 0;
            for ($j = $i; $j < $n; $j++) {
                $mx = max($mx, $nums[$j]);
                $total += $nums[$j];
                $waste[$i][$j] = $mx * ($j - $i + 1) - $total;
            }
        }

        $segments = $k + 1;
        $dp = array_fill(0, $n + 1, array_fill(0, $segments + 1, $INF));
        $dp[0][0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            for ($s = 1; $s <= min($segments, $i); $s++) {
                for ($p = $s - 1; $p < $i; $p++) {
                    if ($dp[$p][$s - 1] === $INF) {
                        continue;
                    }
                    $dp[$i][$s] = min($dp[$i][$s], $dp[$p][$s - 1] + $waste[$p][$i - 1]);
                }
            }
        }
        $ans = $INF;
        for ($s = 1; $s <= $segments; $s++) {
            $ans = min($ans, $dp[$n][$s]);
        }
        return $ans;
    }
}
