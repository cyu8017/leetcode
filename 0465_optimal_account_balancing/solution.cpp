// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
    int dfs(int index, std::vector<int>& debts) {
        while (index < static_cast<int>(debts.size()) && debts[index] == 0) {
            ++index;
        }
        if (index == static_cast<int>(debts.size())) {
            return 0;
        }
        int best = static_cast<int>(debts.size());
        for (int nextIndex = index + 1; nextIndex < static_cast<int>(debts.size()); ++nextIndex) {
            if (static_cast<long long>(debts[index]) * debts[nextIndex] < 0) {
                debts[nextIndex] += debts[index];
                best = std::min(best, 1 + dfs(index + 1, debts));
                debts[nextIndex] -= debts[index];
            }
        }
        return best;
    }

public:
    int minTransfers(std::vector<std::vector<int>>& transactions) {
        std::unordered_map<int, int> balances;
        for (const auto& transaction : transactions) {
            int source = transaction[0];
            int target = transaction[1];
            int amount = transaction[2];
            balances[source] -= amount;
            balances[target] += amount;
        }

        std::vector<int> debts;
        for (const auto& entry : balances) {
            if (entry.second != 0) {
                debts.push_back(entry.second);
            }
        }
        return dfs(0, debts);
    }
};
