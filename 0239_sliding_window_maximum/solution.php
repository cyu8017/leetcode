// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function maxSlidingWindow($nums, $k) {
        $window = [];
        $result = [];

        foreach ($nums as $index => $num) {
            while (!empty($window) && $nums[$window[count($window) - 1]] <= $num) {
                array_pop($window);
            }
            $window[] = $index;
            if ($window[0] <= $index - $k) {
                array_shift($window);
            }
            if ($index >= $k - 1) {
                $result[] = $nums[$window[0]];
            }
        }

        return $result;
    }
}
