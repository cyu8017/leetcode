// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

#include <deque>
#include <string>
#include <vector>

class Fenwick {
public:
    explicit Fenwick(int n) : bit_(n + 1, 0) {}

    void add(int i, int delta) {
        ++i;
        while (i < static_cast<int>(bit_.size())) {
            bit_[i] += delta;
            i += i & -i;
        }
    }

    int sum(int i) const {
        int out = 0;
        while (i > 0) {
            out += bit_[i];
            i -= i & -i;
        }
        return out;
    }

private:
    std::vector<int> bit_;
};

class Solution {
public:
    std::string minInteger(std::string num, int k) {
        std::vector<std::deque<int>> positions(10);
        for (int i = 0; i < static_cast<int>(num.size()); ++i) {
            positions[num[i] - '0'].push_back(i);
        }
        Fenwick fw(static_cast<int>(num.size()));
        std::string out;
        out.reserve(num.size());
        for (std::size_t step = 0; step < num.size(); ++step) {
            for (int digit = 0; digit < 10; ++digit) {
                if (positions[digit].empty()) {
                    continue;
                }
                const int index = positions[digit].front();
                const int cost = index - fw.sum(index);
                if (cost <= k) {
                    k -= cost;
                    positions[digit].pop_front();
                    fw.add(index, 1);
                    out.push_back(static_cast<char>('0' + digit));
                    break;
                }
            }
        }
        return out;
    }
};
