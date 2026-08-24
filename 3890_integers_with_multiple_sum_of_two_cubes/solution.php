<?php
// LeetCode 3890 - Integers With Multiple Sum of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

class Solution {
    static $GOOD = null;
    function init() {
        if (self::$GOOD !== null) return;
        $LIMIT = 1000000000;
        $cnt = [];
        $cubes = [];
        for ($i = 0; $i <= 1000; $i++) $cubes[$i] = $i * $i * $i;
        for ($a = 1; $a <= 1000; $a++) {
            for ($b = $a; $b <= 1000; $b++) {
                $x = $cubes[$a] + $cubes[$b];
                if ($x > $LIMIT) break;
                $cnt[$x] = ($cnt[$x] ?? 0) + 1;
            }
        }
        self::$GOOD = [];
        foreach ($cnt as $k => $v) {
            if ($v > 1) self::$GOOD[] = $k;
        }
        sort(self::$GOOD);
    }
    function findGoodIntegers($n) {
        $this->init();
        $lo = 0;
        $hi = count(self::$GOOD);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if (self::$GOOD[$mid] <= $n) $lo = $mid + 1;
            else $hi = $mid;
        }
        return array_slice(self::$GOOD, 0, $lo);
    }
}
