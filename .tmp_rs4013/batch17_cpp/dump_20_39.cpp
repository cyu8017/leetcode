

########## 3414_maximum_score_of_non_overlapping_intervals ##########
// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
    struct It { int l, r, w, i; };
    struct State {
        long long score = 0;
        std::vector<int> idx;
    };

    static State better(const State& a, const State& b) {
        if (a.score != b.score) return a.score > b.score ? a : b;
        for (int i = 0; i < (int)a.idx.size() && i < (int)b.idx.size(); i++) {
            if (a.idx[i] != b.idx[i]) return a.idx[i] < b.idx[i] ? a : b;
        }
        return a.idx.size() <= b.idx.size() ? a : b;
    }

public:
    std::vector<int> maximumWeight(std::vector<std::vector<int>>& intervals) {
        int n = (int)intervals.size();
        std::vector<It> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {intervals[i][0], intervals[i][1], intervals[i][2], i};
        std::sort(arr.begin(), arr.end(), [](const It& a, const It& b) { return a.r < b.r; });
        std::vector<std::vector<State>> dp(n + 1, std::vector<State>(5));
        for (int i = 1; i <= n; i++) {
            It cur = arr[i - 1];
            for (int t = 0; t <= 4; t++) dp[i][t] = dp[i - 1][t];
            int p = (int)(std::lower_bound(arr.begin(), arr.begin() + (i - 1), cur.l,
                [](const It& a, int val) { return a.r < val; }) - arr.begin());
            int prev = p;
            for (int t = 1; t <= 4; t++) {
                State prevState = dp[prev][t - 1];
                State cand;
                cand.score = prevState.score + cur.w;
                cand.idx = prevState.idx;
                cand.idx.push_back(cur.i);
                std::sort(cand.idx.begin(), cand.idx.end());
                dp[i][t] = better(dp[i][t], cand);
            }
        }
        State best = dp[n][0];
        for (int t = 1; t <= 4; t++) best = better(best, dp[n][t]);
        return best.idx;
    }
};


########## 3416_subsequences_with_a_unique_middle_mode_ii ##########
// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

#include <unordered_map>
#include <vector>

class Solution {
    bool uniqueMode(const std::vector<int>& a) {
        std::unordered_map<int, int> freq;
        for (int x : a) freq[x]++;
        int best = 0, cnt = 0;
        for (auto& [_, f] : freq) {
            if (f > best) { best = f; cnt = 1; }
            else if (f == best) cnt++;
        }
        return cnt == 1;
    }

public:
    int subsequencesWithMiddleMode(std::vector<int>& nums) {
        const int mod = 1000000007;
        int n = (int)nums.size();
        int ans = 0;
        for (int mid = 2; mid < n - 2; mid++) {
            for (int a = 0; a < mid; a++) {
                for (int b = a + 1; b < mid; b++) {
                    for (int c = mid + 1; c < n; c++) {
                        for (int d = c + 1; d < n; d++) {
                            std::vector<int> seq{nums[a], nums[b], nums[mid], nums[c], nums[d]};
                            if (uniqueMode(seq)) ans = (ans + 1) % mod;
                        }
                    }
                }
            }
        }
        return ans;
    }
};


########## 3417_zigzag_grid_traversal_with_skip ##########
// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

#include <vector>

class Solution {
public:
    std::vector<int> zigzagTraversal(std::vector<std::vector<int>>& grid) {
        std::vector<int> ans;
        bool skip = false;
        for (int i = 0; i < (int)grid.size(); i++) {
            auto& row = grid[i];
            if (i % 2 == 0) {
                for (int v : row) {
                    if (!skip) ans.push_back(v);
                    skip = !skip;
                }
            } else {
                for (int j = (int)row.size() - 1; j >= 0; j--) {
                    if (!skip) ans.push_back(row[j]);
                    skip = !skip;
                }
            }
        }
        return ans;
    }
};


########## 3418_maximum_amount_of_money_robot_can_earn ##########
// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumAmount(std::vector<std::vector<int>>& coins) {
        int m = (int)coins.size(), n = (int)coins[0].size();
        const int neg = -(1 << 30);
        std::vector<std::vector<std::vector<int>>> dp(m, std::vector<std::vector<int>>(n, std::vector<int>(3, neg)));
        if (coins[0][0] < 0) {
            dp[0][0][0] = coins[0][0];
            dp[0][0][1] = 0;
            dp[0][0][2] = 0;
        } else {
            dp[0][0][0] = coins[0][0];
            dp[0][0][1] = coins[0][0];
            dp[0][0][2] = coins[0][0];
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int k = 0; k < 3; k++) {
                    int best = neg;
                    if (i > 0) best = std::max(best, dp[i - 1][j][k]);
                    if (j > 0) best = std::max(best, dp[i][j - 1][k]);
                    if (best == neg) continue;
                    if (coins[i][j] >= 0) dp[i][j][k] = best + coins[i][j];
                    else dp[i][j][k] = std::max(dp[i][j][k], best + coins[i][j]);
                }
                for (int k = 1; k < 3; k++) {
                    int best = neg;
                    if (i > 0) best = std::max(best, dp[i - 1][j][k - 1]);
                    if (j > 0) best = std::max(best, dp[i][j - 1][k - 1]);
                    if (best != neg && coins[i][j] < 0) dp[i][j][k] = std::max(dp[i][j][k], best);
                }
            }
        }
        return std::max({dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]});
    }
};


########## 3419_minimize_the_maximum_edge_weight_of_graph ##########
// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

#include <queue>
#include <vector>

class Solution {
public:
    int minMaxWeight(int n, std::vector<std::vector<int>>& edges, int threshold) {
        (void)threshold;
        auto ok = [&](int mid) {
            std::vector<std::vector<int>> g(n);
            for (auto& e : edges) {
                int a = e[0], b = e[1], w = e[2];
                if (w <= mid) g[b].push_back(a);
            }
            std::vector<char> vis(n);
            std::queue<int> q;
            q.push(0);
            vis[0] = 1;
            int cnt = 1;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : g[u]) {
                    if (!vis[v]) {
                        vis[v] = 1;
                        cnt++;
                        q.push(v);
                    }
                }
            }
            return cnt == n;
        };
        int lo = 1, hi = 1000001, ans = -1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) {
                ans = mid;
                hi = mid;
            } else lo = mid + 1;
        }
        return ans;
    }
};


########## 3420_count_non_decreasing_subarrays_after_k_operations ##########
// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long countNonDecreasingSubarrays(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long cost = 0;
            int maxV = nums[i];
            for (int j = i; j < n; j++) {
                if (nums[j] >= maxV) maxV = nums[j];
                else cost += maxV - nums[j];
                if (cost > k) break;
                ans++;
            }
        }
        return ans;
    }
};


########## 3422_minimum_operations_to_make_subarray_elements_equal ##########
// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        long long ans = 1LL << 62;
        for (int i = 0; i + k <= n; i++) {
            std::vector<int> sub(nums.begin() + i, nums.begin() + i + k);
            std::sort(sub.begin(), sub.end());
            int med = sub[k / 2];
            long long cost = 0;
            for (int x : sub) cost += std::abs(x - med);
            if (cost < ans) ans = cost;
        }
        return ans;
    }
};


########## 3423_maximum_difference_between_adjacent_elements_in_a_circular_array ##########
// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int maxAdjacentDistance(std::vector<int>& nums) {
        int ans = 0;
        int n = (int)nums.size();
        for (int i = 0; i < n; i++) {
            int d = std::abs(nums[i] - nums[(i + 1) % n]);
            if (d > ans) ans = d;
        }
        return ans;
    }
};


########## 3424_minimum_cost_to_make_arrays_identical ##########
// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long minCost(std::vector<int>& arr, std::vector<int>& brr, long long k) {
        long long noSwap = 0;
        for (int i = 0; i < (int)arr.size(); i++) noSwap += std::abs(arr[i] - brr[i]);
        std::vector<int> a2 = arr, b2 = brr;
        std::sort(a2.begin(), a2.end());
        std::sort(b2.begin(), b2.end());
        long long withSwap = k;
        for (int i = 0; i < (int)a2.size(); i++) withSwap += std::abs(a2[i] - b2[i]);
        return noSwap < withSwap ? noSwap : withSwap;
    }
};


########## 3425_longest_special_path ##########
// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

#include <functional>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> longestSpecialPath(std::vector<std::vector<int>>& edges, std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        int bestLen = 0, bestNodes = 1;
        std::unordered_map<int, int> last;
        std::function<void(int, int, int, int, std::vector<int>&)> dfs =
            [&](int u, int p, int dist, int left, std::vector<int>& path) {
            int prevPos = -1;
            bool seen = last.count(nums[u]);
            if (seen) prevPos = last[nums[u]];
            last[nums[u]] = (int)path.size();
            int newLeft = left;
            if (seen && prevPos >= left) newLeft = prevPos + 1;
            path.push_back(dist);
            int length = dist - path[newLeft];
            int nodes = (int)path.size() - newLeft;
            if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
                bestLen = length;
                bestNodes = nodes;
            }
            for (auto [to, w] : g[u]) {
                if (to == p) continue;
                dfs(to, u, dist + w, newLeft, path);
            }
            path.pop_back();
            if (seen) last[nums[u]] = prevPos;
            else last.erase(nums[u]);
        };
        std::vector<int> path;
        dfs(0, -1, 0, 0, path);
        return {bestLen, bestNodes};
    }
};


########## 3426_manhattan_distances_of_all_arrangements_of_pieces ##########
// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

class Solution {
    static long long modPow(long long a, long long e, int mod) {
        long long r = 1;
        a %= mod;
        while (e > 0) {
            if (e & 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return r;
    }
    static int comb(int n, int k, int mod) {
        if (k < 0 || k > n) return 0;
        long long num = 1, den = 1;
        for (int i = 0; i < k; i++) {
            num = num * (n - i) % mod;
            den = den * (i + 1) % mod;
        }
        return (int)(num * modPow(den, mod - 2, mod) % mod);
    }

public:
    int distanceSum(int m, int n, int k) {
        const int mod = 1000000007;
        if (k < 2) return 0;
        int totalCells = m * n;
        int pairChoose = comb(totalCells - 2, k - 2, mod);
        long long sumDist = 0;
        for (int d = 1; d < m; d++) sumDist += (long long)d * (m - d) * n * n;
        for (int d = 1; d < n; d++) sumDist += (long long)d * (n - d) * m * m;
        return (int)(sumDist % mod * pairChoose % mod);
    }
};


########## 3427_sum_of_variable_length_subarrays ##########
// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

#include <vector>

class Solution {
public:
    int subarraySum(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int start = i - nums[i];
            if (start < 0) start = 0;
            ans += pref[i + 1] - pref[start];
        }
        return ans;
    }
};


########## 3428_maximum_and_minimum_sums_of_at_most_size_k_subsequences ##########
// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minMaxSums(std::vector<int>& nums, int k) {
        const int mod = 1000000007;
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::vector<std::vector<int>> C(n + 1, std::vector<int>(k, 0));
        for (int i = 0; i <= n; i++) {
            C[i][0] = 1;
            for (int j = 1; j < k && j <= i; j++) C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int waysMax = 0;
            for (int j = 0; j < k && j <= i; j++) waysMax = (waysMax + C[i][j]) % mod;
            int waysMin = 0;
            int right = n - i - 1;
            for (int j = 0; j < k && j <= right; j++) waysMin = (waysMin + C[right][j]) % mod;
            ans = (int)((ans + (long long)nums[i] * waysMax % mod + (long long)nums[i] * waysMin % mod) % mod);
        }
        return ans;
    }
};


########## 3429_paint_house_iv ##########
// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long minCost(int n, std::vector<std::vector<int>>& cost) {
        const long long inf = 1LL << 60;
        int m = n / 2;
        long long dp[3][3];
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                dp[a][b] = (a == b) ? inf : (long long)cost[0][a] + cost[n - 1][b];
            }
        }
        for (int i = 1; i < m; i++) {
            long long ndp[3][3];
            for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) ndp[a][b] = inf;
            for (int pa = 0; pa < 3; pa++) {
                for (int pb = 0; pb < 3; pb++) {
                    if (dp[pa][pb] >= inf) continue;
                    for (int a = 0; a < 3; a++) {
                        if (a == pa) continue;
                        for (int b = 0; b < 3; b++) {
                            if (b == pb || a == b) continue;
                            long long v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b];
                            if (v < ndp[a][b]) ndp[a][b] = v;
                        }
                    }
                }
            }
            for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) dp[a][b] = ndp[a][b];
        }
        long long ans = inf;
        for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) if (dp[a][b] < ans) ans = dp[a][b];
        return ans;
    }
};


########## 3430_maximum_and_minimum_sums_of_at_most_size_k_subarrays ##########
// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long minMaxSubarraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int mn = nums[i], mx = nums[i];
            for (int j = i; j < n && j - i + 1 <= k; j++) {
                if (nums[j] < mn) mn = nums[j];
                if (nums[j] > mx) mx = nums[j];
                ans += mn + mx;
            }
        }
        return ans;
    }
};


########## 3431_minimum_unlocked_indices_to_sort_nums ##########
// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

#include <vector>

class Solution {
public:
    int minUnlockedIndices(std::vector<int>& nums, std::vector<int>& locked) {
        int n = (int)nums.size();
        bool need = false;
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[i - 1]) { need = true; break; }
        }
        if (!need) return 0;
        int left = n, right = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] > nums[j]) {
                    if (i < left) left = i;
                    if (j > right) right = j;
                }
            }
        }
        if (right < left) return 0;
        int ans = 0;
        for (int i = left; i <= right; i++) if (locked[i] == 1) ans++;
        std::vector<int> tmp = nums, lock = locked;
        for (int i = left; i <= right; i++) lock[i] = 0;
        bool changed = true;
        while (changed) {
            changed = false;
            for (int i = 0; i + 1 < n; i++) {
                if (lock[i] == 0 && lock[i + 1] == 0 && tmp[i] > tmp[i + 1]) {
                    std::swap(tmp[i], tmp[i + 1]);
                    changed = true;
                }
            }
        }
        for (int i = 1; i < n; i++) if (tmp[i] < tmp[i - 1]) return -1;
        return ans;
    }
};


########## 3432_count_partitions_with_even_sum_difference ##########
// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

#include <vector>

class Solution {
public:
    int countPartitions(std::vector<int>& nums) {
        int total = 0;
        for (int x : nums) total += x;
        int ans = 0, left = 0;
        for (int i = 0; i < (int)nums.size() - 1; i++) {
            left += nums[i];
            if ((left - (total - left)) % 2 == 0) ans++;
        }
        return ans;
    }
};


########## 3433_count_mentions_per_user ##########
// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> countMentions(int numberOfUsers, std::vector<std::vector<std::string>>& events) {
        std::stable_sort(events.begin(), events.end(), [](const auto& a, const auto& b) {
            int ti = std::stoi(a[1]), tj = std::stoi(b[1]);
            if (ti != tj) return ti < tj;
            return a[0] > b[0];
        });
        std::vector<char> online(numberOfUsers, 1);
        std::vector<int> offlineUntil(numberOfUsers, 0);
        std::vector<int> ans(numberOfUsers, 0);
        for (auto& e : events) {
            int t = std::stoi(e[1]);
            for (int i = 0; i < numberOfUsers; i++) {
                if (!online[i] && offlineUntil[i] <= t) online[i] = 1;
            }
            if (e[0] == "OFFLINE") {
                int id = std::stoi(e[2]);
                online[id] = 0;
                offlineUntil[id] = t + 60;
            } else {
                const std::string& msg = e[2];
                if (msg == "ALL") {
                    for (int i = 0; i < numberOfUsers; i++) ans[i]++;
                } else if (msg == "HERE") {
                    for (int i = 0; i < numberOfUsers; i++) if (online[i]) ans[i]++;
                } else {
                    std::istringstream iss(msg);
                    std::string part;
                    while (iss >> part) {
                        int id = std::stoi(part.substr(2));
                        ans[id]++;
                    }
                }
            }
        }
        return ans;
    }
};


########## 3434_maximum_frequency_after_subarray_operation ##########
// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k) {
        int base = 0;
        for (int x : nums) if (x == k) base++;
        int ans = base;
        std::unordered_set<int> uniq(nums.begin(), nums.end());
        for (int v : uniq) {
            if (v == k) continue;
            int best = 0, cur = 0;
            for (int x : nums) {
                int delta = 0;
                if (x == v) delta = 1;
                else if (x == k) delta = -1;
                cur += delta;
                if (cur < 0) cur = 0;
                if (cur > best) best = cur;
            }
            if (base + best > ans) ans = base + best;
        }
        return ans;
    }
};


########## 3435_frequencies_of_shortest_supersequences ##########
// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> supersequences(std::vector<std::string>& words) {
        bool used[26] = {};
        for (auto& w : words) {
            used[w[0] - 'a'] = true;
            used[w[1] - 'a'] = true;
        }
        std::vector<int> letters;
        for (int i = 0; i < 26; i++) if (used[i]) letters.push_back(i);
        int m = (int)letters.size();
        int best = 1000000000;
        std::vector<std::vector<int>> bestFreqs;
        int freq[26] = {};
        std::function<void(int)> dfs = [&](int i) {
            if (i == m) {
                bool ok = true;
                for (auto& w : words) {
                    int a = w[0] - 'a', b = w[1] - 'a';
                    if (a == b) {
                        if (freq[a] < 2) { ok = false; break; }
                    } else if (freq[a] < 1 || freq[b] < 1) { ok = false; break; }
                }
                if (!ok) return;
                int sum = 0;
                std::vector<int> f(26);
                for (int j = 0; j < 26; j++) { f[j] = freq[j]; sum += freq[j]; }
                if (sum < best) {
                    best = sum;
                    bestFreqs = {f};
                } else if (sum == best) bestFreqs.push_back(f);
                return;
            }
            int L = letters[i];
            for (int c = 1; c <= 2; c++) {
                freq[L] = c;
                dfs(i + 1);
            }
            freq[L] = 0;
        };
        dfs(0);
        return bestFreqs;
    }
};
