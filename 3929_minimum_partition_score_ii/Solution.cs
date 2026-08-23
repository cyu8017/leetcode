// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

public class Solution {
    private struct Line {
        public long Slope, Intercept;
        public int Count;
        public bool Valid;
        public Line(long slope, long intercept, int count, bool valid) {
            Slope = slope; Intercept = intercept; Count = count; Valid = valid;
        }
    }
    private struct State {
        public long Value;
        public int Count;
        public bool Valid;
        public State(long value, int count, bool valid) {
            Value = value; Count = count; Valid = valid;
        }
    }

    private static State Better(State a, State b) {
        if (!a.Valid) return b;
        if (!b.Valid) return a;
        if (a.Value != b.Value) return a.Value < b.Value ? a : b;
        return a.Count >= b.Count ? a : b;
    }

    private static State Evaluate(Line line, long x) {
        if (!line.Valid) return default;
        return new State(line.Slope * x + line.Intercept, line.Count, true);
    }

    public long MinPartitionScore(int[] nums, int k) {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        State Run(long penalty) {
            Line[] tree = new Line[4 * (n + 1)];
            void Insert(int node, int left, int right, Line line) {
                if (!tree[node].Valid) {
                    tree[node] = line;
                    return;
                }
                int mid = (left + right) / 2;
                long xLeft = prefix[left], xMid = prefix[mid];
                State leftBetter = Better(Evaluate(line, xLeft), Evaluate(tree[node], xLeft));
                State midBetter = Better(Evaluate(line, xMid), Evaluate(tree[node], xMid));
                bool lineWinsLeft = leftBetter.Value == Evaluate(line, xLeft).Value && leftBetter.Count == line.Count;
                bool lineWinsMid = midBetter.Value == Evaluate(line, xMid).Value && midBetter.Count == line.Count;
                if (lineWinsMid) {
                    var tmp = tree[node];
                    tree[node] = line;
                    line = tmp;
                }
                if (left == right) return;
                if (lineWinsLeft != lineWinsMid) Insert(node * 2, left, mid, line);
                else Insert(node * 2 + 1, mid + 1, right, line);
            }
            State Query(int node, int left, int right, int index) {
                State result = Evaluate(tree[node], prefix[index]);
                if (left == right) return result;
                int mid = (left + right) / 2;
                if (index <= mid) return Better(result, Query(node * 2, left, mid, index));
                return Better(result, Query(node * 2 + 1, mid + 1, right, index));
            }
            Insert(1, 0, n, new Line(0, 0, 0, true));
            State current = default;
            for (int i = 1; i <= n; i++) {
                State best = Query(1, 0, n, i);
                long x = prefix[i];
                current = new State(best.Value + x * x + x + penalty, best.Count + 1, true);
                Insert(1, 0, n, new Line(-2 * x, current.Value + x * x - x, current.Count, true));
            }
            return current;
        }

        long bound = prefix[n] * prefix[n] + prefix[n] + 1;
        long low = 0, high = bound;
        while (low < high) {
            long mid = low + (high - low + 1) / 2;
            if (Run(mid).Count >= k) low = mid;
            else high = mid - 1;
        }
        State state = Run(low);
        return (state.Value - low * k) / 2;
    }
}
