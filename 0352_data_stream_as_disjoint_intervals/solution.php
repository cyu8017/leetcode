// LeetCode 0352 - Data Stream as Disjoint Intervals
// https://leetcode.com/problems/data-stream-as-disjoint-intervals/

class SummaryRanges {
    /** @var int[][] */
    private array $intervals = [];

    function addNum(int $value): void {
        $this->add_num($value);
    }

    function add_num(int $value): void {
        $newInterval = [$value, $value];
        $merged = [];
        $inserted = false;

        foreach ($this->intervals as $interval) {
            if ($interval[1] < $value - 1) {
                $merged[] = $interval;
            } elseif ($interval[0] > $value + 1) {
                if (!$inserted) {
                    $merged[] = $newInterval;
                    $inserted = true;
                }
                $merged[] = $interval;
            } else {
                $newInterval[0] = min($newInterval[0], $interval[0]);
                $newInterval[1] = max($newInterval[1], $interval[1]);
            }
        }

        if (!$inserted) {
            $merged[] = $newInterval;
        }

        $this->intervals = $merged;
    }

    /**
     * @return int[][]
     */
    function getIntervals(): array {
        return $this->get_intervals();
    }

    /**
     * @return int[][]
     */
    function get_intervals(): array {
        return $this->intervals;
    }
}
