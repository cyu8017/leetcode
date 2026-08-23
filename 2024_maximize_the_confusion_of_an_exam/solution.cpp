// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        auto maxWith = [&](char ch) {
            int left = 0, bad = 0, best = 0;
            for (int right = 0; right < (int)answerKey.size(); right++) {
                if (answerKey[right] != ch) bad++;
                while (bad > k) {
                    if (answerKey[left] != ch) bad--;
                    left++;
                }
                best = max(best, right - left + 1);
            }
            return best;
        };
        return max(maxWith('T'), maxWith('F'));
    }
};
