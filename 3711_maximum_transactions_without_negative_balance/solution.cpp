// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

#include <set>
#include <vector>

class Solution {
public:
    int maxTransactions(std::vector<int>& transactions) {
        std::multiset<int> tm;
        int ans = (int)transactions.size();
        long long s = 0;
        for (int x : transactions) {
            s += x;
            tm.insert(x);
            while (s < 0) {
                int y = *tm.begin();
                s -= y;
                ans--;
                tm.erase(tm.begin());
            }
        }
        return ans;
    }
};
