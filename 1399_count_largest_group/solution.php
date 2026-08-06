<?php
class Solution {
    function countLargestGroup($n) {
        $c = [];
        for ($x = 1; $x <= $n; $x++) {
            $s = array_sum(array_map('intval', str_split(strval($x))));
            $c[$s] = ($c[$s] ?? 0) + 1;
        }
        $m = max($c);
        $ans = 0;
        foreach ($c as $v) if ($v === $m) $ans++;
        return $ans;
    }
}
