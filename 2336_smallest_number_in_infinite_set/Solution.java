// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

class SmallestInfiniteSet {
    private int next = 1;
    private final Set<Integer> added = new HashSet<>();
    private final PriorityQueue<Integer> heap = new PriorityQueue<>();

    public int popSmallest() {
        if (!heap.isEmpty()) {
            int x = heap.poll();
            added.remove(x);
            return x;
        }
        return next++;
    }

    public void addBack(int num) {
        if (num < next && added.add(num)) {
            heap.offer(num);
        }
    }
}
