<?php
class Solution {
    function numOfWays($n) {
        $mod = 1000000007;
        $aba = 6;
        $abc = 6;
        for ($i = 1; $i < $n; $i++) {
            $naba = (3 * $aba + 2 * $abc) % $mod;
            $nabc = (2 * $aba + 2 * $abc) % $mod;
            $aba = $naba;
            $abc = $nabc;
        }
        return ($aba + $abc) % $mod;
    }
}
