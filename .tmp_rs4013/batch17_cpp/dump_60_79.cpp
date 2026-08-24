

########## 3458_select_k_disjoint_special_substrings ##########
// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

#include <string>
#include <vector>
#include <algorithm>
#include <set>

class Solution {
public:
    bool maxSubstringLength(std::string s, int k) {
        int n = (int)s.size();
        std::vector<int> first(26, n), last(26, -1);
        for (int i = 0; i < n; i++) {
            int ci = s[i] - 'a';
            if (first[ci] == n) first[ci] = i;
            last[ci] = i;
        }
        std::vector<std::pair<int, int>> segs;
        for (int c = 0; c < 26; c++) {
            if (last[c] == -1) continue;
            int l = first[c], r = last[c];
            for (int i = l; i <= r; i++) {
                int ci = s[i] - 'a';
                if (first[ci] < l) {
                    l = first[ci];
                    i = l - 1;
                    continue;
                }
                if (last[ci] > r) r = last[ci];
            }
            if (!(l == 0 && r == n - 1)) segs.push_back({l, r});
        }
        std::set<std::pair<int, int>> uniq;
        std::vector<std::pair<int, int>> arr;
        for (auto& sg : segs) {
            if (uniq.insert(sg).second) arr.push_back(sg);
        }
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.second < b.second; });
        int cnt = 0, end = -1;
        for (auto& sg : arr) {
            if (sg.first > end) {
                cnt++;
                end = sg.second;
            }
        }
        return cnt >= k;
    }
};


########## 3459_length_of_longest_v_shaped_diagonal_segment ##########
// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

#include <vector>
#include <map>
#include <array>

class Solution {
public:
    int lenOfVDiagonal(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int dirs[4][2] = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
        int nextDir[4] = {1, 2, 3, 0};
        int ans = 0;
        std::map<std::array<int, 5>, int> memo;
        auto dfs = [&](auto&& self, int i, int j, int d, int turned, int expect) -> int {
            if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect) return 0;
            std::array<int, 5> key = {i, j, d, turned, expect};
            if (memo.count(key)) return memo[key];
            int ni = i + dirs[d][0], nj = j + dirs[d][1];
            int nx = (expect == 2) ? 0 : 2;
            int best = 1 + self(self, ni, nj, d, turned, nx);
            if (turned == 0) {
                int nd = nextDir[d];
                int ti = i + dirs[nd][0], tj = j + dirs[nd][1];
                int cand = 1 + self(self, ti, tj, nd, 1, nx);
                if (cand > best) best = cand;
            }
            return memo[key] = best;
        };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 1) continue;
                for (int d = 0; d < 4; d++) {
                    int ni = i + dirs[d][0], nj = j + dirs[d][1];
                    int best = 1 + dfs(dfs, ni, nj, d, 0, 2);
                    if (best > ans) ans = best;
                }
                if (ans < 1) ans = 1;
            }
        }
        return ans;
    }
};


########## 3460_longest_common_prefix_after_at_most_one_removal ##########
// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

#include <string>

class Solution {
public:
    int longestCommonPrefix(std::string s, std::string t) {
        int i = 0, j = 0;
        bool removed = false;
        while (i < (int)s.size() && j < (int)t.size()) {
            if (s[i] == t[j]) {
                i++;
                j++;
                continue;
            }
            if (removed) break;
            removed = true;
            i++;
        }
        return j;
    }
};


########## 3461_check_if_digits_are_equal_in_string_after_operations_i ##########
// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

#include <string>
#include <vector>

class Solution {
public:
    bool hasSameDigits(std::string s) {
        std::vector<char> b(s.begin(), s.end());
        while ((int)b.size() > 2) {
            std::vector<char> nb(b.size() - 1);
            for (int i = 0; i + 1 < (int)b.size(); i++) {
                nb[i] = char('0' + (b[i] - '0' + b[i + 1] - '0') % 10);
            }
            b.swap(nb);
        }
        return b[0] == b[1];
    }
};


########## 3462_maximum_sum_with_at_most_k_elements ##########
// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    long long maxSum(std::vector<std::vector<int>>& grid, std::vector<int>& limits, int k) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> h;
        long long sum = 0;
        for (int i = 0; i < (int)grid.size(); i++) {
            std::vector<int> r = grid[i];
            std::sort(r.rbegin(), r.rend());
            int lim = limits[i];
            if (lim > (int)r.size()) lim = (int)r.size();
            for (int j = 0; j < lim; j++) {
                h.push(r[j]);
                sum += r[j];
                if ((int)h.size() > k) {
                    sum -= h.top();
                    h.pop();
                }
            }
        }
        return sum;
    }
};


########## 3463_check_if_digits_are_equal_in_string_after_operations_ii ##########
// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

#include <string>

class Solution {
    int modPowP(int a, int e, int p) {
        int r = 1;
        while (e > 0) {
            if (e & 1) r = r * a % p;
            a = a * a % p;
            e >>= 1;
        }
        return r;
    }
    int modInvPrime(int a, int p) { return modPowP(a, p - 2, p); }
    int binomMod(int n, int k, int p) {
        if (k < 0 || k > n) return 0;
        int num = 1, den = 1;
        for (int i = 0; i < k; i++) {
            num = num * (n - i) % p;
            den = den * (i + 1) % p;
        }
        return num * modInvPrime(den, p) % p;
    }
    int crt(int a1, int m1, int a2, int m2) {
        for (int x = 0; x < m1 * m2; x++) {
            if (x % m1 == a1 && x % m2 == a2) return x;
        }
        return 0;
    }
    int binomMod10(int n, int k) {
        return crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5);
    }
    int combineDigit(const std::string& s, int n, int offset) {
        int sum = 0;
        for (int i = 0; i <= n - 2; i++) {
            sum = (sum + binomMod10(n - 2, i) * (s[i + offset] - '0')) % 10;
        }
        return sum;
    }
public:
    bool hasSameDigits(std::string s) {
        int n = (int)s.size();
        return combineDigit(s, n, 0) == combineDigit(s, n, 1);
    }
};


########## 3464_maximize_the_distance_between_points_on_a_square ##########
// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

#include <vector>
#include <algorithm>

class Solution {
    bool canPlace(const std::vector<int>& arr, int perim, int k, int mid) {
        int n = (int)arr.size();
        for (int s = 0; s < n; s++) {
            int cnt = 1;
            int last = arr[s];
            int idx = s;
            for (; cnt < k;) {
                int target = last + mid;
                bool found = false;
                for (int step = 1; step < n; step++) {
                    int ni = (idx + step) % n;
                    int val = arr[ni];
                    int add = (ni <= idx) ? perim : 0;
                    if (val + add >= target) {
                        last = val + add;
                        idx = ni;
                        cnt++;
                        found = true;
                        break;
                    }
                }
                if (!found) break;
            }
            if (cnt == k && last - arr[s] <= perim - mid) return true;
        }
        return false;
    }
public:
    int maxDistance(int side, std::vector<std::vector<int>>& points, int k) {
        std::vector<int> arr(points.size());
        for (int i = 0; i < (int)points.size(); i++) {
            int x = points[i][0], y = points[i][1];
            int d;
            if (y == 0) d = x;
            else if (x == side) d = side + y;
            else if (y == side) d = 2 * side + (side - x);
            else d = 3 * side + (side - y);
            arr[i] = d;
        }
        std::sort(arr.begin(), arr.end());
        int perim = 4 * side;
        int lo = 0, hi = 2 * side;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (canPlace(arr, perim, k, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};


########## 3466_maximum_coin_collection ##########
// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

#include <vector>
#include <algorithm>
#include <cstdint>

class Solution {
public:
    long long maxCoins(std::vector<int>& lane1, std::vector<int>& lane2) {
        int n = (int)lane1.size();
        const long long neg = (long long)(-1LL << 60);
        long long dp[2][2];
        dp[0][0] = lane1[0];
        dp[1][0] = lane2[0];
        dp[0][1] = dp[1][1] = neg;
        long long ans = std::max(dp[0][0], dp[1][0]);
        for (int i = 1; i < n; i++) {
            long long ndp[2][2];
            ndp[0][0] = std::max(dp[0][0], 0LL) + lane1[i];
            ndp[1][0] = std::max(dp[1][0], 0LL) + lane2[i];
            ndp[0][1] = std::max(dp[0][1], dp[1][0]) + lane1[i];
            ndp[1][1] = std::max(dp[1][1], dp[0][0]) + lane2[i];
            if (lane1[i] > ndp[0][0]) ndp[0][0] = lane1[i];
            if (lane2[i] > ndp[1][0]) ndp[1][0] = lane2[i];
            for (int a = 0; a < 2; a++)
                for (int b = 0; b < 2; b++) {
                    dp[a][b] = ndp[a][b];
                    if (dp[a][b] > ans) ans = dp[a][b];
                }
        }
        return ans;
    }
};


########## 3467_transform_array_by_parity ##########
// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

#include <vector>

class Solution {
public:
    std::vector<int> transformArray(std::vector<int>& nums) {
        for (int i = 0; i < (int)nums.size(); i++) nums[i] %= 2;
        int j = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] == 0) {
                std::swap(nums[i], nums[j]);
                j++;
            }
        }
        return nums;
    }
};


########## 3468_find_the_number_of_copy_arrays ##########
// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

#include <vector>

class Solution {
public:
    int countArrays(std::vector<int>& original, std::vector<std::vector<int>>& bounds) {
        int n = (int)original.size();
        int lo = bounds[0][0], hi = bounds[0][1];
        for (int i = 1; i < n; i++) {
            int diff = original[i] - original[i - 1];
            int lo2 = bounds[i][0], hi2 = bounds[i][1];
            int nlo = lo + diff, nhi = hi + diff;
            if (nlo < lo2) nlo = lo2;
            if (nhi > hi2) nhi = hi2;
            if (nlo > nhi) return 0;
            lo = nlo;
            hi = nhi;
        }
        return hi - lo + 1;
    }
};


########## 3469_find_minimum_cost_to_remove_array_elements ##########
// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

#include <vector>
#include <map>
#include <array>
#include <algorithm>

class Solution {
    std::map<std::array<int, 2>, int> memo;
    std::vector<int> nums;
    int n;
    int max2(int a, int b) { return a > b ? a : b; }
    int min3(int a, int b, int c) { return std::min(a, std::min(b, c)); }
    int dfs(int i, int prev) {
        if (i >= n) return prev == -1 ? 0 : nums[prev];
        std::array<int, 2> key = {i, prev};
        if (memo.count(key)) return memo[key];
        int res;
        if (prev == -1) {
            if (i + 1 >= n) res = nums[i];
            else if (i + 2 >= n) res = max2(nums[i], nums[i + 1]);
            else {
                int a = nums[i], b = nums[i + 1], c = nums[i + 2];
                res = min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2));
            }
        } else {
            if (i + 1 >= n) res = max2(nums[prev], nums[i]);
            else {
                int a = nums[prev], b = nums[i], c = nums[i + 1];
                res = min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1));
            }
        }
        return memo[key] = res;
    }
public:
    int minCost(std::vector<int>& nums_) {
        nums = nums_;
        n = (int)nums.size();
        memo.clear();
        return dfs(0, -1);
    }
};


########## 3470_permutations_iv ##########
// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

#include <vector>

class Solution {
public:
    std::vector<int> permute(int n, long long k) {
        std::vector<long long> fact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i;
            if (fact[i] > (long long)1e18) fact[i] = (long long)1e18 + 1;
        }
        std::vector<bool> used(n + 1, false);
        std::vector<int> ans;
        auto dfs = [&](auto&& self, int pos) -> bool {
            if (pos == n) return true;
            for (int x = 1; x <= n; x++) {
                if (used[x]) continue;
                if (pos > 0 && (ans[pos - 1] % 2 == x % 2)) continue;
                int rem = n - pos - 1;
                long long cnt = fact[rem];
                if (cnt >= k) {
                    used[x] = true;
                    ans.push_back(x);
                    if (self(self, pos + 1)) return true;
                    ans.pop_back();
                    used[x] = false;
                } else {
                    k -= cnt;
                }
            }
            return false;
        };
        if (!dfs(dfs, 0)) return {};
        return ans;
    }
};


########## 3471_find_the_largest_almost_missing_integer ##########
// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int largestInteger(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::unordered_map<int, int> cnt;
        for (int i = 0; i + k <= n; i++) {
            std::unordered_set<int> seen;
            for (int j = i; j < i + k; j++) seen.insert(nums[j]);
            for (int x : seen) cnt[x]++;
        }
        int ans = -1;
        for (auto& [x, c] : cnt) {
            if (c == 1 && x > ans) ans = x;
        }
        return ans;
    }
};


########## 3472_longest_palindromic_subsequence_after_at_most_k_operations ##########
// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
    int distCirc(char a, char b) {
        int d = abs((int)a - (int)b);
        return std::min(d, 26 - d);
    }
public:
    int longestPalindromicSubsequence(std::string s, int k) {
        int n = (int)s.size();
        std::vector<std::vector<std::vector<int>>> dp(n, std::vector<std::vector<int>>(n, std::vector<int>(k + 1, -1)));
        auto dfs = [&](auto&& self, int i, int j, int ops) -> int {
            if (i > j) return 0;
            if (i == j) return 1;
            if (dp[i][j][ops] != -1) return dp[i][j][ops];
            int best = self(self, i + 1, j, ops);
            best = std::max(best, self(self, i, j - 1, ops));
            int cost = distCirc(s[i], s[j]);
            if (cost <= ops) best = std::max(best, 2 + self(self, i + 1, j - 1, ops - cost));
            return dp[i][j][ops] = best;
        };
        return dfs(dfs, 0, n - 1, k);
    }
};


########## 3473_sum_of_k_subarrays_with_length_at_least_m ##########
// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, int k, int m) {
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        const long long neg = (long long)(-1LL << 60);
        std::vector<std::vector<long long>> dp(k + 1, std::vector<long long>(n + 1, neg));
        for (int i = 0; i <= n; i++) dp[0][i] = 0;
        for (int t = 1; t <= k; t++) {
            long long best = neg;
            for (int i = t * m; i <= n; i++) {
                int j = i - m;
                best = std::max(best, dp[t - 1][j] - pref[j]);
                dp[t][i] = best + pref[i];
            }
            for (int i = 1; i <= n; i++) dp[t][i] = std::max(dp[t][i], dp[t][i - 1]);
        }
        return dp[k][n];
    }
};


########## 3474_lexicographically_smallest_generated_string ##########
// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

#include <string>
#include <vector>

class Solution {
public:
    std::string generateString(std::string str1, std::string str2) {
        int n = (int)str1.size(), m = (int)str2.size();
        int L = n + m - 1;
        std::string ans(L, '?');
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; j++) {
                    if (ans[i + j] != '?' && ans[i + j] != str2[j]) return "";
                    ans[i + j] = str2[j];
                }
            }
        }
        for (char& c : ans) if (c == '?') c = 'a';
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'F') {
                bool match = true;
                for (int j = 0; j < m; j++) if (ans[i + j] != str2[j]) { match = false; break; }
                if (match) {
                    bool changed = false;
                    for (int j = m - 1; j >= 0; j--) {
                        int pos = i + j;
                        bool forced = false;
                        for (int t = 0; t < n; t++) {
                            if (str1[t] == 'T' && pos >= t && pos < t + m) { forced = true; break; }
                        }
                        if (!forced) {
                            ans[pos] = 'b';
                            changed = true;
                            break;
                        }
                    }
                    if (!changed) return "";
                }
            }
        }
        for (int i = 0; i < n; i++) {
            bool match = true;
            for (int j = 0; j < m; j++) if (ans[i + j] != str2[j]) { match = false; break; }
            if (str1[i] == 'T' && !match) return "";
            if (str1[i] == 'F' && match) return "";
        }
        return ans;
    }
};


########## 3476_maximize_profit_from_task_assignment ##########
// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxProfit(std::vector<int>& workers, std::vector<std::vector<int>>& tasks) {
        std::sort(workers.begin(), workers.end());
        std::sort(tasks.begin(), tasks.end(), [](auto& a, auto& b) { return a[0] < b[0]; });
        long long ans = 0;
        std::vector<bool> used(tasks.size(), false);
        for (int w : workers) {
            int best = -1, bi = -1;
            for (int i = 0; i < (int)tasks.size(); i++) {
                if (used[i]) continue;
                if (tasks[i][0] > w) break;
                if (tasks[i][1] > best) {
                    best = tasks[i][1];
                    bi = i;
                }
            }
            if (bi >= 0) {
                used[bi] = true;
                ans += best;
            }
        }
        return ans;
    }
};


########## 3477_fruits_into_baskets_ii ##########
// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

#include <vector>

class Solution {
public:
    int numOfUnplacedFruits(std::vector<int>& fruits, std::vector<int>& baskets) {
        std::vector<bool> used(baskets.size(), false);
        int unplaced = 0;
        for (int f : fruits) {
            bool placed = false;
            for (int j = 0; j < (int)baskets.size(); j++) {
                if (!used[j] && baskets[j] >= f) {
                    used[j] = true;
                    placed = true;
                    break;
                }
            }
            if (!placed) unplaced++;
        }
        return unplaced;
    }
};


########## 3478_choose_k_elements_with_maximum_sum ##########
// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<long long> findMaxSum(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        int n = (int)nums1.size();
        struct Item { int v1, v2, i; };
        std::vector<Item> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {nums1[i], nums2[i], i};
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.v1 < b.v1; });
        std::vector<long long> ans(n);
        std::priority_queue<int, std::vector<int>, std::greater<int>> h;
        long long sum = 0;
        for (int i = 0; i < n;) {
            int v = arr[i].v1;
            int start = i;
            while (i < n && arr[i].v1 == v) i++;
            for (int t = start; t < i; t++) ans[arr[t].i] = sum;
            for (int t = start; t < i; t++) {
                h.push(arr[t].v2);
                sum += arr[t].v2;
                if ((int)h.size() > k) {
                    sum -= h.top();
                    h.pop();
                }
            }
        }
        return ans;
    }
};


########## 3479_fruits_into_baskets_iii ##########
// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

#include <vector>

class Solution {
public:
    int numOfUnplacedFruits(std::vector<int>& fruits, std::vector<int>& baskets) {
        int n = (int)baskets.size();
        int size = 1;
        while (size < n) size <<= 1;
        std::vector<int> tree(size * 2);
        for (int i = 0; i < n; i++) tree[size + i] = baskets[i];
        for (int i = size - 1; i > 0; i--) tree[i] = std::max(tree[i * 2], tree[i * 2 + 1]);
        auto find = [&](auto&& self, int node, int nl, int nr, int need) -> int {
            if (tree[node] < need) return -1;
            if (nl == nr) return nl;
            int mid = (nl + nr) / 2;
            int left = self(self, node * 2, nl, mid, need);
            if (left != -1) return left;
            return self(self, node * 2 + 1, mid + 1, nr, need);
        };
        auto update = [&](int idx) {
            int p = size + idx;
            tree[p] = -1;
            for (p >>= 1; p > 0; p >>= 1) tree[p] = std::max(tree[p * 2], tree[p * 2 + 1]);
        };
        int unplaced = 0;
        for (int f : fruits) {
            int idx = find(find, 1, 0, size - 1, f);
            if (idx == -1 || idx >= n) unplaced++;
            else update(idx);
        }
        return unplaced;
    }
};
