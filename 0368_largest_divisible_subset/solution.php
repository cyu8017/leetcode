// LeetCode 0368 - Largest Divisible Subset
// https://leetcode.com/problems/largest-divisible-subset/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function largestDivisibleSubset($nums) {
        return $this->largest_divisible_subset($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function largest_divisible_subset($nums) {
        sort($nums);
        $chains = [];
        foreach ($nums as $num) {
            $chains[$num] = [$num];
        }

        $best = [];
        foreach ($nums as $num) {
            foreach ($chains as $prev => $chain) {
                if ($prev < $num && $num % $prev === 0 && count($chain) + 1 > count($chains[$num])) {
                    $chains[$num] = array_merge($chain, [$num]);
                }
            }
            if (count($chains[$num]) > count($best)) {
                $best = $chains[$num];
            }
        }

        return $best;
    }
}
