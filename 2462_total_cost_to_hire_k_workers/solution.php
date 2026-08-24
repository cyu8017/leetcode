<?php
// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

class Solution {
    function totalCost($costs, $k, $candidates) {
        $leftH = new SplPriorityQueue();
        $rightH = new SplPriorityQueue();
        $n = count($costs);
        $l = 0;
        $r = $n - 1;
        while ($l <= $r && $leftH->count() < $candidates) {
            $leftH->insert([$costs[$l], $l], [-$costs[$l], -$l]);
            $l++;
        }
        while ($r >= $l && $rightH->count() < $candidates) {
            $rightH->insert([$costs[$r], $r], [-$costs[$r], -$r]);
            $r--;
        }
        $ans = 0;
        for ($t = 0; $t < $k; $t++) {
            $useLeft = false;
            if (!$leftH->isEmpty() && !$rightH->isEmpty()) {
                $lt = $leftH->top();
                $rt = $rightH->top();
                if ($lt[0] < $rt[0] || ($lt[0] === $rt[0] && $lt[1] <= $rt[1])) $useLeft = true;
            } elseif (!$leftH->isEmpty()) {
                $useLeft = true;
            }
            if ($useLeft) {
                $ans += $leftH->extract()[0];
                if ($l <= $r) {
                    $leftH->insert([$costs[$l], $l], [-$costs[$l], -$l]);
                    $l++;
                }
            } else {
                $ans += $rightH->extract()[0];
                if ($l <= $r) {
                    $rightH->insert([$costs[$r], $r], [-$costs[$r], -$r]);
                    $r--;
                }
            }
        }
        return $ans;
    }
}
