// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

import java.util.*;

class DinnerPlates {
    private final int capacity;
    private final List<Deque<Integer>> stacks = new ArrayList<>();
    private final PriorityQueue<Integer> available = new PriorityQueue<>();

    public DinnerPlates(int capacity) {
        this.capacity = capacity;
    }

    public void push(int val) {
        while (!available.isEmpty() && (available.peek() >= stacks.size() || stacks.get(available.peek()).size() == capacity)) {
            available.poll();
        }
        if (available.isEmpty()) {
            stacks.add(new ArrayDeque<>());
            available.offer(stacks.size() - 1);
        }
        int idx = available.peek();
        stacks.get(idx).push(val);
        if (stacks.get(idx).size() == capacity) available.poll();
    }

    public int pop() {
        while (!stacks.isEmpty() && stacks.get(stacks.size() - 1).isEmpty()) stacks.remove(stacks.size() - 1);
        return stacks.isEmpty() ? -1 : popAtStack(stacks.size() - 1);
    }

    public int popAtStack(int index) {
        if (index < 0 || index >= stacks.size() || stacks.get(index).isEmpty()) return -1;
        if (stacks.get(index).size() == capacity) available.offer(index);
        return stacks.get(index).pop();
    }
}
