// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

class Solution {
    /**
     * @param Integer[][] $costs
     * @return Integer
     */
    function minCostII($costs) {
        if (count($costs) === 0) {
            return 0;
        }
        $colorCount = count($costs[0]);
        $previous = $costs[0];
        for ($row = 1; $row < count($costs); $row++) {
            $minCost = min($previous);
            $minIndex = array_search($minCost, $previous, true);
            $secondMin = min(array_values(array_filter(
                $previous,
                fn($value, $index) => $index !== $minIndex,
                ARRAY_FILTER_USE_BOTH
            )));
            $current = [];
            for ($color = 0; $color < $colorCount; $color++) {
                $extra = $color === $minIndex ? $secondMin : $minCost;
                $current[] = $costs[$row][$color] + $extra;
            }
            $previous = $current;
        }
        return min($previous);
    }
}
