// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

class MyStack {
    private $queue = [];

    function push($x) {
        $this->queue[] = $x;
        for ($i = 0; $i < count($this->queue) - 1; $i++) {
            $this->queue[] = array_shift($this->queue);
        }
    }

    function pop() {
        return array_shift($this->queue);
    }

    function top() {
        return $this->queue[0];
    }

    function empty() {
        return count($this->queue) === 0;
    }
}
