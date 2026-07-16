// LeetCode 0346 - Moving Average from Data Stream
// https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage {
    private int $size;
    private array $values = [];
    private int $total = 0;

    function __construct(int $size) {
        $this->size = $size;
    }

    function next(int $val): float {
        $this->values[] = $val;
        $this->total += $val;
        if (count($this->values) > $this->size) {
            $this->total -= array_shift($this->values);
        }
        return $this->total / count($this->values);
    }
}
