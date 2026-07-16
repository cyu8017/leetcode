// LeetCode 0377 - Combination Sum IV
// https://leetcode.com/problems/combination-sum-iv/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function combinationSum4($nums, $target) {
        return $this->combination_sum4($nums, $target);
    }

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function combination_sum4($nums, $target) {
        $dp = array_fill(0, $target + 1, 0);
        $dp[0] = 1;

        for ($amount = 1; $amount <= $target; $amount++) {
            foreach ($nums as $num) {
                if ($amount >= $num) {
                    $dp[$amount] += $dp[$amount - $num];
                }
            }
        }

        return $dp[$target];
    }
}
