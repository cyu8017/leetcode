using System.Collections.Generic;

public class MinStack {
    private readonly Stack<int> stack = new();
    private readonly Stack<int> minimums = new();
    public void Push(int val) { stack.Push(val); minimums.Push(minimums.Count == 0 ? val : System.Math.Min(val, minimums.Peek())); }
    public void Pop() { stack.Pop(); minimums.Pop(); }
    public int Top() => stack.Peek();
    public int GetMin() => minimums.Peek();
}