<?php
// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $restrictions
     * @param Integer[][] $requests
     * @return Boolean[]
     */
    function friendRequests($n, $restrictions, $requests) {
        $parent = range(0, $n - 1);
        $find = null;
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $unite = function ($a, $b) use (&$parent, &$find) {
            $a = $find($a);
            $b = $find($b);
            if ($a !== $b) $parent[$a] = $b;
        };
        $ans = [];
        foreach ($requests as $i => $req) {
            $u = $find($req[0]);
            $v = $find($req[1]);
            $ok = true;
            if ($u !== $v) {
                foreach ($restrictions as $r) {
                    $x = $find($r[0]);
                    $y = $find($r[1]);
                    if (($x === $u && $y === $v) || ($x === $v && $y === $u)) { $ok = false; break; }
                }
            }
            $ans[$i] = $ok;
            if ($ok) $unite($u, $v);
        }
        return $ans;
    }
}
