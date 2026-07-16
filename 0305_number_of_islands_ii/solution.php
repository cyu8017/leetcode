// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

class Solution {
    /** @var array<int, int> */
    private $parent = [];
    /** @var array<int, int> */
    private $rank = [];

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $positions
     * @return Integer[]
     */
    function numIslands2($m, $n, $positions) {
        $this->parent = [];
        $this->rank = [];
        $directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $result = [];
        $islands = 0;

        foreach ($positions as $position) {
            $row = $position[0];
            $col = $position[1];
            $index = $row * $n + $col;
            if (isset($this->parent[$index])) {
                $result[] = $islands;
                continue;
            }

            $this->parent[$index] = $index;
            $this->rank[$index] = 0;
            $islands++;

            foreach ($directions as $direction) {
                $nr = $row + $direction[0];
                $nc = $col + $direction[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) {
                    continue;
                }
                $neighbor = $nr * $n + $nc;
                if (!isset($this->parent[$neighbor])) {
                    continue;
                }
                if ($this->union($index, $neighbor)) {
                    $islands--;
                }
            }
            $result[] = $islands;
        }
        return $result;
    }

    /**
     * @param int $index
     * @return int
     */
    private function find($index) {
        if ($this->parent[$index] !== $index) {
            $this->parent[$index] = $this->find($this->parent[$index]);
        }
        return $this->parent[$index];
    }

    /**
     * @param int $left
     * @param int $right
     * @return bool
     */
    private function union($left, $right) {
        $rootLeft = $this->find($left);
        $rootRight = $this->find($right);
        if ($rootLeft === $rootRight) {
            return false;
        }
        if ($this->rank[$rootLeft] < $this->rank[$rootRight]) {
            $tmp = $rootLeft;
            $rootLeft = $rootRight;
            $rootRight = $tmp;
        }
        $this->parent[$rootRight] = $rootLeft;
        if ($this->rank[$rootLeft] === $this->rank[$rootRight]) {
            $this->rank[$rootLeft]++;
        }
        return true;
    }
}
