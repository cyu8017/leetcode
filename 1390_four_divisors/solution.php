<?php
class Solution {
    function sumFourDivisors($nums) {
        $ans = 0;
        foreach ($nums as $x) {
            $ds = [];
            $lim = intval(sqrt($x));
            for ($d = 1; $d <= $lim; $d++) {
                if ($x % $d === 0) {
                    $ds[$d] = true;
                    $ds[intdiv($x, $d)] = true;
                }
                if (count($ds) > 4) break;
            }
            if (count($ds) === 4) $ans += array_sum(array_keys($ds));
        }
        return $ans;
    }
}
