// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsets($nums) {
        $result = [[]];

        foreach ($nums as $num) {
            $size = count($result);
            for ($i = 0; $i < $size; $i++) {
                $result[] = array_merge($result[$i], [$num]);
            }
        }

        return $result;
    }
}
