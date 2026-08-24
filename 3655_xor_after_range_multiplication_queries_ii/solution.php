<?php
// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

class Solution {
    function xorAfterQueries($nums, $queries) {
        $MOD = 1000000007;
        $n = count($nums);
        $byK = [];
        foreach ($queries as $q) {
            if (!isset($byK[$q[2]])) $byK[$q[2]] = [];
            $byK[$q[2]][] = $q;
        }
        $res = $nums;
        foreach ($byK as $list) {
            $fac = array_fill(0, $n, 1);
            foreach ($list as $u)
                for ($i = $u[0]; $i <= $u[1]; $i += $u[2])
                    $fac[$i] = ($fac[$i] * $u[3]) % $MOD;
            for ($i = 0; $i < $n; $i++)
                $res[$i] = ($res[$i] * $fac[$i]) % $MOD;
        }
        $ans = 0;
        foreach ($res as $v) $ans ^= $v;
        return $ans;
    }
}
