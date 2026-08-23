// LeetCode 3753 - Total Waviness of Numbers in Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

#include <algorithm>
#include <functional>
#include <map>
#include <tuple>
#include <vector>

class Solution {
    struct Result {
        long long count = 0, sum = 0;
    };

    long long wavinessUpTo(long long limit) {
        if (limit < 0) return 0;
        std::vector<int> digits;
        if (limit == 0) digits.push_back(0);
        else {
            for (long long value = limit; value > 0; value /= 10) digits.push_back((int)(value % 10));
            std::reverse(digits.begin(), digits.end());
        }
        using Key = std::tuple<int, int, int, bool>;
        std::map<Key, Result> memo;
        std::function<Result(int, int, int, bool, bool)> dfs =
            [&](int position, int secondLast, int last, bool started, bool tight) -> Result {
            if (position == (int)digits.size()) return {1, 0};
            Key key{position, secondLast, last, started};
            if (!tight) {
                auto it = memo.find(key);
                if (it != memo.end()) return it->second;
            }
            int upper = tight ? digits[position] : 9;
            Result result;
            for (int digit = 0; digit <= upper; digit++) {
                bool nextTight = tight && digit == upper;
                int nextSecondLast = secondLast, nextLast = last;
                bool nextStarted = started || digit != 0;
                long long add = 0;
                if (!nextStarted) {
                    nextSecondLast = nextLast = 10;
                } else if (!started) {
                    nextSecondLast = 10;
                    nextLast = digit;
                } else {
                    if (secondLast != 10 &&
                        ((last > secondLast && last > digit) || (last < secondLast && last < digit))) {
                        add = 1;
                    }
                    nextSecondLast = last;
                    nextLast = digit;
                }
                Result child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight);
                result.count += child.count;
                result.sum += child.sum + add * child.count;
            }
            if (!tight) memo[key] = result;
            return result;
        };
        return dfs(0, 10, 10, false, true).sum;
    }

public:
    long long totalWaviness(long long a, long long b) {
        return wavinessUpTo(b) - wavinessUpTo(a - 1);
    }
};
