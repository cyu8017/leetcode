<?php
class Solution {
    function xorOperation($n, $start) {
        $ans = 0;
        for ($i = 0; $i < $n; $i++) $ans ^= $start + 2 * $i;
        return $ans;
    }
}
