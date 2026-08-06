<?php
class Solution {
    function canArrange($arr, $k) {
        $count = array_fill(0, $k, 0);
        foreach ($arr as $x) {
            $r = $x % $k;
            if ($r < 0) $r += $k;
            $count[$r]++;
        }
        if ($count[0] % 2) return false;
        for ($r = 1; $r < $k; $r++) {
            if ($count[$r] !== $count[$k - $r]) return false;
        }
        return true;
    }
}
