<?php
class Solution {
    function minInsertions($s) {
        $n = strlen($s);
        $dp = array_fill(0, $n, 0);
        for ($left = $n - 2; $left >= 0; $left--) {
            $diagonal = 0;
            for ($right = $left + 1; $right < $n; $right++) {
                $old = $dp[$right];
                if ($s[$left] === $s[$right]) $dp[$right] = $diagonal;
                else $dp[$right] = 1 + min($dp[$right], $dp[$right - 1]);
                $diagonal = $old;
            }
        }
        return $n ? $dp[$n - 1] : 0;
    }
}
