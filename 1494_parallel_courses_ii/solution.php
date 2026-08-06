<?php
class Solution {
    function minNumberOfSemesters($n, $relations, $k) {
        $prereq = array_fill(0, $n, 0);
        foreach ($relations as [$a, $b]) $prereq[$b - 1] |= 1 << ($a - 1);
        $full = (1 << $n) - 1;
        $inf = 1000000000;
        $dp = array_fill(0, 1 << $n, $inf);
        $dp[0] = 0;
        for ($mask = 0; $mask <= $full; $mask++) {
            if ($dp[$mask] === $inf) continue;
            $available = 0;
            for ($c = 0; $c < $n; $c++) {
                if ((($mask >> $c) & 1) === 0 && ($prereq[$c] & $mask) === $prereq[$c]) {
                    $available |= 1 << $c;
                }
            }
            $bitCount = substr_count(decbin($available), "1");
            $choices = [];
            if ($bitCount <= $k) {
                $choices[] = $available;
            } else {
                $sub = $available;
                while ($sub) {
                    if (substr_count(decbin($sub), "1") === $k) $choices[] = $sub;
                    $sub = ($sub - 1) & $available;
                }
            }
            foreach ($choices as $take) {
                $dp[$mask | $take] = min($dp[$mask | $take], $dp[$mask] + 1);
            }
        }
        return $dp[$full];
    }
}
