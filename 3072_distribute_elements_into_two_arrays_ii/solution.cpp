// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

#include <algorithm>
#include <vector>

class Solution {
    struct BIT {
        int n;
        std::vector<int> c;
        explicit BIT(int n_) : n(n_), c(n_ + 1, 0) {}
        void update(int x, int delta) { for (; x <= n; x += x & -x) c[x] += delta; }
        int query(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    };
public:
    std::vector<int> resultArray(std::vector<int>& nums) {
        std::vector<int> st = nums;
        std::sort(st.begin(), st.end());
        int n = (int)st.size();
        BIT tree1(n + 1), tree2(n + 1);
        auto idx = [&](int x) {
            return (int)(std::lower_bound(st.begin(), st.end(), x) - st.begin()) + 1;
        };
        tree1.update(idx(nums[0]), 1);
        tree2.update(idx(nums[1]), 1);
        std::vector<int> arr1{nums[0]}, arr2{nums[1]};
        for (int i = 2; i < (int)nums.size(); i++) {
            int x = nums[i];
            int id = idx(x);
            int a = (int)arr1.size() - tree1.query(id);
            int b = (int)arr2.size() - tree2.query(id);
            if (a > b || (a == b && arr1.size() <= arr2.size())) {
                arr1.push_back(x);
                tree1.update(id, 1);
            } else {
                arr2.push_back(x);
                tree2.update(id, 1);
            }
        }
        arr1.insert(arr1.end(), arr2.begin(), arr2.end());
        return arr1;
    }
};
