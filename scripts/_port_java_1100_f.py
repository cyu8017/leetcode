#!/usr/bin/env python3
"""Port Java batch F: 1186-1201."""
from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
S: dict[str, str] = {}

S["1186_maximum_subarray_sum_with_one_deletion"] = r"""// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution {
    public int maximumSum(int[] arr) {
        int keep = arr[0], delete = arr[0], ans = arr[0];
        for (int i = 1; i < arr.length; i++) {
            int x = arr[i];
            delete = Math.max(keep, delete + x);
            keep = Math.max(keep + x, x);
            ans = Math.max(ans, Math.max(keep, delete));
        }
        return ans;
    }
}
"""

S["1187_make_array_strictly_increasing"] = r"""// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

import java.util.*;

class Solution {
    public int makeArrayIncreasing(int[] arr1, int[] arr2) {
        TreeSet<Integer> set = new TreeSet<>();
        for (int x : arr2) set.add(x);
        Integer[] sorted = set.toArray(new Integer[0]);
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(-1, 0);
        for (int num : arr1) {
            Map<Integer, Integer> next = new HashMap<>();
            for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                int prev = e.getKey(), ops = e.getValue();
                if (num > prev) next.merge(num, ops, Math::min);
                int idx = upperBound(sorted, prev);
                if (idx < sorted.length) {
                    int chosen = sorted[idx];
                    next.merge(chosen, ops + 1, Math::min);
                }
            }
            dp = next;
            if (dp.isEmpty()) return -1;
        }
        int ans = Integer.MAX_VALUE;
        for (int v : dp.values()) ans = Math.min(ans, v);
        return ans;
    }
    private int upperBound(Integer[] a, int target) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= target) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
"""

S["1188_design_bounded_blocking_queue"] = r"""// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

import java.util.*;
import java.util.concurrent.*;

class BoundedBlockingQueue {
    private final int capacity;
    private final Deque<Integer> queue = new ArrayDeque<>();
    private final Semaphore notFull;
    private final Semaphore notEmpty = new Semaphore(0);
    private final Object lock = new Object();

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        this.notFull = new Semaphore(capacity);
    }

    public void enqueue(int element) throws InterruptedException {
        notFull.acquire();
        synchronized (lock) { queue.addLast(element); }
        notEmpty.release();
    }

    public int dequeue() throws InterruptedException {
        notEmpty.acquire();
        int value;
        synchronized (lock) { value = queue.removeFirst(); }
        notFull.release();
        return value;
    }

    public int size() {
        synchronized (lock) { return queue.size(); }
    }
}
"""

S["1189_maximum_number_of_balloons"] = r"""// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] count = new int[26];
        for (char c : text.toCharArray()) count[c - 'a']++;
        return Math.min(Math.min(count[1], count[0]),
            Math.min(Math.min(count[11] / 2, count[14] / 2), count[13]));
    }
}
"""

S["1190_reverse_substrings_between_each_pair_of_parentheses"] = r"""// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

import java.util.*;

class Solution {
    public String reverseParentheses(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == ')') {
                List<Character> chunk = new ArrayList<>();
                while (!stack.isEmpty() && stack.peek() != '(') chunk.add(stack.pop());
                stack.pop();
                for (char c : chunk) stack.push(c);
            } else stack.push(ch);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) sb.append(stack.removeLast());
        return sb.toString();
    }
}
"""

S["1191_k_concatenation_maximum_sum"] = r"""// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution {
    public int kConcatenationMaxSum(int[] arr, int k) {
        final int MOD = 1_000_000_007;
        long one = kadane(arr);
        if (k == 1) return (int) (one % MOD);
        int[] twice = new int[arr.length * 2];
        System.arraycopy(arr, 0, twice, 0, arr.length);
        System.arraycopy(arr, 0, twice, arr.length, arr.length);
        long two = kadane(twice);
        long total = 0;
        for (int x : arr) total += x;
        long ans;
        if (total > 0) ans = Math.max(one, two + total * (k - 2));
        else ans = Math.max(one, two);
        return (int) (ans % MOD);
    }
    private long kadane(int[] nums) {
        long best = 0, cur = 0;
        for (int x : nums) {
            cur = Math.max(0, cur + x);
            best = Math.max(best, cur);
        }
        return best;
    }
}
"""

S["1192_critical_connections_in_a_network"] = r"""// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

import java.util.*;

class Solution {
    private int time = 0;
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (List<Integer> e : connections) {
            graph[e.get(0)].add(e.get(1));
            graph[e.get(1)].add(e.get(0));
        }
        int[] disc = new int[n], low = new int[n];
        Arrays.fill(disc, -1);
        List<List<Integer>> bridges = new ArrayList<>();
        dfs(0, -1, graph, disc, low, bridges);
        for (List<Integer> b : bridges) {
            if (b.get(0) > b.get(1)) Collections.swap(b, 0, 1);
        }
        return bridges;
    }
    private void dfs(int node, int parent, List<Integer>[] graph, int[] disc, int[] low, List<List<Integer>> bridges) {
        disc[node] = low[node] = time++;
        for (int nxt : graph[node]) {
            if (nxt == parent) continue;
            if (disc[nxt] == -1) {
                dfs(nxt, node, graph, disc, low, bridges);
                low[node] = Math.min(low[node], low[nxt]);
                if (low[nxt] > disc[node]) bridges.add(new ArrayList<>(Arrays.asList(node, nxt)));
            } else low[node] = Math.min(low[node], disc[nxt]);
        }
    }
}
"""

S["1195_fizz_buzz_multithreaded"] = r"""// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

import java.util.function.IntConsumer;

class FizzBuzz {
    private final int n;
    private int current = 1;
    private final Object lock = new Object();

    public FizzBuzz(int n) { this.n = n; }

    public void fizz(Runnable printFizz) throws InterruptedException {
        run(x -> x % 3 == 0 && x % 5 != 0, printFizz);
    }
    public void buzz(Runnable printBuzz) throws InterruptedException {
        run(x -> x % 5 == 0 && x % 3 != 0, printBuzz);
    }
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        run(x -> x % 15 == 0, printFizzBuzz);
    }
    public void number(IntConsumer printNumber) throws InterruptedException {
        synchronized (lock) {
            while (current <= n) {
                if (current % 3 != 0 && current % 5 != 0) {
                    printNumber.accept(current);
                    current++;
                    lock.notifyAll();
                } else lock.wait();
            }
        }
    }
    private void run(java.util.function.IntPredicate pred, Runnable action) throws InterruptedException {
        synchronized (lock) {
            while (current <= n) {
                if (pred.test(current)) {
                    action.run();
                    current++;
                    lock.notifyAll();
                } else lock.wait();
            }
        }
    }
}
"""

S["1196_how_many_apples_can_you_put_into_the_basket"] = r"""// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

import java.util.*;

class Solution {
    public int maxNumberOfApples(int[] weight) {
        Arrays.sort(weight);
        int total = 0;
        for (int i = 0; i < weight.length; i++) {
            total += weight[i];
            if (total > 5000) return i;
        }
        return weight.length;
    }
}
"""

S["1197_minimum_knight_moves"] = r"""// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

import java.util.*;

class Solution {
    private final Map<String, Integer> memo = new HashMap<>();
    public int minKnightMoves(int x, int y) {
        return dfs(Math.abs(x), Math.abs(y));
    }
    private int dfs(int a, int b) {
        if (a + b == 0) return 0;
        if (a + b == 2) return 2;
        String key = a + "," + b;
        if (memo.containsKey(key)) return memo.get(key);
        int ans = Math.min(dfs(Math.abs(a - 1), Math.abs(b - 2)), dfs(Math.abs(a - 2), Math.abs(b - 1))) + 1;
        memo.put(key, ans);
        return ans;
    }
}
"""

def write_if_stub(name: str, content: str) -> None:
    path = ROOT / name / "solution.java"
    if not path.exists():
        print("missing", name); return
    cur = path.read_text(encoding="utf-8")
    if "void solve()" in cur or len(cur.strip()) < 120:
        path.write_text(content, encoding="utf-8", newline="\n")
        print("wrote", name)
    else:
        print("skip", name)

def main():
    for name, content in S.items():
        write_if_stub(name, content)
    print("done", len(S))

if __name__ == "__main__":
    main()
