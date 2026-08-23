// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

#include <queue>
#include <string>
#include <utility>
#include <vector>

class Solution {
    std::vector<bool> sieve(int n) {
        std::vector<bool> isP(n, false);
        for (int i = 2; i < n; i++) isP[i] = true;
        for (int i = 2; i * i < n; i++) {
            if (isP[i]) {
                for (int j = i * i; j < n; j += i) isP[j] = false;
            }
        }
        return isP;
    }

public:
    int minOperations(int n, int m) {
        auto isPrime = sieve(100000);
        if (isPrime[n]) return -1;
        std::vector<int> dist(100000, -1);
        using Item = std::pair<int, int>;
        std::priority_queue<Item, std::vector<Item>, std::greater<Item>> pq;
        pq.push({n, n});
        dist[n] = n;
        while (!pq.empty()) {
            auto [cost, val] = pq.top();
            pq.pop();
            if (cost != dist[val]) continue;
            if (val == m) return cost;
            std::string s = std::to_string(val);
            for (int i = 0; i < (int)s.size(); i++) {
                char orig = s[i];
                for (int d : {-1, 1}) {
                    int nd = (orig - '0') + d;
                    if (nd < 0 || nd > 9) continue;
                    if (i == 0 && nd == 0 && (int)s.size() > 1) continue;
                    s[i] = char('0' + nd);
                    int nv = std::stoi(s);
                    s[i] = orig;
                    if (isPrime[nv]) continue;
                    int nc = cost + nv;
                    if (dist[nv] == -1 || nc < dist[nv]) {
                        dist[nv] = nc;
                        pq.push({nc, nv});
                    }
                }
            }
        }
        return -1;
    }
};
