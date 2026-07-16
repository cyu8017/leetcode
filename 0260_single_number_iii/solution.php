// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function singleNumber($nums) {
        $xorAll = 0;
        foreach ($nums as $num) {
            $xorAll ^= $num;
        }
        $diff = $xorAll & -$xorAll;
        $first = 0;
        $second = 0;
        foreach ($nums as $num) {
            if ($num & $diff) {
                $first ^= $num;
            } else {
                $second ^= $num;
            }
        }
        return [$first, $second];
    }
}
