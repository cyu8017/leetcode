// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
#include <climits>
#include <vector>

class Solution {
public:
    int binarySearchableNumbers(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ok(n, 1);
        int mx = INT_MIN, mi = INT_MAX;
        for (int i = 0; i < n; i++) {
            if (nums[i] < mx) ok[i] = 0;
            else mx = nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] > mi) ok[i] = 0;
            else mi = nums[i];
        }
        int ans = 0;
        for (int v : ok) ans += v;
        return ans;
    }
};
