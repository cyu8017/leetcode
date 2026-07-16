// LeetCode 0057 - Insert Interval
// https://leetcode.com/problems/insert-interval/

class Solution {
    /**
     * @param Integer[][] $intervals
     * @param Integer[] $newInterval
     * @return Integer[][]
     */
    function insert($intervals, $newInterval) {
        $result = [];
        $i = 0;

        while ($i < count($intervals) && $intervals[$i][1] < $newInterval[0]) {
            $result[] = $intervals[$i];
            $i++;
        }

        while ($i < count($intervals) && $intervals[$i][0] <= $newInterval[1]) {
            $newInterval[0] = min($newInterval[0], $intervals[$i][0]);
            $newInterval[1] = max($newInterval[1], $intervals[$i][1]);
            $i++;
        }

        $result[] = $newInterval;

        while ($i < count($intervals)) {
            $result[] = $intervals[$i];
            $i++;
        }

        return $result;
    }
}
