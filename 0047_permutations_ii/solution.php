// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function permuteUnique($nums) {
        sort($nums);
        $result = [];
        $path = [];
        $used = array_fill(0, count($nums), false);

        $backtrack = function () use (&$backtrack, $nums, &$result, &$path, &$used) {
            if (count($path) === count($nums)) {
                $result[] = $path;
                return;
            }

            for ($i = 0; $i < count($nums); $i++) {
                if ($used[$i]) {
                    continue;
                }
                if ($i > 0 && $nums[$i] === $nums[$i - 1] && !$used[$i - 1]) {
                    continue;
                }
                $used[$i] = true;
                $path[] = $nums[$i];
                $backtrack();
                array_pop($path);
                $used[$i] = false;
            }
        };

        $backtrack();
        return $result;
    }
}
