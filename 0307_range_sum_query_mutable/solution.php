// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

class NumArray {
    /** @var int[] */
    private $nums;
    /** @var int */
    private $size;
    /** @var int[] */
    private $tree;

    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        $this->nums = $nums;
        $this->size = count($nums);
        $this->tree = array_fill(0, $this->size + 1, 0);
        foreach ($nums as $index => $value) {
            $this->add($index + 1, $value);
        }
    }

    /**
     * @param Integer $index
     * @param Integer $val
     * @return void
     */
    function update($index, $val) {
        $delta = $val - $this->nums[$index];
        $this->nums[$index] = $val;
        $this->add($index + 1, $delta);
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function sumRange($left, $right) {
        return $this->prefix($right + 1) - $this->prefix($left);
    }

    /**
     * @param int $index
     * @param int $delta
     * @return void
     */
    private function add($index, $delta) {
        while ($index <= $this->size) {
            $this->tree[$index] += $delta;
            $index += $index & -$index;
        }
    }

    /**
     * @param int $index
     * @return int
     */
    private function prefix($index) {
        $total = 0;
        while ($index > 0) {
            $total += $this->tree[$index];
            $index -= $index & -$index;
        }
        return $total;
    }
}
