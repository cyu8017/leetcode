<?php
class Solution {
    /**
     * @param String $num
     * @return Integer
     */
    function numberOfCombinations($num) {
        $mod = 1000000007;
        $n = strlen($num);
        if ($num[0] === '0') {
            return 0;
        }

        $lcp = array_fill(0, $n + 1, array_fill(0, $n + 1, 0));
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $n - 1; $j >= 0; $j--) {
                if ($num[$i] === $num[$j]) {
                    $lcp[$i][$j] = $lcp[$i + 1][$j + 1] + 1;
                }
            }
        }

        $le = function ($a, $b, $length) use ($lcp, $num) {
            $common = $lcp[$a][$b];
            if ($common >= $length) {
                return true;
            }
            return $num[$a + $common] < $num[$b + $common];
        };

        $dp = array_fill(0, $n + 1, array_fill(0, $n + 1, 0));
        $pref = array_fill(0, $n + 1, array_fill(0, $n + 1, 0));

        for ($i = 1; $i <= $n; $i++) {
            for ($l = 1; $l <= $i; $l++) {
                $start = $i - $l;
                if ($num[$start] === '0') {
                    $dp[$i][$l] = 0;
                } elseif ($start === 0) {
                    $dp[$i][$l] = 1;
                } else {
                    $ways = $l > 1 ? $pref[$start][min($l - 1, $start)] : 0;
                    if ($start >= $l && $le($start - $l, $start, $l)) {
                        $ways = ($ways + $dp[$start][$l]) % $mod;
                    }
                    $dp[$i][$l] = $ways;
                }
            }
            for ($l = 1; $l <= $n; $l++) {
                $pref[$i][$l] = ($pref[$i][$l - 1] + ($l <= $i ? $dp[$i][$l] : 0)) % $mod;
            }
        }

        return $pref[$n][$n];
    }
}
