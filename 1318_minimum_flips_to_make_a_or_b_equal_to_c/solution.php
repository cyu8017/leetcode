<?php
class Solution {
    function minFlips($a, $b, $c) {
        $flips = 0;
        while ($a || $b || $c) {
            $x = $a & 1;
            $y = $b & 1;
            $z = $c & 1;
            $flips += $z === 0 ? $x + $y : (($x === 0 && $y === 0) ? 1 : 0);
            $a >>= 1;
            $b >>= 1;
            $c >>= 1;
        }
        return $flips;
    }
}
