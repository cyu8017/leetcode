// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

class Solution {
    /**
     * @param int[] $nums
     * @return int
     */
    function numberOfArithmeticSlices($nums) {
        return $this->number_of_arithmetic_slices($nums);
    }

    /**
     * @param int[] $nums
     * @return int
     */
    function number_of_arithmetic_slices($nums) {
        $total = 0;
        $differences = array_fill(0, count($nums), []);

        foreach ($nums as $index => $value) {
            for ($previous = 0; $previous < $index; $previous++) {
                $diff = $value - $nums[$previous];
                $total += $differences[$previous][$diff] ?? 0;
                $differences[$index][$diff] = ($differences[$index][$diff] ?? 0) + ($differences[$previous][$diff] ?? 0) + 1;
            }
        }

        return $total;
    }
}
