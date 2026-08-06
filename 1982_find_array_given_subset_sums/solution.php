<?php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $sums
     * @return Integer[]
     */
    function recoverArray($n, $sums) {
        sort($sums);
        $ans = [];
        for ($k = 0; $k < $n; $k++) {
            $d = $sums[1] - $sums[0];
            $count = [];
            foreach ($sums as $x) {
                if (!isset($count[$x])) {
                    $count[$x] = 0;
                }
                $count[$x]++;
            }
            $without = [];
            $withD = [];
            foreach ($sums as $x) {
                if (!isset($count[$x]) || $count[$x] === 0) {
                    continue;
                }
                $count[$x]--;
                $count[$x + $d]--;
                $without[] = $x;
                $withD[] = $x + $d;
            }
            if (in_array(0, $without, true)) {
                $ans[] = $d;
                $sums = $without;
            } else {
                $ans[] = -$d;
                $sums = $withD;
            }
        }
        return $ans;
    }
}
