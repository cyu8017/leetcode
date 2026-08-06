<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countSpecialSubsequences($nums) {
        $MOD = 1000000007;
        $a = $b = $c = 0;
        foreach ($nums as $x) {
            if ($x == 0) {
                $a = ($a * 2 + 1) % $MOD;
            } elseif ($x == 1) {
                $b = ($b * 2 + $a) % $MOD;
            } else {
                $c = ($c * 2 + $b) % $MOD;
            }
        }
        return $c;
    }
}
