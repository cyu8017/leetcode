// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

#include <climits>
#include <cstdlib>
#include <string>
#include <vector>

class Solution {
    long long makePalindrome(long long half, int length) {
        std::string text = std::to_string(half);
        std::string pal = text;
        if (length % 2 == 0) {
            for (int i = static_cast<int>(text.size()) - 1; i >= 0; --i) {
                pal.push_back(text[i]);
            }
        } else {
            for (int i = static_cast<int>(text.size()) - 2; i >= 0; --i) {
                pal.push_back(text[i]);
            }
        }
        return std::stoll(pal);
    }

    long long pow10ll(int exp) {
        long long value = 1;
        for (int i = 0; i < exp; ++i) {
            value *= 10;
        }
        return value;
    }

public:
    std::string nearestPalindromic(std::string n) {
        int length = static_cast<int>(n.size());
        long long number = std::stoll(n);
        std::vector<long long> candidates;
        candidates.push_back(pow10ll(length - 1) - 1);
        candidates.push_back(pow10ll(length) + 1);

        long long prefix = std::stoll(n.substr(0, (length + 1) / 2));
        for (long long half = prefix - 1; half <= prefix + 1; ++half) {
            candidates.push_back(makePalindrome(half, length));
        }

        long long best = -1;
        long long bestDiff = LLONG_MAX;
        for (long long candidate : candidates) {
            if (candidate == number) {
                continue;
            }
            long long diff = std::llabs(candidate - number);
            if (diff < bestDiff || (diff == bestDiff && candidate < best)) {
                best = candidate;
                bestDiff = diff;
            }
        }
        return std::to_string(best);
    }
};
