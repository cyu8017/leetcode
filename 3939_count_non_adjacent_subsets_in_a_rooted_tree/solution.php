<?php
// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

class Solution {
    function countNonAdjacentSubsets($parent, $nums, $k) {
        $mod = 1000000007;
        $n = count($parent);
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $children[$parent[$i]][] = $i;
        $dp0 = array_fill(0, $n, null);
        $dp1 = array_fill(0, $n, null);
        for ($u = $n - 1; $u >= 0; $u--) {
            $a = array_fill(0, $k, 0);
            $b = array_fill(0, $k, 0);
            $a[0] = 1;
            $b[(($nums[$u] % $k) + $k) % $k] = 1;
            foreach ($children[$u] as $v) {
                $na = array_fill(0, $k, 0);
                $nb = array_fill(0, $k, 0);
                for ($x = 0; $x < $k; $x++) {
                    for ($y = 0; $y < $k; $y++) {
                        $allChild = ($dp0[$v][$y] + $dp1[$v][$y]) % $mod;
                        $na[($x + $y) % $k] = ($na[($x + $y) % $k] + $a[$x] * $allChild) % $mod;
                        $nb[($x + $y) % $k] = ($nb[($x + $y) % $k] + $b[$x] * $dp0[$v][$y]) % $mod;
                    }
                }
                $a = $na;
                $b = $nb;
            }
            $dp0[$u] = $a;
            $dp1[$u] = $b;
        }
        $ans = ($dp0[0][0] + $dp1[0][0] - 1) % $mod;
        if ($ans < 0) $ans += $mod;
        return $ans;
    }
}
