<?php
// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

class Solution {
    function handleQuery($nums1, $nums2, $queries) {
        $n = count($nums1);
        $ones = array_fill(0, 4 * $n, 0);
        $lazy = array_fill(0, 4 * $n, false);
        $build = function($idx, $l, $r) use (&$build, &$ones, $nums1) {
            if ($l === $r) {
                $ones[$idx] = $nums1[$l];
                return;
            }
            $m = ($l + $r) >> 1;
            $build($idx * 2, $l, $m);
            $build($idx * 2 + 1, $m + 1, $r);
            $ones[$idx] = $ones[$idx * 2] + $ones[$idx * 2 + 1];
        };
        $apply = function($idx, $l, $r) use (&$ones, &$lazy) {
            $ones[$idx] = ($r - $l + 1) - $ones[$idx];
            $lazy[$idx] = !$lazy[$idx];
        };
        $push = function($idx, $l, $r) use (&$lazy, $apply) {
            if ($lazy[$idx] && $l !== $r) {
                $m = ($l + $r) >> 1;
                $apply($idx * 2, $l, $m);
                $apply($idx * 2 + 1, $m + 1, $r);
                $lazy[$idx] = false;
            }
        };
        $update = function($idx, $l, $r, $ql, $qr) use (&$update, &$ones, $push, $apply) {
            if ($ql <= $l && $r <= $qr) {
                $apply($idx, $l, $r);
                return;
            }
            $push($idx, $l, $r);
            $m = ($l + $r) >> 1;
            if ($ql <= $m) $update($idx * 2, $l, $m, $ql, $qr);
            if ($qr > $m) $update($idx * 2 + 1, $m + 1, $r, $ql, $qr);
            $ones[$idx] = $ones[$idx * 2] + $ones[$idx * 2 + 1];
        };
        $build(1, 0, $n - 1);
        $sum2 = 0;
        foreach ($nums2 as $x) $sum2 += $x;
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) $update(1, 0, $n - 1, $q[1], $q[2]);
            else if ($q[0] === 2) $sum2 += $q[1] * $ones[1];
            else $ans[] = $sum2;
        }
        return $ans;
    }
}
