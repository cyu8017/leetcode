// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int sortArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        auto solveOne = [&](bool startZero) {
            std::vector<int> arr = nums;
            std::unordered_map<int, int> pos;
            for (int i = 0; i < n; i++) pos[arr[i]] = i;
            int ops = 0;
            while (true) {
                int empty = pos[0];
                int should = startZero ? empty : (empty == n - 1 ? 0 : empty + 1);
                if (arr[empty] == should) {
                    int found = -1;
                    for (int i = 0; i < n; i++) {
                        int want = startZero ? i : (i == n - 1 ? 0 : i + 1);
                        if (arr[i] != want) {
                            found = i;
                            break;
                        }
                    }
                    if (found == -1) return ops;
                    int v = arr[found];
                    std::swap(arr[empty], arr[found]);
                    pos[0] = found;
                    pos[v] = empty;
                    ops++;
                    continue;
                }
                int j = pos[should];
                int v = arr[j];
                std::swap(arr[empty], arr[j]);
                pos[0] = j;
                pos[v] = empty;
                ops++;
            }
        };
        return std::min(solveOne(true), solveOne(false));
    }
};
