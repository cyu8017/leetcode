
================================================================================
// FOLDER: 2830_maximize_the_profit_as_the_salesman
================================================================================
// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximizeTheProfit(int n, std::vector<std::vector<int>>& offers) {
        std::vector<std::vector<std::vector<int>>> byEnd(n);
        for (auto& o : offers) byEnd[o[1]].push_back(o);
        std::vector<int> dp(n + 1, 0);
        for (int end = 0; end < n; end++) {
            dp[end + 1] = dp[end];
            for (auto& o : byEnd[end]) {
                dp[end + 1] = std::max(dp[end + 1], dp[o[0]] + o[2]);
            }
        }
        return dp[n];
    }
};

================================================================================
// FOLDER: 2831_find_the_longest_equal_subarray
================================================================================
// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestEqualSubarray(std::vector<int>& nums, int k) {
        std::unordered_map<int, std::vector<int>> pos;
        for (int i = 0; i < (int)nums.size(); i++) pos[nums[i]].push_back(i);
        int ans = 0;
        for (auto& [_, p] : pos) {
            int left = 0;
            for (int right = 0; right < (int)p.size(); right++) {
                while (p[right] - p[left] - (right - left) > k) left++;
                ans = std::max(ans, right - left + 1);
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2832_maximal_range_that_each_element_is_maximum_in_it
================================================================================
// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

#include <vector>

class Solution {
public:
    std::vector<int> maximumLength(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> left(n), right(n), st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && nums[st.back()] < nums[i]) st.pop_back();
            left[i] = st.empty() ? -1 : st.back();
            st.push_back(i);
        }
        st.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && nums[st.back()] <= nums[i]) st.pop_back();
            right[i] = st.empty() ? n : st.back();
            st.push_back(i);
        }
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = right[i] - left[i] - 1;
        return ans;
    }
};

================================================================================
// FOLDER: 2833_furthest_point_from_origin
================================================================================
// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

#include <cstdlib>
#include <string>

class Solution {
public:
    int furthestDistanceFromOrigin(std::string moves) {
        int L = 0, R = 0, u = 0;
        for (char c : moves) {
            if (c == 'L') L++;
            else if (c == 'R') R++;
            else u++;
        }
        return std::abs(L - R) + u;
    }
};

================================================================================
// FOLDER: 2834_find_the_minimum_possible_sum_of_a_beautiful_array
================================================================================
// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution {
public:
    int minimumPossibleSum(int n, int target) {
        const int MOD = 1000000007;
        int m = target / 2;
        if (n <= m) return (int)(1LL * n * (n + 1) / 2 % MOD);
        long long sum = 1LL * m * (m + 1) / 2;
        int remain = n - m;
        sum += 1LL * remain * target + 1LL * remain * (remain - 1) / 2;
        return (int)(sum % MOD);
    }
};

================================================================================
// FOLDER: 2835_minimum_operations_to_form_subsequence_with_target_sum
================================================================================
// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int target) {
        std::vector<int> cnt(32, 0);
        long long sum = 0;
        for (int v : nums) {
            sum += v;
            int b = 0;
            while ((1 << b) < v) b++;
            cnt[b]++;
        }
        if (sum < target) return -1;
        int ans = 0;
        for (int i = 0; i < 31; i++) {
            if (target & (1 << i)) {
                if (cnt[i] > 0) cnt[i]--;
                else {
                    int j = i + 1;
                    while (j < 32 && cnt[j] == 0) j++;
                    if (j == 32) return -1;
                    while (j > i) {
                        cnt[j]--;
                        cnt[j - 1] += 2;
                        ans++;
                        j--;
                    }
                    cnt[i]--;
                }
            }
            cnt[i + 1] += cnt[i] / 2;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2836_maximize_value_of_function_in_a_ball_passing_game
================================================================================
// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long getMaxFunctionValue(std::vector<int>& receiver, long long k) {
        int n = (int)receiver.size();
        const int LOG = 36;
        std::vector<std::vector<int>> up(LOG, std::vector<int>(n));
        std::vector<std::vector<long long>> sum(LOG, std::vector<long long>(n));
        for (int i = 0; i < n; i++) {
            up[0][i] = receiver[i];
            sum[0][i] = receiver[i];
        }
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                int mid = up[j - 1][i];
                up[j][i] = up[j - 1][mid];
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int cur = i;
            long long total = i;
            long long kk = k;
            for (int j = 0; j < LOG; j++) {
                if (kk & (1LL << j)) {
                    total += sum[j][cur];
                    cur = up[j][cur];
                }
            }
            ans = std::max(ans, total);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2838_maximum_coins_heroes_can_collect
================================================================================
// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> maximumCoins(std::vector<int>& heroes, std::vector<int>& monsters, std::vector<int>& coins) {
        int n = (int)monsters.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return monsters[a] < monsters[b]; });
        std::vector<long long> pref(n + 1);
        std::vector<int> ms(n);
        for (int i = 0; i < n; i++) {
            ms[i] = monsters[idx[i]];
            pref[i + 1] = pref[i] + coins[idx[i]];
        }
        std::vector<long long> ans(heroes.size());
        for (int i = 0; i < (int)heroes.size(); i++) {
            int p = (int)(std::upper_bound(ms.begin(), ms.end(), heroes[i]) - ms.begin());
            ans[i] = pref[p];
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2839_check_if_strings_can_be_made_equal_with_operations_i
================================================================================
// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

#include <algorithm>
#include <string>

class Solution {
public:
    bool canBeEqual(std::string s1, std::string s2) {
        std::string a{s1[0], s1[2]}, b{s2[0], s2[2]}, c{s1[1], s1[3]}, d{s2[1], s2[3]};
        std::sort(a.begin(), a.end());
        std::sort(b.begin(), b.end());
        std::sort(c.begin(), c.end());
        std::sort(d.begin(), d.end());
        return a == b && c == d;
    }
};

================================================================================
// FOLDER: 2840_check_if_strings_can_be_made_equal_with_operations_ii
================================================================================
// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

#include <array>
#include <string>

class Solution {
public:
    bool checkStrings(std::string s1, std::string s2) {
        std::array<int, 26> even1{}, odd1{}, even2{}, odd2{};
        for (int i = 0; i < (int)s1.size(); i++) {
            if (i % 2 == 0) { even1[s1[i] - 'a']++; even2[s2[i] - 'a']++; }
            else { odd1[s1[i] - 'a']++; odd2[s2[i] - 'a']++; }
        }
        return even1 == even2 && odd1 == odd2;
    }
};

================================================================================
// FOLDER: 2841_maximum_sum_of_almost_unique_subarray
================================================================================
// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, int m, int k) {
        std::unordered_map<int, int> freq;
        long long sum = 0, ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            freq[nums[i]]++;
            sum += nums[i];
            if (i >= k) {
                int out = nums[i - k];
                sum -= out;
                if (--freq[out] == 0) freq.erase(out);
            }
            if (i >= k - 1 && (int)freq.size() >= m) ans = std::max(ans, sum);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2842_count_k_subsequences_of_a_string_with_maximum_beauty
================================================================================
// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int countKSubsequencesWithMaxBeauty(std::string s, int k) {
        const int MOD = 1000000007;
        int freq[26] = {};
        for (char c : s) freq[c - 'a']++;
        std::vector<int> vals;
        for (int f : freq) if (f > 0) vals.push_back(f);
        if ((int)vals.size() < k) return 0;
        std::sort(vals.begin(), vals.end(), std::greater<int>());
        int threshold = vals[k - 1];
        int need = 0, avail = 0;
        long long prod = 1;
        for (int v : vals) {
            if (v > threshold) { prod = prod * v % MOD; need++; }
            else if (v == threshold) avail++;
        }
        int remain = k - need;
        auto modPow = [&](long long a, long long b) {
            long long res = 1;
            a %= MOD;
            while (b > 0) {
                if (b & 1) res = res * a % MOD;
                a = a * a % MOD;
                b >>= 1;
            }
            return res;
        };
        auto comb = [&](int n, int r) {
            if (r < 0 || r > n) return 0LL;
            long long num = 1, den = 1;
            for (int i = 0; i < r; i++) {
                num = num * (n - i) % MOD;
                den = den * (i + 1) % MOD;
            }
            return num * modPow(den, MOD - 2) % MOD;
        };
        prod = prod * comb(avail, remain) % MOD;
        for (int i = 0; i < remain; i++) prod = prod * threshold % MOD;
        return (int)prod;
    }
};

================================================================================
// FOLDER: 2843_count_symmetric_integers
================================================================================
// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

#include <string>

class Solution {
public:
    int countSymmetricIntegers(int low, int high) {
        int ans = 0;
        for (int x = low; x <= high; x++) {
            std::string s = std::to_string(x);
            if (s.size() % 2) continue;
            int mid = (int)s.size() / 2, a = 0, b = 0;
            for (int i = 0; i < mid; i++) {
                a += s[i] - '0';
                b += s[mid + i] - '0';
            }
            if (a == b) ans++;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2844_minimum_operations_to_make_a_special_number
================================================================================
// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minimumOperations(std::string num) {
        int n = (int)num.size();
        int ans = n;
        bool has0 = false;
        for (char c : num) if (c == '0') has0 = true;
        if (has0) ans = std::min(ans, n - 1);
        std::vector<std::string> targets = {"00", "25", "50", "75"};
        for (auto& t : targets) {
            int j = n - 1;
            while (j >= 0 && num[j] != t[1]) j--;
            if (j < 0) continue;
            int i = j - 1;
            while (i >= 0 && num[i] != t[0]) i--;
            if (i < 0) continue;
            ans = std::min(ans, n - i - 2);
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2845_count_of_interesting_subarrays
================================================================================
// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countInterestingSubarrays(std::vector<int>& nums, int modulo, int k) {
        std::unordered_map<int, int> freq{{0, 1}};
        long long ans = 0;
        int pref = 0;
        for (int v : nums) {
            if (v % modulo == k) pref++;
            int need = (pref - k) % modulo;
            if (need < 0) need += modulo;
            ans += freq[need];
            freq[pref % modulo]++;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2846_minimum_edge_weight_equilibrium_queries_in_a_tree
================================================================================
// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

#include <array>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> minOperationsQueries(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        const int LOG = 15;
        std::vector<std::vector<int>> up(LOG, std::vector<int>(n));
        std::vector<int> depth(n);
        std::vector<std::array<int, 27>> cnt(n);
        auto dfs = [&](auto&& self, int u, int p) -> void {
            up[0][u] = p;
            for (auto [v, w] : g[u]) {
                if (v == p) continue;
                depth[v] = depth[u] + 1;
                cnt[v] = cnt[u];
                cnt[v][w]++;
                self(self, v, u);
            }
        };
        dfs(dfs, 0, 0);
        for (int j = 1; j < LOG; j++)
            for (int i = 0; i < n; i++) up[j][i] = up[j - 1][up[j - 1][i]];
        auto lca = [&](int a, int b) {
            if (depth[a] < depth[b]) std::swap(a, b);
            int diff = depth[a] - depth[b];
            for (int j = 0; j < LOG; j++) if (diff & (1 << j)) a = up[j][a];
            if (a == b) return a;
            for (int j = LOG - 1; j >= 0; j--) {
                if (up[j][a] != up[j][b]) { a = up[j][a]; b = up[j][b]; }
            }
            return up[0][a];
        };
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int a = queries[i][0], b = queries[i][1];
            int c = lca(a, b);
            int total = depth[a] + depth[b] - 2 * depth[c];
            int best = 0;
            for (int w = 1; w <= 26; w++) {
                int f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w];
                best = std::max(best, f);
            }
            ans[i] = total - best;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2847_smallest_number_with_given_digit_product
================================================================================
// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string smallestNumber(long long n) {
        if (n == 0) return "0";
        if (n == 1) return "1";
        std::string digits;
        for (int d = 9; d >= 2; d--) {
            while (n % d == 0) {
                digits.push_back(char('0' + d));
                n /= d;
            }
        }
        if (n > 1) return "-1";
        std::reverse(digits.begin(), digits.end());
        return digits;
    }
};

================================================================================
// FOLDER: 2848_points_that_intersect_with_cars
================================================================================
// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

#include <vector>

class Solution {
public:
    int numberOfPoints(std::vector<std::vector<int>>& nums) {
        int cov[102] = {};
        for (auto& r : nums)
            for (int x = r[0]; x <= r[1]; x++) cov[x] = 1;
        int ans = 0;
        for (int v : cov) ans += v;
        return ans;
    }
};

================================================================================
// FOLDER: 2849_determine_if_a_cell_is_reachable_at_a_given_time
================================================================================
// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

#include <algorithm>
#include <cstdlib>

class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int need = std::max(std::abs(sx - fx), std::abs(sy - fy));
        if (need == 0) return t != 1;
        return t >= need;
    }
};

================================================================================
// FOLDER: 2850_minimum_moves_to_spread_stones_over_grid
================================================================================
// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int minimumMoves(std::vector<std::vector<int>>& grid) {
        std::vector<std::pair<int, int>> extras, zeros;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == 0) zeros.push_back({i, j});
                else if (grid[i][j] > 1) {
                    for (int k = 0; k < grid[i][j] - 1; k++) extras.push_back({i, j});
                }
            }
        }
        if (zeros.empty()) return 0;
        int best = 1 << 30;
        auto dfs = [&](auto&& self, int i, int cost) -> void {
            if (cost >= best) return;
            if (i == (int)zeros.size()) { best = cost; return; }
            for (int j = 0; j < (int)extras.size(); j++) {
                if (extras[j].first < 0) continue;
                auto e = extras[j];
                extras[j].first = -1;
                int d = std::abs(e.first - zeros[i].first) + std::abs(e.second - zeros[i].second);
                self(self, i + 1, cost + d);
                extras[j] = e;
            }
        };
        dfs(dfs, 0, 0);
        return best;
    }
};

================================================================================
// FOLDER: 2851_string_transformation
================================================================================
// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

#include <string>

class Solution {
public:
    int numberOfWays(std::string s, std::string t, long long k) {
        const int MOD = 1000000007;
        int n = (int)s.size();
        std::string ss = s + s;
        if (ss.substr(0, 2 * n - 1).find(t) == std::string::npos) return 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) if (ss.substr(i, n) == t) cnt++;
        auto modPow = [&](long long a, long long b) {
            long long res = 1;
            a %= MOD;
            while (b > 0) {
                if (b & 1) res = res * a % MOD;
                a = a * a % MOD;
                b >>= 1;
            }
            return (int)res;
        };
        int same = (s == t);
        int pk = modPow(n - 1, k);
        int invn = modPow(n, MOD - 2);
        int sign = (k % 2 == 1) ? MOD - 1 : 1;
        int waysSame = (int)((1LL * pk + 1LL * ((n - 1) % MOD) * sign % MOD) % MOD * invn % MOD);
        int waysDiff = (int)((1LL * pk - sign + MOD) % MOD * invn % MOD);
        if (same) return waysSame;
        return (int)(1LL * waysDiff * cnt % MOD);
    }
};

================================================================================
// FOLDER: 2852_sum_of_remoteness_of_all_cells
================================================================================
// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

#include <queue>
#include <vector>

class Solution {
public:
    long long sumRemoteness(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<char>> seen(m, std::vector<char>(n, 0));
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        long long total = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] != -1) total += grid[i][j];
        long long ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == -1 || seen[i][j]) continue;
                std::queue<std::pair<int, int>> q;
                q.push({i, j});
                seen[i][j] = 1;
                long long sum = 0;
                int cnt = 0;
                while (!q.empty()) {
                    auto [x, y] = q.front(); q.pop();
                    sum += grid[x][y];
                    cnt++;
                    for (auto& d : dirs) {
                        int ni = x + d[0], nj = y + d[1];
                        if (ni >= 0 && nj >= 0 && ni < m && nj < n && !seen[ni][nj] && grid[ni][nj] != -1) {
                            seen[ni][nj] = 1;
                            q.push({ni, nj});
                        }
                    }
                }
                ans += (total - sum) * cnt;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2855_minimum_right_shifts_to_sort_the_array
================================================================================
// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

#include <vector>

class Solution {
public:
    int minimumRightShifts(std::vector<int>& nums) {
        int n = (int)nums.size(), drops = 0, idx = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                drops++;
                idx = i;
            }
        }
        if (drops == 0) return 0;
        if (drops > 1) return -1;
        return n - 1 - idx;
    }
};

================================================================================
// FOLDER: 2856_minimum_array_length_after_pair_removals
================================================================================
// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minLengthAfterRemovals(std::vector<int>& nums) {
        int n = (int)nums.size(), mx = 0;
        std::unordered_map<int, int> freq;
        for (int v : nums) mx = std::max(mx, ++freq[v]);
        if (mx <= n / 2) return n % 2;
        return 2 * mx - n;
    }
};

================================================================================
// FOLDER: 2857_count_pairs_of_points_with_distance_k
================================================================================
// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

#include <map>
#include <vector>

class Solution {
public:
    int countPairs(std::vector<std::vector<int>>& coordinates, int k) {
        std::map<std::pair<int, int>, int> freq;
        int ans = 0;
        for (auto& p : coordinates) {
            int x = p[0], y = p[1];
            for (int a = 0; a <= k; a++) {
                int b = k - a;
                ans += freq[{x ^ a, y ^ b}];
            }
            freq[{x, y}]++;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2858_minimum_edge_reversals_so_every_node_is_reachable
================================================================================
// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> minEdgeReversals(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back({v, 0});
            g[v].push_back({u, 1});
        }
        std::vector<int> ans(n);
        std::function<void(int, int)> dfs1 = [&](int u, int p) {
            for (auto [v, ww] : g[u]) {
                if (v == p) continue;
                ans[0] += ww;
                dfs1(v, u);
            }
        };
        dfs1(0, -1);
        std::function<void(int, int)> dfs2 = [&](int u, int p) {
            for (auto [v, ww] : g[u]) {
                if (v == p) continue;
                if (ww == 0) ans[v] = ans[u] + 1;
                else ans[v] = ans[u] - 1;
                dfs2(v, u);
            }
        };
        dfs2(0, -1);
        return ans;
    }
};

================================================================================
// FOLDER: 2859_sum_of_values_at_indices_with_k_set_bits
================================================================================
// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

#include <vector>

class Solution {
public:
    int sumIndicesWithKSetBits(std::vector<int>& nums, int k) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            int bits = 0, x = i;
            while (x > 0) {
                bits += x & 1;
                x >>= 1;
            }
            if (bits == k) ans += nums[i];
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2860_happy_students
================================================================================
// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countWays(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size(), ans = 0;
        if (nums[0] > 0) ans++;
        for (int i = 0; i < n; i++) {
            int selected = i + 1;
            if (selected > nums[i] && (i == n - 1 || selected < nums[i + 1])) ans++;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2861_maximum_number_of_alloys
================================================================================
// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

#include <vector>

class Solution {
public:
    int maxNumberOfAlloys(int n, int k, int budget, std::vector<std::vector<int>>& composition,
                          std::vector<int>& stock, std::vector<int>& cost) {
        (void)k;
        auto ok = [&](long long machines) {
            for (auto& comp : composition) {
                long long spend = 0;
                for (int i = 0; i < n; i++) {
                    long long need = machines * comp[i] - stock[i];
                    if (need > 0) spend += need * cost[i];
                }
                if (spend <= budget) return true;
            }
            return false;
        };
        long long lo = 0, hi = 1000000000LL, ans = 0;
        while (lo <= hi) {
            long long mid = (lo + hi) / 2;
            if (ok(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return (int)ans;
    }
};

================================================================================
// FOLDER: 2862_maximum_element_sum_of_a_complete_subset_of_indices
================================================================================
// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maximumSum(std::vector<int>& nums) {
        int n = (int)nums.size();
        auto squareFree = [](int x) {
            int res = 1;
            for (int p = 2; p * p <= x; p++) {
                int cnt = 0;
                while (x % p == 0) {
                    x /= p;
                    cnt++;
                }
                if (cnt % 2 == 1) res *= p;
            }
            if (x > 1) res *= x;
            return res;
        };
        std::unordered_map<int, long long> groups;
        long long ans = 0;
        for (int i = 1; i <= n; i++) {
            int sf = squareFree(i);
            groups[sf] += nums[i - 1];
            if (groups[sf] > ans) ans = groups[sf];
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2863_maximum_length_of_semi_decreasing_subarrays
================================================================================
// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

#include <vector>

class Solution {
public:
    int maxSubarrayLength(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        std::vector<int> st;
        for (int i = n - 1; i >= 0; i--) {
            if (st.empty() || nums[i] > nums[st.back()]) st.push_back(i);
        }
        for (int i = 0; i < n; i++) {
            while (!st.empty() && nums[i] > nums[st.back()]) {
                int j = st.back();
                st.pop_back();
                if (j - i + 1 > ans) ans = j - i + 1;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2864_maximum_odd_binary_number
================================================================================
// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

#include <string>

class Solution {
public:
    std::string maximumOddBinaryNumber(std::string s) {
        int ones = 0;
        for (char c : s) if (c == '1') ones++;
        int zeros = (int)s.size() - ones;
        std::string b;
        b.reserve(s.size());
        for (int i = 0; i < ones - 1; i++) b.push_back('1');
        for (int i = 0; i < zeros; i++) b.push_back('0');
        b.push_back('1');
        return b;
    }
};

================================================================================
// FOLDER: 2865_beautiful_towers_i
================================================================================
// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

#include <vector>

class Solution {
public:
    long long maximumSumOfHeights(std::vector<int>& heights) {
        int n = (int)heights.size();
        long long ans = 0;
        for (int peak = 0; peak < n; peak++) {
            long long sum = heights[peak];
            int mn = heights[peak];
            for (int i = peak - 1; i >= 0; i--) {
                if (heights[i] < mn) mn = heights[i];
                sum += mn;
            }
            mn = heights[peak];
            for (int i = peak + 1; i < n; i++) {
                if (heights[i] < mn) mn = heights[i];
                sum += mn;
            }
            if (sum > ans) ans = sum;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2866_beautiful_towers_ii
================================================================================
// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

#include <vector>

class Solution {
public:
    long long maximumSumOfHeights(std::vector<int>& maxHeights) {
        int n = (int)maxHeights.size();
        std::vector<long long> left(n);
        std::vector<int> st = {-1};
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            while ((int)st.size() > 1 && maxHeights[st.back()] >= maxHeights[i]) {
                int j = st.back();
                st.pop_back();
                sum -= 1LL * maxHeights[j] * (j - st.back());
            }
            sum += 1LL * maxHeights[i] * (i - st.back());
            left[i] = sum;
            st.push_back(i);
        }
        std::vector<long long> right(n);
        st = {n};
        sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            while ((int)st.size() > 1 && maxHeights[st.back()] >= maxHeights[i]) {
                int j = st.back();
                st.pop_back();
                sum -= 1LL * maxHeights[j] * (st.back() - j);
            }
            sum += 1LL * maxHeights[i] * (st.back() - i);
            right[i] = sum;
            st.push_back(i);
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long cand = left[i] + right[i] - maxHeights[i];
            if (cand > ans) ans = cand;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2867_count_valid_paths_in_a_tree
================================================================================
// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

#include <functional>
#include <vector>

class Solution {
public:
    long long countPaths(int n, std::vector<std::vector<int>>& edges) {
        std::vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) isPrime[j] = false;
            }
        }
        std::vector<std::vector<int>> g(n + 1);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::function<int(int, int)> dfs = [&](int u, int p) {
            if (isPrime[u]) return 0;
            int sz = 1;
            for (int v : g[u]) if (v != p) sz += dfs(v, u);
            return sz;
        };
        long long ans = 0;
        for (int u = 1; u <= n; u++) {
            if (!isPrime[u]) continue;
            long long total = 0;
            for (int v : g[u]) {
                int c = dfs(v, u);
                ans += c;
                ans += total * c;
                total += c;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2868_the_wording_game
================================================================================
// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

#include <string>
#include <vector>

class Solution {
public:
    bool canAliceWin(std::vector<std::string>& a, std::vector<std::string>& b) {
        int i = 0, j = 0;
        char last = 0;
        bool alice = true;
        while (true) {
            if (alice) {
                while (i < (int)a.size() && a[i][0] <= last) i++;
                if (i == (int)a.size()) return false;
                last = a[i].back();
                i++;
            } else {
                while (j < (int)b.size() && b[j][0] <= last) j++;
                if (j == (int)b.size()) return true;
                last = b[j].back();
                j++;
            }
            alice = !alice;
        }
    }
};

================================================================================
// FOLDER: 2869_minimum_operations_to_collect_elements
================================================================================
// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        std::unordered_set<int> need;
        for (int i = 1; i <= k; i++) need.insert(i);
        for (int i = (int)nums.size() - 1; i >= 0; i--) {
            need.erase(nums[i]);
            if (need.empty()) return (int)nums.size() - i;
        }
        return (int)nums.size();
    }
};

================================================================================
// FOLDER: 2870_minimum_number_of_operations_to_make_array_empty
================================================================================
// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int v : nums) freq[v]++;
        int ans = 0;
        for (auto& [_, c] : freq) {
            if (c == 1) return -1;
            ans += (c + 2) / 3;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2871_split_array_into_maximum_number_of_subarrays
================================================================================
// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

#include <vector>

class Solution {
public:
    int maxSubarrays(std::vector<int>& nums) {
        int ans = 0, cur = -1;
        for (int v : nums) {
            if (cur == -1) cur = v;
            else cur &= v;
            if (cur == 0) {
                ans++;
                cur = -1;
            }
        }
        return ans == 0 ? 1 : ans;
    }
};

================================================================================
// FOLDER: 2872_maximum_number_of_k_divisible_components
================================================================================
// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

#include <functional>
#include <vector>

class Solution {
public:
    int maxKDivisibleComponents(int n, std::vector<std::vector<int>>& edges, std::vector<int>& values, int k) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = 0;
        std::function<int(int, int)> dfs = [&](int u, int p) {
            int sum = values[u] % k;
            for (int v : g[u]) {
                if (v == p) continue;
                sum = (sum + dfs(v, u)) % k;
            }
            if (sum == 0) ans++;
            return sum;
        };
        dfs(0, -1);
        return ans;
    }
};

================================================================================
// FOLDER: 2873_maximum_value_of_an_ordered_triplet_i
================================================================================
// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

#include <vector>

class Solution {
public:
    long long maximumTripletValue(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++) {
                    long long cand = 1LL * (nums[i] - nums[j]) * nums[k];
                    if (cand > ans) ans = cand;
                }
        return ans;
    }
};

================================================================================
// FOLDER: 2874_maximum_value_of_an_ordered_triplet_ii
================================================================================
// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

#include <vector>

class Solution {
public:
    long long maximumTripletValue(std::vector<int>& nums) {
        long long ans = 0, maxI = 0, maxDiff = 0;
        for (int v : nums) {
            long long val = v;
            if (maxDiff * val > ans) ans = maxDiff * val;
            if (maxI - val > maxDiff) maxDiff = maxI - val;
            if (val > maxI) maxI = val;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2875_minimum_size_subarray_in_infinite_array
================================================================================
// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

#include <vector>

class Solution {
public:
    int minSizeSubarray(std::vector<int>& nums, int target) {
        int n = (int)nums.size();
        long long total = 0;
        for (int v : nums) total += v;
        int ans = 1 << 30;
        if (total > 0) {
            int loops = (int)(target / total);
            int remain = (int)(target % total);
            if (remain == 0) return loops * n;
            std::vector<int> arr = nums;
            arr.insert(arr.end(), nums.begin(), nums.end());
            int left = 0, sum = 0, best = 1 << 30;
            for (int right = 0; right < (int)arr.size(); right++) {
                sum += arr[right];
                while (sum > remain && left <= right) {
                    sum -= arr[left];
                    left++;
                }
                if (sum == remain && right - left + 1 < best) best = right - left + 1;
            }
            if (best < (1 << 30)) ans = loops * n + best;
        }
        return ans == (1 << 30) ? -1 : ans;
    }
};

================================================================================
// FOLDER: 2876_count_visited_nodes_in_a_directed_graph
================================================================================
// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> countVisitedNodes(std::vector<int>& edges) {
        int n = (int)edges.size();
        std::vector<int> ans(n), state(n);
        std::vector<int> stack;
        std::function<void(int)> dfs = [&](int u) {
            state[u] = 1;
            stack.push_back(u);
            int v = edges[u];
            if (state[v] == 0) dfs(v);
            else if (state[v] == 1) {
                int idx = (int)stack.size() - 1;
                while (stack[idx] != v) idx--;
                int cyc = (int)stack.size() - idx;
                for (int i = idx; i < (int)stack.size(); i++) ans[stack[i]] = cyc;
            }
            if (ans[u] == 0) ans[u] = ans[edges[u]] + 1;
            state[u] = 2;
            stack.pop_back();
        };
        for (int i = 0; i < n; i++) if (state[i] == 0) dfs(i);
        return ans;
    }
};

================================================================================
// FOLDER: 2877_create_a_dataframe_from_list
================================================================================
// LeetCode 2877 - Create a DataFrame from List
// https://leetcode.com/problems/create-a-dataframe-from-list/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> createDataframe(std::vector<std::vector<int>>& studentData) {
        (void)studentData;
        return {};
    }
};

================================================================================
// FOLDER: 2878_get_the_size_of_a_dataframe
================================================================================
// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<int> getDataframeSize(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2879_display_the_first_three_rows
================================================================================
// LeetCode 2879 - Display the First Three Rows
// https://leetcode.com/problems/display-the-first-three-rows/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> selectFirstRows(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2880_select_data
================================================================================
// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> selectData(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2881_create_a_new_column
================================================================================
// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> createBonusColumn(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2882_drop_duplicate_rows
================================================================================
// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> dropDuplicateEmails(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2883_drop_missing_data
================================================================================
// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> dropMissingData(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2884_modify_columns
================================================================================
// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> modifySalaryColumn(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2885_rename_columns
================================================================================
// LeetCode 2885 - Rename Columns
// https://leetcode.com/problems/rename-columns/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> renameColumns(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2886_change_data_type
================================================================================
// LeetCode 2886 - Change Data Type
// https://leetcode.com/problems/change-data-type/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> changeDatatype(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2887_fill_missing_data
================================================================================
// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> fillMissingValues(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2888_reshape_data_concatenate
================================================================================
// LeetCode 2888 - Reshape Data: Concatenate
// https://leetcode.com/problems/reshape-data-concatenate/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> concatenateTables(std::vector<std::vector<int>>& df1, std::vector<std::vector<int>>& df2) {
        (void)df1; (void)df2;
        return {};
    }
};

================================================================================
// FOLDER: 2889_reshape_data_pivot
================================================================================
// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> pivotTable(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2890_reshape_data_melt
================================================================================
// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> meltTable(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2891_method_chaining
================================================================================
// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/
// Pandas stand-in: Go returns nil.

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findHeavyAnimals(std::vector<std::vector<int>>& df) {
        (void)df;
        return {};
    }
};

================================================================================
// FOLDER: 2892_minimizing_array_after_replacing_pairs_with_their_product
================================================================================
// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

#include <vector>

class Solution {
public:
    int minArrayLength(std::vector<int>& nums, int k) {
        if (nums.empty()) return 0;
        int ans = 1;
        long long prod = nums[0];
        for (int i = 1; i < (int)nums.size(); i++) {
            if (prod <= k && nums[i] <= k && (nums[i] == 0 || prod <= k / nums[i])) {
                prod *= nums[i];
            } else {
                ans++;
                prod = nums[i];
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2894_divisible_and_non_divisible_sums_difference
================================================================================
// LeetCode 2894 - Divisible and Non-divisible Sums Difference
// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution {
public:
    int differenceOfSums(int n, int m) {
        int num1 = 0, num2 = 0;
        for (int i = 1; i <= n; i++) {
            if (i % m == 0) num2 += i;
            else num1 += i;
        }
        return num1 - num2;
    }
};

================================================================================
// FOLDER: 2895_minimum_processing_time
================================================================================
// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minProcessingTime(std::vector<int>& processorTime, std::vector<int>& tasks) {
        std::sort(processorTime.begin(), processorTime.end());
        std::sort(tasks.begin(), tasks.end(), std::greater<int>());
        int ans = 0;
        for (int i = 0; i < (int)processorTime.size(); i++) {
            int fin = processorTime[i] + tasks[i * 4];
            if (fin > ans) ans = fin;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2896_apply_operations_to_make_two_strings_equal
================================================================================
// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

#include <string>
#include <vector>

class Solution {
public:
    int minOperations(std::string s1, std::string s2, int x) {
        std::vector<int> diff;
        for (int i = 0; i < (int)s1.size(); i++)
            if (s1[i] != s2[i]) diff.push_back(i);
        int m = (int)diff.size();
        if (m % 2 == 1) return -1;
        if (m == 0) return 0;
        std::vector<int> dp2(m + 1, 1 << 30);
        dp2[0] = 0;
        for (int i = 0; i < m; i++) {
            if (dp2[i] >= (1 << 30)) continue;
            if (i + 1 < m) {
                int cand = diff[i + 1] - diff[i];
                if (cand > x) cand = x;
                if (dp2[i] + cand < dp2[i + 2]) dp2[i + 2] = dp2[i] + cand;
            }
        }
        return dp2[m] >= (1 << 30) ? -1 : dp2[m];
    }
};

================================================================================
// FOLDER: 2897_apply_operations_on_array_to_maximize_sum_of_squares
================================================================================
// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

#include <vector>

class Solution {
public:
    int maxSum(std::vector<int>& nums, int k) {
        const int mod = 1000000007;
        std::vector<int> cnt(32);
        for (int v : nums)
            for (int b = 0; b < 32; b++)
                if (v & (1 << b)) cnt[b]++;
        int ans = 0;
        for (int i = 0; i < k; i++) {
            int cur = 0;
            for (int b = 0; b < 32; b++) {
                if (cnt[b] > 0) {
                    cur |= 1 << b;
                    cnt[b]--;
                }
            }
            ans = (ans + 1LL * (cur % mod) * (cur % mod) % mod) % mod;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2898_maximum_linear_stock_score
================================================================================
// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& prices) {
        std::unordered_map<int, long long> best;
        long long ans = 0;
        for (int i = 0; i < (int)prices.size(); i++) {
            int key = prices[i] - (i + 1);
            long long cand = best[key] + prices[i];
            if (cand > best[key]) best[key] = cand;
            if (best[key] > ans) ans = best[key];
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2899_last_visited_integers
================================================================================
// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

#include <vector>

class Solution {
public:
    std::vector<int> lastVisitedIntegers(std::vector<int>& nums) {
        std::vector<int> seen, ans;
        int k = 0;
        for (int v : nums) {
            if (v != -1) {
                seen.push_back(v);
                k = 0;
            } else {
                k++;
                if (k > (int)seen.size()) ans.push_back(-1);
                else ans.push_back(seen[(int)seen.size() - k]);
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2900_longest_unequal_adjacent_groups_subsequence_i
================================================================================
// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> getLongestSubsequence(std::vector<std::string>& words, std::vector<int>& groups) {
        std::vector<std::string> ans = {words[0]};
        int last = groups[0];
        for (int i = 1; i < (int)words.size(); i++) {
            if (groups[i] != last) {
                ans.push_back(words[i]);
                last = groups[i];
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2901_longest_unequal_adjacent_groups_subsequence_ii
================================================================================
// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> getWordsInLongestSubsequence(std::vector<std::string>& words, std::vector<int>& groups) {
        int n = (int)words.size();
        std::vector<int> dp(n, 1), prev(n, -1);
        auto hamming = [](const std::string& a, const std::string& b) {
            if (a.size() != b.size()) return 100;
            int d = 0;
            for (int i = 0; i < (int)a.size(); i++) if (a[i] != b[i]) d++;
            return d;
        };
        int best = 1, bestI = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (groups[i] != groups[j] && hamming(words[i], words[j]) == 1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > best) {
                best = dp[i];
                bestI = i;
            }
        }
        std::vector<std::string> path;
        for (int i = bestI; i != -1; i = prev[i]) path.push_back(words[i]);
        std::reverse(path.begin(), path.end());
        return path;
    }
};

================================================================================
// FOLDER: 2902_count_of_sub_multisets_with_bounded_sum
================================================================================
// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countSubMultisets(std::vector<int>& nums, int l, int r) {
        const int mod = 1000000007;
        std::unordered_map<int, int> freq;
        int total = 0;
        for (int v : nums) {
            freq[v]++;
            total += v;
        }
        if (total < l) return 0;
        if (r > total) r = total;
        std::vector<int> dp(r + 1);
        dp[0] = 1;
        int zeros = freq[0];
        freq.erase(0);
        for (auto& [v, c] : freq) {
            std::vector<int> ndp(r + 1);
            for (int sum = 0; sum <= r; sum++) {
                if (dp[sum] == 0) continue;
                for (int k = 0; k <= c && sum + k * v <= r; k++)
                    ndp[sum + k * v] = (ndp[sum + k * v] + dp[sum]) % mod;
            }
            dp.swap(ndp);
        }
        int ans = 0;
        for (int s = l; s <= r; s++) ans = (ans + dp[s]) % mod;
        ans = 1LL * ans * (zeros + 1) % mod;
        return ans;
    }
};

================================================================================
// FOLDER: 2903_find_indices_with_index_and_value_difference_i
================================================================================
// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> findIndices(std::vector<int>& nums, int indexDifference, int valueDifference) {
        int n = (int)nums.size();
        for (int i = 0; i < n; i++)
            for (int j = i; j < n; j++) {
                int di = std::abs(j - i), dv = std::abs(nums[i] - nums[j]);
                if (di >= indexDifference && dv >= valueDifference) return {i, j};
            }
        return {-1, -1};
    }
};

================================================================================
// FOLDER: 2904_shortest_and_lexicographically_smallest_beautiful_string
================================================================================
// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

#include <string>

class Solution {
public:
    std::string shortestBeautifulSubstring(std::string s, int k) {
        std::string ans;
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            int ones = 0;
            for (int j = i; j < n; j++) {
                if (s[j] == '1') ones++;
                if (ones == k) {
                    std::string cand = s.substr(i, j - i + 1);
                    if (ans.empty() || cand.size() < ans.size() || (cand.size() == ans.size() && cand < ans))
                        ans = cand;
                    break;
                }
                if (ones > k) break;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2905_find_indices_with_index_and_value_difference_ii
================================================================================
// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

#include <vector>

class Solution {
public:
    std::vector<int> findIndices(std::vector<int>& nums, int indexDifference, int valueDifference) {
        int n = (int)nums.size();
        int minIdx = 0, maxIdx = 0;
        for (int j = indexDifference; j < n; j++) {
            int i = j - indexDifference;
            if (nums[i] < nums[minIdx]) minIdx = i;
            if (nums[i] > nums[maxIdx]) maxIdx = i;
            if (nums[j] - nums[minIdx] >= valueDifference) return {minIdx, j};
            if (nums[maxIdx] - nums[j] >= valueDifference) return {maxIdx, j};
        }
        return {-1, -1};
    }
};

================================================================================
// FOLDER: 2906_construct_product_matrix
================================================================================
// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> constructProductMatrix(std::vector<std::vector<int>>& grid) {
        const int mod = 12345;
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> ans(m, std::vector<int>(n));
        int pref = 1;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                ans[i][j] = pref;
                pref = 1LL * pref * (grid[i][j] % mod) % mod;
            }
        int suf = 1;
        for (int i = m - 1; i >= 0; i--)
            for (int j = n - 1; j >= 0; j--) {
                ans[i][j] = 1LL * ans[i][j] * suf % mod;
                suf = 1LL * suf * (grid[i][j] % mod) % mod;
            }
        return ans;
    }
};

================================================================================
// FOLDER: 2907_maximum_profitable_triplets_with_increasing_prices_i
================================================================================
// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices, std::vector<int>& profits) {
        int n = (int)prices.size(), ans = -1;
        for (int j = 0; j < n; j++) {
            int bestL = -1, bestR = -1;
            for (int i = 0; i < j; i++)
                if (prices[i] < prices[j] && profits[i] > bestL) bestL = profits[i];
            for (int k = j + 1; k < n; k++)
                if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k];
            if (bestL >= 0 && bestR >= 0) {
                int cand = bestL + profits[j] + bestR;
                if (cand > ans) ans = cand;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2908_minimum_sum_of_mountain_triplets_i
================================================================================
// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

#include <vector>

class Solution {
public:
    int minimumSum(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 1 << 30;
        for (int j = 1; j < n - 1; j++) {
            int left = 1 << 30, right = 1 << 30;
            for (int i = 0; i < j; i++)
                if (nums[i] < nums[j] && nums[i] < left) left = nums[i];
            for (int k = j + 1; k < n; k++)
                if (nums[k] < nums[j] && nums[k] < right) right = nums[k];
            if (left < (1 << 30) && right < (1 << 30)) {
                int cand = left + nums[j] + right;
                if (cand < ans) ans = cand;
            }
        }
        return ans == (1 << 30) ? -1 : ans;
    }
};

================================================================================
// FOLDER: 2909_minimum_sum_of_mountain_triplets_ii
================================================================================
// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

#include <vector>

class Solution {
public:
    int minimumSum(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> left(n), right(n);
        int mn = 1 << 30;
        for (int i = 0; i < n; i++) {
            left[i] = mn;
            if (nums[i] < mn) mn = nums[i];
        }
        mn = 1 << 30;
        for (int i = n - 1; i >= 0; i--) {
            right[i] = mn;
            if (nums[i] < mn) mn = nums[i];
        }
        int ans = 1 << 30;
        for (int j = 1; j < n - 1; j++) {
            if (left[j] < nums[j] && right[j] < nums[j]) {
                int cand = left[j] + nums[j] + right[j];
                if (cand < ans) ans = cand;
            }
        }
        return ans == (1 << 30) ? -1 : ans;
    }
};

================================================================================
// FOLDER: 2910_minimum_number_of_groups_to_create_a_valid_assignment
================================================================================
// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minGroupsForValidAssignment(std::vector<int>& balls) {
        std::unordered_map<int, int> freq;
        for (int b : balls) freq[b]++;
        std::vector<int> counts;
        int minF = 1 << 30;
        for (auto& [_, f] : freq) {
            counts.push_back(f);
            if (f < minF) minF = f;
        }
        for (int size = minF; size >= 1; size--) {
            bool ok = true;
            int groups = 0;
            for (int c : counts) {
                int rem = c % (size + 1);
                int g2 = c / (size + 1);
                if (rem == 0) groups += g2;
                else if (size - rem <= g2) groups += g2 + 1;
                else {
                    ok = false;
                    break;
                }
            }
            if (ok) return groups;
        }
        return (int)balls.size();
    }
};

================================================================================
// FOLDER: 2911_minimum_changes_to_make_k_semi_palindromes
================================================================================
// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

#include <string>
#include <vector>

class Solution {
public:
    int minimumChanges(std::string s, int k) {
        int n = (int)s.size();
        std::vector<std::vector<int>> cost(n, std::vector<int>(n, 1 << 20));
        auto semiCost = [&](int l, int r) {
            int length = r - l + 1, best = 1 << 20;
            for (int d = 1; d < length; d++) {
                if (length % d != 0) continue;
                int chg = 0;
                for (int start = 0; start < d; start++) {
                    std::string chars;
                    for (int i = l + start; i <= r; i += d) chars.push_back(s[i]);
                    for (int i = 0, j = (int)chars.size() - 1; i < j; i++, j--)
                        if (chars[i] != chars[j]) chg++;
                }
                if (chg < best) best = chg;
            }
            return best;
        };
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                cost[i][j] = semiCost(i, j);
        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n + 1, 1 << 20));
        dp[0][0] = 0;
        for (int p = 1; p <= k; p++)
            for (int i = 1; i <= n; i++)
                for (int t = 0; t < i - 1; t++) {
                    int cand = dp[p - 1][t] + cost[t][i - 1];
                    if (cand < dp[p][i]) dp[p][i] = cand;
                }
        return dp[k][n];
    }
};

================================================================================
// FOLDER: 2912_number_of_ways_to_reach_destination_in_the_grid
================================================================================
// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

#include <vector>

class Solution {
public:
    int numberOfWays(int n, int m, int k, std::vector<int>& source, std::vector<int>& dest) {
        const int mod = 1000000007;
        int sx = source[0], sy = source[1], tx = dest[0], ty = dest[1];
        long long same = 0, row = 0, col = 0, other = 0;
        if (sx == tx && sy == ty) same = 1;
        else if (sx == tx) row = 1;
        else if (sy == ty) col = 1;
        else other = 1;
        for (int step = 0; step < k; step++) {
            long long ns = (row * (m - 1) + col * (n - 1)) % mod;
            long long nr = (same + row * (m - 2) % mod + other * (n - 1) % mod) % mod;
            long long nc = (same + col * (n - 2) % mod + other * (m - 1) % mod) % mod;
            long long no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4) % mod) % mod;
            same = ns; row = nr; col = nc; other = no;
        }
        if (sx == tx && sy == ty) return (int)same;
        if (sx == tx) return (int)row;
        if (sy == ty) return (int)col;
        return (int)other;
    }
};

================================================================================
// FOLDER: 2913_subarrays_distinct_element_sum_of_squares_i
================================================================================
// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int sumCounts(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::unordered_set<int> seen;
            for (int j = i; j < n; j++) {
                seen.insert(nums[j]);
                int d = (int)seen.size();
                ans += d * d;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2914_minimum_number_of_changes_to_make_binary_string_beautiful
================================================================================
// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

#include <string>

class Solution {
public:
    int minChanges(std::string s) {
        int ans = 0;
        for (int i = 0; i < (int)s.size(); i += 2)
            if (s[i] != s[i + 1]) ans++;
        return ans;
    }
};

================================================================================
// FOLDER: 2915_length_of_the_longest_subsequence_that_sums_to_target
================================================================================
// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

#include <vector>

class Solution {
public:
    int lengthOfLongestSubsequence(std::vector<int>& nums, int target) {
        std::vector<int> dp(target + 1, -1);
        dp[0] = 0;
        for (int v : nums)
            for (int s = target; s >= v; s--)
                if (dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]) dp[s] = dp[s - v] + 1;
        return dp[target];
    }
};

================================================================================
// FOLDER: 2916_subarrays_distinct_element_sum_of_squares_ii
================================================================================
// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

#include <functional>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int sumCounts(std::vector<int>& nums) {
        const int mod = 1000000007;
        int n = (int)nums.size();
        std::unordered_map<int, int> last;
        struct Node { int sum = 0, sumSq = 0, lazy = 0; };
        std::vector<Node> tree(4 * (n + 2));
        auto apply = [&](int idx, int l, int r, int val) {
            int length = r - l + 1;
            tree[idx].sumSq = (int)((tree[idx].sumSq + 2LL * val % mod * tree[idx].sum % mod +
                                     1LL * val % mod * val % mod * length % mod) % mod);
            tree[idx].sum = (int)((tree[idx].sum + 1LL * val % mod * length % mod) % mod);
            tree[idx].lazy = (tree[idx].lazy + val) % mod;
        };
        std::function<void(int, int, int, int, int, int)> update = [&](int idx, int l, int r, int ql, int qr, int val) {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                apply(idx, l, r, val);
                return;
            }
            if (tree[idx].lazy != 0 && l != r) {
                int mid = (l + r) / 2;
                apply(idx * 2, l, mid, tree[idx].lazy);
                apply(idx * 2 + 1, mid + 1, r, tree[idx].lazy);
                tree[idx].lazy = 0;
            }
            int mid = (l + r) / 2;
            update(idx * 2, l, mid, ql, qr, val);
            update(idx * 2 + 1, mid + 1, r, ql, qr, val);
            tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % mod;
            tree[idx].sumSq = (tree[idx * 2].sumSq + tree[idx * 2 + 1].sumSq) % mod;
        };
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int v = nums[i - 1];
            int prev = last.count(v) ? last[v] : 0;
            update(1, 1, n, prev + 1, i, 1);
            ans = (ans + tree[1].sumSq) % mod;
            last[v] = i;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2917_find_the_k_or_of_an_array
================================================================================
// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

#include <vector>

class Solution {
public:
    int findKOr(std::vector<int>& nums, int k) {
        int ans = 0;
        for (int b = 0; b < 31; b++) {
            int cnt = 0;
            for (int v : nums) if (v & (1 << b)) cnt++;
            if (cnt >= k) ans |= 1 << b;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2918_minimum_equal_sum_of_two_arrays_after_replacing_zeros
================================================================================
// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

#include <vector>

class Solution {
public:
    long long minSum(std::vector<int>& nums1, std::vector<int>& nums2) {
        long long s1 = 0, s2 = 0;
        int z1 = 0, z2 = 0;
        for (int v : nums1) {
            if (v == 0) { z1++; s1++; }
            else s1 += v;
        }
        for (int v : nums2) {
            if (v == 0) { z2++; s2++; }
            else s2 += v;
        }
        if (z1 == 0 && s1 < s2) return -1;
        if (z2 == 0 && s2 < s1) return -1;
        return s1 > s2 ? s1 : s2;
    }
};

================================================================================
// FOLDER: 2919_minimum_increment_operations_to_make_array_beautiful
================================================================================
// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minIncrementOperations(std::vector<int>& nums, int k) {
        long long dp0 = 0, dp1 = 0, dp2 = 0;
        for (int v : nums) {
            long long cost = v < k ? (k - v) : 0;
            long long nd0 = cost + std::min({dp0, dp1, dp2});
            dp0 = dp1; dp1 = dp2; dp2 = nd0;
        }
        return std::min({dp0, dp1, dp2});
    }
};

================================================================================
// FOLDER: 2920_maximum_points_after_collecting_coins_from_all_nodes
================================================================================
// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

#include <functional>
#include <map>
#include <vector>

class Solution {
public:
    int maximumPoints(std::vector<std::vector<int>>& edges, std::vector<int>& coins, int k) {
        int n = (int)coins.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::map<std::pair<int, int>, int> memo;
        std::function<int(int, int, int)> dfs = [&](int u, int p, int shifts) {
            if (shifts > 14) shifts = 14;
            auto key = std::make_pair(u, shifts);
            if (memo.count(key)) return memo[key];
            int c = coins[u] >> shifts;
            int opt1 = c - k, opt2 = c / 2;
            for (int v : g[u]) {
                if (v == p) continue;
                opt1 += dfs(v, u, shifts);
                opt2 += dfs(v, u, shifts + 1);
            }
            int best = opt1 > opt2 ? opt1 : opt2;
            return memo[key] = best;
        };
        return dfs(0, -1, 0);
    }
};

================================================================================
// FOLDER: 2921_maximum_profitable_triplets_with_increasing_prices_ii
================================================================================
// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices, std::vector<int>& profits) {
        int n = (int)prices.size(), ans = -1;
        std::vector<int> maxLeft(n, -1), bit(5002, 0);
        auto update = [&](int i, int val) {
            for (; i < (int)bit.size(); i += i & -i)
                if (val > bit[i]) bit[i] = val;
        };
        auto query = [&](int i) {
            int best = -1;
            for (; i > 0; i -= i & -i)
                if (bit[i] > best) best = bit[i];
            return best;
        };
        for (int j = 0; j < n; j++) {
            maxLeft[j] = query(prices[j] - 1);
            update(prices[j], profits[j]);
        }
        for (int j = 0; j < n; j++) {
            int bestR = -1;
            for (int k = j + 1; k < n; k++)
                if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k];
            if (maxLeft[j] >= 0 && bestR >= 0) {
                int cand = maxLeft[j] + profits[j] + bestR;
                if (cand > ans) ans = cand;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2923_find_champion_i
================================================================================
// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

#include <vector>

class Solution {
public:
    int findChampion(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        for (int i = 0; i < n; i++) {
            bool win = true;
            for (int j = 0; j < n; j++)
                if (i != j && grid[i][j] == 0) { win = false; break; }
            if (win) return i;
        }
        return -1;
    }
};

================================================================================
// FOLDER: 2924_find_champion_ii
================================================================================
// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

#include <vector>

class Solution {
public:
    int findChampion(int n, std::vector<std::vector<int>>& edges) {
        std::vector<int> indeg(n);
        for (auto& e : edges) indeg[e[1]]++;
        int ans = -1;
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) {
                if (ans != -1) return -1;
                ans = i;
            }
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2925_maximum_score_after_applying_operations_on_a_tree
================================================================================
// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

#include <functional>
#include <vector>

class Solution {
public:
    long long maximumScoreAfterOperations(std::vector<std::vector<int>>& edges, std::vector<int>& values) {
        int n = (int)values.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        long long total = 0;
        for (int v : values) total += v;
        std::function<long long(int, int)> dfs = [&](int u, int p) {
            long long sumKids = 0;
            bool isLeaf = true;
            for (int v : g[u]) {
                if (v == p) continue;
                isLeaf = false;
                sumKids += dfs(v, u);
            }
            if (isLeaf) return (long long)values[u];
            return values[u] < sumKids ? (long long)values[u] : sumKids;
        };
        return total - dfs(0, -1);
    }
};

================================================================================
// FOLDER: 2926_maximum_balanced_subsequence_sum
================================================================================
// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxBalancedSubsequenceSum(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> keys(n), uniq;
        for (int i = 0; i < n; i++) keys[i] = nums[i] - i;
        uniq = keys;
        std::sort(uniq.begin(), uniq.end());
        uniq.erase(std::unique(uniq.begin(), uniq.end()), uniq.end());
        auto idxOf = [&](int v) {
            return (int)(std::lower_bound(uniq.begin(), uniq.end(), v) - uniq.begin()) + 1;
        };
        const long long negInf = -(1LL << 60);
        std::vector<long long> bit(uniq.size() + 2, negInf);
        auto update = [&](int i, long long val) {
            for (; i < (int)bit.size(); i += i & -i)
                if (val > bit[i]) bit[i] = val;
        };
        auto query = [&](int i) {
            long long best = negInf;
            for (; i > 0; i -= i & -i)
                if (bit[i] > best) best = bit[i];
            return best;
        };
        long long ans = negInf;
        for (int i = 0; i < n; i++) {
            int id = idxOf(keys[i]);
            long long best = query(id);
            long long cur = nums[i];
            if (best > negInf / 2) {
                long long cand = best + nums[i];
                if (cand > cur) cur = cand;
            }
            update(id, cur);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2927_distribute_candies_among_children_iii
================================================================================
// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

class Solution {
public:
    long long distributeCandies(int n, int limit) {
        auto comb = [](long long x) -> long long {
            if (x < 2) return 0;
            return x * (x - 1) / 2;
        };
        long long ans = comb((long long)n + 2);
        ans -= 3 * comb((long long)(n - limit) + 1);
        ans += 3 * comb((long long)(n - 2 * (limit + 1)) + 2);
        ans -= comb((long long)(n - 3 * (limit + 1)) + 2);
        if (ans < 0) ans = 0;
        return ans;
    }
};

================================================================================
// FOLDER: 2928_distribute_candies_among_children_i
================================================================================
// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/

class Solution {
public:
    int distributeCandies(int n, int limit) {
        int ans = 0;
        for (int i = 0; i <= limit; i++)
            for (int j = 0; j <= limit; j++) {
                int k = n - i - j;
                if (k >= 0 && k <= limit) ans++;
            }
        return ans;
    }
};

================================================================================
// FOLDER: 2929_distribute_candies_among_children_ii
================================================================================
// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution {
public:
    long long distributeCandies(int n, int limit) {
        auto comb2 = [](long long x) -> long long {
            if (x < 0) return 0;
            return (x + 1) * (x + 2) / 2;
        };
        long long ans = comb2(n);
        ans -= 3 * comb2(n - (limit + 1));
        ans += 3 * comb2(n - 2 * (limit + 1));
        ans -= comb2(n - 3 * (limit + 1));
        return ans;
    }
};

================================================================================
// FOLDER: 2930_number_of_strings_which_can_be_rearranged_to_contain_substring
================================================================================
// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

class Solution {
public:
    int stringCount(int n) {
        const int mod = 1000000007;
        auto modPow = [&](long long a, int b) {
            long long res = 1;
            a %= mod;
            while (b > 0) {
                if (b & 1) res = res * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return (int)res;
        };
        if (n < 4) return 0;
        long long ans = modPow(26, n);
        ans = (ans - 3LL * modPow(25, n) % mod + mod) % mod;
        ans = (ans + 3LL * modPow(24, n) % mod) % mod;
        ans = (ans - modPow(23, n) + mod) % mod;
        ans = (ans + 1LL * (n % mod) * modPow(25, n - 1) % mod) % mod;
        ans = (ans - 2LL * (n % mod) % mod * modPow(24, n - 1) % mod + mod) % mod;
        ans = (ans + 1LL * (n % mod) * modPow(23, n - 1) % mod) % mod;
        ans = (ans - 1LL * (n % mod) * ((n - 1 + mod) % mod) % mod * modPow(24, n - 2) % mod % mod + mod) % mod;
        ans = (ans + 1LL * (n % mod) * ((n - 1 + mod) % mod) % mod * modPow(23, n - 2) % mod) % mod;
        return (int)ans;
    }
};

================================================================================
// FOLDER: 2931_maximum_spending_after_buying_items
================================================================================
// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

#include <vector>

class Solution {
public:
    long long maxSpending(std::vector<std::vector<int>>& values) {
        int m = (int)values.size(), n = (int)values[0].size();
        std::vector<int> idx(m, n - 1);
        long long ans = 0, day = 1;
        int total = m * n;
        for (int t = 0; t < total; t++) {
            int bestI = -1; long long bestV = (1LL << 60);
            for (int i = 0; i < m; i++) {
                if (idx[i] >= 0 && values[i][idx[i]] < bestV) {
                    bestV = values[i][idx[i]];
                    bestI = i;
                }
            }
            ans += 1LL * bestV * day;
            idx[bestI]--;
            day++;
        }
        return ans;
    }
};

================================================================================
// FOLDER: 2932_maximum_strong_pair_xor_i
================================================================================
// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumStrongPairXor(std::vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++)
            for (int j = i; j < (int)nums.size(); j++) {
                int x = nums[i], y = nums[j];
                if (std::abs(x - y) <= std::min(x, y)) {
                    int xorr = x ^ y;
                    if (xorr > ans) ans = xorr;
                }
            }
        return ans;
    }
};

================================================================================
// FOLDER: 2933_high_access_employees
================================================================================
// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> findHighAccessEmployees(std::vector<std::vector<std::string>>& accessTimes) {
        std::unordered_map<std::string, std::vector<int>> m;
        for (auto& a : accessTimes) {
            const std::string& name = a[0];
            const std::string& t = a[1];
            int hh = (t[0] - '0') * 10 + (t[1] - '0');
            int mm = (t[2] - '0') * 10 + (t[3] - '0');
            m[name].push_back(hh * 60 + mm);
        }
        std::vector<std::string> ans;
        for (auto& [name, times] : m) {
            std::sort(times.begin(), times.end());
            for (int i = 0; i + 2 < (int)times.size(); i++) {
                if (times[i + 2] - times[i] < 60) {
                    ans.push_back(name);
                    break;
                }
            }
        }
        std::sort(ans.begin(), ans.end());
        return ans;
    }
};

================================================================================
// FOLDER: 2934_minimum_operations_to_maximize_last_elements_in_arrays
================================================================================
// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size();
        auto calc = [&](std::vector<int>& a1, std::vector<int>& a2) {
            int ops = 0;
            int last1 = a1[n - 1], last2 = a2[n - 1];
            for (int i = 0; i < n - 1; i++) {
                int x = a1[i], y = a2[i];
                if (x <= last1 && y <= last2) continue;
                if (y <= last1 && x <= last2) { ops++; continue; }
                return 1 << 30;
            }
            return ops;
        };
        int ans = calc(nums1, nums2);
        std::swap(nums1[n - 1], nums2[n - 1]);
        int cand = calc(nums1, nums2) + 1;
        if (cand < ans) ans = cand;
        return ans >= (1 << 30) ? -1 : ans;
    }
};
