// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int oddEvenJumps(std::vector<int>& arr) {
        int n = (int)arr.size();
        std::vector<int> nextHigher(n, 0), nextLower(n, 0), order(n);
        std::iota(order.begin(), order.end(), 0);
        std::sort(order.begin(), order.end(), [&](int i, int j) {
            return arr[i] == arr[j] ? i < j : arr[i] < arr[j];
        });
        std::vector<int> stack;
        for (int i : order) {
            while (!stack.empty() && stack.back() < i) {
                nextHigher[stack.back()] = i;
                stack.pop_back();
            }
            stack.push_back(i);
        }
        stack.clear();
        std::sort(order.begin(), order.end(), [&](int i, int j) {
            return arr[i] == arr[j] ? i < j : arr[i] > arr[j];
        });
        for (int i : order) {
            while (!stack.empty() && stack.back() < i) {
                nextLower[stack.back()] = i;
                stack.pop_back();
            }
            stack.push_back(i);
        }
        std::vector<char> odd(n, 0), even(n, 0);
        odd[n - 1] = even[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nextHigher[i]) odd[i] = even[nextHigher[i]];
            if (nextLower[i]) even[i] = odd[nextLower[i]];
        }
        return (int)std::accumulate(odd.begin(), odd.end(), 0);
    }
};
