// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

#include <vector>
#include <array>

class ATM {
    std::array<long long, 5> cnt{};
    std::array<int, 5> vals{{20, 50, 100, 200, 500}};
public:
    ATM() {}

    void deposit(std::vector<int> banknotesCount) {
        for (int i = 0; i < 5; ++i) cnt[i] += banknotesCount[i];
    }

    std::vector<int> withdraw(int amount) {
        std::vector<int> take(5);
        long long remain = amount;
        auto tmp = cnt;
        for (int i = 4; i >= 0; --i) {
            long long need = remain / vals[i];
            if (need > tmp[i]) need = tmp[i];
            take[i] = (int)need;
            remain -= need * vals[i];
        }
        if (remain != 0) return {-1};
        for (int i = 0; i < 5; ++i) cnt[i] -= take[i];
        return take;
    }
};
