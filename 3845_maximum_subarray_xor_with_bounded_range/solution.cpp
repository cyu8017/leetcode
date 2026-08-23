// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

#include <vector>

class Solution {
    struct Node {
        int next[2]{0, 0};
        int count = 0;
    };

    std::vector<Node> nodes;

    void add(int x, int delta) {
        int u = 0;
        nodes[u].count += delta;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            if (nodes[u].next[bit] == 0) {
                nodes[u].next[bit] = (int)nodes.size();
                nodes.push_back(Node{});
            }
            u = nodes[u].next[bit];
            nodes[u].count += delta;
        }
    }

    int query(int x) {
        int u = 0, res = 0;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            int want = bit ^ 1;
            int v = nodes[u].next[want];
            if (v != 0 && nodes[v].count > 0) {
                res |= 1 << b;
                u = v;
            } else {
                u = nodes[u].next[bit];
            }
        }
        return res;
    }

public:
    int maxSubarrayXor(std::vector<int>& nums, int k) {
        nodes.assign(1, Node{});
        int n = (int)nums.size();
        std::vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] ^ nums[i];
        std::vector<int> maxQ, minQ;
        int left = 0, trieLeft = 0, ans = 0;
        for (int r = 0; r < n; r++) {
            int x = nums[r];
            while (!maxQ.empty() && nums[maxQ.back()] <= x) maxQ.pop_back();
            maxQ.push_back(r);
            while (!minQ.empty() && nums[minQ.back()] >= x) minQ.pop_back();
            minQ.push_back(r);
            while (nums[maxQ[0]] - nums[minQ[0]] > k) {
                if (maxQ[0] == left) maxQ.erase(maxQ.begin());
                if (minQ[0] == left) minQ.erase(minQ.begin());
                left++;
            }
            add(pref[r], 1);
            while (trieLeft < left) {
                add(pref[trieLeft], -1);
                trieLeft++;
            }
            int cur = query(pref[r + 1]);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
