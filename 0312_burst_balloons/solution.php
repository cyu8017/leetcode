// LeetCode 0312 - Burst Balloons
// https://leetcode.com/problems/burst-balloons/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxCoins($nums) {
        $balloons = array_merge([1], $nums, [1]);
        $size = count($balloons);
        $dp = array_fill(0, $size, array_fill(0, $size, 0));
        for ($length = 3; $length <= $size; $length++) {
            for ($left = 0; $left <= $size - $length; $left++) {
                $right = $left + $length - 1;
                for ($mid = $left + 1; $mid < $right; $mid++) {
                    $coins = $dp[$left][$mid] + $dp[$mid][$right] +
                        $balloons[$left] * $balloons[$mid] * $balloons[$right];
                    $dp[$left][$right] = max($dp[$left][$right], $coins);
                }
            }
        }
        return $dp[0][$size - 1];
    }
}
