// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

#include <unordered_set>

class Solution {
public:
    int countTriples(int n) {
        std::unordered_set<int> squares;
        for (int i = 1; i <= n; i++) squares.insert(i * i);
        int ans = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                if (squares.count(a * a + b * b)) ans++;
            }
        }
        return ans;
    }
};
