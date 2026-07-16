// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

class Solution {
    /**
     * @param Integer[] $nums
     * @return String[]
     */
    function summaryRanges($nums) {
        $result = [];
        $index = 0;
        $length = count($nums);

        while ($index < $length) {
            $start = $nums[$index];
            while ($index + 1 < $length && $nums[$index + 1] === $nums[$index] + 1) {
                $index++;
            }
            if ($start === $nums[$index]) {
                $result[] = (string)$start;
            } else {
                $result[] = $start . "->" . $nums[$index];
            }
            $index++;
        }

        return $result;
    }
}
