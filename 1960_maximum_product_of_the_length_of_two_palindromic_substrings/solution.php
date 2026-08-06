<?php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maxProduct($s) {
        $n = strlen($s);
        $radius = array_fill(0, $n, 0);
        $center = 0;
        $right = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i < $right) {
                $radius[$i] = min($right - $i, $radius[2 * $center - $i]);
            }
            while (
                $i - $radius[$i] - 1 >= 0
                && $i + $radius[$i] + 1 < $n
                && $s[$i - $radius[$i] - 1] === $s[$i + $radius[$i] + 1]
            ) {
                $radius[$i]++;
            }
            if ($i + $radius[$i] > $right) {
                $center = $i;
                $right = $i + $radius[$i];
            }
        }

        $end = array_fill(0, $n, 1);
        $start = array_fill(0, $n, 1);
        for ($i = 0; $i < $n; $i++) {
            $r = $radius[$i];
            $end[$i + $r] = max($end[$i + $r], 2 * $r + 1);
            $start[$i - $r] = max($start[$i - $r], 2 * $r + 1);
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            $end[$i] = max($end[$i], $end[$i + 1] - 2);
        }
        for ($i = 1; $i < $n; $i++) {
            $start[$i] = max($start[$i], $start[$i - 1] - 2);
        }

        $pre = array_fill(0, $n, 0);
        $pre[0] = $end[0];
        for ($i = 1; $i < $n; $i++) {
            $pre[$i] = max($pre[$i - 1], $end[$i]);
        }
        $suf = array_fill(0, $n, 0);
        $suf[$n - 1] = $start[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            $suf[$i] = max($suf[$i + 1], $start[$i]);
        }

        $ans = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $ans = max($ans, $pre[$i] * $suf[$i + 1]);
        }
        return $ans;
    }
}
