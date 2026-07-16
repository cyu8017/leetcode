// LeetCode 0403 - Frog Jump
// https://leetcode.com/problems/frog-jump/

class Solution {
    /**
     * @param Integer[] $stones
     * @return Boolean
     */
    function canCross($stones) {
        return $this->can_cross($stones);
    }

    /**
     * @param Integer[] $stones
     * @return Boolean
     */
    function can_cross($stones) {
        $stoneSet = array_flip($stones);
        $jumps = [];
        foreach ($stones as $stone) {
            $jumps[$stone] = [];
        }
        $jumps[0][0] = true;

        foreach ($stones as $stone) {
            foreach (array_keys($jumps[$stone]) as $jump) {
                foreach ([$jump - 1, $jump, $jump + 1] as $nextJump) {
                    if ($nextJump > 0 && isset($stoneSet[$stone + $nextJump])) {
                        $jumps[$stone + $nextJump][$nextJump] = true;
                    }
                }
            }
        }

        return !empty($jumps[$stones[count($stones) - 1]]);
    }
}
