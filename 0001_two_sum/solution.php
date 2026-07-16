// LeetCode 0001 - Two Sum
// https://leetcode.com/problems/two-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $seen = [];
        foreach ($nums as $i => $num) {
            $complement = $target - $num;
            if (array_key_exists($complement, $seen)) {
                return [$seen[$complement], $i];
            }
            $seen[$num] = $i;
        }
        return [];
    }
}
