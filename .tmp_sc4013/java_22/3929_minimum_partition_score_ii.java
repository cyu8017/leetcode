// CONFIG class=Solution method=minPartitionScore types=None
// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

class Solution {
    static class Line {
        long slope, intercept;
        int count;
        boolean valid;
        Line() {}
        Line(long slope, long intercept, int count, boolean valid) {
            this.slope = slope; this.intercept = intercept; this.count = count; this.valid = valid;
        }
    }
    static class State {
        long value;
        int count;
        boolean valid;
        State() {}
        State(long value, int count, boolean valid) {
            this.value = value; this.count = count; this.valid = valid;
        }
    }

    private static State better(State a, State b) {
        if (!a.valid) return b;
        if (!b.valid) return a;
        if (a.value != b.value) return a.value < b.value ? a : b;
        return a.count >= b.count ? a : b;
    }

    private static State evaluate(Line line, long x) {
        if (!line.valid) return new State();
        return new State(line.slope * x + line.intercept, line.count, true);
    }

    private long[] prefix;
    private int n;

    private void insert(Line[] tree, int node, int left, int right, Line line) {
        if (!tree[node].valid) {
            tree[node] = line;
            return;
        }
        int mid = (left + right) / 2;
        long xLeft = prefix[left], xMid = prefix[mid];
        State leftBetter = better(evaluate(line, xLeft), evaluate(tree[node], xLeft));
        State midBetter = better(evaluate(line, xMid), evaluate(tree[node], xMid));
        boolean lineWinsLeft = leftBetter.value == evaluate(line, xLeft).value && leftBetter.count == line.count;
        boolean lineWinsMid = midBetter.value == evaluate(line, xMid).value && midBetter.count == line.count;
        if (lineWinsMid) {
            Line tmp = tree[node];
            tree[node] = line;
            line = tmp;
        }
        if (left == right) return;
        if (lineWinsLeft != lineWinsMid) insert(tree, node * 2, left, mid, line);
        else insert(tree, node * 2 + 1, mid + 1, right, line);
    }

    private State query(Line[] tree, int node, int left, int right, int index) {
        State result = evaluate(tree[node], prefix[index]);
        if (left == right) return result;
        int mid = (left + right) / 2;
        if (index <= mid) return better(result, query(tree, node * 2, left, mid, index));
        return better(result, query(tree, node * 2 + 1, mid + 1, right, index));
    }

    private State run(long penalty) {
        Line[] tree = new Line[4 * (n + 1)];
        for (int i = 0; i < tree.length; i++) tree[i] = new Line();
        insert(tree, 1, 0, n, new Line(0, 0, 0, true));
        State current = new State();
        for (int i = 1; i <= n; i++) {
            State best = query(tree, 1, 0, n, i);
            long x = prefix[i];
            current = new State(best.value + x * x + x + penalty, best.count + 1, true);
            insert(tree, 1, 0, n, new Line(-2 * x, current.value + x * x - x, current.count, true));
        }
        return current;
    }

    public long minPartitionScore(int[] nums, int k) {
        n = nums.length;
        prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        long bound = prefix[n] * prefix[n] + prefix[n] + 1;
        long low = 0, high = bound;
        while (low < high) {
            long mid = low + (high - low + 1) / 2;
            if (run(mid).count >= k) low = mid;
            else high = mid - 1;
        }
        State state = run(low);
        return (state.value - low * k) / 2;
    }
}
