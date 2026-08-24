<?php
// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

function leadingZeroCount($x) {
    if ($x === 0) return 32;
    $n = 0;
    for ($bit = 31; $bit >= 0; $bit--) {
        if ((($x >> $bit) & 1) !== 0) break;
        $n++;
    }
    return $n;
}

class Solution {
    function minimumDifference($nums, $k) {
        $mx = 0;
        foreach ($nums as $v) $mx = max($mx, $v);
        $m = $mx === 0 ? 1 : 32 - leadingZeroCount($mx);
        $cnt = array_fill(0, $m, 0);
        $ans = PHP_INT_MAX;
        $s = 0;
        $i = 0;
        $n = count($nums);
        for ($j = 0; $j < $n; $j++) {
            $x = $nums[$j];
            $s |= $x;
            $ans = min($ans, abs($s - $k));
            for ($h = 0; $h < $m; $h++) if ((($x >> $h) & 1) !== 0) $cnt[$h]++;
            while ($i < $j && $s > $k) {
                $y = $nums[$i];
                for ($h = 0; $h < $m; $h++) {
                    if ((($y >> $h) & 1) !== 0) {
                        $cnt[$h]--;
                        if ($cnt[$h] === 0) $s ^= 1 << $h;
                    }
                }
                $ans = min($ans, abs($s - $k));
                $i++;
            }
        }
        return $ans;
    }
}
