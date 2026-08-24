<?php
// LeetCode 0416 - Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canPartition($nums) {
        return $this->can_partition($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function can_partition($nums) {
        $total = array_sum($nums);
        if ($total % 2 !== 0) {
            return false;
        }

        $target = intdiv($total, 2);
        $possible = [0 => true];

        foreach ($nums as $value) {
            $next = $possible;
            foreach ($possible as $amount => $_) {
                $updated = $amount + $value;
                if ($updated <= $target) {
                    $next[$updated] = true;
                }
            }
            $possible = $next;
            if (isset($possible[$target])) {
                return true;
            }
        }

        return isset($possible[$target]);
    }
}
