// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long minDamage(int power, std::vector<int>& damage, std::vector<int>& health) {
        int n = (int)damage.size();
        struct Enemy { int dmg, hits; };
        std::vector<Enemy> arr(n);
        int totalDmg = 0;
        for (int i = 0; i < n; i++) {
            int hits = (health[i] + power - 1) / power;
            arr[i] = {damage[i], hits};
            totalDmg += damage[i];
        }
        std::sort(arr.begin(), arr.end(), [](const Enemy& a, const Enemy& b) {
            return (int64_t)a.hits * b.dmg < (int64_t)b.hits * a.dmg;
        });
        int64_t ans = 0, cur = totalDmg;
        for (auto& e : arr) {
            ans += cur * e.hits;
            cur -= e.dmg;
        }
        return ans;
    }
};
