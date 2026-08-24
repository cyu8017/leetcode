
================================================================================
// FOLDER: 3502_minimum_cost_to_reach_every_position
// URL: https://leetcode.com/problems/minimum-cost-to-reach-every-position/
// CONFIG: {"class": "Solution", "method": "minCosts", "paramOrder": ["cost"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minCosts
// PY DEFS: ['minCosts']
// CPP FNS: ['minCosts', 'ans']
================================================================================
// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> minCosts(std::vector<int>& cost) {
        int n = (int)cost.size();
        std::vector<int> ans(n);
        int mi = cost[0];
        for (int i = 0; i < n; i++) {
            mi = std::min(mi, cost[i]);
            ans[i] = mi;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3503_longest_palindrome_after_substring_concatenation_i
// URL: https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/
// CONFIG: {"class": "Solution", "method": "longestPalindrome", "paramOrder": ["s", "t"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=longestPalindrome
// PY DEFS: ['longestPalindrome', 'expand', 'calc']
// CPP FNS: ['expand', 'calc', 'g', 'longestPalindrome']
================================================================================
// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
    void expand(const std::string& s, std::vector<int>& g, int l, int r) {
        while (l >= 0 && r < (int)s.size() && s[l] == s[r]) {
            g[l] = std::max(g[l], r - l + 1);
            l--; r++;
        }
    }
    std::vector<int> calc(const std::string& s) {
        int n = (int)s.size();
        std::vector<int> g(n);
        for (int i = 0; i < n; i++) {
            expand(s, g, i, i);
            expand(s, g, i, i + 1);
        }
        return g;
    }
public:
    int longestPalindrome(std::string s, std::string t) {
        int m = (int)s.size(), n = (int)t.size();
        std::reverse(t.begin(), t.end());
        auto g1 = calc(s), g2 = calc(t);
        int ans = 0;
        for (int v : g1) ans = std::max(ans, v);
        for (int v : g2) ans = std::max(ans, v);
        std::vector<std::vector<int>> f(m + 1, std::vector<int>(n + 1));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    f[i][j] = f[i - 1][j - 1] + 1;
                    int a = (i < m) ? g1[i] : 0;
                    int b = (j < n) ? g2[j] : 0;
                    ans = std::max(ans, f[i][j] * 2 + a);
                    ans = std::max(ans, f[i][j] * 2 + b);
                }
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3504_longest_palindrome_after_substring_concatenation_ii
// URL: https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/
// CONFIG: {"class": "Solution", "method": "longestPalindrome", "paramOrder": ["s", "t"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=longestPalindrome
// PY DEFS: ['expand', 'calc', 'longestPalindrome']
// CPP FNS: ['expand', 'calc', 'g', 'longestPalindrome']
================================================================================
// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
    void expand(const std::string& s, std::vector<int>& g, int l, int r) {
        while (l >= 0 && r < (int)s.size() && s[l] == s[r]) {
            g[l] = std::max(g[l], r - l + 1);
            l--; r++;
        }
    }
    std::vector<int> calc(const std::string& s) {
        int n = (int)s.size();
        std::vector<int> g(n);
        for (int i = 0; i < n; i++) {
            expand(s, g, i, i);
            expand(s, g, i, i + 1);
        }
        return g;
    }
public:
    int longestPalindrome(std::string s, std::string t) {
        int m = (int)s.size(), n = (int)t.size();
        std::reverse(t.begin(), t.end());
        auto g1 = calc(s), g2 = calc(t);
        int ans = 0;
        for (int v : g1) ans = std::max(ans, v);
        for (int v : g2) ans = std::max(ans, v);
        std::vector<std::vector<int>> f(m + 1, std::vector<int>(n + 1));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    f[i][j] = f[i - 1][j - 1] + 1;
                    int a = (i < m) ? g1[i] : 0;
                    int b = (j < n) ? g2[j] : 0;
                    ans = std::max(ans, f[i][j] * 2 + a);
                    ans = std::max(ans, f[i][j] * 2 + b);
                }
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3505_minimum_operations_to_make_elements_within_k_subarrays_equal
// URL: https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
// CONFIG: {"class": "Solution", "method": "minOperations", "paramOrder": ["nums", "x", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minOperations
// PY DEFS: ['minOperations']
// CPP FNS: ['minOperations', 'minOps', 'w']
================================================================================
// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long minOperations(std::vector<int>& nums, int x, int k) {
        int n = (int)nums.size();
        std::vector<long long> minOps(n - x + 1);
        for (int i = 0; i + x <= n; i++) {
            std::vector<int> w(nums.begin() + i, nums.begin() + i + x);
            std::sort(w.begin(), w.end());
            int med = w[(x - 1) / 2];
            long long ops = 0;
            for (int v : w) ops += std::abs(v - med);
            minOps[i] = ops;
        }
        const long long inf = 1LL << 62;
        std::vector<std::vector<long long>> dp(n + 1, std::vector<long long>(k + 1, inf));
        dp[n][0] = 0;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= k; j++) {
                dp[i][j] = dp[i + 1][j];
                if (j > 0 && i + x <= n && minOps[i] + dp[i + x][j - 1] < dp[i][j])
                    dp[i][j] = minOps[i] + dp[i + x][j - 1];
            }
        }
        return dp[0][k];
    }
};

================================================================================
// FOLDER: 3506_find_time_required_to_eliminate_bacterial_strains
// URL: https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["timeReq", "splitTime"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['minEliminationTime']
// CPP FNS: ['minEliminationTime']
================================================================================
// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

#include <vector>
#include <queue>

class Solution {
public:
    long long minEliminationTime(std::vector<int>& timeReq, int splitTime) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        for (int v : timeReq) pq.push(v);
        while ((int)pq.size() > 1) {
            pq.pop();
            int x = pq.top(); pq.pop();
            pq.push(x + splitTime);
        }
        return pq.top();
    }
};

----- PYTHON -----
# LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
# https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

from typing import List


class Solution:
    def minEliminationTime(self, timeReq: List[int], splitTime: int) -> int:
        pq = sorted(timeReq)
        while len(pq) > 1:
            pq.pop(0)
            x = pq.pop(0)
            v = x + splitTime
            lo, hi = 0, len(pq)
            while lo < hi:
                mid = (lo + hi) >> 1
                if pq[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            pq.insert(lo, v)
        return pq[0]

================================================================================
// FOLDER: 3507_minimum_pair_removal_to_sort_array_i
// URL: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
// CONFIG: {"class": "Solution", "method": "minimumPairRemoval", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minimumPairRemoval
// PY DEFS: ['isNonDecreasing', 'minimumPairRemoval']
// CPP FNS: ['isNonDecreasing', 'minimumPairRemoval']
================================================================================
// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

#include <vector>

class Solution {
    bool isNonDecreasing(const std::vector<int>& a) {
        for (int i = 1; i < (int)a.size(); i++) if (a[i] < a[i - 1]) return false;
        return true;
    }
public:
    int minimumPairRemoval(std::vector<int>& nums) {
        std::vector<int> arr = nums;
        int ans = 0;
        while (!isNonDecreasing(arr)) {
            int k = 0, s = arr[0] + arr[1];
            for (int i = 1; i + 1 < (int)arr.size(); i++) {
                int t = arr[i] + arr[i + 1];
                if (s > t) { s = t; k = i; }
            }
            arr[k] = s;
            arr.erase(arr.begin() + k + 1);
            ans++;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3508_implement_router
// URL: https://leetcode.com/problems/implement-router/
// CONFIG: {"class": "Router", "method": "__init__", "paramOrder": ["memoryLimit"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Router method=__init__
// PY DEFS: ['lowerBound', '__init__', 'f', 'addPacket', 'forwardPacket', 'getCount']
// CPP FNS: ['f', 'addPacket', 'forwardPacket', 'getCount']
================================================================================
// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <algorithm>

class Router {
    int lim;
    std::unordered_set<long long> vis;
    std::deque<std::array<int, 3>> q;
    std::unordered_map<int, int> idx;
    std::unordered_map<int, std::vector<int>> d;
    long long f(int a, int b, int c) {
        return ((long long)a << 46) | ((long long)b << 29) | (long long)c;
    }
public:
    Router(int memoryLimit) : lim(memoryLimit) {}

    bool addPacket(int source, int destination, int timestamp) {
        long long x = f(source, destination, timestamp);
        if (vis.count(x)) return false;
        vis.insert(x);
        if ((int)q.size() >= lim) forwardPacket();
        q.push_back({source, destination, timestamp});
        d[destination].push_back(timestamp);
        return true;
    }

    std::vector<int> forwardPacket() {
        if (q.empty()) return {};
        auto packet = q.front(); q.pop_front();
        int s = packet[0], dest = packet[1], t = packet[2];
        vis.erase(f(s, dest, t));
        idx[dest]++;
        return {s, dest, t};
    }

    int getCount(int destination, int startTime, int endTime) {
        auto& ls = d[destination];
        int k = idx[destination];
        auto it1 = std::lower_bound(ls.begin() + k, ls.end(), startTime);
        auto it2 = std::lower_bound(ls.begin() + k, ls.end(), endTime + 1);
        return (int)(it2 - it1);
    }
};

----- PYTHON -----
# LeetCode 3508 - Implement Router
# https://leetcode.com/problems/implement-router/

from typing import List


def lowerBound(a: List[int], frm: int, target: int) -> int:
    lo, hi = frm, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Router:
    def __init__(self, memoryLimit: int):
        self.lim = memoryLimit
        self.vis = set()
        self.q = []
        self.idx = {}
        self.d = {}

    def f(self, a: int, b: int, c: int) -> int:
        return (a << 46) | (b << 29) | c

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        x = self.f(source, destination, timestamp)
        if x in self.vis:
            return False
        self.vis.add(x)
        if len(self.q) >= self.lim:
            self.forwardPacket()
        self.q.append([source, destination, timestamp])
        if destination not in self.d:
            self.d[destination] = []
        self.d[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        packet = self.q.pop(0)
        s, dest, t = packet[0], packet[1], packet[2]
        self.vis.discard(self.f(s, dest, t))
        self.idx[dest] = self.idx.get(dest, 0) + 1
        return [s, dest, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ls = self.d.get(destination)
        if not ls:
            return 0
        k = self.idx.get(destination, 0)
        return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime)

================================================================================
// FOLDER: 3509_maximum_product_of_subsequences_with_an_alternating_sum_equal_to_k
// URL: https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/
// CONFIG: {"class": "Solution", "method": "maxProduct", "paramOrder": ["nums", "k", "limit"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxProduct
// PY DEFS: ['maxProduct', 'dp']
// CPP FNS: ['dp', 'maxProduct']
================================================================================
// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

#include <vector>
#include <map>
#include <array>
#include <algorithm>
#include <cstdlib>

class Solution {
    static const int MIN = -5000;
    std::map<std::array<int, 4>, int> memo;
    std::vector<int> nums;
    int limit;
    int dp(int i, int product, int state, int kk) {
        if (i == (int)nums.size()) {
            if (kk == 0 && state != 0 && product <= limit) return product;
            return MIN;
        }
        std::array<int, 4> key = {i, product, state, kk};
        if (memo.count(key)) return memo[key];
        int res = dp(i + 1, product, state, kk);
        if (state == 0) res = std::max(res, dp(i + 1, nums[i], 1, kk - nums[i]));
        if (state == 1) {
            int np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = std::max(res, dp(i + 1, np, 2, kk + nums[i]));
        }
        if (state == 2) {
            int np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = std::max(res, dp(i + 1, np, 1, kk - nums[i]));
        }
        return memo[key] = res;
    }
public:
    int maxProduct(std::vector<int>& nums_, int k, int limit_) {
        nums = nums_;
        limit = limit_;
        memo.clear();
        int sumAll = 0;
        for (int v : nums) sumAll += v;
        if (std::abs(k) > sumAll) return -1;
        int ans = dp(0, 1, 0, k);
        return ans == MIN ? -1 : ans;
    }
};

================================================================================
// FOLDER: 3510_minimum_pair_removal_to_sort_array_ii
// URL: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
// CONFIG: {"class": "Solution", "method": "minimumPairRemoval", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minimumPairRemoval
// PY DEFS: ['minimumPairRemoval', 'key', 'addSl', 'remSl', 'ceiling', 'floor']
// CPP FNS: ['minimumPairRemoval']
================================================================================
// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

#include <vector>
#include <set>

class Solution {
public:
    int minimumPairRemoval(std::vector<int>& nums) {
        int n = (int)nums.size();
        int inv = 0, ans = 0;
        std::set<std::pair<int, int>> sl;
        std::set<int> idx;
        for (int i = 0; i < n; i++) idx.insert(i);
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] > nums[i + 1]) inv++;
            sl.insert({nums[i] + nums[i + 1], i});
        }
        while (inv > 0) {
            ans++;
            auto p = *sl.begin();
            sl.erase(sl.begin());
            int s = p.first, i = p.second;
            auto jIt = idx.lower_bound(i + 1);
            int j = *jIt;
            if (nums[i] > nums[j]) inv--;
            auto hIt = idx.upper_bound(i - 1);
            if (hIt != idx.begin()) {
                --hIt;
                int h = *hIt;
                if (nums[h] > nums[i]) inv--;
                sl.erase({nums[h] + nums[i], h});
                if (nums[h] > s) inv++;
                sl.insert({nums[h] + s, h});
            }
            auto kIt = idx.lower_bound(j + 1);
            if (kIt != idx.end()) {
                int k = *kIt;
                if (nums[j] > nums[k]) inv--;
                sl.erase({nums[j] + nums[k], j});
                if (s > nums[k]) inv++;
                sl.insert({s + nums[k], i});
            }
            nums[i] = s;
            idx.erase(j);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3511_make_a_positive_array
// URL: https://leetcode.com/problems/make-a-positive-array/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['makeArrayPositive']
// CPP FNS: ['makeArrayPositive']
================================================================================
// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

#include <vector>
#include <algorithm>

class Solution {
public:
    int makeArrayPositive(std::vector<int>& nums) {
        int ans = 0, l = -1;
        long long preMx = 0, s = 0;
        for (int r = 0; r < (int)nums.size(); r++) {
            s += nums[r];
            if (r - l > 2 && s <= preMx) {
                ans++;
                l = r;
                preMx = 0;
                s = 0;
            } else if (r - l >= 2) {
                preMx = std::max(preMx, s - nums[r] - nums[r - 1]);
            }
        }
        return ans;
    }
};

----- PYTHON -----
# LeetCode 3511 - Make a Positive Array
# https://leetcode.com/problems/make-a-positive-array/

from typing import List


class Solution:
    def makeArrayPositive(self, nums: List[int]) -> int:
        ans = 0
        l = -1
        pre_mx = 0
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            if r - l > 2 and s <= pre_mx:
                ans += 1
                l = r
                pre_mx = 0
                s = 0
            elif r - l >= 2:
                pre_mx = max(pre_mx, s - nums[r] - nums[r - 1])
        return ans

================================================================================
// FOLDER: 3512_minimum_operations_to_make_array_sum_divisible_by_k
// URL: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
// CONFIG: {"class": "Solution", "method": "minOperations", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minOperations
// PY DEFS: ['minOperations']
// CPP FNS: ['minOperations']
================================================================================
// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        int ans = 0;
        for (int x : nums) ans = (ans + x) % k;
        return ans;
    }
};

================================================================================
// FOLDER: 3513_number_of_unique_xor_triplets_i
// URL: https://leetcode.com/problems/number-of-unique-xor-triplets-i/
// CONFIG: {"class": "Solution", "method": "uniqueXorTriplets", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=uniqueXorTriplets
// PY DEFS: ['uniqueXorTriplets']
// CPP FNS: ['uniqueXorTriplets']
================================================================================
// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

#include <vector>
#include <bit>

class Solution {
public:
    int uniqueXorTriplets(std::vector<int>& nums) {
        int n = (int)nums.size();
        if (n <= 2) return n;
        unsigned x = (unsigned)n;
        int len = 0;
        while (x) { len++; x >>= 1; }
        return 1 << len;
    }
};

================================================================================
// FOLDER: 3514_number_of_unique_xor_triplets_ii
// URL: https://leetcode.com/problems/number-of-unique-xor-triplets-ii/
// CONFIG: {"class": "Solution", "method": "uniqueXorTriplets", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=uniqueXorTriplets
// PY DEFS: ['uniqueXorTriplets']
// CPP FNS: ['uniqueXorTriplets', 'st', 's']
================================================================================
// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    int uniqueXorTriplets(std::vector<int>& nums) {
        int mx = *std::max_element(nums.begin(), nums.end()) << 1;
        std::vector<char> st(mx);
        for (int a : nums) for (int b : nums) st[a ^ b] = 1;
        std::vector<int> s(mx);
        for (int ab = 0; ab < mx; ab++) {
            if (st[ab]) for (int c : nums) s[ab ^ c] = 1;
        }
        int ans = 0;
        for (int v : s) ans += v;
        return ans;
    }
};

================================================================================
// FOLDER: 3515_shortest_path_in_a_weighted_tree
// URL: https://leetcode.com/problems/shortest-path-in-a-weighted-tree/
// CONFIG: {"class": "Solution", "method": "treeQueries", "paramOrder": ["n", "edges", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=treeQueries
// PY DEFS: ['treeQueries', 'dfs', 'add', 'rangeAdd', 'point']
// CPP FNS: ['treeQueries', 'inT', 'bit']
================================================================================
// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

#include <vector>
#include <map>
#include <array>

class Solution {
public:
    std::vector<int> treeQueries(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<std::pair<int, int>>> g(n + 1);
        std::map<std::array<int, 2>, int> weight;
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
            int a = std::min(u, v), b = std::max(u, v);
            weight[{a, b}] = w;
        }
        std::vector<int> inT(n + 1), outT(n + 1), dist(n + 1), parent(n + 1);
        int time = 0;
        auto dfs = [&](auto&& self, int u, int p) -> void {
            inT[u] = time++;
            for (auto& [to, w] : g[u]) {
                if (to == p) continue;
                parent[to] = u;
                dist[to] = dist[u] + w;
                self(self, to, u);
            }
            outT[u] = time - 1;
        };
        dfs(dfs, 1, 0);
        std::vector<int> bit(n + 2);
        auto add = [&](int i, int v) {
            for (; i <= n; i += i & -i) bit[i] += v;
        };
        auto rangeAdd = [&](int l, int r, int v) {
            add(l + 1, v);
            add(r + 2, -v);
        };
        auto point = [&](int i) {
            int s = 0;
            for (i++; i > 0; i -= i & -i) s += bit[i];
            return s;
        };
        for (int i = 1; i <= n; i++) rangeAdd(inT[i], inT[i], dist[i]);
        std::vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], nw = q[3];
                int a = std::min(u, v), b = std::max(u, v);
                int ow = weight[{a, b}];
                int delta = nw - ow;
                weight[{a, b}] = nw;
                int child = (parent[u] == v) ? u : v;
                rangeAdd(inT[child], outT[child], delta);
            } else {
                ans.push_back(point(inT[q[1]]));
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3516_find_closest_person
// URL: https://leetcode.com/problems/find-closest-person/
// CONFIG: {"class": "Solution", "method": "findClosest", "paramOrder": ["x", "y", "z"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=findClosest
// PY DEFS: ['findClosest']
// CPP FNS: ['findClosest']
================================================================================
// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

#include <cstdlib>

class Solution {
public:
    int findClosest(int x, int y, int z) {
        int a = std::abs(x - z), b = std::abs(y - z);
        if (a == b) return 0;
        return a < b ? 1 : 2;
    }
};

================================================================================
// FOLDER: 3517_smallest_palindromic_rearrangement_i
// URL: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
// CONFIG: {"class": "Solution", "method": "smallestPalindrome", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=smallestPalindrome
// PY DEFS: ['smallestPalindrome']
// CPP FNS: ['smallestPalindrome', 'cnt']
================================================================================
// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

#include <string>
#include <vector>

class Solution {
public:
    std::string smallestPalindrome(std::string s) {
        std::vector<int> cnt(26);
        for (char c : s) cnt[c - 'a']++;
        std::string t;
        char ch = 0;
        for (char c = 'a'; c <= 'z'; c++) {
            int v = cnt[c - 'a'] / 2;
            t.append(v, c);
            cnt[c - 'a'] -= v * 2;
            if (cnt[c - 'a'] == 1) ch = c;
        }
        std::string sb = t;
        if (ch) sb.push_back(ch);
        for (int i = (int)t.size() - 1; i >= 0; i--) sb.push_back(t[i]);
        return sb;
    }
};

================================================================================
// FOLDER: 3518_smallest_palindromic_rearrangement_ii
// URL: https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/
// CONFIG: {"class": "Solution", "method": "smallestPalindrome", "paramOrder": ["s", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=smallestPalindrome
// PY DEFS: ['nCk', 'countArr', 'smallestPalindrome']
// CPP FNS: ['nCk', 'countArr', 'smallestPalindrome', 'cnt', 'half']
================================================================================
// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

#include <string>
#include <vector>

class Solution {
    static const int MAX = 1000001;
    int nCk(int n, int kk) {
        if (kk < 0 || kk > n) return 0;
        long long res = 1;
        if (kk > n - kk) kk = n - kk;
        for (int i = 1; i <= kk; i++) {
            res = res * (n - i + 1) / i;
            if (res >= MAX) return MAX;
        }
        return (int)res;
    }
    int countArr(std::vector<int>& h) {
        int total = 0;
        for (int f : h) total += f;
        long long res = 1;
        for (int f : h) {
            res *= nCk(total, f);
            if (res >= MAX) return MAX;
            total -= f;
        }
        return (int)res;
    }
public:
    std::string smallestPalindrome(std::string s, int k) {
        std::vector<int> cnt(26);
        for (char c : s) cnt[c - 'a']++;
        int odd = 0;
        for (int c : cnt) if (c % 2) odd++;
        if (odd > 1) return "";
        std::vector<int> half(26);
        char mid = 0;
        for (int i = 0; i < 26; i++) {
            half[i] = cnt[i] / 2;
            if (cnt[i] % 2) mid = char('a' + i);
        }
        if (countArr(half) < k) return "";
        int halfLen = 0;
        for (int f : half) halfLen += f;
        std::string left;
        for (int t = 0; t < halfLen; t++) {
            for (int i = 0; i < 26; i++) {
                if (half[i] == 0) continue;
                half[i]--;
                int arr = countArr(half);
                if (arr >= k) {
                    left.push_back(char('a' + i));
                    break;
                }
                k -= arr;
                half[i]++;
            }
        }
        std::string res = left;
        if (mid) res.push_back(mid);
        for (int i = (int)left.size() - 1; i >= 0; i--) res.push_back(left[i]);
        return res;
    }
};

================================================================================
// FOLDER: 3519_count_numbers_with_non_decreasing_digits
// URL: https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/
// CONFIG: {"class": "Solution", "method": "countNumbers", "paramOrder": ["l", "r", "b"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=countNumbers
// PY DEFS: ['toDigits', 'dec', 'countUpto', 'dfs', 'countNumbers']
// CPP FNS: ['toDigits', 'dec', 'countUpto', 'countNumbers']
================================================================================
// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

#include <string>
#include <vector>
#include <map>
#include <array>
#include <algorithm>

class Solution {
    static const int MOD = 1000000007;
    // convert decimal string to base-b digits (MSB first) using repeated division
    std::vector<int> toDigits(std::string s, int b) {
        if (s == "0") return {0};
        std::vector<int> digs;
        while (!(s.size() == 1 && s[0] == '0')) {
            int rem = 0;
            std::string q;
            for (char c : s) {
                int cur = rem * 10 + (c - '0');
                int d = cur / b;
                rem = cur % b;
                if (!q.empty() || d != 0) q.push_back(char('0' + d));
            }
            digs.push_back(rem);
            s = q.empty() ? "0" : q;
        }
        std::reverse(digs.begin(), digs.end());
        return digs;
    }
    std::string dec(std::string s) {
        int i = (int)s.size() - 1;
        while (i >= 0 && s[i] == '0') { s[i] = '9'; i--; }
        if (i < 0) return "0";
        s[i]--;
        if (s[0] == '0' && s.size() > 1) s.erase(s.begin());
        // trim leading zeros
        size_t p = 0;
        while (p + 1 < s.size() && s[p] == '0') p++;
        return s.substr(p);
    }
    int countUpto(const std::vector<int>& digs, int b) {
        int m = (int)digs.size();
        std::map<std::array<int, 3>, int> memo;
        auto dfs = [&](auto&& self, int pos, int last, bool tight) -> int {
            if (pos == m) return 1;
            std::array<int, 3> key = {pos, last, tight ? 1 : 0};
            if (memo.count(key)) return memo[key];
            int up = tight ? digs[pos] : b - 1;
            int res = 0;
            for (int d = last; d <= up; d++)
                res = (res + self(self, pos + 1, d, tight && d == up)) % MOD;
            return memo[key] = res;
        };
        return dfs(dfs, 0, 0, true);
    }
public:
    int countNumbers(std::string l, std::string r, int b) {
        auto rd = toDigits(r, b);
        auto ld = toDigits(dec(l), b);
        return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD;
    }
};

================================================================================
// FOLDER: 3520_minimum_threshold_for_inversion_pairs_count
// URL: https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['upperBound', 'countInv', 'minThreshold']
// CPP FNS: ['countInv', 'minThreshold']
================================================================================
// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

#include <vector>
#include <algorithm>

class Solution {
    bool countInv(const std::vector<int>& nums, int k, int threshold) {
        std::vector<int> sorted;
        long long inv = 0;
        for (int num : nums) {
            auto left = std::upper_bound(sorted.begin(), sorted.end(), num) - sorted.begin();
            auto right = std::upper_bound(sorted.begin(), sorted.end(), num + threshold) - sorted.begin();
            inv += right - left;
            sorted.insert(std::upper_bound(sorted.begin(), sorted.end(), num), num);
        }
        return inv >= k;
    }
public:
    int minThreshold(std::vector<int>& nums, int k) {
        int mx = 0;
        for (int v : nums) if (v > mx) mx = v;
        int l = 0, r = mx + 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (countInv(nums, k, m)) r = m;
            else l = m + 1;
        }
        return l > mx ? -1 : l;
    }
};

----- PYTHON -----
# LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
# https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

from typing import List


def upperBound(a: List[int], target: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def countInv(nums: List[int], k: int, threshold: int) -> bool:
    sorted_arr: List[int] = []
    inv = 0
    for num in nums:
        left = upperBound(sorted_arr, num)
        right = upperBound(sorted_arr, num + threshold)
        inv += right - left
        sorted_arr.insert(upperBound(sorted_arr, num), num)
    return inv >= k


class Solution:
    def minThreshold(self, nums: List[int], k: int) -> int:
        mx = 0
        for v in nums:
            if v > mx:
                mx = v
        l, r = 0, mx + 1
        while l < r:
            m = (l + r) >> 1
            if countInv(nums, k, m):
                r = m
            else:
                l = m + 1
        return -1 if l > mx else l

================================================================================
// FOLDER: 3522_calculate_score_after_performing_instructions
// URL: https://leetcode.com/problems/calculate-score-after-performing-instructions/
// CONFIG: {"class": "Solution", "method": "calculateScore", "paramOrder": ["instructions", "values"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=calculateScore
// PY DEFS: ['calculateScore']
// CPP FNS: ['calculateScore', 'vis']
================================================================================
// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

#include <string>
#include <vector>

class Solution {
public:
    long long calculateScore(std::vector<std::string>& instructions, std::vector<int>& values) {
        int n = (int)values.size();
        std::vector<char> vis(n);
        long long ans = 0;
        int i = 0;
        while (i >= 0 && i < n && !vis[i]) {
            vis[i] = 1;
            if (instructions[i][0] == 'a') {
                ans += values[i];
                i += 1;
            } else {
                i += values[i];
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3523_make_array_non_decreasing
// URL: https://leetcode.com/problems/make-array-non-decreasing/
// CONFIG: {"class": "Solution", "method": "maximumPossibleSize", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maximumPossibleSize
// PY DEFS: ['maximumPossibleSize']
// CPP FNS: ['maximumPossibleSize']
================================================================================
// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

#include <vector>

class Solution {
public:
    int maximumPossibleSize(std::vector<int>& nums) {
        int ans = 0, mx = 0;
        for (int x : nums) {
            if (mx <= x) {
                ans++;
                mx = x;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3524_find_x_value_of_array_i
// URL: https://leetcode.com/problems/find-x-value-of-array-i/
// CONFIG: {"class": "Solution", "method": "resultArray", "paramOrder": ["nums", "k"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=resultArray
// PY DEFS: ['resultArray']
// CPP FNS: ['resultArray', 'ans', 'newDp']
================================================================================
// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

#include <vector>

class Solution {
public:
    std::vector<long long> resultArray(std::vector<int>& nums, int k) {
        std::vector<long long> ans(k), dp(k);
        for (int num : nums) {
            std::vector<long long> newDp(k);
            int nm = num % k;
            newDp[nm] = 1;
            for (int i = 0; i < k; i++) newDp[(i * nm) % k] += dp[i];
            for (int i = 0; i < k; i++) ans[i] += newDp[i];
            dp.swap(newDp);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3525_find_x_value_of_array_ii
// URL: https://leetcode.com/problems/find-x-value-of-array-ii/
// CONFIG: {"class": "Solution", "method": "resultArray", "paramOrder": ["nums", "k", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=resultArray
// PY DEFS: ['resultArray']
// CPP FNS: ['resultArray', 'ans']
================================================================================
// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

#include <vector>

class Solution {
public:
    std::vector<int> resultArray(std::vector<int>& nums, int k, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int idx = queries[qi][0], val = queries[qi][1], start = queries[qi][2], x = queries[qi][3];
            nums[idx] = val;
            int prod = 1, cnt = 0;
            for (int i = start; i < n; i++) {
                prod = prod * (nums[i] % k) % k;
                if (prod == x) cnt++;
            }
            ans[qi] = cnt;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3526_range_xor_queries_with_subarray_reversals
// URL: https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["nums", "queries"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['getResults', 'at', 'set_at']
// CPP FNS: ['getResults']
================================================================================
// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> getResults(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        std::vector<int> a = nums;
        std::vector<int> ans;
        for (auto& q : queries) {
            int typ = q[0];
            if (typ == 1) {
                int l = q[1], r = q[2];
                while (l < r) { std::swap(a[l], a[r]); l++; r--; }
            } else if (typ == 2) {
                int l = q[1], r = q[2], x = 0;
                for (int i = l; i <= r; i++) x ^= a[i];
                ans.push_back(x);
            } else {
                a[q[1]] = q[2];
            }
        }
        return ans;
    }
};

----- PYTHON -----
# LeetCode 3526 - Range XOR Queries with Subarray Reversals
# https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

from typing import List


class Solution:
    def getResults(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        a = nums[:]
        ans = []

        def at(i: int) -> int:
            return a[i] if 0 <= i < len(a) else 0

        def set_at(i: int, val: int) -> None:
            if i < 0:
                return
            while len(a) <= i:
                a.append(0)
            a[i] = val

        for q in queries:
            typ = q[0]
            if typ == 1:
                l, r = q[1], q[2]
                while l < r:
                    left, right = at(l), at(r)
                    set_at(l, right)
                    set_at(r, left)
                    l += 1
                    r -= 1
            elif typ == 2:
                x = 0
                for i in range(q[1], q[2] + 1):
                    x ^= at(i)
                ans.append(x)
            else:
                set_at(q[1], q[2])
        return ans

================================================================================
// FOLDER: 3527_find_the_most_common_response
// URL: https://leetcode.com/problems/find-the-most-common-response/
// CONFIG: {"class": "Solution", "method": "findCommonResponse", "paramOrder": ["responses"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=findCommonResponse
// PY DEFS: ['findCommonResponse']
// CPP FNS: ['findCommonResponse']
================================================================================
// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    std::string findCommonResponse(std::vector<std::vector<std::string>>& responses) {
        std::unordered_map<std::string, int> cnt;
        for (auto& ws : responses) {
            std::unordered_set<std::string> s;
            for (auto& w : ws) {
                if (s.insert(w).second) cnt[w]++;
            }
        }
        std::string ans = responses[0][0];
        for (auto& [w, v] : cnt) {
            if (cnt[ans] < v || (cnt[ans] == v && w < ans)) ans = w;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3528_unit_conversion_i
// URL: https://leetcode.com/problems/unit-conversion-i/
// CONFIG: {"class": "Solution", "method": "baseUnitConversions", "paramOrder": ["conversions"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=baseUnitConversions
// PY DEFS: ['baseUnitConversions', 'dfs']
// CPP FNS: ['baseUnitConversions', 'ans']
================================================================================
// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

#include <vector>

class Solution {
public:
    std::vector<int> baseUnitConversions(std::vector<std::vector<int>>& conversions) {
        const int mod = 1000000007;
        int n = (int)conversions.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : conversions) g[e[0]].push_back({e[1], e[2]});
        std::vector<int> ans(n);
        auto dfs = [&](auto&& self, int s, int mul) -> void {
            ans[s] = mul;
            for (auto& [t, w] : g[s]) self(self, t, (int)(1LL * mul * w % mod));
        };
        dfs(dfs, 0, 1);
        return ans;
    }
};

================================================================================
// FOLDER: 3529_count_cells_in_overlapping_horizontal_and_vertical_substrings
// URL: https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/
// CONFIG: {"class": "Solution", "method": "countCells", "paramOrder": ["grid", "pattern"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=countCells
// PY DEFS: ['countCells']
// CPP FNS: ['countCells']
================================================================================
// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

#include <string>
#include <vector>

class Solution {
public:
    int countCells(std::vector<std::vector<char>>& grid, std::string pattern) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::string row, col;
        row.reserve(m * n); col.reserve(m * n);
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) row.push_back(grid[i][j]);
        for (int j = 0; j < n; j++) for (int i = 0; i < m; i++) col.push_back(grid[i][j]);
        std::vector<std::vector<char>> hMark(m, std::vector<char>(n)), vMark(m, std::vector<char>(n));
        int plen = (int)pattern.size();
        for (int i = 0; i + plen <= (int)row.size(); i++) {
            if (row.compare(i, plen, pattern) == 0) {
                for (int t = 0; t < plen; t++) {
                    int pos = i + t;
                    hMark[pos / n][pos % n] = 1;
                }
            }
        }
        for (int i = 0; i + plen <= (int)col.size(); i++) {
            if (col.compare(i, plen, pattern) == 0) {
                for (int t = 0; t < plen; t++) {
                    int pos = i + t;
                    vMark[pos % m][pos / m] = 1;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++)
            if (hMark[i][j] && vMark[i][j]) ans++;
        return ans;
    }
};

================================================================================
// FOLDER: 3530_maximum_profit_from_valid_topological_order_in_dag
// URL: https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/
// CONFIG: {"class": "Solution", "method": "maxProfit", "paramOrder": ["n", "edges", "score"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxProfit
// PY DEFS: ['maxProfit', 'popcount']
// CPP FNS: ['pop', 'maxProfit', 'need']
================================================================================
// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

#include <vector>

class Solution {
    int pop(int x) {
        int c = 0;
        while (x) { c += x & 1; x >>= 1; }
        return c;
    }
public:
    int maxProfit(int n, std::vector<std::vector<int>>& edges, std::vector<int>& score) {
        std::vector<int> need(n), dp(1 << n, -1);
        dp[0] = 0;
        for (auto& e : edges) need[e[1]] |= 1 << e[0];
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] < 0) continue;
            int pos = pop(mask) + 1;
            for (int i = 0; i < n; i++) {
                if ((mask >> i) & 1) continue;
                if ((mask & need[i]) == need[i]) {
                    int nm = mask | (1 << i);
                    int v = dp[mask] + score[i] * pos;
                    if (v > dp[nm]) dp[nm] = v;
                }
            }
        }
        return dp[(1 << n) - 1];
    }
};

================================================================================
// FOLDER: 3531_count_covered_buildings
// URL: https://leetcode.com/problems/count-covered-buildings/
// CONFIG: {"class": "Solution", "method": "countCoveredBuildings", "paramOrder": ["n", "buildings"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=countCoveredBuildings
// PY DEFS: ['countCoveredBuildings']
// CPP FNS: ['countCoveredBuildings']
================================================================================
// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int countCoveredBuildings(int n, std::vector<std::vector<int>>& buildings) {
        std::unordered_map<int, std::vector<int>> g1, g2;
        for (auto& b : buildings) {
            g1[b[0]].push_back(b[1]);
            g2[b[1]].push_back(b[0]);
        }
        for (auto& [_, list] : g1) std::sort(list.begin(), list.end());
        for (auto& [_, list] : g2) std::sort(list.begin(), list.end());
        int ans = 0;
        for (auto& b : buildings) {
            int x = b[0], y = b[1];
            auto& l1 = g1[x];
            auto& l2 = g2[y];
            if (l2.front() < x && x < l2.back() && l1.front() < y && y < l1.back()) ans++;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3532_path_existence_queries_in_a_graph_i
// URL: https://leetcode.com/problems/path-existence-queries-in-a-graph-i/
// CONFIG: {"class": "Solution", "method": "pathExistenceQueries", "paramOrder": ["n", "nums", "maxDiff", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=pathExistenceQueries
// PY DEFS: ['pathExistenceQueries']
// CPP FNS: ['pathExistenceQueries', 'g']
================================================================================
// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

#include <vector>

class Solution {
public:
    std::vector<bool> pathExistenceQueries(int n, std::vector<int>& nums, int maxDiff, std::vector<std::vector<int>>& queries) {
        std::vector<int> g(n);
        int cnt = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] > maxDiff) cnt++;
            g[i] = cnt;
        }
        std::vector<bool> ans;
        for (auto& q : queries) ans.push_back(g[q[0]] == g[q[1]]);
        return ans;
    }
};

================================================================================
// FOLDER: 3533_concatenated_divisibility
// URL: https://leetcode.com/problems/concatenated-divisibility/
// CONFIG: {"class": "Solution", "method": "concatenatedDivisibility", "paramOrder": ["nums", "k"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=concatenatedDivisibility
// PY DEFS: ['concatenatedDivisibility', 'dp', 'reconstruct']
// CPP FNS: ['concatenatedDivisibility', 'pows']
================================================================================
// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

#include <vector>
#include <algorithm>
#include <map>

class Solution {
public:
    std::vector<int> concatenatedDivisibility(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::vector<int> pows(n);
        for (int i = 0; i < n; i++) {
            int p = 1, num = nums[i];
            if (num == 0) p = 10 % k;
            else {
                for (int x = num; x > 0; x /= 10) p = p * 10 % k;
            }
            pows[i] = p;
        }
        std::map<std::pair<int, int>, bool> memo;
        auto dp = [&](auto&& self, int mask, int mod) -> bool {
            if (mask == (1 << n) - 1) return mod == 0;
            auto kk = std::make_pair(mask, mod);
            if (memo.count(kk)) return memo[kk];
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 0) {
                    int nm = (mod * pows[i] + nums[i]) % k;
                    if (self(self, mask | (1 << i), nm)) return memo[kk] = true;
                }
            }
            return memo[kk] = false;
        };
        auto reconstruct = [&](auto&& self, int mask, int mod) -> std::vector<int> {
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 0) {
                    int nm = (mod * pows[i] + nums[i]) % k;
                    if (dp(dp, mask | (1 << i), nm)) {
                        auto rest = self(self, mask | (1 << i), nm);
                        rest.insert(rest.begin(), nums[i]);
                        return rest;
                    }
                }
            }
            return {};
        };
        if (!dp(dp, 0, 0)) return {};
        return reconstruct(reconstruct, 0, 0);
    }
};

================================================================================
// FOLDER: 3534_path_existence_queries_in_a_graph_ii
// URL: https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
// CONFIG: {"class": "Solution", "method": "pathExistenceQueries", "paramOrder": ["n", "nums", "maxDiff", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=pathExistenceQueries
// PY DEFS: ['pathExistenceQueries']
// CPP FNS: ['pathExistenceQueries']
================================================================================
// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

#include <vector>
#include <algorithm>
#include <array>

class Solution {
public:
    std::vector<int> pathExistenceQueries(int n, std::vector<int>& nums, int maxDiff, std::vector<std::vector<int>>& queries) {
        std::vector<std::array<int, 2>> pairs(n);
        for (int i = 0; i < n; i++) pairs[i] = {nums[i], i};
        std::sort(pairs.begin(), pairs.end());
        int m = 20;
        std::vector<std::vector<int>> f(n, std::vector<int>(m));
        int r = n - 1;
        for (int l = n - 1; l >= 0; l--) {
            while (pairs[r][0] - pairs[l][0] > maxDiff) r--;
            int i = pairs[l][1], j = pairs[r][1];
            f[i][0] = j;
            for (int k = 1; k < m; k++) f[i][k] = f[f[i][k - 1]][k - 1];
        }
        std::vector<int> ans;
        for (auto& q : queries) {
            int i = q[0], j = q[1];
            if (nums[i] > nums[j]) std::swap(i, j);
            if (i == j) { ans.push_back(0); continue; }
            if (nums[i] == nums[j]) { ans.push_back(1); continue; }
            int d = 0;
            for (int k = m - 1; k >= 0; k--) {
                if (nums[f[i][k]] < nums[j]) {
                    d |= 1 << k;
                    i = f[i][k];
                }
            }
            if (nums[f[i][0]] < nums[j]) ans.push_back(-1);
            else ans.push_back(d + 1);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3535_unit_conversion_ii
// URL: https://leetcode.com/problems/unit-conversion-ii/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["conversions", "queries"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['queryConversions', 'qpow', 'dfs']
// CPP FNS: ['qpow', 'queryConversions', 'res', 'ans']
================================================================================
// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

#include <vector>

class Solution {
    static const int MOD = 1000000007;
    long long qpow(long long x, int n) {
        long long res = 1;
        while (n > 0) {
            if (n & 1) res = res * x % MOD;
            x = x * x % MOD;
            n >>= 1;
        }
        return res;
    }
public:
    std::vector<int> queryConversions(std::vector<std::vector<int>>& conversions, std::vector<std::vector<int>>& queries) {
        int n = (int)conversions.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : conversions) g[e[0]].push_back({e[1], e[2]});
        std::vector<int> res(n);
        auto dfs = [&](auto&& self, int s, int mul) -> void {
            res[s] = mul;
            for (auto& [t, w] : g[s]) self(self, t, (int)(1LL * mul * w % MOD));
        };
        dfs(dfs, 0, 1);
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++)
            ans[i] = (int)(1LL * res[queries[i][1]] * qpow(res[queries[i][0]], MOD - 2) % MOD);
        return ans;
    }
};

----- PYTHON -----
# LeetCode 3535 - Unit Conversion II
# https://leetcode.com/problems/unit-conversion-ii/

from typing import List


class Solution:
    def queryConversions(
        self, conversions: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MOD = 1000000007

        def qpow(x: int, n: int) -> int:
            res = 1
            bx, bn = x, n
            while bn > 0:
                if bn & 1:
                    res = res * bx % MOD
                bx = bx * bx % MOD
                bn >>= 1
            return res

        n = len(conversions) + 1
        g = [[] for _ in range(n)]
        for e in conversions:
            g[e[0]].append((e[1], e[2]))
        res = [0] * n

        def dfs(s: int, mul: int) -> None:
            res[s] = mul
            for to, w in g[s]:
                dfs(to, mul * w % MOD)

        dfs(0, 1)
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            ans[i] = res[q[1]] * qpow(res[q[0]], MOD - 2) % MOD
        return ans

================================================================================
// FOLDER: 3536_maximum_product_of_two_digits
// URL: https://leetcode.com/problems/maximum-product-of-two-digits/
// CONFIG: {"class": "Solution", "method": "maxProduct", "paramOrder": ["n"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxProduct
// PY DEFS: ['maxProduct']
// CPP FNS: ['maxProduct']
================================================================================
// LeetCode 3536 - Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution {
public:
    int maxProduct(int n) {
        int a = 0, b = 0;
        for (; n > 0; n /= 10) {
            int x = n % 10;
            if (a < x) { b = a; a = x; }
            else if (b < x) b = x;
        }
        return a * b;
    }
};

================================================================================
// FOLDER: 3537_fill_a_special_grid
// URL: https://leetcode.com/problems/fill-a-special-grid/
// CONFIG: {"class": "Solution", "method": "specialGrid", "paramOrder": ["n"], "types": {"return": "integer[][]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=specialGrid
// PY DEFS: ['specialGrid', 'dfs']
// CPP FNS: []
================================================================================
// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> specialGrid(int n) {
        int m = 1 << n;
        std::vector<std::vector<int>> ans(m, std::vector<int>(m));
        int val = 0;
        auto dfs = [&](auto&& self, int x, int y, int k) -> void {
            if (k == 1) { ans[x][y] = val++; return; }
            int h = k / 2;
            self(self, x, y, h);
            self(self, x + h, y, h);
            self(self, x + h, y - h, h);
            self(self, x, y - h, h);
        };
        dfs(dfs, 0, m - 1, m);
        return ans;
    }
};

================================================================================
// FOLDER: 3538_merge_operations_for_minimum_travel_time
// URL: https://leetcode.com/problems/merge-operations-for-minimum-travel-time/
// CONFIG: {"class": "Solution", "method": "minTravelTime", "paramOrder": ["l", "n", "k", "position", "time"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minTravelTime
// PY DEFS: ['minTravelTime', 'dp']
// CPP FNS: ['minTravelTime', 'prefix']
================================================================================
// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

#include <vector>
#include <map>
#include <array>
#include <algorithm>

class Solution {
public:
    int minTravelTime(int l, int n, int k, std::vector<int>& position, std::vector<int>& time) {
        std::vector<int> prefix(n);
        prefix[0] = time[0];
        for (int i = 1; i < n; i++) prefix[i] = prefix[i - 1] + time[i];
        const long long inf = (long long)1e18;
        std::map<std::array<int, 3>, long long> memo;
        auto dp = [&](auto&& self, int i, int skips, int last) -> long long {
            if (i == n - 1) return skips == 0 ? 0 : inf;
            std::array<int, 3> key = {i, skips, last};
            if (memo.count(key)) return memo[key];
            int rate = prefix[i];
            if (last > 0) rate -= prefix[last - 1];
            long long res = inf;
            int end = n - 1;
            if (i + skips + 1 < end) end = i + skips + 1;
            for (int j = i + 1; j <= end; j++) {
                long long cand = 1LL * (position[j] - position[i]) * rate + self(self, j, skips - (j - i - 1), i + 1);
                if (cand < res) res = cand;
            }
            return memo[key] = res;
        };
        (void)l;
        return (int)dp(dp, 0, k, 0);
    }
};

================================================================================
// FOLDER: 3539_find_sum_of_array_product_of_magical_sequences
// URL: https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/
// CONFIG: {"class": "Solution", "method": "magicalSum", "paramOrder": ["m", "k", "nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=magicalSum
// PY DEFS: ['magicalSum', 'qpow', 'comb', 'dfs']
// CPP FNS: ['qpow', 'initFact', 'comb', 'magicalSum']
================================================================================
// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

#include <vector>

class Solution {
    static const int N = 31;
    static const int MOD = 1000000007;
    long long f[N], g[N];
    bool inited = false;
    long long qpow(long long a, long long k) {
        long long res = 1;
        while (k > 0) {
            if (k & 1) res = res * a % MOD;
            a = a * a % MOD;
            k >>= 1;
        }
        return res;
    }
    void initFact() {
        if (inited) return;
        f[0] = g[0] = 1;
        for (int i = 1; i < N; i++) {
            f[i] = f[i - 1] * i % MOD;
            g[i] = qpow(f[i], MOD - 2);
        }
        inited = true;
    }
    long long comb(int m, int n) {
        if (n < 0 || n > m) return 0;
        return f[m] * g[n] % MOD * g[m - n] % MOD;
    }
public:
    int magicalSum(int m, int k, std::vector<int>& nums) {
        initFact();
        int n = (int)nums.size();
        std::vector dp(n + 1, std::vector(m + 1, std::vector(k + 1, std::vector<long long>(N, -1))));
        auto dfs = [&](auto&& self, int i, int j, int kk, int st) -> long long {
            if (kk < 0 || (i == n && j > 0)) return 0;
            if (i == n) {
                while (st > 0) { kk -= st & 1; st >>= 1; }
                return kk == 0 ? 1 : 0;
            }
            if (dp[i][j][kk][st] != -1) return dp[i][j][kk][st];
            long long res = 0;
            for (int t = 0; t <= j; t++) {
                int nt = t + st;
                int nk = kk - (nt & 1);
                long long p = qpow(nums[i], t);
                long long tmp = comb(j, t) * p % MOD * self(self, i + 1, j - t, nk, nt >> 1) % MOD;
                res = (res + tmp) % MOD;
            }
            return dp[i][j][kk][st] = res;
        };
        return (int)dfs(dfs, 0, m, k, 0);
    }
};

================================================================================
// FOLDER: 3540_minimum_time_to_visit_all_houses
// URL: https://leetcode.com/problems/minimum-time-to-visit-all-houses/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["forward", "backward", "queries"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['minTotalTime']
// CPP FNS: ['minTotalTime', 'pf']
================================================================================
// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long minTotalTime(std::vector<int>& forward, std::vector<int>& backward, std::vector<int>& queries) {
        int n = (int)forward.size();
        int sumB = 0;
        for (int v : backward) sumB += v;
        std::vector<int> pf(n + 1), pb(n + 1);
        for (int i = 0; i < n; i++) {
            pf[i + 1] = pf[i] + forward[i];
            pb[i + 1] = pb[i] + backward[i];
        }
        long long ans = 0;
        int pos = 0;
        for (int q : queries) {
            int r = 0;
            if (q < pos) r = pf[n];
            r += pf[q] - pf[pos];
            int l = 0;
            if (q > pos) l = sumB;
            l += pb[pos] - pb[q];
            ans += std::min(l, r);
            pos = q;
        }
        return ans;
    }
};

----- PYTHON -----
# LeetCode 3540 - Minimum Time to Visit All Houses
# https://leetcode.com/problems/minimum-time-to-visit-all-houses/

from typing import List


class Solution:
    def minTotalTime(
        self, forward: List[int], backward: List[int], queries: List[int]
    ) -> int:
        n = len(forward)
        sum_b = sum(backward)
        pf = [0] * (n + 1)
        pb = [0] * (n + 1)
        for i in range(n):
            pf[i + 1] = pf[i] + forward[i]
            pb[i + 1] = pb[i] + backward[i]
        ans = 0
        pos = 0
        for q in queries:
            r = 0
            if q < pos:
                r = pf[n]
            r += pf[q] - pf[pos]
            lft = 0
            if q > pos:
                lft = sum_b
            lft += pb[pos] - pb[q]
            ans += min(lft, r)
            pos = q
        return ans

================================================================================
// FOLDER: 3541_find_most_frequent_vowel_and_consonant
// URL: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
// CONFIG: {"class": "Solution", "method": "maxFreqSum", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxFreqSum
// PY DEFS: ['maxFreqSum']
// CPP FNS: ['maxFreqSum']
================================================================================
// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

#include <string>
#include <algorithm>

class Solution {
public:
    int maxFreqSum(std::string s) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        int a = 0, b = 0;
        for (int i = 0; i < 26; i++) {
            char c = char(i + 'a');
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                a = std::max(a, cnt[i]);
            else b = std::max(b, cnt[i]);
        }
        return a + b;
    }
};

================================================================================
// FOLDER: 3542_minimum_operations_to_convert_all_elements_to_zero
// URL: https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/
// CONFIG: {"class": "Solution", "method": "minOperations", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minOperations
// PY DEFS: ['minOperations']
// CPP FNS: ['minOperations']
================================================================================
// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::vector<int> stk;
        int ans = 0;
        for (int x : nums) {
            while (!stk.empty() && stk.back() > x) {
                ans++;
                stk.pop_back();
            }
            if (x != 0 && (stk.empty() || stk.back() != x)) stk.push_back(x);
        }
        ans += (int)stk.size();
        return ans;
    }
};

================================================================================
// FOLDER: 3543_maximum_weighted_k_edge_path
// URL: https://leetcode.com/problems/maximum-weighted-k-edge-path/
// CONFIG: {"class": "Solution", "method": "maxWeight", "paramOrder": ["n", "edges", "k", "t"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxWeight
// PY DEFS: ['maxWeight']
// CPP FNS: ['maxWeight']
================================================================================
// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

#include <vector>
#include <unordered_set>

class Solution {
public:
    int maxWeight(int n, std::vector<std::vector<int>>& edges, int k, int t) {
        std::vector<std::vector<std::pair<int, int>>> graph(n);
        for (auto& e : edges) graph[e[0]].push_back({e[1], e[2]});
        std::vector<std::vector<std::unordered_set<int>>> dp(n, std::vector<std::unordered_set<int>>(k + 1));
        for (int u = 0; u < n; u++) dp[u][0].insert(0);
        for (int i = 0; i < k; i++) {
            for (int u = 0; u < n; u++) {
                for (int sum : dp[u][i]) {
                    for (auto& [to, w] : graph[u]) {
                        int ns = sum + w;
                        if (ns < t) dp[to][i + 1].insert(ns);
                    }
                }
            }
        }
        int ans = -1;
        for (int u = 0; u < n; u++)
            for (int sum : dp[u][k]) if (sum > ans) ans = sum;
        return ans;
    }
};

================================================================================
// FOLDER: 3544_subtree_inversion_sum
// URL: https://leetcode.com/problems/subtree-inversion-sum/
// CONFIG: {"class": "Solution", "method": "subtreeInversionSum", "paramOrder": ["edges", "nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=subtreeInversionSum
// PY DEFS: ['subtreeInversionSum', 'dp']
// CPP FNS: ['subtreeInversionSum', 'parent']
================================================================================
// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

#include <vector>
#include <map>
#include <tuple>

class Solution {
public:
    long long subtreeInversionSum(std::vector<std::vector<int>>& edges, std::vector<int>& nums, int k) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        std::vector<int> parent(n, -1);
        std::map<std::tuple<int, int, bool>, long long> memo;
        auto dp = [&](auto&& self, int u, int steps, bool inv) -> long long {
            auto key = std::make_tuple(u, steps, inv);
            if (memo.count(key)) return memo[key];
            long long num = nums[u];
            if (inv) num = -num;
            long long negNum = -num;
            for (int v : graph[u]) {
                if (v == parent[u]) continue;
                parent[v] = u;
                int ns = steps + 1;
                if (ns > k) ns = k;
                num += self(self, v, ns, inv);
                if (steps == k) negNum += self(self, v, 1, !inv);
            }
            long long res = num;
            if (steps == k && negNum > res) res = negNum;
            return memo[key] = res;
        };
        return dp(dp, 0, k, false);
    }
};

================================================================================
// FOLDER: 3545_minimum_deletions_for_at_most_k_distinct_characters
// URL: https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/
// CONFIG: {"class": "Solution", "method": "minDeletion", "paramOrder": ["s", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minDeletion
// PY DEFS: ['minDeletion']
// CPP FNS: ['minDeletion', 'cnt']
================================================================================
// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minDeletion(std::string s, int k) {
        std::vector<int> cnt(26);
        for (char c : s) cnt[c - 'a']++;
        std::sort(cnt.begin(), cnt.end());
        int ans = 0;
        for (int i = 0; i + k < 26; i++) ans += cnt[i];
        return ans;
    }
};

================================================================================
// FOLDER: 3546_equal_sum_grid_partition_i
// URL: https://leetcode.com/problems/equal-sum-grid-partition-i/
// CONFIG: {"class": "Solution", "method": "canPartitionGrid", "paramOrder": ["grid"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=canPartitionGrid
// PY DEFS: ['canPartitionGrid']
// CPP FNS: ['canPartitionGrid']
================================================================================
// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

#include <vector>

class Solution {
public:
    bool canPartitionGrid(std::vector<std::vector<int>>& grid) {
        long long s = 0;
        for (auto& row : grid) for (int x : row) s += x;
        if (s % 2) return false;
        int m = (int)grid.size(), n = (int)grid[0].size();
        long long pre = 0;
        for (int i = 0; i < m; i++) {
            for (int x : grid[i]) pre += x;
            if (pre * 2 == s && i + 1 < m) return true;
        }
        pre = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) pre += grid[i][j];
            if (pre * 2 == s && j + 1 < n) return true;
        }
        return false;
    }
};

================================================================================
// FOLDER: 3547_maximum_sum_of_edge_values_in_a_graph
// URL: https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/
// CONFIG: {"class": "Solution", "method": "maxScore", "paramOrder": ["n", "edges"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxScore
// PY DEFS: ['calc3547', 'get_comp', 'maxScore']
// CPP FNS: ['calc', 'maxScore', 'seen']
================================================================================
// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

#include <vector>
#include <algorithm>

class Solution {
    long long calc(int left, int right, bool isCycle) {
        int w0 = right, w1 = right;
        long long score = 0;
        for (int value = right - 1; value >= left; value--) {
            score += 1LL * w0 * value;
            w0 = w1;
            w1 = value;
        }
        if (isCycle) score += 1LL * w0 * w1;
        return score;
    }
public:
    long long maxScore(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        std::vector<char> seen(n);
        std::vector<int> cycleSizes, pathSizes;
        auto getComp = [&](int start) {
            std::vector<int> comp = {start};
            seen[start] = 1;
            for (int i = 0; i < (int)comp.size(); i++) {
                for (int v : graph[comp[i]]) {
                    if (!seen[v]) { seen[v] = 1; comp.push_back(v); }
                }
            }
            return comp;
        };
        for (int i = 0; i < n; i++) {
            if (seen[i]) continue;
            auto comp = getComp(i);
            bool allDeg2 = true;
            for (int u : comp) if ((int)graph[u].size() != 2) { allDeg2 = false; break; }
            if (allDeg2) cycleSizes.push_back((int)comp.size());
            else if ((int)comp.size() > 1) pathSizes.push_back((int)comp.size());
        }
        long long ans = 0;
        int curN = n;
        for (int cs : cycleSizes) {
            ans += calc(curN - cs + 1, curN, true);
            curN -= cs;
        }
        std::sort(pathSizes.rbegin(), pathSizes.rend());
        for (int ps : pathSizes) {
            ans += calc(curN - ps + 1, curN, false);
            curN -= ps;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3548_equal_sum_grid_partition_ii
// URL: https://leetcode.com/problems/equal-sum-grid-partition-ii/
// CONFIG: {"class": "Solution", "method": "canPartitionGrid", "paramOrder": ["grid"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=canPartitionGrid
// PY DEFS: ['rotate3548', 'check3548', 'canPartitionGrid']
// CPP FNS: ['check', 'canPartitionGrid']
================================================================================
// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

#include <vector>
#include <unordered_map>

class Solution {
    std::vector<std::vector<int>> rotate(const std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> t(n, std::vector<int>(m));
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) t[j][i] = grid[i][j];
        return t;
    }
    bool check(const std::vector<std::vector<int>>& g) {
        int m = (int)g.size(), n = (int)g[0].size();
        long long s1 = 0, s2 = 0;
        std::unordered_map<long long, int> cnt1, cnt2;
        for (auto& row : g) for (int x : row) {
            long long v = x;
            s2 += v;
            cnt2[v]++;
        }
        for (int i = 0; i < m - 1; i++) {
            for (int x : g[i]) {
                long long v = x;
                s1 += v; s2 -= v;
                cnt1[v]++; cnt2[v]--;
            }
            if (s1 == s2) return true;
            if (s1 < s2) {
                long long diff = s2 - s1;
                if (cnt2[diff] > 0) {
                    if ((m - i - 1 > 1 && n > 1) ||
                        (i == m - 2 && (g[i + 1][0] == diff || g[i + 1][n - 1] == diff)) ||
                        (n == 1 && (g[i + 1][0] == diff || g[m - 1][0] == diff)))
                        return true;
                }
            } else {
                long long diff = s1 - s2;
                if (cnt1[diff] > 0) {
                    if ((i + 1 > 1 && n > 1) ||
                        (i == 0 && (g[0][0] == diff || g[0][n - 1] == diff)) ||
                        (n == 1 && (g[0][0] == diff || g[i][0] == diff)))
                        return true;
                }
            }
        }
        return false;
    }
public:
    bool canPartitionGrid(std::vector<std::vector<int>>& grid) {
        return check(grid) || check(rotate(grid));
    }
};

================================================================================
// FOLDER: 3549_multiply_two_polynomials
// URL: https://leetcode.com/problems/multiply-two-polynomials/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["poly1", "poly2"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['__init__', 'mul', 'add', 'sub', 'div', 'fft', 'multiply']
// CPP FNS: ['fft', 'multiply', 'fa', 'res']
================================================================================
// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

class Solution {
    using cd = std::complex<double>;
    void fft(std::vector<cd>& a, bool invert) {
        int n = (int)a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) std::swap(a[i], a[j]);
        }
        for (int length = 2; length <= n; length <<= 1) {
            double angle = 2 * acos(-1.0) / length * (invert ? -1 : 1);
            cd wlen(cos(angle), sin(angle));
            for (int i = 0; i < n; i += length) {
                cd w(1);
                int half = length >> 1;
                for (int j = 0; j < half; j++) {
                    cd u = a[i + j];
                    cd v = a[i + j + half] * w;
                    a[i + j] = u + v;
                    a[i + j + half] = u - v;
                    w *= wlen;
                }
            }
        }
        if (invert) for (auto& x : a) x /= n;
    }
public:
    std::vector<long long> multiply(std::vector<int>& poly1, std::vector<int>& poly2) {
        if (poly1.empty() || poly2.empty()) return {};
        int m = (int)poly1.size() + (int)poly2.size() - 1;
        int n = 1;
        while (n < m) n <<= 1;
        std::vector<cd> fa(n), fb(n);
        for (int i = 0; i < (int)poly1.size(); i++) fa[i] = poly1[i];
        for (int i = 0; i < (int)poly2.size(); i++) fb[i] = poly2[i];
        fft(fa, false);
        fft(fb, false);
        for (int i = 0; i < n; i++) fa[i] *= fb[i];
        fft(fa, true);
        std::vector<long long> res(m);
        for (int i = 0; i < m; i++) res[i] = (long long)llround(fa[i].real());
        return res;
    }
};

----- PYTHON -----
# LeetCode 3549 - Multiply Two Polynomials
# https://leetcode.com/problems/multiply-two-polynomials/

import math
from typing import List


class Complex:
    def __init__(self, re: float, im: float) -> None:
        self.re = re
        self.im = im

    def mul(self, o: "Complex") -> "Complex":
        return Complex(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def add(self, o: "Complex") -> "Complex":
        return Complex(self.re + o.re, self.im + o.im)

    def sub(self, o: "Complex") -> "Complex":
        return Complex(self.re - o.re, self.im - o.im)

    def div(self, x: float) -> "Complex":
        return Complex(self.re / x, self.im / x)


def fft(a: List[Complex], invert: bool) -> None:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while (j & bit) != 0:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        angle = 2 * math.pi / length * (-1 if invert else 1)
        wlen = Complex(math.cos(angle), math.sin(angle))
        for i in range(0, n, length):
            w = Complex(1, 0)
            half = length >> 1
            for jj in range(half):
                u = a[i + jj]
                v = a[i + jj + half].mul(w)
                a[i + jj] = u.add(v)
                a[i + jj + half] = u.sub(v)
                w = w.mul(wlen)
        length <<= 1
    if invert:
        for i in range(n):
            a[i] = a[i].div(n)


class Solution:
    def multiply(self, poly1: List[int], poly2: List[int]) -> List[int]:
        if not poly1 or not poly2:
            return []
        m = len(poly1) + len(poly2) - 1
        n = 1
        while n < m:
            n <<= 1
        fa = [Complex(0, 0) for _ in range(n)]
        fb = [Complex(0, 0) for _ in range(n)]
        for i in range(n):
            fa[i] = Complex(poly1[i] if i < len(poly1) else 0, 0)
            fb[i] = Complex(poly2[i] if i < len(poly2) else 0, 0)
        fft(fa, False)
        fft(fb, False)
        for i in range(n):
            fa[i] = fa[i].mul(fb[i])
        fft(fa, True)
        return [int(round(fa[i].re)) for i in range(m)]

================================================================================
// FOLDER: 3550_smallest_index_with_digit_sum_equal_to_index
// URL: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
// CONFIG: {"class": "Solution", "method": "smallestIndex", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=smallestIndex
// PY DEFS: ['smallestIndex']
// CPP FNS: ['smallestIndex']
================================================================================
// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

#include <vector>

class Solution {
public:
    int smallestIndex(std::vector<int>& nums) {
        for (int i = 0; i < (int)nums.size(); i++) {
            int x = nums[i], s = 0;
            for (; x > 0; x /= 10) s += x % 10;
            if (s == i) return i;
        }
        return -1;
    }
};

================================================================================
// FOLDER: 3551_minimum_swaps_to_sort_by_digit_sum
// URL: https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/
// CONFIG: {"class": "Solution", "method": "minSwaps", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minSwaps
// PY DEFS: ['f3551', 'minSwaps']
// CPP FNS: ['f', 'minSwaps', 'vis']
================================================================================
// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

#include <vector>
#include <algorithm>
#include <unordered_map>
#include <array>

class Solution {
    int f(int x) {
        int s = 0;
        while (x) { s += x % 10; x /= 10; }
        return s;
    }
public:
    int minSwaps(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<std::array<int, 2>> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {f(nums[i]), nums[i]};
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) {
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });
        std::unordered_map<int, int> d;
        for (int i = 0; i < n; i++) d[arr[i][1]] = i;
        std::vector<char> vis(n);
        int ans = n;
        for (int i = 0; i < n; i++) {
            if (!vis[i]) {
                ans--;
                int j = i;
                while (!vis[j]) {
                    vis[j] = 1;
                    j = d[nums[j]];
                }
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3552_grid_teleportation_traversal
// URL: https://leetcode.com/problems/grid-teleportation-traversal/
// CONFIG: {"class": "Solution", "method": "minMoves", "paramOrder": ["matrix"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minMoves
// PY DEFS: ['minMoves']
// CPP FNS: ['minMoves']
================================================================================
// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

#include <string>
#include <vector>
#include <deque>
#include <unordered_map>
#include <cctype>

class Solution {
public:
    int minMoves(std::vector<std::string>& matrix) {
        int m = (int)matrix.size(), n = (int)matrix[0].size();
        std::unordered_map<char, std::vector<std::pair<int, int>>> g;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (std::isalpha(matrix[i][j])) g[matrix[i][j]].push_back({i, j});
        int dirs[5] = {-1, 0, 1, 0, -1};
        const int INF = 1 << 30;
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, INF));
        dist[0][0] = 0;
        std::deque<std::pair<int, int>> q;
        q.push_back({0, 0});
        while (!q.empty()) {
            auto [i, j] = q.front(); q.pop_front();
            int d = dist[i][j];
            if (i == m - 1 && j == n - 1) return d;
            char c = matrix[i][j];
            if (g.count(c)) {
                for (auto& [x, y] : g[c]) {
                    if (d < dist[x][y]) {
                        dist[x][y] = d;
                        q.push_front({x, y});
                    }
                }
                g.erase(c);
            }
            for (int idx = 0; idx < 4; idx++) {
                int x = i + dirs[idx], y = j + dirs[idx + 1];
                if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] != '#' && d + 1 < dist[x][y]) {
                    dist[x][y] = d + 1;
                    q.push_back({x, y});
                }
            }
        }
        return -1;
    }
};

================================================================================
// FOLDER: 3553_minimum_weighted_subgraph_with_the_required_paths_ii
// URL: https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/
// CONFIG: {"class": "Solution", "method": "minimumWeight", "paramOrder": ["edges", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minimumWeight
// PY DEFS: ['minimumWeight', 'dfs', 'lca', 'path']
// CPP FNS: ['minimumWeight', 'depth', 'ans']
================================================================================
// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> minimumWeight(std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        const int LOG = 17;
        std::vector<std::vector<int>> parent(LOG, std::vector<int>(n, -1));
        std::vector<int> depth(n), dist(n);
        auto dfs = [&](auto&& self, int u, int p) -> void {
            parent[0][u] = p;
            for (auto& [to, w] : g[u]) {
                if (to == p) continue;
                depth[to] = depth[u] + 1;
                dist[to] = dist[u] + w;
                self(self, to, u);
            }
        };
        dfs(dfs, 0, -1);
        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                if (parent[k - 1][v] != -1)
                    parent[k][v] = parent[k - 1][parent[k - 1][v]];
        auto lca = [&](int u, int v) {
            if (depth[u] < depth[v]) std::swap(u, v);
            for (int k = LOG - 1; k >= 0; k--)
                if (parent[k][u] != -1 && depth[parent[k][u]] >= depth[v])
                    u = parent[k][u];
            if (u == v) return u;
            for (int k = LOG - 1; k >= 0; k--)
                if (parent[k][u] != -1 && parent[k][u] != parent[k][v]) {
                    u = parent[k][u];
                    v = parent[k][v];
                }
            return parent[0][u];
        };
        auto path = [&](int u, int v) {
            int a = lca(u, v);
            return dist[u] + dist[v] - 2 * dist[a];
        };
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int a = queries[i][0], b = queries[i][1], c = queries[i][2];
            ans[i] = (path(a, b) + path(b, c) + path(a, c)) / 2;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3555_smallest_subarray_to_sort_in_every_sliding_window
// URL: https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['f3555', 'minSubarraySort']
// CPP FNS: ['minSubarraySort']
================================================================================
// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> minSubarraySort(std::vector<int>& nums, int k) {
        const int inf = 1 << 30;
        int n = (int)nums.size();
        auto f = [&](int i, int j) {
            int mi = inf, mx = -inf, l = -1, r = -1;
            for (int p = i; p <= j; p++) {
                if (nums[p] < mx) r = p;
                else mx = nums[p];
                int q = j - p + i;
                if (nums[q] > mi) l = q;
                else mi = nums[q];
            }
            if (r == -1) return 0;
            return r - l + 1;
        };
        std::vector<int> ans;
        for (int i = 0; i <= n - k; i++) ans.push_back(f(i, i + k - 1));
        return ans;
    }
};

----- PYTHON -----
# LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
# https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

from typing import List


def f3555(nums: List[int], i: int, j: int, inf: int) -> int:
    mi, mx = inf, -inf
    l, r = -1, -1
    for p in range(i, j + 1):
        if nums[p] < mx:
            r = p
        else:
            mx = nums[p]
        q = j - p + i
        if nums[q] > mi:
            l = q
        else:
            mi = nums[q]
    if r == -1:
        return 0
    return r - l + 1


class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        inf = 1 << 30
        n = len(nums)
        return [f3555(nums, i, i + k - 1, inf) for i in range(n - k + 1)]

================================================================================
// FOLDER: 3556_sum_of_largest_prime_substrings
// URL: https://leetcode.com/problems/sum-of-largest-prime-substrings/
// CONFIG: {"class": "Solution", "method": "sumOfLargestPrimes", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=sumOfLargestPrimes
// PY DEFS: ['is_prime3556', 'sumOfLargestPrimes']
// CPP FNS: ['isPrime', 'sumOfLargestPrimes', 'nums']
================================================================================
// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <cmath>

class Solution {
    bool isPrime(long long x) {
        if (x < 2) return false;
        long long sqrtX = (long long)std::sqrt((double)x);
        for (long long i = 2; i <= sqrtX; i++) if (x % i == 0) return false;
        return true;
    }
public:
    long long sumOfLargestPrimes(std::string s) {
        std::unordered_set<long long> st;
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            long long x = 0;
            for (int j = i; j < n; j++) {
                x = x * 10 + (s[j] - '0');
                if (isPrime(x)) st.insert(x);
            }
        }
        std::vector<long long> nums(st.begin(), st.end());
        std::sort(nums.begin(), nums.end());
        long long ans = 0;
        for (int i = (int)nums.size() - 1; i >= 0 && (int)nums.size() - i <= 3; i--)
            ans += nums[i];
        return ans;
    }
};

================================================================================
// FOLDER: 3557_find_maximum_number_of_non_intersecting_substrings
// URL: https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/
// CONFIG: {"class": "Solution", "method": "maxSubstrings", "paramOrder": ["word"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxSubstrings
// PY DEFS: ['maxSubstrings']
// CPP FNS: ['maxSubstrings']
================================================================================
// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

#include <string>
#include <unordered_map>

class Solution {
public:
    int maxSubstrings(std::string word) {
        int ans = 0;
        std::unordered_map<char, int> first;
        for (int i = 0; i < (int)word.size(); i++) {
            char c = word[i];
            if (!first.count(c)) first[c] = i;
            else if (i - first[c] + 1 >= 4) {
                ans++;
                first.clear();
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3558_number_of_ways_to_assign_edge_weights_i
// URL: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/
// CONFIG: {"class": "Solution", "method": "assignEdgeWeights", "paramOrder": ["edges"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=assignEdgeWeights
// PY DEFS: ['assignEdgeWeights', 'dfs', 'pow2']
// CPP FNS: ['assignEdgeWeights']
================================================================================
// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int assignEdgeWeights(std::vector<std::vector<int>>& edges) {
        const int mod = 1000000007;
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> g(n + 1);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        auto dfs = [&](auto&& self, int i, int fa) -> int {
            int res = 0;
            for (int j : g[i]) {
                if (j != fa) res = std::max(res, self(self, j, i) + 1);
            }
            return res;
        };
        auto pow2 = [&](int exp) {
            long long a = 2, res = 1;
            while (exp > 0) {
                if (exp & 1) res = res * a % mod;
                a = a * a % mod;
                exp >>= 1;
            }
            return (int)res;
        };
        return pow2(dfs(dfs, 1, 0) - 1);
    }
};

================================================================================
// FOLDER: 3559_number_of_ways_to_assign_edge_weights_ii
// URL: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/
// CONFIG: {"class": "Solution", "method": "assignEdgeWeights", "paramOrder": ["edges", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=assignEdgeWeights
// PY DEFS: ['assignEdgeWeights', 'dfs', 'lca', 'mod_pow']
// CPP FNS: ['assignEdgeWeights', 'depth', 'ans']
================================================================================
// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> assignEdgeWeights(std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        const int MOD = 1000000007;
        const int LOG = 17;
        int n = (int)edges.size() + 1;
        std::vector<int> depth(n + 1);
        std::vector<std::vector<int>> graph(n + 1);
        std::vector<std::vector<int>> parent(LOG, std::vector<int>(n + 1, -1));
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        auto dfs = [&](auto&& self, int u, int p) -> void {
            parent[0][u] = p;
            for (int v : graph[u]) {
                if (v != p) {
                    depth[v] = depth[u] + 1;
                    self(self, v, u);
                }
            }
        };
        dfs(dfs, 1, -1);
        for (int k = 1; k < LOG; k++) {
            for (int v = 1; v <= n; v++) {
                if (parent[k - 1][v] != -1) parent[k][v] = parent[k - 1][parent[k - 1][v]];
            }
        }
        auto lca = [&](int u, int v) {
            if (depth[u] < depth[v]) std::swap(u, v);
            for (int k = LOG - 1; k >= 0; k--) {
                if (parent[k][u] != -1 && depth[parent[k][u]] >= depth[v]) u = parent[k][u];
            }
            if (u == v) return u;
            for (int k = LOG - 1; k >= 0; k--) {
                if (parent[k][u] != -1 && parent[k][u] != parent[k][v]) {
                    u = parent[k][u];
                    v = parent[k][v];
                }
            }
            return parent[0][u];
        };
        auto modPow = [&](int exp) {
            long long base = 2, res = 1;
            while (exp > 0) {
                if (exp & 1) res = res * base % MOD;
                base = base * base % MOD;
                exp >>= 1;
            }
            return (int)res;
        };
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) {
                ans[i] = 0;
                continue;
            }
            int a = lca(u, v);
            int d = depth[u] + depth[v] - 2 * depth[a];
            ans[i] = modPow(d - 1);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3560_find_minimum_log_transportation_cost
// URL: https://leetcode.com/problems/find-minimum-log-transportation-cost/
// CONFIG: {"class": "Solution", "method": "minCuttingCost", "paramOrder": ["n", "m", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minCuttingCost
// PY DEFS: ['minCuttingCost']
// CPP FNS: ['minCuttingCost']
================================================================================
// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

#include <algorithm>

class Solution {
public:
    long long minCuttingCost(int n, int m, int k) {
        int x = std::max(n, m);
        if (x <= k) return 0;
        return 1LL * k * (x - k);
    }
};

================================================================================
// FOLDER: 3561_resulting_string_after_adjacent_removals
// URL: https://leetcode.com/problems/resulting-string-after-adjacent-removals/
// CONFIG: {"class": "Solution", "method": "resultingString", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=resultingString
// PY DEFS: ['is_contiguous', 'resultingString']
// CPP FNS: ['resultingString']
================================================================================
// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

#include <cmath>
#include <string>

class Solution {
public:
    std::string resultingString(std::string s) {
        auto isContiguous = [](char a, char b) {
            int x = std::abs(a - b);
            return x == 1 || x == 25;
        };
        std::string stk;
        for (char c : s) {
            if (!stk.empty() && isContiguous(stk.back(), c)) stk.pop_back();
            else stk.push_back(c);
        }
        return stk;
    }
};

================================================================================
// FOLDER: 3562_maximum_profit_from_trading_stocks_with_discounts
// URL: https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/
// CONFIG: {"class": "Solution", "method": "maxProfit", "paramOrder": ["n", "present", "future", "hierarchy", "budget"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxProfit
// PY DEFS: ['maxProfit', 'dfs']
// CPP FNS: ['maxProfit']
================================================================================
// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

#include <algorithm>
#include <array>
#include <vector>

class Solution {
public:
    int maxProfit(int n, std::vector<int>& present, std::vector<int>& future,
                  std::vector<std::vector<int>>& hierarchy, int budget) {
        std::vector<std::vector<int>> g(n + 1);
        for (auto& e : hierarchy) g[e[0]].push_back(e[1]);

        auto dfs = [&](auto&& self, int u) -> std::vector<std::array<int, 2>> {
            std::vector<std::array<int, 2>> nxt(budget + 1);
            for (int v : g[u]) {
                auto fv = self(self, v);
                for (int j = budget; j >= 0; j--) {
                    for (int jv = 0; jv <= j; jv++) {
                        for (int pre = 0; pre < 2; pre++) {
                            nxt[j][pre] = std::max(nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre]);
                        }
                    }
                }
            }
            std::vector<std::array<int, 2>> f(budget + 1);
            int price = future[u - 1];
            for (int j = 0; j <= budget; j++) {
                for (int pre = 0; pre < 2; pre++) {
                    int cost = present[u - 1] / (pre + 1);
                    if (j >= cost) {
                        int buyProfit = nxt[j - cost][1] + (price - cost);
                        f[j][pre] = std::max(nxt[j][0], buyProfit);
                    } else {
                        f[j][pre] = nxt[j][0];
                    }
                }
            }
            return f;
        };
        return dfs(dfs, 1)[budget][0];
    }
};

================================================================================
// FOLDER: 3563_lexicographically_smallest_string_after_adjacent_removals
// URL: https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/
// CONFIG: {"class": "Solution", "method": "lexicographicallySmallestString", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=lexicographicallySmallestString
// PY DEFS: ['is_consec3563', 'lexicographicallySmallestString']
// CPP FNS: ['lexicographicallySmallestString']
================================================================================
// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

#include <cmath>
#include <string>
#include <vector>

class Solution {
public:
    std::string lexicographicallySmallestString(std::string s) {
        int n = (int)s.size();
        std::vector<std::vector<std::string>> dp(n + 1, std::vector<std::string>(n + 1));
        auto isConsec = [](char a, char b) {
            int d = std::abs(a - b);
            return d == 1 || d == 25;
        };
        for (int length = 1; length <= n; length++) {
            for (int i = 0; i + length <= n; i++) {
                int j = i + length;
                std::string minStr = std::string(1, s[i]) + dp[i + 1][j];
                for (int k = i + 1; k < j; k++) {
                    if (isConsec(s[i], s[k]) && dp[i + 1][k].empty()) {
                        const std::string& cand = dp[k + 1][j];
                        if (cand < minStr) minStr = cand;
                    }
                }
                dp[i][j] = minStr;
            }
        }
        return dp[0][n];
    }
};

================================================================================
// FOLDER: 3565_sequential_grid_path_cover
// URL: https://leetcode.com/problems/sequential-grid-path-cover/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["grid", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['findPath', 'f', 'dfs']
// CPP FNS: []
================================================================================
// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findPath(std::vector<std::vector<int>>& grid, int k) {
        (void)k;
        int m = (int)grid.size(), n = (int)grid[0].size();
        uint64_t st = 0;
        std::vector<std::vector<int>> path;
        int dirs[5] = {-1, 0, 1, 0, -1};
        auto f = [&](int i, int j) { return i * n + j; };

        auto dfs = [&](auto&& self, int i, int j, int v) -> bool {
            path.push_back({i, j});
            if ((int)path.size() == m * n) return true;
            int idx = f(i, j);
            st |= 1ULL << idx;
            if (grid[i][j] == v) v++;
            for (int t = 0; t < 4; t++) {
                int x = i + dirs[t], y = j + dirs[t + 1];
                if (0 <= x && x < m && 0 <= y && y < n) {
                    int idx2 = f(x, y);
                    if (((st >> idx2) & 1ULL) == 0 && (grid[x][y] == 0 || grid[x][y] == v)) {
                        if (self(self, x, y, v)) return true;
                    }
                }
            }
            path.pop_back();
            st ^= 1ULL << idx;
            return false;
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 || grid[i][j] == 1) {
                    if (dfs(dfs, i, j, 1)) return path;
                    path.clear();
                    st = 0;
                }
            }
        }
        return {};
    }
};

----- PYTHON -----
# LeetCode 3565 - Sequential Grid Path Cover
# https://leetcode.com/problems/sequential-grid-path-cover/

from typing import List


class Solution:
    def findPath(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dirs = [-1, 0, 1, 0, -1]
        st = 0
        path = []

        def f(i: int, j: int) -> int:
            return i * n + j

        def dfs(i: int, j: int, v: int) -> bool:
            nonlocal st
            path.append([i, j])
            if len(path) == m * n:
                return True
            idx = f(i, j)
            st |= 1 << idx
            if grid[i][j] == v:
                v += 1
            for t in range(4):
                x, y = i + dirs[t], j + dirs[t + 1]
                if 0 <= x < m and 0 <= y < n:
                    idx2 = f(x, y)
                    if ((st >> idx2) & 1) == 0 and (grid[x][y] == 0 or grid[x][y] == v):
                        if dfs(x, y, v):
                            return True
            path.pop()
            st ^= 1 << idx
            return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == 1:
                    if dfs(i, j, 1):
                        return path
                    path.clear()
                    st = 0
        return []

================================================================================
// FOLDER: 3566_partition_array_into_two_equal_product_subsets
// URL: https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/
// CONFIG: {"class": "Solution", "method": "checkEqualPartitions", "paramOrder": ["nums", "target"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=checkEqualPartitions
// PY DEFS: ['checkEqualPartitions']
// CPP FNS: ['checkEqualPartitions']
================================================================================
// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

#include <vector>

class Solution {
public:
    bool checkEqualPartitions(std::vector<int>& nums, long long target) {
        int n = (int)nums.size();
        for (int i = 0; i < (1 << n); i++) {
            long long x = 1, y = 1;
            for (int j = 0; j < n; j++) {
                if ((i >> j) & 1) x *= nums[j];
                else y *= nums[j];
                if (x > target || y > target) break;
            }
            if (x == target && y == target) return true;
        }
        return false;
    }
};

================================================================================
// FOLDER: 3567_minimum_absolute_difference_in_sliding_submatrix
// URL: https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/
// CONFIG: {"class": "Solution", "method": "minAbsDiff", "paramOrder": ["grid", "k"], "types": {"return": "integer[][]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minAbsDiff
// PY DEFS: ['minAbsDiff']
// CPP FNS: []
================================================================================
// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

#include <algorithm>
#include <climits>
#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> minAbsDiff(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> ans(m - k + 1, std::vector<int>(n - k + 1));
        for (int i = 0; i <= m - k; i++) {
            for (int j = 0; j <= n - k; j++) {
                std::vector<int> nums;
                for (int x = i; x < i + k; x++)
                    for (int y = j; y < j + k; y++) nums.push_back(grid[x][y]);
                std::sort(nums.begin(), nums.end());
                int d = INT_MAX;
                for (int t = 1; t < (int)nums.size(); t++) {
                    if (nums[t] != nums[t - 1]) d = std::min(d, std::abs(nums[t] - nums[t - 1]));
                }
                if (d != INT_MAX) ans[i][j] = d;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3568_minimum_moves_to_clean_the_classroom
// URL: https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/
// CONFIG: {"class": "Solution", "method": "minMoves", "paramOrder": ["classroom", "energy"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minMoves
// PY DEFS: ['minMoves']
// CPP FNS: ['minMoves']
================================================================================
// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

#include <string>
#include <vector>

class Solution {
public:
    int minMoves(std::vector<std::string>& classroom, int energy) {
        int m = (int)classroom.size(), n = (int)classroom[0].size();
        std::vector<std::vector<int>> d(m, std::vector<int>(n));
        int x = 0, y = 0, cnt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = classroom[i][j];
                if (c == 'S') {
                    x = i;
                    y = j;
                } else if (c == 'L') {
                    d[i][j] = cnt++;
                }
            }
        }
        if (cnt == 0) return 0;

        std::vector<std::vector<std::vector<std::vector<bool>>>> vis(
            m, std::vector<std::vector<std::vector<bool>>>(
                   n, std::vector<std::vector<bool>>(energy + 1, std::vector<bool>(1 << cnt, false))));
        struct State {
            int i, j, curEnergy, mask;
        };
        std::vector<State> q{{x, y, energy, (1 << cnt) - 1}};
        vis[x][y][energy][(1 << cnt) - 1] = true;
        int dirs[5] = {-1, 0, 1, 0, -1};
        int ans = 0;
        while (!q.empty()) {
            std::vector<State> t = q;
            q.clear();
            for (auto& s : t) {
                int i = s.i, j = s.j, curEnergy = s.curEnergy, mask = s.mask;
                if (mask == 0) return ans;
                if (curEnergy <= 0) continue;
                for (int k = 0; k < 4; k++) {
                    int nx = i + dirs[k], ny = j + dirs[k + 1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && classroom[nx][ny] != 'X') {
                        int nxtEnergy = classroom[nx][ny] == 'R' ? energy : curEnergy - 1;
                        int nxtMask = mask;
                        if (classroom[nx][ny] == 'L') nxtMask &= ~(1 << d[nx][ny]);
                        if (!vis[nx][ny][nxtEnergy][nxtMask]) {
                            vis[nx][ny][nxtEnergy][nxtMask] = true;
                            q.push_back({nx, ny, nxtEnergy, nxtMask});
                        }
                    }
                }
            }
            ans++;
        }
        return -1;
    }
};

================================================================================
// FOLDER: 3569_maximize_count_of_distinct_primes_after_split
// URL: https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/
// CONFIG: {"class": "Solution", "method": "maximumCount", "paramOrder": ["nums", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maximumCount
// PY DEFS: ['maximumCount']
// CPP FNS: ['maximumCount', 'isP', 'ans']
================================================================================
// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> maximumCount(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int mx = 0;
        for (int v : nums) mx = std::max(mx, v);
        for (auto& q : queries) mx = std::max(mx, q[1]);
        std::vector<bool> isP(mx + 1, false);
        for (int i = 2; i <= mx; i++) isP[i] = true;
        for (int i = 2; i * i <= mx; i++) {
            if (isP[i]) {
                for (int j = i * i; j <= mx; j += i) isP[j] = false;
            }
        }
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            nums[queries[qi][0]] = queries[qi][1];
            int best = 0;
            std::unordered_map<int, int> left, right;
            for (int v : nums) {
                if (v <= mx && isP[v]) right[v]++;
            }
            for (int i = 0; i < (int)nums.size() - 1; i++) {
                int v = nums[i];
                if (v <= mx && isP[v]) {
                    left[v]++;
                    if (--right[v] == 0) right.erase(v);
                }
                best = std::max(best, (int)left.size() + (int)right.size());
            }
            ans[qi] = best;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3571_find_the_shortest_superstring_ii
// URL: https://leetcode.com/problems/find-the-shortest-superstring-ii/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["s1", "s2"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['shortestSuperstring']
// CPP FNS: ['shortestSuperstring']
================================================================================
// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

#include <string>

class Solution {
public:
    std::string shortestSuperstring(std::string s1, std::string s2) {
        if (s1.size() > s2.size()) return shortestSuperstring(s2, s1);
        int m = (int)s1.size();
        if (s2.find(s1) != std::string::npos) return s2;
        for (int i = 0; i < m; i++) {
            if (s2.rfind(s1.substr(i), 0) == 0) return s1.substr(0, i) + s2;
            if (s2.size() >= (size_t)(m - i) && s2.compare(s2.size() - (m - i), m - i, s1, 0, m - i) == 0)
                return s2 + s1.substr(m - i);
        }
        return s1 + s2;
    }
};

----- PYTHON -----
# LeetCode 3571 - Find the Shortest Superstring II
# https://leetcode.com/problems/find-the-shortest-superstring-ii/


class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        if len(s1) > len(s2):
            return self.shortestSuperstring(s2, s1)
        m = len(s1)
        if s1 in s2:
            return s2
        for i in range(m):
            if s2.startswith(s1[i:]):
                return s1[:i] + s2
            length = m - i
            if len(s2) >= length and s2[-length:] == s1[:length]:
                return s2 + s1[m - i :]
        return s1 + s2

================================================================================
// FOLDER: 3572_maximize_ysum_by_picking_a_triplet_of_distinct_xvalues
// URL: https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/
// CONFIG: {"class": "Solution", "method": "maxSumDistinctTriplet", "paramOrder": ["x", "y"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxSumDistinctTriplet
// PY DEFS: ['maxSumDistinctTriplet']
// CPP FNS: ['maxSumDistinctTriplet']
================================================================================
// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxSumDistinctTriplet(std::vector<int>& x, std::vector<int>& y) {
        int n = (int)x.size();
        std::vector<std::pair<int, int>> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {x[i], y[i]};
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.second > b.second; });
        int ans = 0;
        std::unordered_set<int> vis;
        for (int i = 0; i < n; i++) {
            int a = arr[i].first, b = arr[i].second;
            if (!vis.count(a)) {
                vis.insert(a);
                ans += b;
                if ((int)vis.size() == 3) return ans;
            }
        }
        return -1;
    }
};

================================================================================
// FOLDER: 3573_best_time_to_buy_and_sell_stock_v
// URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/
// CONFIG: {"class": "Solution", "method": "maximumProfit", "paramOrder": ["prices", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maximumProfit
// PY DEFS: ['maximumProfit']
// CPP FNS: ['maximumProfit']
================================================================================
// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

#include <algorithm>
#include <array>
#include <vector>

class Solution {
public:
    long long maximumProfit(std::vector<int>& prices, int k) {
        int n = (int)prices.size();
        std::vector<std::vector<std::array<long long, 3>>> f(n, std::vector<std::array<long long, 3>>(k + 1));
        for (int j = 1; j <= k; j++) {
            f[0][j][1] = -prices[0];
            f[0][j][2] = prices[0];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                f[i][j][0] = std::max({f[i - 1][j][0], f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]});
                f[i][j][1] = std::max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i]);
                f[i][j][2] = std::max(f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i]);
            }
        }
        return f[n - 1][k][0];
    }
};

================================================================================
// FOLDER: 3574_maximize_subarray_gcd_score
// URL: https://leetcode.com/problems/maximize-subarray-gcd-score/
// CONFIG: {"class": "Solution", "method": "maxGCDScore", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxGCDScore
// PY DEFS: ['gcd3574', 'maxGCDScore']
// CPP FNS: ['maxGCDScore', 'cnt']
================================================================================
// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

#include <algorithm>
#include <climits>
#include <numeric>
#include <vector>

class Solution {
public:
    long long maxGCDScore(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> cnt(n);
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x % 2 == 0) {
                cnt[i]++;
                x /= 2;
            }
        }
        long long ans = 0;
        for (int l = 0; l < n; l++) {
            int g = 0, mi = INT_MAX, t = 0;
            for (int r = l; r < n; r++) {
                g = std::gcd(g, nums[r]);
                if (cnt[r] < mi) {
                    mi = cnt[r];
                    t = 1;
                } else if (cnt[r] == mi) {
                    t++;
                }
                long long score = 1LL * g * (r - l + 1);
                if (t <= k) score *= 2;
                ans = std::max(ans, score);
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3575_maximum_good_subtree_score
// URL: https://leetcode.com/problems/maximum-good-subtree-score/
// CONFIG: {"class": "Solution", "method": "goodSubtreeSum", "paramOrder": ["vals", "par"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=goodSubtreeSum
// PY DEFS: ['goodSubtreeSum', 'digit_mask', 'dfs']
// CPP FNS: ['goodSubtreeSum']
================================================================================
// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int goodSubtreeSum(std::vector<int>& vals, std::vector<int>& par) {
        const int MOD = 1000000007;
        int n = (int)vals.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[par[i]].push_back(i);
        int ans = 0;
        auto digitMask = [](int x) -> std::tuple<int, bool, int> {
            int v = x, mask = 0;
            if (x == 0) return {1, true, 0};
            while (x > 0) {
                int d = x % 10;
                if (mask & (1 << d)) return {0, false, 0};
                mask |= 1 << d;
                x /= 10;
            }
            return {mask, true, v};
        };
        auto dfs = [&](auto&& self, int u) -> std::unordered_map<int, int> {
            std::unordered_map<int, int> dp{{0, 0}};
            auto [mask, ok, v] = digitMask(vals[u]);
            if (ok) dp[mask] = v;
            for (int c : g[u]) {
                auto child = self(self, c);
                std::unordered_map<int, int> ndp;
                for (auto& [m1, s1] : dp) {
                    for (auto& [m2, s2] : child) {
                        if ((m1 & m2) == 0) {
                            int nm = m1 | m2;
                            ndp[nm] = std::max(ndp[nm], s1 + s2);
                        }
                    }
                }
                for (auto& [m, s] : dp) ndp[m] = std::max(ndp[m], s);
                for (auto& [m, s] : child) ndp[m] = std::max(ndp[m], s);
                dp = std::move(ndp);
            }
            int best = 0;
            for (auto& [_, s] : dp) best = std::max(best, s);
            ans = (ans + best) % MOD;
            return dp;
        };
        dfs(dfs, 0);
        return ans;
    }
};

================================================================================
// FOLDER: 3576_transform_array_to_all_equal_elements
// URL: https://leetcode.com/problems/transform-array-to-all-equal-elements/
// CONFIG: {"class": "Solution", "method": "canMakeEqual", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=canMakeEqual
// PY DEFS: ['check3576', 'canMakeEqual']
// CPP FNS: ['canMakeEqual']
================================================================================
// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

#include <vector>

class Solution {
public:
    bool canMakeEqual(std::vector<int>& nums, int k) {
        auto check = [&](int target, int kk) {
            int cnt = 0, sign = 1;
            for (int i = 0; i < (int)nums.size() - 1; i++) {
                int x = nums[i] * sign;
                if (x == target) sign = 1;
                else {
                    sign = -1;
                    cnt++;
                }
            }
            return cnt <= kk && nums.back() * sign == target;
        };
        return check(nums[0], k) || check(-nums[0], k);
    }
};

================================================================================
// FOLDER: 3577_count_the_number_of_computer_unlocking_permutations
// URL: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
// CONFIG: {"class": "Solution", "method": "countPermutations", "paramOrder": ["complexity"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=countPermutations
// PY DEFS: ['countPermutations']
// CPP FNS: ['countPermutations']
================================================================================
// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

#include <vector>

class Solution {
public:
    int countPermutations(std::vector<int>& complexity) {
        const long long mod = 1000000007;
        long long ans = 1;
        for (int i = 1; i < (int)complexity.size(); i++) {
            if (complexity[i] <= complexity[0]) return 0;
            ans = ans * i % mod;
        }
        return (int)ans;
    }
};

================================================================================
// FOLDER: 3578_count_partitions_with_max_min_difference_at_most_k
// URL: https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/
// CONFIG: {"class": "Solution", "method": "countPartitions", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=countPartitions
// PY DEFS: ['countPartitions', 'add', 'rem']
// CPP FNS: ['countPartitions', 'f']
================================================================================
// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

#include <set>
#include <vector>

class Solution {
public:
    int countPartitions(std::vector<int>& nums, int k) {
        const int mod = 1000000007;
        std::multiset<int> sl;
        int n = (int)nums.size();
        std::vector<int> f(n + 1), g(n + 1);
        f[0] = g[0] = 1;
        for (int l = 1, r = 1; r <= n; r++) {
            sl.insert(nums[r - 1]);
            while (*sl.rbegin() - *sl.begin() > k) {
                sl.erase(sl.find(nums[l - 1]));
                l++;
            }
            f[r] = g[r - 1];
            if (l >= 2) f[r] = (f[r] - g[l - 2] + mod) % mod;
            g[r] = (g[r - 1] + f[r]) % mod;
        }
        return f[n];
    }
};

================================================================================
// FOLDER: 3579_minimum_steps_to_convert_string_with_operations
// URL: https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/
// CONFIG: {"class": "Solution", "method": "minOperations", "paramOrder": ["word1", "word2"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minOperations
// PY DEFS: ['minOperations', 'calc']
// CPP FNS: ['minOperations', 'f']
================================================================================
// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

#include <algorithm>
#include <climits>
#include <string>
#include <vector>

class Solution {
public:
    int minOperations(std::string word1, std::string word2) {
        int n = (int)word1.size();
        std::vector<int> f(n + 1, INT_MAX / 2);
        f[0] = 0;
        auto calc = [&](int l, int r, bool rev) {
            int cnt[26][26] = {};
            int res = 0;
            for (int i = l; i <= r; i++) {
                int j = rev ? r - (i - l) : i;
                int a = word1[j] - 'a';
                int b = word2[i] - 'a';
                if (a != b) {
                    if (cnt[b][a] > 0) cnt[b][a]--;
                    else {
                        cnt[a][b]++;
                        res++;
                    }
                }
            }
            return res;
        };
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int a = calc(j, i - 1, false);
                int b = 1 + calc(j, i - 1, true);
                f[i] = std::min(f[i], f[j] + std::min(a, b));
            }
        }
        return f[n];
    }
};

================================================================================
// FOLDER: 3581_count_odd_letters_from_number
// URL: https://leetcode.com/problems/count-odd-letters-from-number/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["n"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['countOddLetters']
// CPP FNS: ['countOddLetters']
================================================================================
// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

#include <string>
#include <unordered_map>

class Solution {
public:
    int countOddLetters(int n) {
        static const std::unordered_map<int, std::string> d = {
            {0, "zero"}, {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"},
            {5, "five"}, {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"},
        };
        unsigned mask = 0;
        while (n > 0) {
            int x = n % 10;
            n /= 10;
            for (char c : d.at(x)) mask ^= 1u << (c - 'a');
        }
        return __builtin_popcount(mask);
    }
};

----- PYTHON -----
# LeetCode 3581 - Count Odd Letters from Number
# https://leetcode.com/problems/count-odd-letters-from-number/


class Solution:
    def countOddLetters(self, n: int) -> int:
        d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        mask = 0
        while n > 0:
            for c in d[n % 10]:
                mask ^= 1 << (ord(c) - 97)
            n //= 10
        cnt = 0
        while mask:
            cnt += mask & 1
            mask >>= 1
        return cnt

================================================================================
// FOLDER: 3582_generate_tag_for_video_caption
// URL: https://leetcode.com/problems/generate-tag-for-video-caption/
// CONFIG: {"class": "Solution", "method": "generateTag", "paramOrder": ["caption"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=generateTag
// PY DEFS: ['generateTag']
// CPP FNS: ['generateTag']
================================================================================
// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

#include <cctype>
#include <sstream>
#include <string>

class Solution {
public:
    std::string generateTag(std::string caption) {
        std::istringstream iss(caption);
        std::string word, ans = "#";
        int i = 0;
        while (iss >> word) {
            for (char& c : word) c = (char)std::tolower((unsigned char)c);
            if (i == 0) ans += word;
            else {
                if (!word.empty()) word[0] = (char)std::toupper((unsigned char)word[0]);
                ans += word;
            }
            if ((int)ans.size() >= 100) break;
            i++;
        }
        if ((int)ans.size() > 100) ans.resize(100);
        return ans;
    }
};

================================================================================
// FOLDER: 3583_count_special_triplets
// URL: https://leetcode.com/problems/count-special-triplets/
// CONFIG: {"class": "Solution", "method": "specialTriplets", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=specialTriplets
// PY DEFS: ['specialTriplets']
// CPP FNS: ['specialTriplets']
================================================================================
// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int specialTriplets(std::vector<int>& nums) {
        std::unordered_map<int, int> left, right;
        for (int x : nums) right[x]++;
        long long ans = 0, mod = 1000000007;
        for (int x : nums) {
            right[x]--;
            ans = (ans + 1LL * left[x * 2] * right[x * 2] % mod) % mod;
            left[x]++;
        }
        return (int)ans;
    }
};

================================================================================
// FOLDER: 3584_maximum_product_of_first_and_last_elements_of_a_subsequence
// URL: https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/
// CONFIG: {"class": "Solution", "method": "maximumProduct", "paramOrder": ["nums", "m"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maximumProduct
// PY DEFS: ['maximumProduct']
// CPP FNS: ['maximumProduct']
================================================================================
// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long maximumProduct(std::vector<int>& nums, int m) {
        long long ans = LLONG_MIN;
        int mx = INT_MIN, mi = INT_MAX;
        for (int i = m - 1; i < (int)nums.size(); i++) {
            int x = nums[i], y = nums[i - m + 1];
            mi = std::min(mi, y);
            mx = std::max(mx, y);
            ans = std::max(ans, std::max(1LL * x * mi, 1LL * x * mx));
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3585_find_weighted_median_node_in_tree
// URL: https://leetcode.com/problems/find-weighted-median-node-in-tree/
// CONFIG: {"class": "Solution", "method": "findMedian", "paramOrder": ["n", "edges", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=findMedian
// PY DEFS: ['findMedian']
// CPP FNS: ['findMedian', 'ans', 'parent']
================================================================================
// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> findMedian(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        struct Edge { int to, w; };
        std::vector<std::vector<Edge>> g(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int u = queries[qi][0], v = queries[qi][1];
            std::vector<int> parent(n, -2), pw(n);
            parent[u] = -1;
            std::queue<int> q;
            q.push(u);
            while (!q.empty()) {
                int x = q.front();
                q.pop();
                if (x == v) break;
                for (auto& e : g[x]) {
                    if (parent[e.to] == -2) {
                        parent[e.to] = x;
                        pw[e.to] = e.w;
                        q.push(e.to);
                    }
                }
            }
            std::vector<int> nodes{v}, weights;
            int cur = v;
            while (cur != u) {
                weights.push_back(pw[cur]);
                cur = parent[cur];
                nodes.push_back(cur);
            }
            std::reverse(nodes.begin(), nodes.end());
            std::reverse(weights.begin(), weights.end());
            int total = 0;
            for (int w : weights) total += w;
            int need = (total + 1) / 2, sum = 0, med = u;
            for (int i = 0; i < (int)weights.size(); i++) {
                sum += weights[i];
                med = nodes[i + 1];
                if (sum >= need) break;
            }
            ans[qi] = med;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3587_minimum_adjacent_swaps_to_alternate_parity
// URL: https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/
// CONFIG: {"class": "Solution", "method": "minSwaps", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minSwaps
// PY DEFS: ['calc3587', 'minSwaps']
// CPP FNS: ['minSwaps']
================================================================================
// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    int minSwaps(std::vector<int>& nums) {
        std::vector<int> pos[2];
        for (int i = 0; i < (int)nums.size(); i++) pos[nums[i] & 1].push_back(i);
        if (std::abs((int)pos[0].size() - (int)pos[1].size()) > 1) return -1;
        auto calc = [&](int k) {
            int res = 0;
            for (int i = 0; i < (int)nums.size(); i += 2) res += std::abs(pos[k][i / 2] - i);
            return res;
        };
        if (pos[0].size() > pos[1].size()) return calc(0);
        if (pos[0].size() < pos[1].size()) return calc(1);
        return std::min(calc(0), calc(1));
    }
};

================================================================================
// FOLDER: 3588_find_maximum_area_of_a_triangle
// URL: https://leetcode.com/problems/find-maximum-area-of-a-triangle/
// CONFIG: {"class": "Solution", "method": "maxArea", "paramOrder": ["coords"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxArea
// PY DEFS: ['calc3588', 'maxArea']
// CPP FNS: ['maxArea']
================================================================================
// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maxArea(std::vector<std::vector<int>>& coords) {
        auto calc = [&]() -> long long {
            int mn = 1e9, mx = 0;
            std::unordered_map<int, int> f, g;
            for (auto& c : coords) {
                int x = c[0], y = c[1];
                mn = std::min(mn, x);
                mx = std::max(mx, x);
                if (f.count(x)) {
                    f[x] = std::min(f[x], y);
                    g[x] = std::max(g[x], y);
                } else {
                    f[x] = y;
                    g[x] = y;
                }
            }
            long long ans = 0;
            for (auto& [x, y] : f) {
                int d = g[x] - y;
                ans = std::max(ans, 1LL * d * std::max(mx - x, x - mn));
            }
            return ans;
        };
        long long ans = calc();
        for (auto& c : coords) std::swap(c[0], c[1]);
        ans = std::max(ans, calc());
        return ans > 0 ? ans : -1;
    }
};

================================================================================
// FOLDER: 3589_count_prime_gap_balanced_subarrays
// URL: https://leetcode.com/problems/count-prime-gap-balanced-subarrays/
// CONFIG: {"class": "Solution", "method": "primeSubarray", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=primeSubarray
// PY DEFS: ['primeSubarray']
// CPP FNS: ['primeSubarray', 'isPrime']
================================================================================
// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    int primeSubarray(std::vector<int>& nums, int k) {
        int mx = 0;
        for (int v : nums) mx = std::max(mx, v);
        std::vector<bool> isPrime(mx + 1, false);
        for (int i = 2; i <= mx; i++) isPrime[i] = true;
        for (int i = 2; i * i <= mx; i++)
            if (isPrime[i])
                for (int j = i * i; j <= mx; j += i) isPrime[j] = false;
        int n = (int)nums.size(), ans = 0;
        for (int l = 0; l < n; l++) {
            std::vector<int> primes;
            for (int r = l; r < n; r++) {
                if (isPrime[nums[r]]) primes.push_back(nums[r]);
                if ((int)primes.size() >= 2) {
                    int mn = primes[0], mxp = primes[0];
                    for (int p : primes) {
                        mn = std::min(mn, p);
                        mxp = std::max(mxp, p);
                    }
                    if (mxp - mn <= k) ans++;
                }
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3590_kth_smallest_path_xor_sum
// URL: https://leetcode.com/problems/kth-smallest-path-xor-sum/
// CONFIG: {"class": "Solution", "method": "kthSmallest", "paramOrder": ["par", "vals", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=kthSmallest
// PY DEFS: ['kthSmallest', 'dfs', 'dfs2']
// CPP FNS: ['kthSmallest', 'xorPath', 'inT', 'ans', 'sub']
================================================================================
// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> kthSmallest(std::vector<int>& par, std::vector<int>& vals, std::vector<std::vector<int>>& queries) {
        int n = (int)par.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[par[i]].push_back(i);
        std::vector<int> xorPath(n);
        auto dfs = [&](auto&& self, int u) -> void {
            xorPath[u] ^= vals[u];
            for (int v : g[u]) {
                xorPath[v] = xorPath[u];
                self(self, v);
            }
        };
        dfs(dfs, 0);
        std::vector<int> inT(n), outT(n), order;
        auto dfs2 = [&](auto&& self, int u) -> void {
            inT[u] = (int)order.size();
            order.push_back(xorPath[u]);
            for (int v : g[u]) self(self, v);
            outT[u] = (int)order.size();
        };
        dfs2(dfs2, 0);
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int u = queries[i][0], k = queries[i][1];
            std::vector<int> sub(order.begin() + inT[u], order.begin() + outT[u]);
            std::sort(sub.begin(), sub.end());
            sub.erase(std::unique(sub.begin(), sub.end()), sub.end());
            ans[i] = k > (int)sub.size() ? -1 : sub[k - 1];
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3591_check_if_any_element_has_prime_frequency
// URL: https://leetcode.com/problems/check-if-any-element-has-prime-frequency/
// CONFIG: {"class": "Solution", "method": "checkPrimeFrequency", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=checkPrimeFrequency
// PY DEFS: ['is_prime3591', 'checkPrimeFrequency']
// CPP FNS: ['isPrime', 'checkPrimeFrequency']
================================================================================
// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

#include <unordered_map>
#include <vector>

class Solution {
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++)
            if (x % i == 0) return false;
        return true;
    }

public:
    bool checkPrimeFrequency(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        for (auto& [_, c] : cnt)
            if (isPrime(c)) return true;
        return false;
    }
};

================================================================================
// FOLDER: 3592_inverse_coin_change
// URL: https://leetcode.com/problems/inverse-coin-change/
// CONFIG: {"class": "Solution", "method": "findCoins", "paramOrder": ["numWays"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=findCoins
// PY DEFS: ['findCoins']
// CPP FNS: ['findCoins', 'dp']
================================================================================
// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

#include <vector>

class Solution {
public:
    std::vector<int> findCoins(std::vector<int>& numWays) {
        int n = (int)numWays.size();
        std::vector<int> dp(n + 1), coins;
        dp[0] = 1;
        for (int amt = 1; amt <= n; amt++) {
            int ways = numWays[amt - 1];
            if (dp[amt] == ways) continue;
            if (dp[amt] + 1 == ways) {
                coins.push_back(amt);
                for (int x = amt; x <= n; x++) dp[x] += dp[x - amt];
                if (dp[amt] != ways) return {};
                continue;
            }
            return {};
        }
        return coins;
    }
};

================================================================================
// FOLDER: 3593_minimum_increments_to_equalize_leaf_paths
// URL: https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/
// CONFIG: {"class": "Solution", "method": "minIncrease", "paramOrder": ["n", "edges", "cost"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minIncrease
// PY DEFS: ['minIncrease', 'dfs']
// CPP FNS: ['minIncrease']
================================================================================
// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minIncrease(int n, std::vector<std::vector<int>>& edges, std::vector<int>& cost) {
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        int ans = 0;
        auto dfs = [&](auto&& self, int u, int p) -> long long {
            if ((int)graph[u].size() == 1 && p != -1) return cost[u];
            std::vector<long long> childVals;
            for (int v : graph[u]) {
                if (v == p) continue;
                childVals.push_back(self(self, v, u));
            }
            if (childVals.empty()) return cost[u];
            long long mx = 0;
            for (long long c : childVals) mx = std::max(mx, c);
            for (long long c : childVals)
                if (c < mx) ans++;
            return mx + cost[u];
        };
        dfs(dfs, 0, -1);
        return ans;
    }
};

================================================================================
// FOLDER: 3594_minimum_time_to_transport_all_individuals
// URL: https://leetcode.com/problems/minimum-time-to-transport-all-individuals/
// CONFIG: {"class": "Solution", "method": "minTime", "paramOrder": ["n", "k", "m", "time", "mul"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minTime
// PY DEFS: ['minTime']
// CPP FNS: ['minTime']
================================================================================
// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

#include <algorithm>
#include <vector>

class Solution {
public:
    double minTime(int n, int k, int m, std::vector<int>& time, std::vector<double>& mul) {
        std::vector<int> t = time;
        std::sort(t.begin(), t.end());
        double total = 0;
        int stage = 0, left = n;
        while (left > 0) {
            int take = std::min(k, left);
            int slow = t[left - 1];
            total += (double)slow * mul[stage % m];
            left -= take;
            stage++;
            if (left > 0) {
                total += (double)t[0] * mul[stage % m];
                stage++;
            }
        }
        return total;
    }
};

================================================================================
// FOLDER: 3595_once_twice
// URL: https://leetcode.com/problems/once-twice/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['onceTwice']
// CPP FNS: ['onceTwice']
================================================================================
// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> onceTwice(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        int a = 0, b = 0;
        for (auto& [x, c] : freq) {
            if (c == 1) a = x;
            else if (c == 2) b = x;
        }
        return {a, b};
    }
};

----- PYTHON -----
# LeetCode 3595 - Once Twice
# https://leetcode.com/problems/once-twice/

from typing import List


class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        a = b = 0
        for key, v in freq.items():
            if v == 1:
                a = key
            elif v == 2:
                b = key
        return [a, b]

================================================================================
// FOLDER: 3596_minimum_cost_path_with_alternating_directions_i
// URL: https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/
// CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["m", "n"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=solve
// PY DEFS: ['minCost']
// CPP FNS: ['minCost']
================================================================================
// LeetCode 3596 - Minimum Cost Path with Alternating Directions I
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/


class Solution {
public:
    int minCost(int m, int n) {
        if (m == 1 && n == 1) return 1;
        if (m == 1 && n == 2) return 3;
        if (m == 2 && n == 1) return 3;
        return -1;
    }
};

----- PYTHON -----
# LeetCode 3596 - Minimum Cost Path with Alternating Directions I
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/


class Solution:
    def minCost(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        if m == 1 and n == 2:
            return 3
        if m == 2 and n == 1:
            return 3
        return -1

================================================================================
// FOLDER: 3597_partition_string
// URL: https://leetcode.com/problems/partition-string/
// CONFIG: {"class": "Solution", "method": "partitionString", "paramOrder": ["s"], "types": {"return": "string[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=partitionString
// PY DEFS: ['partitionString']
// CPP FNS: ['partitionString']
================================================================================
// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::string> partitionString(std::string s) {
        std::unordered_set<std::string> vis;
        std::vector<std::string> ans;
        std::string t;
        for (char c : s) {
            t += c;
            if (!vis.count(t)) {
                vis.insert(t);
                ans.push_back(t);
                t.clear();
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3598_longest_common_prefix_between_adjacent_strings_after_removals
// URL: https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/
// CONFIG: {"class": "Solution", "method": "longestCommonPrefix", "paramOrder": ["words"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=longestCommonPrefix
// PY DEFS: ['longestCommonPrefix', 'calc', 'add_key', 'rem_key', 'add', 'remove']
// CPP FNS: ['longestCommonPrefix', 'ans']
================================================================================
// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

#include <algorithm>
#include <map>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> longestCommonPrefix(std::vector<std::string>& words) {
        int n = (int)words.size();
        std::map<int, int> tm;
        auto calc = [&](const std::string& s, const std::string& t) {
            int m = std::min((int)s.size(), (int)t.size());
            for (int k = 0; k < m; k++)
                if (s[k] != t[k]) return k;
            return m;
        };
        auto add = [&](int i, int j) {
            if (i >= 0 && i < n && j >= 0 && j < n) tm[calc(words[i], words[j])]++;
        };
        auto remove = [&](int i, int j) {
            if (i >= 0 && i < n && j >= 0 && j < n) {
                int x = calc(words[i], words[j]);
                if (--tm[x] == 0) tm.erase(x);
            }
        };
        for (int i = 0; i + 1 < n; i++) add(i, i + 1);
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            remove(i, i + 1);
            remove(i - 1, i);
            add(i - 1, i + 1);
            if (!tm.empty() && tm.rbegin()->first > 0) ans[i] = tm.rbegin()->first;
            remove(i - 1, i + 1);
            add(i - 1, i);
            add(i, i + 1);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3599_partition_array_to_minimize_xor
// URL: https://leetcode.com/problems/partition-array-to-minimize-xor/
// CONFIG: {"class": "Solution", "method": "minXor", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minXor
// PY DEFS: ['minXor']
// CPP FNS: ['minXor', 'g']
================================================================================
// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minXor(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> g(n + 1);
        for (int i = 1; i <= n; i++) g[i] = g[i - 1] ^ nums[i - 1];
        const int inf = INT_MAX / 2;
        std::vector<std::vector<int>> f(n + 1, std::vector<int>(k + 1, inf));
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= std::min(i, k); j++) {
                for (int h = j - 1; h < i; h++) {
                    f[i][j] = std::min(f[i][j], std::max(f[h][j - 1], g[i] ^ g[h]));
                }
            }
        }
        return f[n][k];
    }
};

================================================================================
// FOLDER: 3600_maximize_spanning_tree_stability_with_upgrades
// URL: https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
// CONFIG: {"class": "Solution", "method": "maxStability", "paramOrder": ["n", "edges", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=maxStability
// PY DEFS: ['__init__', 'find', 'unite', 'maxStability', 'check']
// CPP FNS: ['find', 'unite', 'check', 'maxStability']
================================================================================
// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

#include <algorithm>
#include <vector>

class Solution {
    struct UnionFind {
        std::vector<int> p, size;
        int cnt;
        UnionFind(int n) : p(n), size(n, 1), cnt(n) {
            for (int i = 0; i < n; i++) p[i] = i;
        }
        int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
        bool unite(int a, int b) {
            int pa = find(a), pb = find(b);
            if (pa == pb) return false;
            if (size[pa] > size[pb]) {
                p[pb] = pa;
                size[pa] += size[pb];
            } else {
                p[pa] = pb;
                size[pb] += size[pa];
            }
            cnt--;
            return true;
        }
    };

    int N, K;
    std::vector<std::vector<int>>* E;

    bool check(int lim) {
        UnionFind uf(N);
        for (auto& e : *E) {
            if (e[2] >= lim) uf.unite(e[0], e[1]);
        }
        int rem = K;
        for (auto& e : *E) {
            if (e[2] * 2 >= lim && rem > 0) {
                if (uf.unite(e[0], e[1])) rem--;
            }
        }
        return uf.cnt == 1;
    }

public:
    int maxStability(int n, std::vector<std::vector<int>>& edges, int k) {
        N = n;
        E = &edges;
        K = k;
        UnionFind uf(n);
        int mn = 1000000;
        for (auto& e : edges) {
            if (e[3] == 1) {
                mn = std::min(mn, e[2]);
                if (!uf.unite(e[0], e[1])) return -1;
            }
        }
        for (auto& e : edges) uf.unite(e[0], e[1]);
        if (uf.cnt > 1) return -1;
        int l = 1, r = mn;
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (check(mid)) l = mid;
            else r = mid - 1;
        }
        return l;
    }
};

================================================================================
// FOLDER: 3602_hexadecimal_and_hexatrigesimal_conversion
// URL: https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/
// CONFIG: {"class": "Solution", "method": "concatHex36", "paramOrder": ["n"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=concatHex36
// PY DEFS: ['f3602', 'concatHex36']
// CPP FNS: ['f', 'concatHex36']
================================================================================
// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

#include <algorithm>
#include <string>

class Solution {
    std::string f(int x, int k) {
        std::string res;
        while (x > 0) {
            int v = x % k;
            res.push_back(v <= 9 ? char('0' + v) : char('A' + v - 10));
            x /= k;
        }
        std::reverse(res.begin(), res.end());
        return res;
    }

public:
    std::string concatHex36(int n) {
        return f(n * n, 16) + f(n * n * n, 36);
    }
};

================================================================================
// FOLDER: 3603_minimum_cost_path_with_alternating_directions_ii
// URL: https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/
// CONFIG: {"class": "Solution", "method": "minCost", "paramOrder": ["m", "n", "waitCost"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minCost
// PY DEFS: ['entry3603', 'minCost']
// CPP FNS: ['minCost']
================================================================================
// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long minCost(int m, int n, std::vector<std::vector<int>>& waitCost) {
        std::vector<std::vector<long long>> dp(m, std::vector<long long>(n, LLONG_MAX / 4));
        auto entry = [](int i, int j) { return 1LL * (i + 1) * (j + 1); };
        dp[0][0] = entry(0, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                if (i > 0) {
                    long long cand = dp[i - 1][j] + entry(i, j);
                    if (!(i - 1 == 0 && j == 0)) cand += waitCost[i - 1][j];
                    dp[i][j] = std::min(dp[i][j], cand);
                }
                if (j > 0) {
                    long long cand = dp[i][j - 1] + entry(i, j);
                    if (!(i == 0 && j - 1 == 0)) cand += waitCost[i][j - 1];
                    dp[i][j] = std::min(dp[i][j], cand);
                }
            }
        }
        return dp[m - 1][n - 1];
    }
};

================================================================================
// FOLDER: 3604_minimum_time_to_reach_destination_in_directed_graph
// URL: https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/
// CONFIG: {"class": "Solution", "method": "minTime", "paramOrder": ["n", "edges"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minTime
// PY DEFS: ['minTime', 'push']
// CPP FNS: ['minTime', 'dist']
================================================================================
// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

#include <climits>
#include <queue>
#include <vector>

class Solution {
public:
    int minTime(int n, std::vector<std::vector<int>>& edges) {
        struct Edge { int to, start, end; };
        std::vector<std::vector<Edge>> g(n);
        for (auto& e : edges) g[e[0]].push_back({e[1], e[2], e[3]});
        const long long inf = (long long)1e18;
        std::vector<long long> dist(n, inf);
        dist[0] = 0;
        using P = std::pair<long long, int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [t, u] = pq.top();
            pq.pop();
            if (t != dist[u]) continue;
            if (u == n - 1) return (int)t;
            for (auto& e : g[u]) {
                long long nt = t;
                if (nt > e.end) continue;
                if (nt < e.start) nt = e.start;
                nt += 1;
                if (nt < dist[e.to]) {
                    dist[e.to] = nt;
                    pq.push({nt, e.to});
                }
            }
        }
        return dist[n - 1] == inf ? -1 : (int)dist[n - 1];
    }
};

================================================================================
// FOLDER: 3605_minimum_stability_factor_of_array
// URL: https://leetcode.com/problems/minimum-stability-factor-of-array/
// CONFIG: {"class": "Solution", "method": "minStable", "paramOrder": ["nums", "maxC"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minStable
// PY DEFS: ['gcd3605', 'ok3605', 'minStable']
// CPP FNS: ['minStable']
================================================================================
// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

#include <numeric>
#include <vector>

class Solution {
public:
    int minStable(std::vector<int>& nums, int maxC) {
        int n = (int)nums.size();
        auto ok = [&](int x) {
            if (x >= n) return true;
            int changes = 0, i = 0;
            while (i + x < n) {
                int g = nums[i];
                for (int j = i + 1; j <= i + x; j++) g = std::gcd(g, nums[j]);
                if (g > 1) {
                    changes++;
                    i += x + 1;
                } else {
                    i++;
                }
            }
            return changes <= maxC;
        };
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};

================================================================================
// FOLDER: 3606_coupon_code_validator
// URL: https://leetcode.com/problems/coupon-code-validator/
// CONFIG: {"class": "Solution", "method": "validateCoupons", "paramOrder": ["code", "businessLine", "isActive"], "types": {"return": "string[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=validateCoupons
// PY DEFS: ['check3606', 'validateCoupons']
// CPP FNS: ['validateCoupons']
================================================================================
// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

#include <algorithm>
#include <cctype>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::string> validateCoupons(std::vector<std::string>& code,
                                             std::vector<std::string>& businessLine,
                                             std::vector<bool>& isActive) {
        std::unordered_set<std::string> bs = {"electronics", "grocery", "pharmacy", "restaurant"};
        auto check = [](const std::string& s) {
            if (s.empty()) return false;
            for (char c : s)
                if (!std::isalnum((unsigned char)c) && c != '_') return false;
            return true;
        };
        std::vector<int> idx;
        for (int i = 0; i < (int)code.size(); i++) {
            if (isActive[i] && bs.count(businessLine[i]) && check(code[i])) idx.push_back(i);
        }
        std::sort(idx.begin(), idx.end(), [&](int i, int j) {
            if (businessLine[i] != businessLine[j]) return businessLine[i] < businessLine[j];
            return code[i] < code[j];
        });
        std::vector<std::string> ans;
        for (int i : idx) ans.push_back(code[i]);
        return ans;
    }
};

================================================================================
// FOLDER: 3607_power_grid_maintenance
// URL: https://leetcode.com/problems/power-grid-maintenance/
// CONFIG: {"class": "Solution", "method": "processQueries", "paramOrder": ["c", "connections", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=processQueries
// PY DEFS: ['processQueries', 'find', 'unite']
// CPP FNS: ['processQueries', 'parent', 'online']
================================================================================
// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> processQueries(int c, std::vector<std::vector<int>>& connections, std::vector<std::vector<int>>& queries) {
        std::vector<int> parent(c + 1);
        for (int i = 0; i <= c; i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            return parent[x] == x ? x : parent[x] = self(self, parent[x]);
        };
        auto unite = [&](int a, int b) {
            int ra = find(find, a), rb = find(find, b);
            if (ra != rb) {
                if (ra < rb) parent[rb] = ra;
                else parent[ra] = rb;
            }
        };
        for (auto& e : connections) unite(e[0], e[1]);
        std::vector<bool> online(c + 1, true);
        std::unordered_map<int, std::vector<int>> comp;
        for (int i = 1; i <= c; i++) comp[find(find, i)].push_back(i);
        for (auto& [_, ids] : comp) std::sort(ids.begin(), ids.end());
        std::unordered_map<int, int> ptr;
        std::vector<int> ans;
        for (auto& q : queries) {
            int t = q[0], x = q[1];
            if (t == 2) {
                online[x] = false;
                continue;
            }
            if (online[x]) {
                ans.push_back(x);
                continue;
            }
            int r = find(find, x);
            auto& ids = comp[r];
            while (ptr[r] < (int)ids.size() && !online[ids[ptr[r]]]) ptr[r]++;
            ans.push_back(ptr[r] < (int)ids.size() ? ids[ptr[r]] : -1);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 3608_minimum_time_for_k_connected_components
// URL: https://leetcode.com/problems/minimum-time-for-k-connected-components/
// CONFIG: {"class": "Solution", "method": "minTime", "paramOrder": ["n", "edges", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
// CASES kind/class/method: None class=Solution method=minTime
// PY DEFS: ['__init__', 'find', 'unite', 'minTime']
// CPP FNS: ['find', 'unite', 'minTime']
================================================================================
// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

#include <algorithm>
#include <vector>

class Solution {
    struct UnionFind {
        std::vector<int> p, size;
        UnionFind(int n) : p(n), size(n, 1) {
            for (int i = 0; i < n; i++) p[i] = i;
        }
        int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
        bool unite(int a, int b) {
            int pa = find(a), pb = find(b);
            if (pa == pb) return false;
            if (size[pa] > size[pb]) {
                p[pb] = pa;
                size[pa] += size[pb];
            } else {
                p[pa] = pb;
                size[pb] += size[pa];
            }
            return true;
        }
    };

public:
    int minTime(int n, std::vector<std::vector<int>>& edges, int k) {
        std::sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
        UnionFind uf(n);
        int cnt = n;
        for (int i = (int)edges.size() - 1; i >= 0; i--) {
            if (uf.unite(edges[i][0], edges[i][1])) {
                cnt--;
                if (cnt < k) return edges[i][2];
            }
        }
        return 0;
    }
};
