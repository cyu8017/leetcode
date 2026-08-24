================================================================================
FOLDER 3717_minimum_operations_to_make_the_array_beautiful
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minOperations', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::unordered_map<int, int> f{{nums[0], 0}};
        for (int i = 1; i < (int)nums.size(); i++) {
            int x = nums[i];
            std::unordered_map<int, int> g;
            for (auto& [pre, s] : f) {
                int cur = (x + pre - 1) / pre * pre;
                while (cur <= 100) {
                    int val = s + (cur - x);
                    auto it = g.find(cur);
                    if (it == g.end() || it->second > val) g[cur] = val;
                    cur += pre;
                }
            }
            f.swap(g);
        }
        int ans = INT_MAX;
        for (auto& [_, v] : f) ans = std::min(ans, v);
        return ans;
    }
};

================================================================================
FOLDER 3718_smallest_missing_multiple_of_k
CONFIG class=Solution method=solve params=['nums', 'k'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'missingMultiple', 'std::vector<int>& nums, int k'), ('std::unordered_set<int>', 's', 'nums.begin(')]
--- CPP ---
// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int missingMultiple(std::vector<int>& nums, int k) {
        std::unordered_set<int> s(nums.begin(), nums.end());
        for (int i = 1;; i++) {
            int x = k * i;
            if (!s.count(x)) return x;
        }
    }
};

================================================================================
FOLDER 3719_longest_balanced_subarray_i
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'longestBalanced', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int longestBalanced(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::unordered_set<int> vis;
            int cnt[2] = {};
            for (int j = i; j < n; j++) {
                if (!vis.count(nums[j])) {
                    vis.insert(nums[j]);
                    cnt[nums[j] & 1]++;
                }
                if (cnt[0] == cnt[1]) ans = std::max(ans, j - i + 1);
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3720_lexicographically_smallest_permutation_greater_than_target
CONFIG class=Solution method=solve params=['s', 'target'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::string', 'lexGreaterPermutation', 'std::string s, std::string target'), ('std::vector<int>', 'cnt', '26, 0'), ('std::string', 'ans', "n, ' '")]
--- CPP ---
// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::string lexGreaterPermutation(std::string s, std::string target) {
        std::vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        int n = (int)s.size();
        std::string ans(n, ' ');
        std::function<bool(int, bool)> dfs = [&](int pos, bool greater) -> bool {
            if (pos == n) return greater;
            int start = greater ? 0 : (target[pos] - 'a');
            for (int c = start; c < 26; c++) {
                if (cnt[c] == 0) continue;
                cnt[c]--;
                ans[pos] = char('a' + c);
                bool ng = greater || c > (target[pos] - 'a');
                if (dfs(pos + 1, ng)) return true;
                cnt[c]++;
            }
            return false;
        };
        if (dfs(0, false)) return ans;
        return "";
    }
};

================================================================================
FOLDER 3721_longest_balanced_subarray_ii
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('explicit', 'SegmentTree', 'int n'), ('void', 'build', 'int u, int l, int r'), ('', 'build', 'u << 1, l, mid'), ('', 'build', 'u << 1 | 1, mid + 1, r'), ('void', 'apply', 'int u, int v'), ('void', 'pushup', 'int u')]
--- CPP ---
// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
    struct Node {
        int l = 0, r = 0, mn = 0, mx = 0, lazy = 0;
    };

    struct SegmentTree {
        std::vector<Node> tr;

        explicit SegmentTree(int n) : tr(n << 2) { build(1, 0, n); }

        void build(int u, int l, int r) {
            tr[u] = {l, r, 0, 0, 0};
            if (l == r) return;
            int mid = (l + r) >> 1;
            build(u << 1, l, mid);
            build(u << 1 | 1, mid + 1, r);
        }

        void apply(int u, int v) {
            tr[u].mn += v;
            tr[u].mx += v;
            tr[u].lazy += v;
        }

        void pushup(int u) {
            tr[u].mn = std::min(tr[u << 1].mn, tr[u << 1 | 1].mn);
            tr[u].mx = std::max(tr[u << 1].mx, tr[u << 1 | 1].mx);
        }

        void pushdown(int u) {
            if (tr[u].lazy != 0) {
                int v = tr[u].lazy;
                apply(u << 1, v);
                apply(u << 1 | 1, v);
                tr[u].lazy = 0;
            }
        }

        void modify(int u, int l, int r, int v) {
            if (tr[u].l >= l && tr[u].r <= r) {
                apply(u, v);
                return;
            }
            pushdown(u);
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (l <= mid) modify(u << 1, l, r, v);
            if (r > mid) modify(u << 1 | 1, l, r, v);
            pushup(u);
        }

        int query(int u, int target) {
            if (tr[u].l == tr[u].r) return tr[u].l;
            pushdown(u);
            int left = u << 1, right = u << 1 | 1;
            if (tr[left].mn <= target && target <= tr[left].mx) return query(left, target);
            return query(right, target);
        }
    };

public:
    int longestBalanced(std::vector<int>& nums) {
        int n = (int)nums.size();
        SegmentTree st(n);
        std::unordered_map<int, int> last;
        int now = 0, ans = 0;
        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            int det = (x & 1) ? 1 : -1;
            auto it = last.find(x);
            if (it != last.end()) {
                st.modify(1, it->second, n, -det);
                now -= det;
            }
            last[x] = i;
            st.modify(1, i, n, det);
            now += det;
            int pos = st.query(1, now);
            ans = std::max(ans, i - pos);
        }
        return ans;
    }
};

================================================================================
FOLDER 3722_lexicographically_smallest_string_after_reverse
CONFIG class=Solution method=solve params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::string', 'lexSmallest', 'std::string s')]
--- CPP ---
// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string lexSmallest(std::string s) {
        std::string ans = s;
        int n = (int)s.size();
        for (int k = 1; k <= n; k++) {
            std::string t1 = s.substr(0, k);
            std::reverse(t1.begin(), t1.end());
            t1 += s.substr(k);
            std::string t2 = s.substr(0, n - k);
            std::string suf = s.substr(n - k);
            std::reverse(suf.begin(), suf.end());
            t2 += suf;
            ans = std::min({ans, t1, t2});
        }
        return ans;
    }
};

================================================================================
FOLDER 3723_maximize_sum_of_squares_of_digits
CONFIG class=Solution method=solve params=['num', 'sum'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::string', 'maxSumOfSquares', 'int num, int sum'), ('std::string', 'ans', "k, '9'")]
--- CPP ---
// LeetCode 3723 - Maximize Sum of Squares of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

#include <string>

class Solution {
public:
    std::string maxSumOfSquares(int num, int sum) {
        if (num * 9 < sum) return "";
        int k = sum / 9, s = sum % 9;
        std::string ans(k, '9');
        if (s > 0) ans.push_back(char('0' + s));
        if ((int)ans.size() < num) ans.append(num - (int)ans.size(), '0');
        return ans;
    }
};

================================================================================
FOLDER 3724_minimum_operations_to_transform_array
CONFIG class=Solution method=solve params=['nums1', 'nums2'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'minOperations', 'std::vector<int>& nums1, std::vector<int>& nums2')]
--- CPP ---
// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums1, std::vector<int>& nums2) {
        long long ans = 1;
        int n = (int)nums1.size();
        bool ok = false;
        int d = 1 << 30;
        for (int i = 0; i < n; i++) {
            int x = std::max(nums1[i], nums2[i]);
            int y = std::min(nums1[i], nums2[i]);
            ans += x - y;
            d = std::min(d, std::min(std::abs(x - nums2[n]), std::abs(y - nums2[n])));
            if (nums2[n] >= y && nums2[n] <= x) ok = true;
        }
        if (!ok) ans += d;
        return ans;
    }
};

================================================================================
FOLDER 3725_count_ways_to_choose_coprime_integers_from_rows
CONFIG class=Solution method=solve params=['mat'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'countCoprime', 'std::vector<std::vector<int>>& mat')]
--- CPP ---
// LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

#include <numeric>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int countCoprime(std::vector<std::vector<int>>& mat) {
        const int MOD = 1000000007;
        int m = (int)mat.size();
        std::unordered_map<int, int> dp;
        for (int v : mat[0]) dp[v]++;
        for (int i = 1; i < m; i++) {
            std::unordered_map<int, int> ndp;
            for (int v : mat[i]) {
                for (auto& [g, cnt] : dp) {
                    int ng = std::gcd(g, v);
                    ndp[ng] = (ndp[ng] + cnt) % MOD;
                }
            }
            dp.swap(ndp);
        }
        return dp[1];
    }
};

================================================================================
FOLDER 3726_remove_zeros_in_decimal_representation
CONFIG class=Solution method=solve params=['n'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'removeZeros', 'long long n')]
--- CPP ---
// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

class Solution {
public:
    long long removeZeros(long long n) {
        long long ans = 0, k = 1;
        while (n > 0) {
            long long x = n % 10;
            if (x > 0) {
                ans = k * x + ans;
                k *= 10;
            }
            n /= 10;
        }
        return ans;
    }
};

================================================================================
FOLDER 3727_maximum_alternating_sum_of_squares
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'maxAlternatingSum', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxAlternatingSum(std::vector<int>& nums) {
        for (int& x : nums) x *= x;
        std::sort(nums.begin(), nums.end());
        int m = (int)nums.size() / 2;
        long long ans = 0;
        for (int i = 0; i < m; i++) ans -= nums[i];
        for (int i = m; i < (int)nums.size(); i++) ans += nums[i];
        return ans;
    }
};

================================================================================
FOLDER 3728_stable_subarrays_with_equal_boundary_and_interior_sum
CONFIG class=Solution method=solve params=['capacity'] kind=None ncases=3
CPP_CLASS Solution METHODS [('public:\n    long long', 'countStableSubarrays', 'std::vector<int>& capacity'), ('std::vector<long long>', 's', 'n + 1')]
--- CPP ---
// LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
    struct KeyHash {
        size_t operator()(const std::pair<int, long long>& p) const {
            return std::hash<int>()(p.first) * 1000003ull + std::hash<long long>()(p.second);
        }
    };

public:
    long long countStableSubarrays(std::vector<int>& capacity) {
        int n = (int)capacity.size();
        std::vector<long long> s(n + 1);
        for (int i = 1; i <= n; i++) s[i] = s[i - 1] + capacity[i - 1];
        std::unordered_map<std::pair<int, long long>, int, KeyHash> cnt;
        long long ans = 0;
        for (int r = 2; r < n; r++) {
            int l = r - 2;
            cnt[{capacity[l], (long long)capacity[l] + s[l + 1]}]++;
            ans += cnt[{capacity[r], s[r]}];
        }
        return ans;
    }
};

================================================================================
FOLDER 3729_count_distinct_subarrays_divisible_by_k_in_sorted_array
CONFIG class=Solution method=solve params=['nums', 'k'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'numGoodSubarrays', 'std::vector<int>& nums, int k')]
--- CPP ---
// LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long numGoodSubarrays(std::vector<int>& nums, int k) {
        long long ans = 0;
        int s = 0;
        std::unordered_map<int, int> cnt{{0, 1}};
        for (int x : nums) {
            s = (s + x) % k;
            ans += cnt[s];
            cnt[s]++;
        }
        int n = (int)nums.size();
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && nums[j] == nums[i]) j++;
            int m = j - i;
            for (int h = 1; h <= m; h++) {
                if (1LL * nums[i] * h % k == 0) ans -= (m - h);
            }
            i = j;
        }
        return ans;
    }
};

================================================================================
FOLDER 3730_maximum_calories_burnt_from_jumps
CONFIG class=Solution method=solve params=['heights'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'maxCaloriesBurnt', 'std::vector<int>& heights')]
--- CPP ---
// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxCaloriesBurnt(std::vector<int>& heights) {
        std::sort(heights.begin(), heights.end());
        long long ans = 0;
        int pre = 0, l = 0, r = (int)heights.size() - 1;
        while (l < r) {
            long long d1 = heights[r] - pre;
            ans += d1 * d1;
            long long d2 = heights[l] - heights[r];
            ans += d2 * d2;
            pre = heights[l];
            l++;
            r--;
        }
        long long d = heights[r] - pre;
        ans += d * d;
        return ans;
    }
};

================================================================================
FOLDER 3731_find_missing_elements
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::vector<int>', 'findMissingElements', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> findMissingElements(std::vector<int>& nums) {
        int mn = 100, mx = 0;
        std::unordered_set<int> s;
        for (int x : nums) {
            mn = std::min(mn, x);
            mx = std::max(mx, x);
            s.insert(x);
        }
        std::vector<int> ans;
        for (int x = mn + 1; x < mx; x++) {
            if (!s.count(x)) ans.push_back(x);
        }
        return ans;
    }
};

================================================================================
FOLDER 3732_maximum_product_of_three_elements_after_one_replacement
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'maxProduct', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxProduct(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        long long a = nums[0], b = nums[1], c = nums[n - 2], d = nums[n - 1];
        const long long x = 100000;
        return std::max({a * b * x, c * d * x, -a * d * x});
    }
};

================================================================================
FOLDER 3733_minimum_time_to_complete_all_deliveries
CONFIG class=Solution method=solve params=['d', 'r'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'minimumTime', 'std::vector<int>& d, std::vector<int>& r')]
--- CPP ---
// LeetCode 3733 - Minimum Time to Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

#include <vector>

class Solution {
public:
    long long minimumTime(std::vector<int>& d, std::vector<int>& r) {
        auto ok = [&](long long T) {
            long long w0 = T - T / r[0];
            long long w1 = T - T / r[1];
            return w0 + w1 >= (long long)d[0] + d[1];
        };
        long long lo = 1, hi = (long long)8e18;
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};

================================================================================
FOLDER 3734_lexicographically_smallest_palindromic_permutation_greater_than_target
CONFIG class=Solution method=solve params=['s', 'target'] kind=None ncases=4
CPP_CLASS Solution METHODS [('std::string', 'lexPalindromicPermutation', 'std::string s, std::string target'), ('std::string', 'left', "halfLen, ' '"), ('return', 'char', "'a' + mid")]
--- CPP ---
// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::string lexPalindromicPermutation(std::string s, std::string target) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        int odd = 0, mid = -1;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] % 2 == 1) { odd++; mid = i; }
        }
        if (odd > 1) return "";
        int half[26] = {};
        for (int i = 0; i < 26; i++) half[i] = cnt[i] / 2;
        int n = (int)s.size();
        int halfLen = n / 2;
        std::string left(halfLen, ' ');
        std::function<bool(int, bool)> dfs = [&](int pos, bool greater) -> bool {
            if (pos == halfLen) {
                if (mid >= 0) {
                    if (greater) return true;
                    return char('a' + mid) > target[halfLen];
                }
                return greater;
            }
            int start = greater ? 0 : (target[pos] - 'a');
            for (int c = start; c < 26; c++) {
                if (half[c] == 0) continue;
                half[c]--;
                left[pos] = char('a' + c);
                if (dfs(pos + 1, greater || c > (target[pos] - 'a'))) return true;
                half[c]++;
            }
            return false;
        };
        if (!dfs(0, false)) return "";
        std::string res = left;
        if (mid >= 0) res.push_back(char('a' + mid));
        for (int i = halfLen - 1; i >= 0; i--) res.push_back(left[i]);
        if (res <= target) return "";
        return res;
    }
};

================================================================================
FOLDER 3735_lexicographically_smallest_string_after_reverse_ii
CONFIG class=Solution method=solve params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::string', 'lexSmallest', 'std::string s')]
--- CPP ---
// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string lexSmallest(std::string s) {
        int n = (int)s.size();
        std::string best = s;
        for (int i = 1; i <= n; i++) {
            std::string t = s;
            std::reverse(t.begin(), t.begin() + i);
            if (t < best) best = t;
        }
        for (int i = 0; i < n; i++) {
            std::string t = s;
            std::reverse(t.begin() + i, t.end());
            if (t < best) best = t;
        }
        return best;
    }
};

================================================================================
FOLDER 3736_minimum_moves_to_equal_array_elements_iii
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'minMoves', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minMoves(std::vector<int>& nums) {
        int mx = 0, s = 0;
        for (int x : nums) {
            mx = std::max(mx, x);
            s += x;
        }
        return mx * (int)nums.size() - s;
    }
};

================================================================================
FOLDER 3737_count_subarrays_with_majority_element_i
CONFIG class=Solution method=solve params=['nums', 'target'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'countMajoritySubarrays', 'std::vector<int>& nums, int target')]
--- CPP ---
// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

#include <vector>

class Solution {
public:
    int countMajoritySubarrays(std::vector<int>& nums, int target) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] == target) cnt++;
                if (cnt * 2 > j - i + 1) ans++;
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3738_longest_non_decreasing_subarray_after_replacing_at_most_one_element
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'longestSubarray', 'std::vector<int>& nums'), ('std::vector<int>', 'left', 'n, 1')]
--- CPP ---
// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> left(n, 1), right(n, 1);
        for (int i = 1; i < n; i++) {
            if (nums[i] >= nums[i - 1]) left[i] = left[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
        }
        int ans = *std::max_element(left.begin(), left.end());
        for (int i = 0; i < n; i++) {
            int a = i > 0 ? left[i - 1] : 0;
            int b = i + 1 < n ? right[i + 1] : 0;
            if (i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1]) {
                ans = std::max(ans, std::max(a + 1, b + 1));
            } else {
                ans = std::max(ans, a + b + 1);
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3739_count_subarrays_with_majority_element_ii
CONFIG class=Solution method=solve params=['nums', 'target'] kind=None ncases=3
CPP_CLASS Solution METHODS [('explicit', 'BIT', 'int n_'), ('void', 'update', 'int x, int delta'), ('int', 'query', 'int x'), ('public:\n    long long', 'countMajoritySubarrays', 'std::vector<int>& nums, int target'), ('BIT', 'tree', '2 * n + 1')]
--- CPP ---
// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

#include <vector>

class Solution {
    struct BIT {
        int n;
        std::vector<int> c;
        explicit BIT(int n_) : n(n_), c(n_ + 1, 0) {}
        void update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        int query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    };

public:
    long long countMajoritySubarrays(std::vector<int>& nums, int target) {
        int n = (int)nums.size();
        BIT tree(2 * n + 1);
        int s = n + 1;
        tree.update(s, 1);
        long long ans = 0;
        for (int x : nums) {
            if (x == target) s++;
            else s--;
            ans += tree.query(s - 1);
            tree.update(s, 1);
        }
        return ans;
    }
};

================================================================================
FOLDER 3740_minimum_distance_between_three_equal_elements_i
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minimumDistance', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumDistance(std::vector<int>& nums) {
        std::unordered_map<int, std::vector<int>> g;
        for (int i = 0; i < (int)nums.size(); i++) g[nums[i]].push_back(i);
        const int inf = 1 << 30;
        int ans = inf;
        for (auto& [_, ls] : g) {
            int m = (int)ls.size();
            for (int h = 0; h < m - 2; h++) {
                ans = std::min(ans, (ls[h + 2] - ls[h]) * 2);
            }
        }
        return ans == inf ? -1 : ans;
    }
};

================================================================================
FOLDER 3741_minimum_distance_between_three_equal_elements_ii
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minimumDistance', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3741 - Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumDistance(std::vector<int>& nums) {
        std::unordered_map<int, std::vector<int>> g;
        for (int i = 0; i < (int)nums.size(); i++) g[nums[i]].push_back(i);
        const int inf = 1 << 30;
        int ans = inf;
        for (auto& [_, ls] : g) {
            int m = (int)ls.size();
            for (int h = 0; h < m - 2; h++) {
                ans = std::min(ans, (ls[h + 2] - ls[h]) * 2);
            }
        }
        return ans == inf ? -1 : ans;
    }
};

================================================================================
FOLDER 3742_maximum_path_score_in_a_grid
CONFIG class=Solution method=solve params=['grid', 'k'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'maxPathScore', 'std::vector<std::vector<int>>& grid, int k'), ('std::vector<std::vector<std::vector<int>>>', 'f', 'm, std::vector<std::vector<int>>(n, std::vector<int>(k + 1, -1')]
--- CPP ---
// LeetCode 3742 - Maximum Path Score in a Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    int maxPathScore(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        const int inf = 1 << 30;
        std::vector<std::vector<std::vector<int>>> f(m, std::vector<std::vector<int>>(n, std::vector<int>(k + 1, -1)));
        std::function<int(int, int, int)> dfs = [&](int i, int j, int kk) -> int {
            if (i < 0 || j < 0 || kk < 0) return -inf;
            if (i == 0 && j == 0) return 0;
            if (f[i][j][kk] != -1) return f[i][j][kk];
            int res = grid[i][j];
            int nk = kk;
            if (grid[i][j] != 0) nk--;
            int a = dfs(i - 1, j, nk);
            int b = dfs(i, j - 1, nk);
            res += std::max(a, b);
            return f[i][j][kk] = res;
        };
        int ans = dfs(m - 1, n - 1, k);
        return ans < 0 ? -1 : ans;
    }
};

================================================================================
FOLDER 3743_maximize_cyclic_partition_score
CONFIG class=Solution method=solve params=['nums', 'k'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'maximumScore', 'std::vector<int>& nums, int k'), ('std::vector<int>', 'seg', 'a.begin('), ('std::vector<std::vector<long long>>', 'dp', 'n + 1, std::vector<long long>(k + 1, NEG')]
--- CPP ---
// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

#include <climits>
#include <vector>

class Solution {
public:
    long long maximumScore(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> a = nums;
        a.insert(a.end(), nums.begin(), nums.end());
        if (k > n) k = n;
        long long best = 0;
        const long long NEG = -(1LL << 60);
        for (int start = 0; start < n; start++) {
            std::vector<int> seg(a.begin() + start, a.begin() + start + n);
            std::vector<std::vector<long long>> dp(n + 1, std::vector<long long>(k + 1, NEG));
            dp[0][0] = 0;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= k && j <= i; j++) {
                    long long mx = NEG;
                    for (int t = i; t >= j; t--) {
                        if (seg[t - 1] > mx) mx = seg[t - 1];
                        if (dp[t - 1][j - 1] > NEG) {
                            long long cand = dp[t - 1][j - 1] + mx;
                            if (cand > dp[i][j]) dp[i][j] = cand;
                        }
                    }
                }
            }
            if (dp[n][k] > best) best = dp[n][k];
        }
        return best;
    }
};

================================================================================
FOLDER 3744_find_kth_character_in_expanded_string
CONFIG class=Solution method=solve params=['s', 'k'] kind=None ncases=2
CPP_CLASS Solution METHODS [('char', 'kthCharacter', 'std::string s, long long k'), ('std::istringstream', 'iss', 's')]
--- CPP ---
// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    char kthCharacter(std::string s, long long k) {
        std::istringstream iss(s);
        std::string w;
        while (iss >> w) {
            long long m = (1 + (long long)w.size()) * (long long)w.size() / 2;
            if (k == m) return ' ';
            if (k > m) {
                k -= m + 1;
            } else {
                long long cur = 0;
                for (int i = 0;; i++) {
                    cur += i + 1;
                    if (k < cur) return w[i];
                }
            }
        }
        return ' ';
    }
};

================================================================================
FOLDER 3745_maximize_expression_of_three_elements
CONFIG class=Solution method=solve params=['nums'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'maximizeExpressionOfThree', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

#include <climits>
#include <vector>

class Solution {
public:
    int maximizeExpressionOfThree(std::vector<int>& nums) {
        const int inf = 1 << 30;
        int a = -inf, b = -inf, c = inf;
        for (int x : nums) {
            if (x < c) c = x;
            if (x >= a) { b = a; a = x; }
            else if (x > b) b = x;
        }
        return a + b - c;
    }
};

================================================================================
FOLDER 3746_minimum_string_length_after_balanced_removals
CONFIG class=Solution method=solve params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minLengthAfterRemovals', 'std::string s')]
--- CPP ---
// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

#include <cstdlib>
#include <string>

class Solution {
public:
    int minLengthAfterRemovals(std::string s) {
        int a = 0;
        for (char c : s) if (c == 'a') a++;
        int b = (int)s.size() - a;
        return std::abs(a - b);
    }
};

================================================================================
FOLDER 3747_count_distinct_integers_after_removing_zeros
CONFIG class=Solution method=solve params=['n'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'countDistinct', 'long long n'), ('std::function<long', 'long', 'int, int, int, int'), ('return', 'dfs', '0, 0, 1, 1')]
--- CPP ---
// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

#include <functional>
#include <string>

class Solution {
public:
    long long countDistinct(long long n) {
        std::string s = std::to_string(n);
        int m = (int)s.size();
        long long f[20][2][2][2];
        for (int i = 0; i < 20; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 2; k++)
                    for (int t = 0; t < 2; t++)
                        f[i][j][k][t] = -1;

        std::function<long long(int, int, int, int)> dfs = [&](int i, int zero, int lead, int limit) -> long long {
            if (i == m) return (zero == 0 && lead == 0) ? 1 : 0;
            if (limit == 0 && f[i][zero][lead][limit] != -1) return f[i][zero][lead][limit];
            int up = limit ? s[i] - '0' : 9;
            long long ans = 0;
            for (int d = 0; d <= up; d++) {
                int nxtZero = zero;
                if (d == 0 && lead == 0) nxtZero = 1;
                int nxtLead = (lead == 1 && d == 0) ? 1 : 0;
                int nxtLimit = (limit == 1 && d == up) ? 1 : 0;
                ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit);
            }
            if (limit == 0) f[i][zero][lead][limit] = ans;
            return ans;
        };
        return dfs(0, 0, 1, 1);
    }
};

================================================================================
FOLDER 3748_count_stable_subarrays
CONFIG class=Solution method=solve params=['nums', 'queries'] kind=None ncases=2
CPP_CLASS Solution METHODS [('std::vector<long long>', 'countStableSubarrays', 'std::vector<int>& nums, std::vector<std::vector<int>>& queries'), ('std::vector<long long>', 'ans', 'queries.size(')]
--- CPP ---
// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> countStableSubarrays(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> seg;
        std::vector<long long> s{0};
        int l = 0;
        for (int r = 0; r < n; r++) {
            if (r == n - 1 || nums[r] > nums[r + 1]) {
                seg.push_back(l);
                long long k = r - l + 1;
                s.push_back(s.back() + k * (k + 1) / 2);
                l = r + 1;
            }
        }
        std::vector<long long> ans(queries.size());
        for (int idx = 0; idx < (int)queries.size(); idx++) {
            int left = queries[idx][0], right = queries[idx][1];
            int i = (int)(std::lower_bound(seg.begin(), seg.end(), left + 1) - seg.begin());
            int j = (int)(std::lower_bound(seg.begin(), seg.end(), right + 1) - seg.begin()) - 1;
            if (i > j) {
                long long k = right - left + 1;
                ans[idx] = k * (k + 1) / 2;
            } else {
                long long a = seg[i] - left;
                long long b = right - seg[j] + 1;
                ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2;
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3749_evaluate_valid_expressions
CONFIG class=Solution method=solve params=['expression'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'evaluateExpression', 'std::string expression'), ('return', 'parse', '0')]
--- CPP ---
// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

#include <cctype>
#include <functional>
#include <string>
#include <utility>

class Solution {
public:
    long long evaluateExpression(std::string expression) {
        std::function<std::pair<long long, int>(int)> parse = [&](int i) -> std::pair<long long, int> {
            if (std::isdigit(expression[i]) || expression[i] == '-') {
                int j = i;
                if (expression[j] == '-') j++;
                while (j < (int)expression.size() && std::isdigit(expression[j])) j++;
                return {std::stoll(expression.substr(i, j - i)), j};
            }
            int j = i;
            while (expression[j] != '(') j++;
            std::string op = expression.substr(i, j - i);
            j++;
            auto [val1, nextJ1] = parse(j);
            j = nextJ1 + 1;
            auto [val2, nextJ2] = parse(j);
            j = nextJ2 + 1;
            long long res = 0;
            if (op == "add") res = val1 + val2;
            else if (op == "sub") res = val1 - val2;
            else if (op == "mul") res = val1 * val2;
            else if (op == "div") res = val1 / val2;
            return {res, j};
        };
        return parse(0).first;
    }
};

================================================================================
FOLDER 3750_minimum_number_of_flips_to_reverse_binary_string
CONFIG class=Solution method=minimumFlips params=['n'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'minimumFlips', 'int n')]
--- CPP ---
// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

#include <algorithm>
#include <string>

class Solution {
public:
    int minimumFlips(int n) {
        std::string s;
        long long x = n;
        if (x == 0) s = "0";
        else {
            while (x > 0) {
                s.push_back(char('0' + (x & 1)));
                x >>= 1;
            }
            std::reverse(s.begin(), s.end());
        }
        int m = (int)s.size(), cnt = 0;
        for (int i = 0; i < m / 2; i++) {
            if (s[i] != s[m - i - 1]) cnt++;
        }
        return cnt * 2;
    }
};

================================================================================
FOLDER 3751_total_waviness_of_numbers_in_range_i
CONFIG class=Solution method=totalWaviness params=['num1', 'num2'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'f', 'int x'), ('public:\n    int', 'totalWaviness', 'int num1, int num2')]
--- CPP ---
// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

#include <vector>

class Solution {
    int f(int x) {
        std::vector<int> nums;
        while (x > 0) {
            nums.push_back(x % 10);
            x /= 10;
        }
        int m = (int)nums.size();
        if (m < 3) return 0;
        int s = 0;
        for (int i = 1; i < m - 1; i++) {
            if ((nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
                (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])) s++;
        }
        return s;
    }

public:
    int totalWaviness(int num1, int num2) {
        int ans = 0;
        for (int x = num1; x <= num2; x++) ans += f(x);
        return ans;
    }
};

================================================================================
FOLDER 3752_lexicographically_smallest_negated_permutation_that_sums_to_target
CONFIG class=Solution method=lexicographicallySmallest params=['n', 'target'] kind=None ncases=2
CPP_CLASS Solution METHODS [('std::vector<int>', 'lexicographicallySmallest', 'int n, long long target'), ('std::vector<bool>', 'negative', 'n + 1, false')]
--- CPP ---
// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

#include <vector>

class Solution {
public:
    std::vector<int> lexicographicallySmallest(int n, long long target) {
        long long total = 1LL * n * (n + 1) / 2;
        if (target < -total || target > total || (total - target) % 2 != 0) return {};
        long long remaining = (total - target) / 2;
        std::vector<bool> negative(n + 1, false);
        for (int value = n; value >= 1; value--) {
            if (value <= remaining) {
                negative[value] = true;
                remaining -= value;
            }
        }
        std::vector<int> answer;
        for (int value = n; value >= 1; value--) {
            if (negative[value]) answer.push_back(-value);
        }
        for (int value = 1; value <= n; value++) {
            if (!negative[value]) answer.push_back(value);
        }
        return answer;
    }
};

================================================================================
FOLDER 3753_total_waviness_of_numbers_in_range_ii
CONFIG class=Solution method=totalWaviness params=['num1', 'num2'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'wavinessUpTo', 'long long limit'), ('return', 'dfs', '0, 10, 10, false, true'), ('public:\n    long long', 'totalWaviness', 'long long a, long long b'), ('return', 'wavinessUpTo', 'b')]
--- CPP ---
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

================================================================================
FOLDER 3754_concatenate_non_zero_digits_and_multiply_by_sum_i
CONFIG class=Solution method=sumAndMultiply params=['n'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'sumAndMultiply', 'int n')]
--- CPP ---
// LeetCode 3754 - Concatenate Non Zero Digits And Multiply By Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution {
public:
    long long sumAndMultiply(int n) {
        int p = 1, x = 0, s = 0;
        while (n > 0) {
            int v = n % 10;
            if (v != 0) {
                s += v;
                x += p * v;
                p *= 10;
            }
            n /= 10;
        }
        return 1LL * x * s;
    }
};

================================================================================
FOLDER 3755_find_maximum_balanced_xor_subarray_length
CONFIG class=Solution method=maxBalancedSubarray params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'maxBalancedSubarray', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxBalancedSubarray(std::vector<int>& nums) {
        std::unordered_map<long long, int> d;
        int a = 0, b = (int)nums.size(), ans = 0;
        d[b] = -1;
        for (int i = 0; i < (int)nums.size(); i++) {
            a ^= nums[i];
            if (nums[i] % 2 == 0) b++;
            else b--;
            long long key = ((long long)a << 32) | (long long)b;
            auto it = d.find(key);
            if (it != d.end()) ans = std::max(ans, i - it->second);
            else d[key] = i;
        }
        return ans;
    }
};

================================================================================
FOLDER 3756_concatenate_non_zero_digits_and_multiply_by_sum_ii
CONFIG class=Solution method=sumAndMultiply params=['s', 'queries'] kind=None ncases=3
CPP_CLASS Solution METHODS [('static const std::vector<long long>&', 'pow10', ''), ('std::vector<long long>', 'p', 'MX'), ('public:\n    std::vector<int>', 'sumAndMultiply', 'std::string s, std::vector<std::vector<int>>& queries'), ('std::vector<int>', 'sumD', 'n + 1'), ('std::vector<long long>', 'p', 'n + 1'), ('std::vector<int>', 'ans', 'queries.size(')]
--- CPP ---
// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum Ii
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

#include <string>
#include <vector>

class Solution {
    static constexpr int MX = 100001;
    static constexpr long long MOD = 1000000007;
    static const std::vector<long long>& pow10() {
        static std::vector<long long> p = [] {
            std::vector<long long> p(MX);
            p[0] = 1;
            for (int i = 1; i < MX; i++) p[i] = p[i - 1] * 10 % MOD;
            return p;
        }();
        return p;
    }

public:
    std::vector<int> sumAndMultiply(std::string s, std::vector<std::vector<int>>& queries) {
        int n = (int)s.size();
        std::vector<int> sumD(n + 1), cntN0(n + 1);
        std::vector<long long> p(n + 1);
        for (int i = 1; i <= n; i++) {
            long long d = s[i - 1] - '0';
            sumD[i] = sumD[i - 1] + (int)d;
            cntN0[i] = cntN0[i - 1];
            if (d > 0) {
                cntN0[i]++;
                p[i] = (p[i - 1] * 10 + d) % MOD;
            } else p[i] = p[i - 1];
        }
        const auto& pw = pow10();
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int l = queries[i][0], r = queries[i][1];
            int n0 = cntN0[r + 1] - cntN0[l];
            long long sd = sumD[r + 1] - sumD[l];
            long long x = (p[r + 1] - p[l] * pw[n0] % MOD + MOD) % MOD;
            ans[i] = (int)(x * sd % MOD);
        }
        return ans;
    }
};

================================================================================
FOLDER 3757_number_of_effective_subsequences
CONFIG class=Solution method=countEffectiveSubsequences params=['nums'] kind=None ncases=4
CPP_CLASS Solution METHODS [('int', 'countEffectiveSubsequences', 'std::vector<int>& nums'), ('std::vector<int>', 'freq', '1 << m'), ('std::vector<int>', 'pow2', 'nums.size(')]
--- CPP ---
// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

#include <vector>

class Solution {
public:
    int countEffectiveSubsequences(std::vector<int>& nums) {
        const int mod = 1000000007;
        int all = 0;
        for (int x : nums) all |= x;
        std::vector<int> bits;
        for (int b = 0; b < 20; b++) if ((all >> b) & 1) bits.push_back(b);
        int m = (int)bits.size();
        std::vector<int> freq(1 << m);
        for (int x : nums) {
            int mask = 0;
            for (int i = 0; i < m; i++) if ((x >> bits[i]) & 1) mask |= 1 << i;
            freq[mask]++;
        }
        std::vector<int> disjoint = freq;
        for (int b = 0; b < m; b++) {
            for (int mask = 0; mask < (1 << m); mask++) {
                if ((mask >> b) & 1) disjoint[mask] += disjoint[mask ^ (1 << b)];
            }
        }
        std::vector<int> pow2(nums.size() + 1);
        pow2[0] = 1;
        for (int i = 1; i <= (int)nums.size(); i++) pow2[i] = pow2[i - 1] * 2 % mod;
        int ans = 0, full = (1 << m) - 1;
        for (int s = 1; s <= full; s++) {
            int ways = pow2[disjoint[full ^ s]];
            int bc = __builtin_popcount(s);
            if (bc & 1) {
                ans += ways;
                if (ans >= mod) ans -= mod;
            } else {
                ans -= ways;
                if (ans < 0) ans += mod;
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3758_convert_number_words_to_digits
CONFIG class=Solution method=convertNumber params=['s'] kind=None ncases=4
CPP_CLASS Solution METHODS [('std::string', 'convertNumber', 'std::string s')]
--- CPP ---
// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

#include <string>
#include <vector>

class Solution {
public:
    std::string convertNumber(std::string s) {
        static const std::vector<std::string> d = {
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
        };
        int n = (int)s.size();
        std::string ans;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                int m = (int)d[j].size();
                if (i + m <= n && s.substr(i, m) == d[j]) {
                    ans.push_back(char('0' + j));
                    i += m - 1;
                    break;
                }
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3759_count_elements_with_at_least_k_greater_values
CONFIG class=Solution method=countElements params=['nums', 'k'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'countElements', 'std::vector<int>& nums, int k')]
--- CPP ---
// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countElements(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (k == 0) return n;
        std::sort(nums.begin(), nums.end());
        int ans = 0;
        for (int i = 0; i < n - k; i++) {
            if (nums[n - k] > nums[i]) ans++;
        }
        return ans;
    }
};

================================================================================
FOLDER 3760_maximum_substrings_with_distinct_start
CONFIG class=Solution method=maxDistinct params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'maxDistinct', 'std::string s')]
--- CPP ---
// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

#include <string>

class Solution {
public:
    int maxDistinct(std::string s) {
        int cnt[26] = {}, ans = 0;
        for (char c : s) {
            cnt[c - 'a']++;
            if (cnt[c - 'a'] == 1) ans++;
        }
        return ans;
    }
};

================================================================================
FOLDER 3761_minimum_absolute_distance_between_mirror_pairs
CONFIG class=Solution method=minMirrorPairDistance params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minMirrorPairDistance', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minMirrorPairDistance(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::unordered_map<int, int> pos;
        int ans = n + 1;
        auto reverse = [](int x) {
            int y = 0;
            for (; x > 0; x /= 10) y = y * 10 + x % 10;
            return y;
        };
        for (int i = 0; i < n; i++) {
            auto it = pos.find(nums[i]);
            if (it != pos.end()) ans = std::min(ans, i - it->second);
            pos[reverse(nums[i])] = i;
        }
        return ans > n ? -1 : ans;
    }
};

================================================================================
FOLDER 3762_minimum_operations_to_equalize_subarrays
CONFIG class=Solution method=minOperations params=['nums', 'k', 'queries'] kind=None ncases=2
CPP_CLASS Solution METHODS [('public:\n    std::vector<long long>', 'minOperations', 'std::vector<int>& nums, int k, std::vector<std::vector<int>>& queries'), ('std::vector<int>', 'quotient', 'n'), ('std::vector<Node>', 'nodes', '1'), ('std::vector<int>', 'roots', 'n + 1'), ('return', 'kth', 'nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount'), ('std::vector<int>', 'logv', 'n + 1')]
--- CPP ---
// LeetCode 3762 - Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
    struct Node {
        int left = 0, right = 0, count = 0;
        long long sum = 0;
    };

public:
    std::vector<long long> minOperations(std::vector<int>& nums, int k, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> quotient(n), remainder(n), values(n);
        for (int i = 0; i < n; i++) {
            quotient[i] = nums[i] / k;
            remainder[i] = nums[i] % k;
            values[i] = quotient[i];
        }
        std::sort(values.begin(), values.end());
        values.erase(std::unique(values.begin(), values.end()), values.end());
        std::vector<Node> nodes(1);
        std::function<int(int, int, int, int, int)> update = [&](int previous, int lo, int hi, int position, int value) -> int {
            int current = (int)nodes.size();
            nodes.push_back(nodes[previous]);
            nodes[current].count++;
            nodes[current].sum += value;
            if (lo < hi) {
                int mid = (lo + hi) / 2;
                if (position <= mid) nodes[current].left = update(nodes[previous].left, lo, mid, position, value);
                else nodes[current].right = update(nodes[previous].right, mid + 1, hi, position, value);
            }
            return current;
        };
        std::vector<int> roots(n + 1);
        int umax = (int)values.size() - 1;
        for (int i = 0; i < n; i++) {
            int position = (int)(std::lower_bound(values.begin(), values.end(), quotient[i]) - values.begin());
            roots[i + 1] = update(roots[i], 0, umax, position, quotient[i]);
        }
        std::function<int(int, int, int, int, int)> kth = [&](int rightRoot, int leftRoot, int lo, int hi, int rank) -> int {
            if (lo == hi) return lo;
            int leftCount = nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count;
            int mid = (lo + hi) / 2;
            if (rank <= leftCount) return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank);
            return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount);
        };
        std::function<std::pair<int, long long>(int, int, int, int, int)> prefixStats =
            [&](int rightRoot, int leftRoot, int lo, int hi, int end) -> std::pair<int, long long> {
            if (end < lo) return {0, 0};
            if (hi <= end) return {nodes[rightRoot].count - nodes[leftRoot].count,
                                   nodes[rightRoot].sum - nodes[leftRoot].sum};
            int mid = (lo + hi) / 2;
            auto [count, sum] = prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end);
            if (end > mid) {
                auto [c2, s2] = prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, end);
                count += c2;
                sum += s2;
            }
            return {count, sum};
        };
        std::vector<int> logv(n + 1);
        for (int i = 2; i <= n; i++) logv[i] = logv[i / 2] + 1;
        int levels = logv[n] + 1;
        std::vector<std::vector<int>> minTable(levels), maxTable(levels);
        minTable[0] = remainder;
        maxTable[0] = remainder;
        for (int level = 1; level < levels; level++) {
            int length = n - (1 << level) + 1;
            minTable[level].resize(length);
            maxTable[level].resize(length);
            int half = 1 << (level - 1);
            for (int i = 0; i < length; i++) {
                minTable[level][i] = std::min(minTable[level - 1][i], minTable[level - 1][i + half]);
                maxTable[level][i] = std::max(maxTable[level - 1][i], maxTable[level - 1][i + half]);
            }
        }
        std::vector<long long> answer(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int left = queries[qi][0], right = queries[qi][1];
            int length = right - left + 1;
            int level = logv[length];
            int offset = right - (1 << level) + 1;
            int minR = std::min(minTable[level][left], minTable[level][offset]);
            int maxR = std::max(maxTable[level][left], maxTable[level][offset]);
            if (minR != maxR) {
                answer[qi] = -1;
                continue;
            }
            int medianIndex = kth(roots[right + 1], roots[left], 0, umax, (length + 1) / 2);
            int median = values[medianIndex];
            auto [leftCount, leftSum] = prefixStats(roots[right + 1], roots[left], 0, umax, medianIndex);
            long long totalSum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum;
            answer[qi] = 1LL * median * leftCount - leftSum + (totalSum - leftSum) - 1LL * median * (length - leftCount);
        }
        return answer;
    }
};

================================================================================
FOLDER 3763_maximum_total_sum_with_threshold_constraints
CONFIG class=Solution method=maxSum params=['nums', 'threshold'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'maxSum', 'std::vector<int>& nums, std::vector<int>& threshold'), ('std::vector<int>', 'idx', 'n')]
--- CPP ---
// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

#include <algorithm>
#include <set>
#include <vector>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, std::vector<int>& threshold) {
        int n = (int)nums.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) {
            return threshold[a] < threshold[b];
        });
        std::multiset<int> tree;
        long long ans = 0;
        int i = 0;
        for (int step = 1;; step++) {
            while (i < n && threshold[idx[i]] <= step) {
                tree.insert(nums[idx[i]]);
                i++;
            }
            if (tree.empty()) break;
            auto it = std::prev(tree.end());
            ans += *it;
            tree.erase(it);
        }
        return ans;
    }
};

================================================================================
FOLDER 3765_complete_prime_number
CONFIG class=Solution method=completePrime params=['num'] kind=None ncases=3
CPP_CLASS Solution METHODS [('bool', 'isPrime', 'int x'), ('public:\n    bool', 'completePrime', 'int num')]
--- CPP ---
// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

#include <string>

class Solution {
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) if (x % i == 0) return false;
        return true;
    }

public:
    bool completePrime(int num) {
        std::string s = std::to_string(num);
        int x = 0;
        for (char c : s) {
            x = x * 10 + (c - '0');
            if (!isPrime(x)) return false;
        }
        x = 0;
        int p = 1;
        for (int i = (int)s.size() - 1; i >= 0; i--) {
            x = p * (s[i] - '0') + x;
            p *= 10;
            if (!isPrime(x)) return false;
        }
        return true;
    }
};

================================================================================
FOLDER 3766_minimum_operations_to_make_binary_palindrome
CONFIG class=Solution method=isPalindrome params=['nums'] kind=None ncases=2
CPP_CLASS Solution METHODS [('static bool', 'isPalindrome', 'const std::string& s'), ('static const std::vector<int>&', 'getPals', ''), ('public:\n    std::vector<int>', 'minOperations', 'std::vector<int>& nums'), ('std::vector<int>', 'ans', 'nums.size(')]
--- CPP ---
// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

#include <algorithm>
#include <climits>
#include <string>
#include <vector>

class Solution {
    static std::vector<int> pals;

    static bool isPalindrome(const std::string& s) {
        int m = (int)s.size();
        for (int i = 0; i < m / 2; i++) if (s[i] != s[m - 1 - i]) return false;
        return true;
    }

    static const std::vector<int>& getPals() {
        static bool inited = false;
        if (!inited) {
            int N = 1 << 14;
            for (int i = 0; i < N; i++) {
                std::string s;
                int x = i;
                if (x == 0) s = "0";
                else {
                    while (x > 0) {
                        s.push_back(char('0' + (x & 1)));
                        x >>= 1;
                    }
                    std::reverse(s.begin(), s.end());
                }
                if (isPalindrome(s)) pals.push_back(i);
            }
            inited = true;
        }
        return pals;
    }

public:
    std::vector<int> minOperations(std::vector<int>& nums) {
        const auto& p = getPals();
        std::vector<int> ans(nums.size());
        for (int k = 0; k < (int)nums.size(); k++) {
            int x = nums[k];
            auto it = std::lower_bound(p.begin(), p.end(), x);
            int t = INT_MAX;
            if (it != p.end()) t = *it - x;
            if (it != p.begin()) t = std::min(t, x - *std::prev(it));
            ans[k] = t;
        }
        return ans;
    }
};

std::vector<int> Solution::pals;

================================================================================
FOLDER 3767_maximize_points_after_choosing_k_tasks
CONFIG class=Solution method=maxPoints params=['technique1', 'technique2', 'k'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'maxPoints', 'std::vector<int>& technique1, std::vector<int>& technique2, int k'), ('std::vector<int>', 'idx', 'n')]
--- CPP ---
// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxPoints(std::vector<int>& technique1, std::vector<int>& technique2, int k) {
        int n = (int)technique1.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int i, int j) {
            return technique1[j] - technique2[j] < technique1[i] - technique2[i];
        });
        long long ans = 0;
        for (int x : technique2) ans += x;
        for (int i = 0; i < k; i++) {
            int index = idx[i];
            ans -= technique2[index];
            ans += technique1[index];
        }
        for (int i = k; i < n; i++) {
            int index = idx[i];
            if (technique1[index] >= technique2[index]) {
                ans -= technique2[index];
                ans += technique1[index];
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3768_minimum_inversion_count_in_subarrays_of_fixed_length
CONFIG class=Solution method=minInversionCount params=['nums', 'k'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'minInversionCount', 'std::vector<int>& nums, int k'), ('std::vector<int>', 'bit', 'vals.size('), ('std::vector<int>', 'rank', 'nums.size('), ('', 'add', 'rank[i], 1'), ('', 'add', 'left, -1'), ('', 'add', 'rank[r], 1')]
--- CPP ---
// LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minInversionCount(std::vector<int>& nums, int k) {
        std::vector<int> vals = nums;
        std::sort(vals.begin(), vals.end());
        vals.erase(std::unique(vals.begin(), vals.end()), vals.end());
        std::vector<int> bit(vals.size() + 1, 0);
        auto add = [&](int i, int delta) {
            for (; i < (int)bit.size(); i += i & -i) bit[i] += delta;
        };
        auto sum = [&](int i) {
            int res = 0;
            for (; i > 0; i -= i & -i) res += bit[i];
            return res;
        };
        std::vector<int> rank(nums.size());
        long long inv = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            rank[i] = (int)(std::lower_bound(vals.begin(), vals.end(), nums[i]) - vals.begin()) + 1;
            if (i < k) {
                inv += i - sum(rank[i]);
                add(rank[i], 1);
            }
        }
        long long best = inv;
        for (int r = k; r < (int)nums.size(); r++) {
            int left = rank[r - k];
            inv -= sum(left - 1);
            add(left, -1);
            inv += k - 1 - sum(rank[r]);
            add(rank[r], 1);
            if (inv < best) best = inv;
        }
        return best;
    }
};

================================================================================
FOLDER 3769_sort_integers_by_binary_reflection
CONFIG class=Solution method=sortByReflection params=['nums'] kind=None ncases=2
CPP_CLASS Solution METHODS [('std::vector<int>', 'sortByReflection', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> sortByReflection(std::vector<int>& nums) {
        auto f = [](int x) {
            int y = 0;
            while (x != 0) {
                y = (y << 1) | (x & 1);
                x >>= 1;
            }
            return y;
        };
        std::sort(nums.begin(), nums.end(), [&](int a, int b) {
            int fa = f(a), fb = f(b);
            if (fa != fb) return fa < fb;
            return a < b;
        });
        return nums;
    }
};

================================================================================
FOLDER 3770_largest_prime_from_consecutive_prime_sum
CONFIG class=Solution method=largestPrime params=['n'] kind=None ncases=2
CPP_CLASS Solution METHODS [('static void', 'ensureInit', ''), ('std::vector<bool>', 'isPrime', 'MX + 1, true'), ('public:\n    int', 'largestPrime', 'int n'), ('', 'ensureInit', '')]
--- CPP ---
// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

#include <algorithm>
#include <vector>

class Solution {
    static constexpr int MX = 500000;
    static std::vector<int> S;
    static bool inited;

    static void ensureInit() {
        if (inited) return;
        std::vector<bool> isPrime(MX + 1, true);
        isPrime[0] = isPrime[1] = false;
        std::vector<int> primes;
        for (int i = 2; i <= MX; i++) {
            if (isPrime[i]) {
                primes.push_back(i);
                if (1LL * i * i <= MX) {
                    for (int j = i * i; j <= MX; j += i) isPrime[j] = false;
                }
            }
        }
        S = {0};
        int t = 0;
        for (int x : primes) {
            t += x;
            if (t > MX) break;
            if (isPrime[t]) S.push_back(t);
        }
        inited = true;
    }

public:
    int largestPrime(int n) {
        ensureInit();
        auto it = std::upper_bound(S.begin(), S.end(), n);
        return *std::prev(it);
    }
};

std::vector<int> Solution::S;
bool Solution::inited = false;

================================================================================
FOLDER 3771_total_score_of_dungeon_runs
CONFIG class=Solution method=totalScore params=['hp', 'damage', 'requirement'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'totalScore', 'int hp, std::vector<int>& damage, std::vector<int>& requirement'), ('std::vector<long long>', 'prefix', 'n + 1')]
--- CPP ---
// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long totalScore(int hp, std::vector<int>& damage, std::vector<int>& requirement) {
        int n = (int)damage.size();
        std::vector<long long> prefix(n + 1);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + damage[i];
        long long answer = 1LL * n * (n + 1) / 2;
        for (int j = 1; j <= n; j++) {
            long long threshold = prefix[j] + (requirement[j - 1] - hp);
            int invalid = (int)(std::lower_bound(prefix.begin(), prefix.begin() + j, threshold) - prefix.begin());
            answer -= invalid;
        }
        return answer;
    }
};

================================================================================
FOLDER 3772_maximum_subgraph_score_in_a_tree
CONFIG class=Solution method=maxSubgraphScore params=['n', 'edges', 'good'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::vector<int>', 'maxSubgraphScore', 'int n, std::vector<std::vector<int>>& edges, std::vector<int>& good'), ('std::vector<std::vector<int>>', 'g', 'n'), ('std::vector<int>', 'parent', 'n, -2'), ('std::vector<int>', 'down', 'n')]
--- CPP ---
// LeetCode 3772 - Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

#include <vector>

class Solution {
public:
    std::vector<int> maxSubgraphScore(int n, std::vector<std::vector<int>>& edges, std::vector<int>& good) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<int> parent(n, -2);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : g[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.push_back(v);
                }
            }
        }
        std::vector<int> down(n);
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            down[u] = 2 * good[u] - 1;
            for (int v : g[u]) {
                if (parent[v] == u && down[v] > 0) down[u] += down[v];
            }
        }
        std::vector<int> ans = down;
        for (int u : order) {
            for (int v : g[u]) {
                if (parent[v] == u) {
                    int outside = ans[u];
                    if (down[v] > 0) outside -= down[v];
                    ans[v] = down[v];
                    if (outside > 0) ans[v] += outside;
                }
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3773_maximum_number_of_equal_length_runs
CONFIG class=Solution method=maxSameLengthRuns params=['s'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'maxSameLengthRuns', 'std::string s')]
--- CPP ---
// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int maxSameLengthRuns(std::string s) {
        std::unordered_map<int, int> cnt;
        int n = (int)s.size(), ans = 0;
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && s[j] == s[i]) j++;
            int m = j - i;
            ans = std::max(ans, ++cnt[m]);
            i = j;
        }
        return ans;
    }
};

================================================================================
FOLDER 3774_absolute_difference_between_maximum_and_minimum_k_elements
CONFIG class=Solution method=absDifference params=['nums', 'k'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'absDifference', 'std::vector<int>& nums, int k')]
--- CPP ---
// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    int absDifference(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = 0, n = (int)nums.size();
        for (int i = 0; i < k; i++) ans += nums[n - i - 1] - nums[i];
        return ans;
    }
};

================================================================================
FOLDER 3775_reverse_words_with_same_vowel_count
CONFIG class=Solution method=reverseWords params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('static int', 'calc', 'const std::string& w'), ('public:\n    std::string', 'reverseWords', 'std::string s'), ('std::istringstream', 'iss', 's')]
--- CPP ---
// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

class Solution {
    static int calc(const std::string& w) {
        int cnt = 0;
        for (char c : w) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++;
        }
        return cnt;
    }

public:
    std::string reverseWords(std::string s) {
        std::istringstream iss(s);
        std::vector<std::string> words;
        std::string w;
        while (iss >> w) words.push_back(w);

        int cnt = calc(words[0]);
        std::vector<std::string> ans;
        ans.push_back(words[0]);

        for (int i = 1; i < (int)words.size(); i++) {
            w = words[i];
            if (calc(w) == cnt) std::reverse(w.begin(), w.end());
            ans.push_back(w);
        }

        std::ostringstream oss;
        for (int i = 0; i < (int)ans.size(); i++) {
            if (i) oss << ' ';
            oss << ans[i];
        }
        return oss.str();
    }
};

================================================================================
FOLDER 3776_minimum_moves_to_balance_circular_array
CONFIG class=Solution method=minMoves params=['balance'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'minMoves', 'std::vector<int>& balance')]
--- CPP ---
// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long minMoves(std::vector<int>& balance) {
        int64_t sum = 0;
        for (int b : balance) sum += b;
        if (sum < 0) return -1;

        int n = (int)balance.size();
        int mn = balance[0], idx = 0;
        for (int i = 1; i < n; i++) {
            if (balance[i] < mn) {
                mn = balance[i];
                idx = i;
            }
        }
        if (mn >= 0) return 0;

        int need = -mn;
        int64_t ans = 0;
        for (int j = 1; j < n; j++) {
            int a = balance[(idx - j + n) % n];
            int b = balance[(idx + j) % n];
            int c1 = std::min(a, need);
            need -= c1;
            ans += (int64_t)c1 * j;
            int c2 = std::min(b, need);
            need -= c2;
            ans += (int64_t)c2 * j;
        }
        return ans;
    }
};

================================================================================
FOLDER 3777_minimum_deletions_to_make_alternating_substring
CONFIG class=Solution method=newBinaryIndexedTree params=['s', 'queries'] kind=None ncases=3
CPP_CLASS Solution METHODS [('explicit', 'BIT', 'int n_'), ('void', 'update', 'int x, int delta'), ('int', 'query', 'int x'), ('public:\n    std::vector<int>', 'minDeletions', 'std::string s, std::vector<std::vector<int>>& queries'), ('std::vector<int>', 'nums', 'n, 0'), ('BIT', 'bit', 'n')]
--- CPP ---
// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

#include <string>
#include <vector>

class Solution {
    struct BIT {
        int n;
        std::vector<int> c;
        explicit BIT(int n_) : n(n_), c(n_ + 1, 0) {}
        void update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        int query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    };

public:
    std::vector<int> minDeletions(std::string s, std::vector<std::vector<int>>& queries) {
        int n = (int)s.size();
        std::vector<int> nums(n, 0);
        BIT bit(n);
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i - 1]) {
                nums[i] = 1;
                bit.update(i + 1, 1);
            }
        }
        std::vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int j = q[1];
                int delta = (nums[j] ^ 1) - nums[j];
                nums[j] ^= 1;
                bit.update(j + 1, delta);
                if (j + 1 < n) {
                    delta = (nums[j + 1] ^ 1) - nums[j + 1];
                    nums[j + 1] ^= 1;
                    bit.update(j + 2, delta);
                }
            } else {
                int l = q[1], r = q[2];
                ans.push_back(bit.query(r + 1) - bit.query(l + 1));
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3778_minimum_distance_excluding_one_maximum_weighted_edge
CONFIG class=Solution method=minCostExcludingMax params=['n', 'edges'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'minCostExcludingMax', 'int n, std::vector<std::vector<int>>& edges'), ('std::vector<std::vector<std::pair<int, int>>>', 'g', 'n'), ('std::vector<std::array<int64_t, 2>>', 'dist', 'n, {INF, INF}')]
--- CPP ---
// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

#include <array>
#include <cstdint>
#include <functional>
#include <queue>
#include <tuple>
#include <utility>
#include <vector>

class Solution {
public:
    long long minCostExcludingMax(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }
        const int64_t INF = (int64_t)4e18;
        std::vector<std::array<int64_t, 2>> dist(n, {INF, INF});
        dist[0][0] = 0;
        using State = std::tuple<int64_t, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> pq;
        pq.push({0, 0, 0});
        while (!pq.empty()) {
            auto [cur, u, used] = pq.top();
            pq.pop();
            if (cur > dist[u][used]) continue;
            if (u == n - 1 && used == 1) return cur;
            for (auto [v, w] : g[u]) {
                int64_t nxt = cur + w;
                if (nxt < dist[v][used]) {
                    dist[v][used] = nxt;
                    pq.push({nxt, v, used});
                }
                if (used == 0) {
                    nxt = cur;
                    if (nxt < dist[v][1]) {
                        dist[v][1] = nxt;
                        pq.push({nxt, v, 1});
                    }
                }
            }
        }
        return dist[n - 1][1];
    }
};

================================================================================
FOLDER 3779_minimum_number_of_operations_to_have_distinct_elements
CONFIG class=Solution method=minOperations params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minOperations', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::unordered_set<int> st;
        for (int i = (int)nums.size() - 1; i >= 0; i--) {
            if (st.count(nums[i])) return i / 3 + 1;
            st.insert(nums[i]);
        }
        return 0;
    }
};

================================================================================
FOLDER 3780_maximum_sum_of_three_numbers_divisible_by_three
CONFIG class=Solution method=maximumSum params=['nums'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'maximumSum', 'std::vector<int>& nums'), ('std::vector<std::vector<int>>', 'g', '3')]
--- CPP ---
// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> g(3);
        for (int x : nums) g[x % 3].push_back(x);
        int ans = 0;
        for (int a = 0; a < 3; a++) {
            if (!g[a].empty()) {
                int x = g[a].back();
                g[a].pop_back();
                for (int b = 0; b < 3; b++) {
                    if (!g[b].empty()) {
                        int y = g[b].back();
                        g[b].pop_back();
                        int c = (3 - (a + b) % 3) % 3;
                        if (!g[c].empty()) {
                            int z = g[c].back();
                            ans = std::max(ans, x + y + z);
                        }
                        g[b].push_back(y);
                    }
                }
                g[a].push_back(x);
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3781_maximum_score_after_binary_swaps
CONFIG class=Solution method=maximumScore params=['nums', 's'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'maximumScore', 'std::vector<int>& nums, std::string s')]
--- CPP ---
// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

#include <cstdint>
#include <queue>
#include <string>
#include <vector>

class Solution {
public:
    long long maximumScore(std::vector<int>& nums, std::string s) {
        int64_t ans = 0;
        std::priority_queue<int> pq;
        for (int i = 0; i < (int)nums.size(); i++) {
            pq.push(nums[i]);
            if (s[i] == '1') {
                ans += pq.top();
                pq.pop();
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3782_last_remaining_integer_after_alternating_deletion_operations
CONFIG class=Solution method=lastRemaining params=['n'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'lastRemaining', 'long long n')]
--- CPP ---
// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

#include <cstdint>

class Solution {
public:
    long long lastRemaining(long long n) {
        int64_t first = 1, step = 2;
        bool left = true;
        while (n > 1) {
            if (!left && n % 2 == 0) first += step;
            n = (n + 1) / 2;
            step *= 2;
            left = !left;
        }
        return first;
    }
};

================================================================================
FOLDER 3783_mirror_distance_of_an_integer
CONFIG class=Solution method=mirrorDistance params=['n'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'mirrorDistance', 'int n')]
--- CPP ---
// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

#include <cstdlib>

class Solution {
public:
    int mirrorDistance(int n) {
        auto reverse = [](int x) {
            int y = 0;
            for (; x > 0; x /= 10) y = y * 10 + x % 10;
            return y;
        };
        return std::abs(n - reverse(n));
    }
};

================================================================================
FOLDER 3784_minimum_deletion_cost_to_make_all_characters_equal
CONFIG class=Solution method=minCost params=['s', 'cost'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'minCost', 'std::string s, std::vector<int>& cost')]
--- CPP ---
// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

#include <algorithm>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long minCost(std::string s, std::vector<int>& cost) {
        int64_t tot = 0;
        std::unordered_map<char, int64_t> g;
        for (int i = 0; i < (int)cost.size(); i++) {
            tot += cost[i];
            g[s[i]] += cost[i];
        }
        int64_t ans = tot;
        for (auto& [_, x] : g) ans = std::min(ans, tot - x);
        return ans;
    }
};

================================================================================
FOLDER 3785_minimum_swaps_to_avoid_forbidden_values
CONFIG class=Solution method=minSwaps params=['nums', 'forbidden'] kind=None ncases=4
CPP_CLASS Solution METHODS [('int', 'minSwaps', 'std::vector<int>& nums, std::vector<int>& forbidden')]
--- CPP ---
// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minSwaps(std::vector<int>& nums, std::vector<int>& forbidden) {
        int n = (int)nums.size();
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        for (int x : forbidden) freq[x]++;
        for (auto& [_, c] : freq) {
            if (c > n) return -1;
        }
        std::unordered_map<int, int> bad;
        int total = 0, largest = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == forbidden[i]) {
                bad[nums[i]]++;
                total++;
                if (bad[nums[i]] > largest) largest = bad[nums[i]];
            }
        }
        if ((total + 1) / 2 > largest) return (total + 1) / 2;
        return largest;
    }
};

================================================================================
FOLDER 3786_total_sum_of_interaction_cost_in_tree_groups
CONFIG class=Solution method=interactionCost params=['n', 'edges', 'group'] kind=None ncases=4
CPP_CLASS Solution METHODS [('long long', 'interactionCost', 'int n, std::vector<std::vector<int>>& edges, std::vector<int>& group'), ('std::vector<std::vector<int>>', 'g', 'n'), ('std::vector<int>', 'parent', 'n, -2'), ('std::vector<std::array<int, 21>>', 'count', 'n')]
--- CPP ---
// LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

#include <array>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long interactionCost(int n, std::vector<std::vector<int>>& edges, std::vector<int>& group) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::array<int, 21> total{};
        for (int x : group) total[x]++;
        std::vector<int> parent(n, -2);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : g[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.push_back(v);
                }
            }
        }
        std::vector<std::array<int, 21>> count(n);
        int64_t ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            count[u][group[u]]++;
            for (int v : g[u]) {
                if (parent[v] != u) continue;
                for (int c = 1; c <= 20; c++) {
                    int x = count[v][c];
                    ans += (int64_t)x * (total[c] - x);
                    count[u][c] += x;
                }
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3787_find_diameter_endpoints_of_a_tree
CONFIG class=Solution method=findSpecialNodes params=['n', 'edges'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::string', 'findSpecialNodes', 'int n, std::vector<std::vector<int>>& edges'), ('std::vector<std::vector<int>>', 'g', 'n'), ('std::vector<int>', 'dist', 'n, -1'), ('std::string', 'ans', "n, '0'")]
--- CPP ---
// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::string findSpecialNodes(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        auto bfs = [&](int start) {
            std::vector<int> dist(n, -1);
            dist[start] = 0;
            std::vector<int> q;
            q.push_back(start);
            int far = start;
            for (int head = 0; head < (int)q.size(); head++) {
                int u = q[head];
                if (dist[u] > dist[far]) far = u;
                for (int v : g[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }
            return std::make_pair(far, dist);
        };
        auto [a, _] = bfs(0);
        auto [b, dist1] = bfs(a);
        auto [__, dist2] = bfs(b);
        (void)__;
        int d = dist1[b];
        std::string ans(n, '0');
        for (int i = 0; i < n; i++) {
            if (dist1[i] == d || dist2[i] == d) ans[i] = '1';
        }
        return ans;
    }
};

================================================================================
FOLDER 3788_maximum_score_of_a_split
CONFIG class=Solution method=maximumScore params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'maximumScore', 'std::vector<int>& nums'), ('std::vector<int64_t>', 'suf', 'n')]
--- CPP ---
// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

#include <algorithm>
#include <cstdint>
#include <limits>
#include <vector>

class Solution {
public:
    long long maximumScore(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int64_t> suf(n);
        suf[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) suf[i] = std::min((int64_t)nums[i], suf[i + 1]);
        int64_t pre = 0;
        int64_t ans = std::numeric_limits<int64_t>::min();
        for (int i = 0; i < n - 1; i++) {
            pre += nums[i];
            ans = std::max(ans, pre - suf[i + 1]);
        }
        return ans;
    }
};

================================================================================
FOLDER 3789_minimum_cost_to_acquire_required_items
CONFIG class=Solution method=minimumCost params=['cost1', 'cost2', 'costBoth', 'need1', 'need2'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'minimumCost', 'int cost1, int cost2, int costBoth, int need1, int need2')]
--- CPP ---
// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

#include <algorithm>
#include <cstdint>

class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        int64_t a = (int64_t)need1 * cost1 + (int64_t)need2 * cost2;
        int64_t b = (int64_t)costBoth * std::max(need1, need2);
        int mn = std::min(need1, need2);
        int64_t c = (int64_t)costBoth * mn + (int64_t)(need1 - mn) * cost1 + (int64_t)(need2 - mn) * cost2;
        return std::min({a, b, c});
    }
};

================================================================================
FOLDER 3790_smallest_all_ones_multiple
CONFIG class=Solution method=minAllOneMultiple params=['k'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minAllOneMultiple', 'int k')]
--- CPP ---
// LeetCode 3790 - Smallest All Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/

class Solution {
public:
    int minAllOneMultiple(int k) {
        if ((k & 1) == 0) return -1;
        int x = 1 % k;
        int ans = 1;
        for (int i = 0; i < k; i++) {
            x = (x * 10 + 1) % k;
            ans++;
            if (x == 0) return ans;
        }
        return -1;
    }
};

================================================================================
FOLDER 3791_number_of_balanced_integers_in_a_range
CONFIG class=Solution method=countBalanced params=['low', 'high'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int64_t', 'dfs', 'int pos, int diff, bool lim'), ('public:\n    long long', 'countBalanced', 'long long low, long long high')]
--- CPP ---
// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

#include <cstdint>
#include <cstring>
#include <string>

class Solution {
    static constexpr int BASE = 90;
    std::string num;
    int64_t f[20][181];

    int64_t dfs(int pos, int diff, bool lim) {
        if (pos >= (int)num.size()) return diff == 0 ? 1 : 0;
        if (!lim && f[pos][diff + BASE] != -1) return f[pos][diff + BASE];
        int up = lim ? num[pos] - '0' : 9;
        int64_t res = 0;
        for (int i = 0; i <= up; i++) {
            if (pos % 2 == 0) res += dfs(pos + 1, diff + i, lim && i == up);
            else res += dfs(pos + 1, diff - i, lim && i == up);
        }
        if (!lim) f[pos][diff + BASE] = res;
        return res;
    }

public:
    long long countBalanced(long long low, long long high) {
        if (high < 11) return 0;
        if (low < 11) low = 11;
        num = std::to_string(low - 1);
        std::memset(f, -1, sizeof(f));
        int64_t a = dfs(0, 0, true);
        num = std::to_string(high);
        std::memset(f, -1, sizeof(f));
        int64_t b = dfs(0, 0, true);
        return b - a;
    }
};

================================================================================
FOLDER 3792_sum_of_increasing_product_blocks
CONFIG class=Solution method=sumOfBlocks params=['n'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'sumOfBlocks', 'int n')]
--- CPP ---
// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

class Solution {
public:
    int sumOfBlocks(int n) {
        const int MOD = 1e9 + 7;
        int ans = 0, k = 1;
        for (int i = 1; i <= n; i++) {
            int x = 1;
            for (int j = k; j < k + i; j++) x = (int)((long long)x * j % MOD);
            ans = (ans + x) % MOD;
            k += i;
        }
        return ans;
    }
};

================================================================================
FOLDER 3794_reverse_string_prefix
CONFIG class=Solution method=reversePrefix params=['s', 'k'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::string', 'reversePrefix', 'std::string s, int k')]
--- CPP ---
// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string reversePrefix(std::string s, int k) {
        std::reverse(s.begin(), s.begin() + k);
        return s;
    }
};

================================================================================
FOLDER 3795_minimum_subarray_length_with_distinct_sum_at_least_k
CONFIG class=Solution method=minLength params=['nums', 'k'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minLength', 'std::vector<int>& nums, int k')]
--- CPP ---
// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

#include <cstdint>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minLength(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        int ans = n + 1, l = 0;
        std::unordered_map<int, int> cnt;
        int64_t s = 0;
        for (int r = 0; r < n; r++) {
            if (++cnt[nums[r]] == 1) s += nums[r];
            while (s >= k) {
                if (r - l + 1 < ans) ans = r - l + 1;
                if (--cnt[nums[l]] == 0) s -= nums[l];
                l++;
            }
        }
        return ans > n ? -1 : ans;
    }
};

================================================================================
FOLDER 3796_find_maximum_value_in_a_constrained_sequence
CONFIG class=Solution method=maxValue params=['n', 'restrictions', 'diff'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'maxValue', 'int n, std::vector<std::vector<int>>& restrictions, std::vector<int>& diff'), ('std::vector<int>', 'bound', 'n, INF')]
--- CPP ---
// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxValue(int n, std::vector<std::vector<int>>& restrictions, std::vector<int>& diff) {
        const int INF = INT_MAX / 4;
        std::vector<int> bound(n, INF);
        bound[0] = 0;
        for (auto& r : restrictions) bound[r[0]] = r[1];
        for (int i = 1; i < n; i++) bound[i] = std::min(bound[i], bound[i - 1] + diff[i - 1]);
        for (int i = n - 2; i >= 0; i--) bound[i] = std::min(bound[i], bound[i + 1] + diff[i]);
        return *std::max_element(bound.begin(), bound.end());
    }
};

================================================================================
FOLDER 3797_count_routes_to_climb_a_rectangular_grid
CONFIG class=Solution method=countRoutes params=['grid', 'd'] kind=None ncases=4
CPP_CLASS Solution METHODS [('int', 'countRoutes', 'std::vector<std::string>& grid, int d'), ('std::vector<int>', 'arrived', 'm, 0'), ('std::vector<int>', 'pref', 'm + 1, 0'), ('std::vector<int>', 'horizontal', 'm, 0'), ('std::vector<int>', 'pref', 'm + 1, 0'), ('std::vector<int>', 'next', 'm, 0')]
--- CPP ---
// LeetCode 3797 - Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

#include <algorithm>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    int countRoutes(std::vector<std::string>& grid, int d) {
        const int MOD = 1000000007;
        int n = (int)grid.size(), m = (int)grid[0].size();
        int upRadius = 0;
        while ((upRadius + 1) * (upRadius + 1) + 1 <= d * d) upRadius++;
        std::vector<int> arrived(m, 0);
        for (int c = 0; c < m; c++) {
            if (grid[n - 1][c] == '.') arrived[c] = 1;
        }
        auto rowWays = [&](int row, const std::vector<int>& base) {
            std::vector<int> pref(m + 1, 0);
            for (int i = 0; i < m; i++) pref[i + 1] = (pref[i] + base[i]) % MOD;
            std::vector<int> horizontal(m, 0);
            for (int c = 0; c < m; c++) {
                if (grid[row][c] == '#') continue;
                int l = std::max(0, c - d), r = std::min(m - 1, c + d);
                horizontal[c] = (pref[r + 1] - pref[l] - base[c]) % MOD;
                if (horizontal[c] < 0) horizontal[c] += MOD;
            }
            return std::make_pair(base, horizontal);
        };
        for (int r = n - 1; r >= 0; r--) {
            auto [base, horizontal] = rowWays(r, arrived);
            if (r == 0) {
                int ans = 0;
                for (int c = 0; c < m; c++) ans = (ans + base[c] + horizontal[c]) % MOD;
                return ans;
            }
            std::vector<int> pref(m + 1, 0);
            for (int c = 0; c < m; c++) pref[c + 1] = (pref[c] + base[c] + horizontal[c]) % MOD;
            std::vector<int> next(m, 0);
            for (int c = 0; c < m; c++) {
                if (grid[r - 1][c] == '#') continue;
                int l = std::max(0, c - upRadius), rr = std::min(m - 1, c + upRadius);
                next[c] = pref[rr + 1] - pref[l];
                if (next[c] < 0) next[c] += MOD;
            }
            arrived = std::move(next);
        }
        return 0;
    }
};

================================================================================
FOLDER 3798_largest_even_number
CONFIG class=Solution method=largestEven params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::string', 'largestEven', 'std::string s')]
--- CPP ---
// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

#include <string>

class Solution {
public:
    std::string largestEven(std::string s) {
        while (!s.empty() && s.back() == '1') s.pop_back();
        return s;
    }
};

================================================================================
FOLDER 3799_word_squares_ii
CONFIG class=Solution method=wordSquares params=['words'] kind=None ncases=2
CPP_CLASS Solution METHODS [('std::vector<std::vector<std::string>>', 'wordSquares', 'std::vector<std::string>& words')]
--- CPP ---
// LeetCode 3799 - Word Squares Ii
// https://leetcode.com/problems/word-squares-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> wordSquares(std::vector<std::string>& words) {
        std::sort(words.begin(), words.end());
        int n = (int)words.size();
        std::vector<std::vector<std::string>> ans;
        for (int i = 0; i < n; i++) {
            const std::string& top = words[i];
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                const std::string& left = words[j];
                for (int k = 0; k < n; k++) {
                    if (k == j || k == i) continue;
                    const std::string& right = words[k];
                    for (int h = 0; h < n; h++) {
                        if (h == k || h == j || h == i) continue;
                        const std::string& bottom = words[h];
                        if (top[0] == left[0] && top[3] == right[0] &&
                            bottom[0] == left[3] && bottom[3] == right[3]) {
                            ans.push_back({top, left, right, bottom});
                        }
                    }
                }
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3800_minimum_cost_to_make_two_binary_strings_equal
CONFIG class=Solution method=minimumCost params=['s', 't', 'flipCost', 'swapCost', 'crossCost'] kind=None ncases=3
CPP_CLASS Solution METHODS [('long long', 'minimumCost', 'std::string s, std::string t, int flipCost, int swapCost, int crossCost')]
--- CPP ---
// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

#include <algorithm>
#include <cstdint>
#include <string>

class Solution {
public:
    long long minimumCost(std::string s, std::string t, int flipCost, int swapCost, int crossCost) {
        int64_t diff[2] = {0, 0};
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            if (s[i] != t[i]) diff[s[i] - '0']++;
        }
        int64_t ans = (diff[0] + diff[1]) * flipCost;
        int64_t mx = std::max(diff[0], diff[1]);
        int64_t mn = std::min(diff[0], diff[1]);
        ans = std::min(ans, mn * swapCost + (mx - mn) * flipCost);
        int64_t avg = (mx + mn) / 2;
        ans = std::min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost);
        return ans;
    }
};

================================================================================
FOLDER 3801_minimum_cost_to_merge_sorted_lists
CONFIG class=Solution method=minMergeCost params=['lists'] kind=None ncases=4
CPP_CLASS Solution METHODS [('long long', 'minMergeCost', 'std::vector<std::vector<int>>& lists'), ('std::vector<std::vector<int>>', 'merged', 'totalMasks'), ('std::vector<int>', 'length', 'totalMasks'), ('std::vector<int64_t>', 'dp', 'totalMasks, 0')]
--- CPP ---
// LeetCode 3801 - Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long minMergeCost(std::vector<std::vector<int>>& lists) {
        int m = (int)lists.size();
        int totalMasks = 1 << m;
        std::vector<std::vector<int>> merged(totalMasks);
        std::vector<int> length(totalMasks), median(totalMasks);
        for (int mask = 1; mask < totalMasks; mask++) {
            int bit = mask & -mask;
            int index = 0;
            while ((1 << index) != bit) index++;
            auto& previous = merged[mask ^ bit];
            auto& current = lists[index];
            std::vector<int> out;
            out.reserve(previous.size() + current.size());
            int i = 0, j = 0;
            while (i < (int)previous.size() || j < (int)current.size()) {
                if (j == (int)current.size() || (i < (int)previous.size() && previous[i] <= current[j])) {
                    out.push_back(previous[i++]);
                } else {
                    out.push_back(current[j++]);
                }
            }
            merged[mask] = out;
            length[mask] = (int)out.size();
            median[mask] = out[(out.size() - 1) / 2];
        }
        const int64_t INF = 1LL << 62;
        std::vector<int64_t> dp(totalMasks, 0);
        for (int mask = 1; mask < totalMasks; mask++) {
            if ((mask & (mask - 1)) == 0) continue;
            dp[mask] = INF;
            int firstBit = mask & -mask;
            for (int left = (mask - 1) & mask; left > 0; left = (left - 1) & mask) {
                if ((left & firstBit) == 0) continue;
                int right = mask ^ left;
                if (right == 0) continue;
                int diff = median[left] - median[right];
                if (diff < 0) diff = -diff;
                int64_t candidate = dp[left] + dp[right] + length[mask] + diff;
                if (candidate < dp[mask]) dp[mask] = candidate;
            }
        }
        return dp[totalMasks - 1];
    }
};

================================================================================
FOLDER 3802_number_of_ways_to_paint_sheets
CONFIG class=Solution method=numberOfWays params=['n', 'limit'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'numberOfWays', 'int n, std::vector<int>& limit'), ('', 'return', 'int64_t'), ('', 'return', 'int')]
--- CPP ---
// LeetCode 3802 - Number of Ways to Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    int numberOfWays(int n, std::vector<int>& limit) {
        const int64_t MOD = 1000000007;
        std::sort(limit.begin(), limit.end());
        std::vector<int> points = {1, n};
        for (int x : limit) {
            if (x + 1 > 1 && x + 1 < n) points.push_back(x + 1);
            if (n - x > 1 && n - x < n) points.push_back(n - x);
        }
        std::sort(points.begin(), points.end());
        points.erase(std::unique(points.begin(), points.end()), points.end());
        auto countGE = [&](int x) -> int64_t {
            return (int64_t)(limit.end() - std::lower_bound(limit.begin(), limit.end(), x));
        };
        int64_t ans = 0;
        for (int i = 0; i + 1 < (int)points.size(); i++) {
            int x = points[i];
            int64_t a = countGE(x), b = countGE(n - x);
            int64_t same = countGE(std::max(x, n - x));
            int64_t ways = (a * b - same) % MOD;
            int64_t length = points[i + 1] - x;
            ans = (ans + ways * length) % MOD;
        }
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
};

================================================================================
FOLDER 3803_count_residue_prefixes
CONFIG class=Solution method=residuePrefixes params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'residuePrefixes', 'std::string s')]
--- CPP ---
// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

#include <string>
#include <unordered_set>

class Solution {
public:
    int residuePrefixes(std::string s) {
        std::unordered_set<char> st;
        int ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            st.insert(s[i]);
            if ((int)st.size() == (i + 1) % 3) ans++;
        }
        return ans;
    }
};

================================================================================
FOLDER 3804_number_of_centered_subarrays
CONFIG class=Solution method=centeredSubarrays params=['nums'] kind=None ncases=2
CPP_CLASS Solution METHODS [('int', 'centeredSubarrays', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int centeredSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::unordered_set<int> st;
            int s = 0;
            for (int j = i; j < n; j++) {
                s += nums[j];
                st.insert(nums[j]);
                if (st.count(s)) ans++;
            }
        }
        return ans;
    }
};

================================================================================
FOLDER 3805_count_caesar_cipher_pairs
CONFIG class=Solution method=countPairs params=['words'] kind=None ncases=2
CPP_CLASS Solution METHODS [('long long', 'countPairs', 'std::vector<std::string>& words')]
--- CPP ---
// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countPairs(std::vector<std::string>& words) {
        std::unordered_map<std::string, int> cnt;
        for (auto s : words) {
            int k = 'z' - s[0];
            for (int i = 1; i < (int)s.size(); i++) {
                s[i] = 'a' + (s[i] - 'a' + k) % 26;
            }
            s[0] = 'z';
            cnt[s]++;
        }
        int64_t ans = 0;
        for (auto& [_, v] : cnt) ans += (int64_t)v * (v - 1) / 2;
        return ans;
    }
};

================================================================================
FOLDER 3806_maximum_bitwise_and_after_increment_operations
CONFIG class=Solution method=maximumAND params=['nums', 'k', 'm'] kind=None ncases=3
CPP_CLASS Solution METHODS [('static int', 'bitLen', 'unsigned x'), ('public:\n    int', 'maximumAND', 'std::vector<int>& nums, int k, int m'), ('std::vector<int>', 'cost', 'nums.size(')]
--- CPP ---
// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

#include <algorithm>
#include <vector>

class Solution {
    static int bitLen(unsigned x) {
        return x == 0 ? 0 : 32 - __builtin_clz(x);
    }

public:
    int maximumAND(std::vector<int>& nums, int k, int m) {
        int mxVal = *std::max_element(nums.begin(), nums.end()) + k;
        int mx = bitLen((unsigned)mxVal);
        int ans = 0;
        std::vector<int> cost(nums.size());
        for (int bit = mx - 1; bit >= 0; bit--) {
            int target = ans | (1 << bit);
            for (int i = 0; i < (int)nums.size(); i++) {
                int x = nums[i];
                int j = bitLen((unsigned)(target & ~x));
                int mask = (1 << j) - 1;
                cost[i] = (target & mask) - (x & mask);
            }
            std::sort(cost.begin(), cost.end());
            int sum = 0;
            for (int i = 0; i < m; i++) sum += cost[i];
            if (sum <= k) ans = target;
        }
        return ans;
    }
};

================================================================================
FOLDER 3807_minimum_cost_to_repair_edges_to_traverse_a_graph
CONFIG class=Solution method=minCost params=['n', 'edges', 'k'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minCost', 'int n, std::vector<std::vector<int>>& edges, int k'), ('std::vector<std::vector<int>>', 'g', 'n'), ('std::vector<char>', 'vis', 'n, 0')]
--- CPP ---
// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minCost(int n, std::vector<std::vector<int>>& edges, int k) {
        std::sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
        auto check = [&](int idx) {
            std::vector<std::vector<int>> g(n);
            for (int i = 0; i <= idx; i++) {
                g[edges[i][0]].push_back(edges[i][1]);
                g[edges[i][1]].push_back(edges[i][0]);
            }
            std::vector<int> q = {0};
            std::vector<char> vis(n, 0);
            vis[0] = 1;
            int dist = 0;
            while (!q.empty()) {
                std::vector<int> nq;
                for (int u : q) {
                    if (u == n - 1) return dist <= k;
                    for (int v : g[u]) {
                        if (!vis[v]) {
                            vis[v] = 1;
                            nq.push_back(v);
                        }
                    }
                }
                q = std::move(nq);
                dist++;
            }
            return false;
        };
        int m = (int)edges.size();
        if (m == 0) return -1;
        int l = 0, r = m - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (check(mid)) r = mid;
            else l = mid + 1;
        }
        if (check(l)) return edges[l][2];
        return -1;
    }
};

================================================================================
FOLDER 3809_best_reachable_tower
CONFIG class=Solution method=bestTower params=['towers', 'center', 'radius'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::vector<int>', 'bestTower', 'std::vector<std::vector<int>>& towers, std::vector<int>& center, int radius')]
--- CPP ---
// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> bestTower(std::vector<std::vector<int>>& towers, std::vector<int>& center, int radius) {
        int cx = center[0], cy = center[1];
        int idx = -1;
        for (int i = 0; i < (int)towers.size(); i++) {
            int x = towers[i][0], y = towers[i][1], q = towers[i][2];
            int dist = std::abs(x - cx) + std::abs(y - cy);
            if (dist > radius) continue;
            if (idx == -1 || towers[idx][2] < q ||
                (towers[idx][2] == q &&
                 (x < towers[idx][0] || (x == towers[idx][0] && y < towers[idx][1])))) {
                idx = i;
            }
        }
        if (idx == -1) return {-1, -1};
        return {towers[idx][0], towers[idx][1]};
    }
};

================================================================================
FOLDER 3810_minimum_operations_to_reach_target_array
CONFIG class=Solution method=minOperations params=['nums', 'target'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minOperations', 'std::vector<int>& nums, std::vector<int>& target'), ('', 'return', 'int')]
--- CPP ---
// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, std::vector<int>& target) {
        std::unordered_set<int> s;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] != target[i]) s.insert(nums[i]);
        }
        return (int)s.size();
    }
};

================================================================================
FOLDER 3811_number_of_alternating_xor_partitions
CONFIG class=Solution method=alternatingXOR params=['nums', 'target1', 'target2'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'alternatingXOR', 'std::vector<int>& nums, int target1, int target2')]
--- CPP ---
// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int alternatingXOR(std::vector<int>& nums, int target1, int target2) {
        const int MOD = 1000000007;
        std::unordered_map<int, int> cnt1, cnt2;
        cnt2[0] = 1;
        int pre = 0, ans = 0;
        for (int x : nums) {
            pre ^= x;
            int a = cnt2[pre ^ target1];
            int b = cnt1[pre ^ target2];
            ans = (a + b) % MOD;
            cnt1[pre] = (cnt1[pre] + a) % MOD;
            cnt2[pre] = (cnt2[pre] + b) % MOD;
        }
        return ans;
    }
};

================================================================================
FOLDER 3812_minimum_edge_toggles_on_a_tree
CONFIG class=Solution method=minimumFlips params=['n', 'edges', 'start', 'target'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::vector<int>', 'minimumFlips', 'int n, std::vector<std::vector<int>>& edges, std::string start, std::string target'), ('std::vector<std::vector<std::pair<int, int>>>', 'g', 'n')]
--- CPP ---
// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

#include <algorithm>
#include <functional>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> minimumFlips(int n, std::vector<std::vector<int>>& edges, std::string start, std::string target) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (int i = 0; i < n - 1; i++) {
            int a = edges[i][0], b = edges[i][1];
            g[a].push_back({b, i});
            g[b].push_back({a, i});
        }
        std::vector<int> ans;
        std::function<bool(int, int)> dfs = [&](int a, int fa) {
            bool rev = start[a] != target[a];
            for (auto [b, i] : g[a]) {
                if (b != fa && dfs(b, a)) {
                    ans.push_back(i);
                    rev = !rev;
                }
            }
            return rev;
        };
        if (dfs(0, -1)) return {-1};
        std::sort(ans.begin(), ans.end());
        return ans;
    }
};

================================================================================
FOLDER 3813_vowel_consonant_score
CONFIG class=Solution method=vowelConsonantScore params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'vowelConsonantScore', 'std::string s')]
--- CPP ---
// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

#include <cctype>
#include <string>

class Solution {
public:
    int vowelConsonantScore(std::string s) {
        int v = 0, c = 0;
        for (char ch : s) {
            if (std::isalpha(static_cast<unsigned char>(ch))) {
                c++;
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') v++;
            }
        }
        c -= v;
        if (c == 0) return 0;
        return v / c;
    }
};

================================================================================
FOLDER 3814_maximum_capacity_within_budget
CONFIG class=Solution method=maxCapacity params=['costs', 'capacity', 'budget'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'maxCapacity', 'std::vector<int>& costs, std::vector<int>& capacity, int budget'), ('std::vector<char>', 'alive', 'm, 1'), ('std::priority_queue<Node, std::vector<Node>,', 'decltype', 'cmp')]
--- CPP ---
// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

#include <algorithm>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int maxCapacity(std::vector<int>& costs, std::vector<int>& capacity, int budget) {
        std::vector<std::pair<int, int>> arr;
        for (int k = 0; k < (int)costs.size(); k++) {
            if (costs[k] < budget) arr.push_back({costs[k], capacity[k]});
        }
        if (arr.empty()) return 0;
        std::sort(arr.begin(), arr.end());
        int m = (int)arr.size();
        std::vector<char> alive(m, 1);
        using Node = std::pair<int, int>;
        auto cmp = [](const Node& a, const Node& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        };
        std::priority_queue<Node, std::vector<Node>, decltype(cmp)> h(cmp);
        for (int i = 0; i < m; i++) h.push({arr[i].second, i});
        while (!h.empty() && !alive[h.top().second]) h.pop();
        int ans = h.top().first;
        int i = 0, j = m - 1;
        while (i < j) {
            alive[i] = 0;
            while (i < j && arr[i].first + arr[j].first >= budget) {
                alive[j] = 0;
                j--;
            }
            while (!h.empty() && !alive[h.top().second]) h.pop();
            if (!h.empty()) ans = std::max(ans, arr[i].second + h.top().first);
            i++;
        }
        return ans;
    }
};

================================================================================
FOLDER 3815_design_auction_system
CONFIG class=AuctionSystem method=None params=None kind=None ncases=1
CPP_CLASS AuctionSystem METHODS [('public:', 'AuctionSystem', ''), ('void', 'addBid', 'int userId, int itemId, int bidAmount'), ('void', 'updateBid', 'int userId, int itemId, int newAmount'), ('', 'addBid', 'userId, itemId, newAmount'), ('void', 'removeBid', 'int userId, int itemId'), ('int', 'getHighestBidder', 'int itemId')]
--- CPP ---
// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

class AuctionSystem {
    struct Bid {
        int amount;
        int userID;
        bool operator<(const Bid& o) const {
            if (amount != o.amount) return amount < o.amount;
            return userID < o.userID;
        }
    };
    std::unordered_map<int, std::unordered_map<int, int>> bids;
    std::unordered_map<int, std::priority_queue<Bid>> heaps;

public:
    AuctionSystem() {}

    void addBid(int userId, int itemId, int bidAmount) {
        bids[itemId][userId] = bidAmount;
        heaps[itemId].push({bidAmount, userId});
    }

    void updateBid(int userId, int itemId, int newAmount) {
        addBid(userId, itemId, newAmount);
    }

    void removeBid(int userId, int itemId) {
        bids[itemId].erase(userId);
    }

    int getHighestBidder(int itemId) {
        auto it = heaps.find(itemId);
        if (it == heaps.end()) return -1;
        auto& h = it->second;
        while (!h.empty()) {
            Bid top = h.top();
            auto bit = bids[itemId].find(top.userID);
            if (bit != bids[itemId].end() && bit->second == top.amount) return top.userID;
            h.pop();
        }
        return -1;
    }
};

================================================================================
FOLDER 3816_lexicographically_smallest_string_after_deleting_duplicate_characters
CONFIG class=Solution method=lexSmallestAfterDeletion params=['s'] kind=None ncases=2
CPP_CLASS Solution METHODS [('std::string', 'lexSmallestAfterDeletion', 'std::string s')]
--- CPP ---
// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

#include <string>
#include <vector>

class Solution {
public:
    std::string lexSmallestAfterDeletion(std::string s) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        std::string stk;
        for (char c : s) {
            while (!stk.empty() && stk.back() > c && cnt[stk.back() - 'a'] > 1) {
                cnt[stk.back() - 'a']--;
                stk.pop_back();
            }
            stk.push_back(c);
        }
        while (cnt[stk.back() - 'a'] > 1) {
            cnt[stk.back() - 'a']--;
            stk.pop_back();
        }
        return stk;
    }
};

================================================================================
FOLDER 3817_good_indices_in_a_digit_string
CONFIG class=Solution method=goodIndices params=['s'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::vector<int>', 'goodIndices', 'std::string s')]
--- CPP ---
// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> goodIndices(std::string s) {
        std::vector<int> ans;
        for (int i = 0; i < (int)s.size(); i++) {
            std::string t = std::to_string(i);
            int k = (int)t.size();
            if (i + 1 - k >= 0 && s.substr(i + 1 - k, k) == t) ans.push_back(i);
        }
        return ans;
    }
};

================================================================================
FOLDER 3818_minimum_prefix_removal_to_make_array_strictly_increasing
CONFIG class=Solution method=minimumPrefixLength params=['nums'] kind=None ncases=3
CPP_CLASS Solution METHODS [('int', 'minimumPrefixLength', 'std::vector<int>& nums')]
--- CPP ---
// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

#include <vector>

class Solution {
public:
    int minimumPrefixLength(std::vector<int>& nums) {
        for (int i = (int)nums.size() - 1; i > 0; i--) {
            if (nums[i - 1] >= nums[i]) return i;
        }
        return 0;
    }
};

================================================================================
FOLDER 3819_rotate_non_negative_elements
CONFIG class=Solution method=rotateElements params=['nums', 'k'] kind=None ncases=3
CPP_CLASS Solution METHODS [('std::vector<int>', 'rotateElements', 'std::vector<int>& nums, int k'), ('std::vector<int>', 'd', 'm')]
--- CPP ---
// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

#include <vector>

class Solution {
public:
    std::vector<int> rotateElements(std::vector<int>& nums, int k) {
        std::vector<int> t;
        for (int x : nums) if (x >= 0) t.push_back(x);
        int m = (int)t.size();
        if (m == 0) return nums;
        std::vector<int> d(m);
        for (int i = 0; i < m; i++) d[((i - k) % m + m) % m] = t[i];
        int j = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] >= 0) nums[i] = d[j++];
        }
        return nums;
    }
};
