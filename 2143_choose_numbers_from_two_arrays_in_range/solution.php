<?php
// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function countSubranges($nums1, $nums2) {
        $MOD = 1000000007;
        $n = count($nums1);
        $ans = 0;
        $dp = [];
        for ($i = 0; $i < $n; $i++) {
            $ndp = [];
            $ndp[$nums1[$i]] = (($ndp[$nums1[$i]] ?? 0) + 1) % $MOD;
            $ndp[-$nums2[$i]] = (($ndp[-$nums2[$i]] ?? 0) + 1) % $MOD;
            foreach ($dp as $diff => $cnt) {
                $ndp[$diff + $nums1[$i]] = (($ndp[$diff + $nums1[$i]] ?? 0) + $cnt) % $MOD;
                $ndp[$diff - $nums2[$i]] = (($ndp[$diff - $nums2[$i]] ?? 0) + $cnt) % $MOD;
            }
            $dp = $ndp;
            $ans = ($ans + ($dp[0] ?? 0)) % $MOD;
        }
        return $ans;
    }
}
