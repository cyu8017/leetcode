// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

#include <vector>

class Solution {
    struct Line {
        long long slope = 0, intercept = 0;
        int count = 0;
        bool valid = false;
    };
    struct State {
        long long value = 0;
        int count = 0;
        bool valid = false;
    };

    static State better(State a, State b) {
        if (!a.valid) return b;
        if (!b.valid) return a;
        if (a.value != b.value) return a.value < b.value ? a : b;
        return a.count >= b.count ? a : b;
    }

    static State evaluate(const Line& line, long long x) {
        if (!line.valid) return {};
        return {line.slope * x + line.intercept, line.count, true};
    }

public:
    long long minPartitionScore(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        auto run = [&](long long penalty) -> State {
            std::vector<Line> tree(4 * (n + 1));
            auto insert = [&](auto&& self, int node, int left, int right, Line line) -> void {
                if (!tree[node].valid) {
                    tree[node] = line;
                    return;
                }
                int mid = (left + right) / 2;
                long long xLeft = prefix[left], xMid = prefix[mid];
                State leftBetter = better(evaluate(line, xLeft), evaluate(tree[node], xLeft));
                State midBetter = better(evaluate(line, xMid), evaluate(tree[node], xMid));
                bool lineWinsLeft = leftBetter.value == evaluate(line, xLeft).value && leftBetter.count == line.count;
                bool lineWinsMid = midBetter.value == evaluate(line, xMid).value && midBetter.count == line.count;
                if (lineWinsMid) std::swap(tree[node], line);
                if (left == right) return;
                if (lineWinsLeft != lineWinsMid) self(self, node * 2, left, mid, line);
                else self(self, node * 2 + 1, mid + 1, right, line);
            };
            auto query = [&](auto&& self, int node, int left, int right, int index) -> State {
                State result = evaluate(tree[node], prefix[index]);
                if (left == right) return result;
                int mid = (left + right) / 2;
                if (index <= mid) return better(result, self(self, node * 2, left, mid, index));
                return better(result, self(self, node * 2 + 1, mid + 1, right, index));
            };
            insert(insert, 1, 0, n, Line{0, 0, 0, true});
            State current;
            for (int i = 1; i <= n; i++) {
                State best = query(query, 1, 0, n, i);
                long long x = prefix[i];
                current = State{best.value + x * x + x + penalty, best.count + 1, true};
                insert(insert, 1, 0, n, Line{-2 * x, current.value + x * x - x, current.count, true});
            }
            return current;
        };

        long long bound = prefix[n] * prefix[n] + prefix[n] + 1;
        long long low = 0, high = bound;
        while (low < high) {
            long long mid = low + (high - low + 1) / 2;
            if (run(mid).count >= k) low = mid;
            else high = mid - 1;
        }
        State state = run(low);
        return (state.value - low * k) / 2;
    }
};
