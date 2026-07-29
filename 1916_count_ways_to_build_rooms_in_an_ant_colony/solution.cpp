// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

#include <functional>
#include <utility>
#include <vector>

class Solution {
    static constexpr int MOD = 1000000007;
    long long modPow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
public:
    int waysToBuildRooms(std::vector<int>& prevRoom) {
        int n = (int)prevRoom.size();
        std::vector<std::vector<int>> children(n);
        for (int room = 0; room < n; room++) {
            if (prevRoom[room] != -1) children[prevRoom[room]].push_back(room);
        }
        std::vector<long long> fact(n + 1, 1), invFact(n + 1, 1);
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i >= 1; i--) invFact[i - 1] = invFact[i] * i % MOD;
        auto comb = [&](int a, int b) {
            return fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
        };
        std::function<std::pair<int, long long>(int)> dfs = [&](int node) -> std::pair<int, long long> {
            int size = 0;
            long long ways = 1;
            for (int child : children[node]) {
                auto [cs, cw] = dfs(child);
                ways = ways * cw % MOD * comb(size + cs, cs) % MOD;
                size += cs;
            }
            return {size + 1, ways};
        };
        return (int)dfs(0).second;
    }
};
