// LeetCode 0325 - Maximum Size Subarray Sum Equals k
// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxSubArrayLen($nums, $k) {
        $prefixIndex = [0 => -1];
        $prefix = 0;
        $best = 0;
        foreach ($nums as $index => $num) {
            $prefix += $num;
            $target = $prefix - $k;
            if (array_key_exists($target, $prefixIndex)) {
                $best = max($best, $index - $prefixIndex[$target]);
            }
            if (!array_key_exists($prefix, $prefixIndex)) {
                $prefixIndex[$prefix] = $index;
            }
        }
        return $best;
    }
}
