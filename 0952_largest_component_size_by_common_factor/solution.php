<?php
// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

class Solution {
    function largestComponentSize($nums) {
        $mx = max($nums);
        $parent = range(0, $mx);
        $find = function ($x) use (&$find, &$parent) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $factors = function ($x) {
            $res = [];
            for ($d = 2; $d * $d <= $x; $d++) {
                if ($x % $d === 0) {
                    $res[] = $d;
                    while ($x % $d === 0) $x = intdiv($x, $d);
                }
            }
            if ($x > 1) $res[] = $x;
            return $res;
        };
        foreach ($nums as $num) {
            foreach ($factors($num) as $f) $parent[$find($num)] = $find($f);
        }
        $cnt = [];
        $ans = 0;
        foreach ($nums as $num) {
            $r = $find($num);
            $c = ($cnt[$r] ?? 0) + 1;
            $cnt[$r] = $c;
            $ans = max($ans, $c);
        }
        return $ans;
    }
}
