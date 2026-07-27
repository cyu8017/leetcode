<?php
// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $requests
     * @return Integer
     */
    function maximumRequests($n, $requests) {
        $m = count($requests);
        $ans = 0;
        for ($mask = 0; $mask < (1 << $m); $mask++) {
            $bits = 0;
            $tmp = $mask;
            while ($tmp) {
                $bits += $tmp & 1;
                $tmp >>= 1;
            }
            if ($bits <= $ans) {
                continue;
            }
            $bal = array_fill(0, $n, 0);
            for ($i = 0; $i < $m; $i++) {
                if (($mask >> $i) & 1) {
                    $bal[$requests[$i][0]]--;
                    $bal[$requests[$i][1]]++;
                }
            }
            $ok = true;
            foreach ($bal as $v) {
                if ($v !== 0) {
                    $ok = false;
                    break;
                }
            }
            if ($ok) {
                $ans = $bits;
            }
        }
        return $ans;
    }
}
