<?php

class Solution {
    /**
     * @param Integer[] $stoneValue
     * @return Integer
     */
    function stoneGameV($stoneValue) {
        $n = count($stoneValue);
        if ($n === 0) {
            return 0;
        }
        $pre = [0];
        foreach ($stoneValue as $x) {
            $pre[] = $pre[count($pre) - 1] + $x;
        }
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        $left = array_fill(0, $n, array_fill(0, $n, 0));
        $right = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            $left[$i][$i] = $right[$i][$i] = $stoneValue[$i];
        }
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i <= $n - $length; $i++) {
                $j = $i + $length - 1;
                $lo = $i;
                $hi = $j - 1;
                while ($lo <= $hi) {
                    $mid = intdiv($lo + $hi, 2);
                    if (2 * ($pre[$mid + 1] - $pre[$i]) >= $pre[$j + 1] - $pre[$i]) {
                        $hi = $mid - 1;
                    } else {
                        $lo = $mid + 1;
                    }
                }
                $split = $lo;
                $leftSum = $pre[$split + 1] - $pre[$i];
                $rightSum = $pre[$j + 1] - $pre[$split + 1];
                $best = $right[$split + 1][$j];
                if ($leftSum === $rightSum) {
                    $best = max($best, $left[$i][$split]);
                } elseif ($split > $i) {
                    $best = max($best, $left[$i][$split - 1]);
                }
                $dp[$i][$j] = $best;
                $total = $pre[$j + 1] - $pre[$i];
                $left[$i][$j] = max($left[$i][$j - 1], $total + $best);
                $right[$i][$j] = max($right[$i + 1][$j], $total + $best);
            }
        }
        return $dp[0][$n - 1];
    }
}
