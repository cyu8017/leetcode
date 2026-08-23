// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

#include <map>
#include <set>
#include <utility>
#include <vector>

class Solution {
    struct SegTree {
        int n;
        std::vector<int> treeIntervalCounts, treeIntervalLengths;
        SegTree(int n_) : n(n_), treeIntervalCounts(4 * n_), treeIntervalLengths(4 * n_) {}
        void add(int i, int val) { addRec(0, 0, n - 1, i, val); }
        void addRec(int treeIndex, int lo, int hi, int i, int val) {
            if (lo == hi) {
                treeIntervalCounts[treeIndex] += val;
                treeIntervalLengths[treeIndex] = treeIntervalCounts[treeIndex] * i;
                return;
            }
            int mid = (lo + hi) / 2;
            if (i <= mid) addRec(2 * treeIndex + 1, lo, mid, i, val);
            else addRec(2 * treeIndex + 2, mid + 1, hi, i, val);
            treeIntervalCounts[treeIndex] = treeIntervalCounts[2 * treeIndex + 1] + treeIntervalCounts[2 * treeIndex + 2];
            treeIntervalLengths[treeIndex] = treeIntervalLengths[2 * treeIndex + 1] + treeIntervalLengths[2 * treeIndex + 2];
        }
        int queryIntervalCounts(int i) { return query(treeIntervalCounts, 0, 0, n - 1, i, n - 1); }
        int queryIntervalLengths(int i) { return query(treeIntervalLengths, 0, 0, n - 1, i, n - 1); }
        int query(std::vector<int>& tree, int treeIndex, int lo, int hi, int i, int j) {
            if (i <= lo && hi <= j) return tree[treeIndex];
            if (j < lo || hi < i) return 0;
            int mid = (lo + hi) / 2;
            return query(tree, treeIndex * 2 + 1, lo, mid, i, j) + query(tree, treeIndex * 2 + 2, mid + 1, hi, i, j);
        }
    };

public:
    std::vector<int> numberOfAlternatingGroups(std::vector<int>& colors, std::vector<std::vector<int>>& queries) {
        int n = (int)colors.size();
        std::vector<int> ans;
        std::vector<int> arr = colors;
        arr.insert(arr.end(), colors.begin(), colors.begin() + n - 1);
        SegTree tree(2 * n - 1);
        std::set<std::pair<int, int>> intervals;

        auto insert = [&](int l, int r) {
            intervals.insert({l, r});
            if (l < n) tree.add(r - l + 1, 1);
        };
        auto remove = [&](int l, int r) {
            intervals.erase({l, r});
            if (l < n) tree.add(r - l + 1, -1);
        };
        auto findInterval = [&](int target) -> std::pair<int, int> {
            int bestL = -1, bestR = -1;
            for (auto& k : intervals) {
                if (k.first <= target && target <= k.second) {
                    if (k.first > bestL) {
                        bestL = k.first;
                        bestR = k.second;
                    }
                }
            }
            return {bestL, bestR};
        };
        auto getNum = [&](int sz) {
            int numIntervals = tree.queryIntervalCounts(sz);
            int sumIntervals = tree.queryIntervalLengths(sz);
            int numAlternatingGroups = sumIntervals - numIntervals * sz + numIntervals;
            auto [l, r] = findInterval(n);
            if (l < 0 || l >= n || r - l + 1 < sz) return numAlternatingGroups;
            if (r >= n) {
                int nonDuplicateGroups = n - l;
                int numGroups = (r - l + 1) - sz + 1;
                int extra = numGroups - nonDuplicateGroups;
                if (extra > 0) numAlternatingGroups -= extra;
            }
            return numAlternatingGroups;
        };
        auto update = [&](int index, int color) {
            if (arr[index] == color) return;
            arr[index] = color;
            auto [start, end] = findInterval(index);
            remove(start, end);
            if (start < index && index < end) {
                insert(start, index - 1);
                insert(index, index);
                insert(index + 1, end);
                return;
            }
            if (start == index && index < end) insert(start + 1, end);
            if (start < index && index == end) insert(start, end - 1);
            int ns = index, ne = index;
            for (;;) {
                bool merged = false;
                for (auto k : intervals) {
                    if (k.second + 1 == ns && arr[k.second] != arr[ns]) {
                        remove(k.first, k.second);
                        ns = k.first;
                        merged = true;
                        break;
                    }
                }
                if (!merged) break;
            }
            for (;;) {
                bool merged = false;
                for (auto k : intervals) {
                    if (k.first == ne + 1 && arr[k.first] != arr[ne]) {
                        remove(k.first, k.second);
                        ne = k.second;
                        merged = true;
                        break;
                    }
                }
                if (!merged) break;
            }
            insert(ns, ne);
        };

        int start = 0;
        for (int i = 1; i < 2 * n - 1; i++) {
            if (arr[i] == arr[i - 1]) {
                insert(start, i - 1);
                start = i;
            }
        }
        insert(start, 2 * n - 2);

        for (auto& query : queries) {
            if (query[0] == 1) ans.push_back(getNum(query[1]));
            else {
                int index = query[1], color = query[2];
                if (arr[index] != color) {
                    update(index, color);
                    if (index < n - 1) update(index + n, color);
                }
            }
        }
        return ans;
    }
};
