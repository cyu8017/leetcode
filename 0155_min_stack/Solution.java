import java.util.ArrayDeque;
import java.util.Deque;

class MinStack {
    private final Deque<Integer> stack = new ArrayDeque<>();
    private final Deque<Integer> minimums = new ArrayDeque<>();
    public void push(int val) { stack.push(val); minimums.push(minimums.isEmpty() ? val : Math.min(val, minimums.peek())); }
    public void pop() { stack.pop(); minimums.pop(); }
    public int top() { return stack.peek(); }
    public int getMin() { return minimums.peek(); }
}