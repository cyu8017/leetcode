

// ========== 000 3609_minimum_moves_to_reach_target_in_grid ==========
// LeetCode 3609 - Minimum Moves to Reach Target in Grid
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/


class Solution {
public:
    int minMoves(int sx, int sy, int tx, int ty) {
        int ans = 0;
        while (tx > sx || ty > sy) {
            if (tx < sx || ty < sy) return -1;
            if (tx == ty) return -1;
            if (tx > ty) {
                if (ty > sy) {
                    if (tx >= 2 * ty) {
                        if (tx % 2 != 0) return -1;
                        tx /= 2;
                    } else {
                        tx -= ty;
                    }
                    ans++;
                } else {
                    if (ty != sy) return -1;
                    while (tx > sx) {
                        if (tx >= 2 * ty) {
                            if (tx % 2 != 0) return -1;
                            tx /= 2;
                        } else {
                            tx -= ty;
                        }
                        ans++;
                        if (tx < sx) return -1;
                    }
                }
            } else {
                if (tx > sx) {
                    if (ty >= 2 * tx) {
                        if (ty % 2 != 0) return -1;
                        ty /= 2;
                    } else {
                        ty -= tx;
                    }
                    ans++;
                } else {
                    if (tx != sx) return -1;
                    while (ty > sy) {
                        if (ty >= 2 * tx) {
                            if (ty % 2 != 0) return -1;
                            ty /= 2;
                        } else {
                            ty -= tx;
                        }
                        ans++;
                        if (ty < sy) return -1;
                    }
                }
            }
        }
        return (tx == sx && ty == sy) ? ans : -1;
    }
};


// ========== 001 3610_minimum_number_of_primes_to_sum_to_target ==========
// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

#include <climits>
#include <vector>

class Solution {
    static std::vector<int> primes;
    static void ensurePrimes() {
        if (!primes.empty()) return;
        int x = 2;
        while ((int)primes.size() < 1000) {
            bool is_prime = true;
            for (int p : primes) {
                if (p * p > x) break;
                if (x % p == 0) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) primes.push_back(x);
            x++;
        }
    }

public:
    int minNumberOfPrimes(int n, int m) {
        ensurePrimes();
        const int inf = INT_MAX / 2;
        std::vector<int> f(n + 1, inf);
        f[0] = 0;
        for (int pi = 0; pi < m; pi++) {
            int x = primes[pi];
            for (int i = x; i <= n; i++)
                if (f[i - x] + 1 < f[i]) f[i] = f[i - x] + 1;
        }
        return f[n] < inf ? f[n] : -1;
    }
};

std::vector<int> Solution::primes;


// ========== 002 3612_process_string_with_special_operations_i ==========
// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

#include <algorithm>
#include <cctype>
#include <string>

class Solution {
public:
    std::string processStr(std::string s) {
        std::string result;
        for (char c : s) {
            if (std::isalpha((unsigned char)c)) result.push_back(c);
            else if (c == '*') {
                if (!result.empty()) result.pop_back();
            } else if (c == '#') result += result;
            else if (c == '%') std::reverse(result.begin(), result.end());
        }
        return result;
    }
};


// ========== 003 3613_minimize_maximum_component_cost ==========
// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minCost(int n, std::vector<std::vector<int>>& edges, int k) {
        std::vector<int> p(n);
        for (int i = 0; i < n; i++) p[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            return p[x] == x ? x : p[x] = self(self, p[x]);
        };
        if (k == n) return 0;
        std::sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
        int cnt = n;
        for (auto& e : edges) {
            int pu = find(find, e[0]), pv = find(find, e[1]);
            if (pu != pv) {
                p[pu] = pv;
                if (--cnt <= k) return e[2];
            }
        }
        return 0;
    }
};


// ========== 004 3614_process_string_with_special_operations_ii ==========
// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

#include <string>

class Solution {
public:
    char processStr(std::string s, long long k) {
        long long m = 0;
        for (char c : s) {
            if (c == '*') m = m > 0 ? m - 1 : 0;
            else if (c == '#') m <<= 1;
            else if (c != '%') m += 1;
        }
        if (k >= m) return '.';
        for (int i = (int)s.size() - 1;; i--) {
            char c = s[i];
            if (c == '*') m += 1;
            else if (c == '#') {
                m /= 2;
                if (k >= m) k -= m;
            } else if (c == '%') {
                k = m - 1 - k;
            } else {
                m -= 1;
                if (k == m) return c;
            }
        }
    }
};


// ========== 005 3615_longest_palindromic_path_in_graph ==========
// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <vector>

class Solution {
    int expandPal(std::vector<std::vector<int>>& g, const std::string& label, int l, int r) {
        std::set<std::pair<int, int>> vis;
        struct State { int l, r, length; };
        std::queue<State> q;
        int len0 = (l != r) ? 2 : 1;
        q.push({l, r, len0});
        int best = len0;
        vis.insert({std::min(l, r), std::max(l, r)});
        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            for (int a : g[cur.l]) {
                for (int b : g[cur.r]) {
                    if (a == b || label[a] != label[b]) continue;
                    auto p = std::make_pair(std::min(a, b), std::max(a, b));
                    if (vis.count(p)) continue;
                    vis.insert(p);
                    int nl = cur.length + 2;
                    best = std::max(best, nl);
                    q.push({a, b, nl});
                }
            }
        }
        return best;
    }

public:
    int maxLen(int n, std::vector<std::vector<int>>& edges, std::string label) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = 1;
        for (int i = 0; i < n; i++) {
            ans = std::max(ans, expandPal(g, label, i, i));
            for (int j : g[i]) {
                if (i < j && label[i] == label[j]) ans = std::max(ans, expandPal(g, label, i, j));
            }
        }
        return ans;
    }
};


// ========== 006 3616_number_of_student_replacements ==========
// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

#include <vector>

class Solution {
public:
    int totalReplacements(std::vector<int>& ranks) {
        int ans = 0, cur = ranks[0];
        for (int x : ranks) {
            if (x < cur) {
                cur = x;
                ans++;
            }
        }
        return ans;
    }
};


// ========== 007 3618_split_array_by_prime_indices ==========
// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

#include <cmath>
#include <vector>

class Solution {
    static constexpr int M = 100010;
    static std::vector<bool>& primes() {
        static std::vector<bool> p;
        if (p.empty()) {
            p.assign(M, true);
            p[0] = p[1] = false;
            for (int i = 2; i < M; i++)
                if (p[i])
                    for (int j = i + i; j < M; j += i) p[j] = false;
        }
        return p;
    }

public:
    long long splitArray(std::vector<int>& nums) {
        auto& pr = primes();
        long long ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (pr[i]) ans += nums[i];
            else ans -= nums[i];
        }
        return std::llabs(ans);
    }
};


// ========== 008 3619_count_islands_with_total_value_divisible_by_k ==========
// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

#include <vector>

class Solution {
public:
    int countIslands(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size(), ans = 0;
        int dirs[5] = {-1, 0, 1, 0, -1};
        auto dfs = [&](auto&& self, int i, int j) -> long long {
            long long s = grid[i][j];
            grid[i][j] = 0;
            for (int d = 0; d < 4; d++) {
                int x = i + dirs[d], y = j + dirs[d + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] > 0) s += self(self, x, y);
            }
            return s;
        };
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] > 0 && dfs(dfs, i, j) % k == 0) ans++;
        return ans;
    }
};


// ========== 009 3620_network_recovery_pathways ==========
// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

#include <algorithm>
#include <climits>
#include <queue>
#include <vector>

class Solution {
public:
    int findMaxPathScore(std::vector<std::vector<int>>& edges, std::vector<bool>& online, long long k) {
        int n = (int)online.size();
        std::vector<std::vector<std::pair<int, int>>> g(n);
        int l = INT_MAX, r = 0;
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            if (!online[u] || !online[v]) continue;
            g[u].push_back({v, w});
            l = std::min(l, w);
            r = std::max(r, w);
        }
        if (l == INT_MAX) return -1;
        auto check = [&](int mid) {
            const int INF = INT_MAX / 2;
            std::vector<int> dist(n, INF);
            dist[0] = 0;
            using P = std::pair<int, int>;
            std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
            pq.push({0, 0});
            while (!pq.empty()) {
                auto [d, u] = pq.top();
                pq.pop();
                if ((long long)d > k) return false;
                if (u == n - 1) return true;
                if (dist[u] < d) continue;
                for (auto [v, w] : g[u]) {
                    if (w < mid) continue;
                    int nd = d + w;
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.push({nd, v});
                    }
                }
            }
            return false;
        };
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (check(mid)) l = mid;
            else r = mid - 1;
        }
        return check(l) ? l : -1;
    }
};


// ========== 010 3621_number_of_integers_with_popcount_depth_equal_to_k_i ==========
// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

#include <map>
#include <string>
#include <tuple>

class Solution {
public:
    long long popcountDepth(long long n, int k) {
        if (k == 0) return n >= 1 ? 1 : 0;
        auto depth = [](int x) {
            if (x <= 0) return 100;
            int d = 0;
            while (x > 1) {
                x = __builtin_popcount((unsigned)x);
                d++;
            }
            return d;
        };
        std::string s;
        for (long long x = n; x > 0; x >>= 1) s = char('0' + (x & 1)) + s;
        if (s.empty()) s = "0";
        std::map<std::tuple<int, int, int, int>, long long> memo;
        auto dfs = [&](auto&& self, int pos, int tight, int started, int pc) -> long long {
            if (pos == (int)s.size()) {
                if (!started) return 0;
                if (pc == 1) return k == 1 ? 1 : 0;
                return depth(pc) == k - 1 ? 1 : 0;
            }
            auto key = std::make_tuple(pos, tight, started, pc);
            if (memo.count(key)) return memo[key];
            int up = tight ? s[pos] - '0' : 1;
            long long res = 0;
            for (int dig = 0; dig <= up; dig++) {
                int nt = (tight && dig == up) ? 1 : 0;
                if (!started && dig == 0) res += self(self, pos + 1, nt, 0, 0);
                else res += self(self, pos + 1, nt, 1, pc + dig);
            }
            return memo[key] = res;
        };
        return dfs(dfs, 0, 1, 0, 0);
    }
};


// ========== 011 3622_check_divisibility_by_digit_sum_and_product ==========
// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/


class Solution {
public:
    bool checkDivisibility(int n) {
        int s = 0, p = 1, x = n;
        while (x) {
            int v = x % 10;
            x /= 10;
            s += v;
            p *= v;
        }
        return n % (s + p) == 0;
    }
};


// ========== 012 3623_count_number_of_trapezoids_i ==========
// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countTrapezoids(std::vector<std::vector<int>>& points) {
        const int mod = 1000000007;
        std::unordered_map<int, int> cnt;
        for (auto& p : points) cnt[p[1]]++;
        long long ans = 0, s = 0;
        for (auto& [_, v] : cnt) {
            long long t = 1LL * v * (v - 1) / 2;
            ans = (ans + s * t) % mod;
            s += t;
        }
        return (int)ans;
    }
};


// ========== 013 3624_number_of_integers_with_popcount_depth_equal_to_k_ii ==========
// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

#include <vector>

class Solution {
    int depth(long long x) {
        if (x == 1) return 0;
        int d = 0;
        while (x > 1) {
            x = __builtin_popcountll((unsigned long long)x);
            d++;
        }
        return d;
    }

public:
    std::vector<int> popcountDepth(std::vector<long long>& nums, std::vector<std::vector<long long>>& queries) {
        std::vector<long long> a = nums;
        std::vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int l = (int)q[1], r = (int)q[2], k = (int)q[3], cnt = 0;
                for (int i = l; i <= r; i++)
                    if (depth(a[i]) == k) cnt++;
                ans.push_back(cnt);
            } else {
                a[(int)q[1]] = q[2];
            }
        }
        return ans;
    }
};


// ========== 014 3625_count_number_of_trapezoids_ii ==========
// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countTrapezoids(std::vector<std::vector<int>>& points) {
        int n = (int)points.size();
        std::unordered_map<double, std::unordered_map<double, int>> cnt1;
        std::unordered_map<int, std::unordered_map<double, int>> cnt2;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = 0; j < i; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                int dx = x2 - x1, dy = y2 - y1;
                double k, b;
                if (dx == 0) {
                    k = 1e9;
                    b = x1;
                } else {
                    k = (double)dy / dx;
                    b = (double)((long long)y1 * dx - (long long)x1 * dy) / dx;
                }
                cnt1[k][b]++;
                int p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000);
                cnt2[p][k]++;
            }
        }
        int ans = 0;
        for (auto& [_, e] : cnt1) {
            int s = 0;
            for (auto& [__, t] : e) {
                ans += s * t;
                s += t;
            }
        }
        for (auto& [_, e] : cnt2) {
            int s = 0;
            for (auto& [__, t] : e) {
                ans -= s * t;
                s += t;
            }
        }
        return ans;
    }
};


// ========== 015 3627_maximum_median_sum_of_subsequences_of_size_3 ==========
// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maximumMedianSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = n / 3; i < n; i += 2) ans += nums[i];
        return ans;
    }
};


// ========== 016 3628_maximum_number_of_subsequences_after_one_inserting ==========
// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

#include <algorithm>
#include <string>

class Solution {
public:
    long long numOfSubsequences(std::string s) {
        auto calc = [&](const std::string& t) {
            long long cnt = 0, a = 0;
            for (char c : s) {
                if (c == t[1]) cnt += a;
                if (c == t[0]) a++;
            }
            return cnt;
        };
        long long l = 0, r = 0;
        for (char c : s)
            if (c == 'T') r++;
        long long ans = 0, mx = 0;
        for (char c : s) {
            if (c == 'T') r--;
            if (c == 'C') ans += l * r;
            if (c == 'L') l++;
            mx = std::max(mx, l * r);
        }
        mx = std::max({mx, calc("LC"), calc("CT")});
        return ans + mx;
    }
};


// ========== 017 3629_minimum_jumps_to_reach_end_via_prime_teleportation ==========
// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

#include <unordered_map>
#include <vector>

class Solution {
    static constexpr int mx = 1000001;
    static std::vector<std::vector<int>>& factors() {
        static std::vector<std::vector<int>> f;
        if (f.empty()) {
            f.assign(mx, {});
            for (int i = 2; i < mx; i++) {
                if (f[i].empty()) {
                    for (int j = i; j < mx; j += i) f[j].push_back(i);
                }
            }
        }
        return f;
    }

public:
    int minJumps(std::vector<int>& nums) {
        auto& fac = factors();
        int n = (int)nums.size();
        std::unordered_map<int, std::vector<int>> g;
        for (int i = 0; i < n; i++)
            for (int p : fac[nums[i]]) g[p].push_back(i);
        int ans = 0;
        std::vector<bool> vis(n);
        vis[0] = true;
        std::vector<int> q{0};
        while (true) {
            std::vector<int> nq;
            for (int i : q) {
                if (i == n - 1) return ans;
                std::vector<int> idx = g[nums[i]];
                idx.push_back(i + 1);
                if (i > 0) idx.push_back(i - 1);
                for (int j : idx) {
                    if (j >= 0 && j < n && !vis[j]) {
                        vis[j] = true;
                        nq.push_back(j);
                    }
                }
                g[nums[i]].clear();
            }
            q = std::move(nq);
            ans++;
        }
    }
};


// ========== 018 3630_partition_array_for_maximum_xor_and_and ==========
// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maximizeXorAndXor(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long best = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int andVal = -1, xorRest = 0;
            for (int i = 0; i < n; i++) {
                if ((mask >> i) & 1) {
                    andVal = andVal < 0 ? nums[i] : (andVal & nums[i]);
                } else {
                    xorRest ^= nums[i];
                }
            }
            if (andVal < 0) andVal = 0;
            int comp = ((1 << n) - 1) ^ mask;
            for (int sub = comp;; sub = (sub - 1) & comp) {
                int x1 = 0;
                for (int i = 0; i < n; i++)
                    if ((sub >> i) & 1) x1 ^= nums[i];
                int x2 = xorRest ^ x1;
                best = std::max(best, (long long)andVal + x1 + x2);
                if (sub == 0) break;
            }
        }
        return best;
    }
};


// ========== 019 3631_sort_threats_by_severity_and_exploitability ==========
// LeetCode 3631 - Sort Threats by Severity and Exploitability
// https://leetcode.com/problems/sort-threats-by-severity-and-exploitability/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> sortThreats(std::vector<std::vector<int>>& threats) {
        std::sort(threats.begin(), threats.end(), [](auto& a, auto& b) {
            long long s1 = 2LL * a[1] + a[2], s2 = 2LL * b[1] + b[2];
            if (s1 == s2) return a[0] < b[0];
            return s2 < s1;
        });
        return threats;
    }
};


// ========== 020 3632_subarrays_with_xor_at_least_k ==========
// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

#include <vector>

class Solution {
public:
    long long subarraysWithXorAtLeastK(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = 0;
            for (int j = i; j < n; j++) {
                x ^= nums[j];
                if (x >= k) ans++;
            }
        }
        return ans;
    }
};


// ========== 021 3633_earliest_finish_time_for_land_and_water_rides_i ==========
// LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
    int calc(std::vector<int>& a1, std::vector<int>& t1, std::vector<int>& a2, std::vector<int>& t2) {
        int minEnd = INT_MAX;
        for (int i = 0; i < (int)a1.size(); i++) minEnd = std::min(minEnd, a1[i] + t1[i]);
        int ans = INT_MAX;
        for (int i = 0; i < (int)a2.size(); i++) ans = std::min(ans, std::max(minEnd, a2[i]) + t2[i]);
        return ans;
    }

public:
    int earliestFinishTime(std::vector<int>& landStartTime, std::vector<int>& landDuration,
                           std::vector<int>& waterStartTime, std::vector<int>& waterDuration) {
        return std::min(calc(landStartTime, landDuration, waterStartTime, waterDuration),
                        calc(waterStartTime, waterDuration, landStartTime, landDuration));
    }
};


// ========== 022 3634_minimum_removals_to_balance_array ==========
// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minRemoval(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size(), cnt = 0;
        for (int i = 0; i < n; i++) {
            int j = n;
            if (1LL * nums[i] * k <= nums[n - 1]) {
                long long target = 1LL * nums[i] * k + 1;
                j = (int)(std::lower_bound(nums.begin(), nums.end(), target) - nums.begin());
            }
            cnt = std::max(cnt, j - i);
        }
        return n - cnt;
    }
};


// ========== 023 3635_earliest_finish_time_for_land_and_water_rides_ii ==========
// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
    int calc(std::vector<int>& a1, std::vector<int>& t1, std::vector<int>& a2, std::vector<int>& t2) {
        int minEnd = INT_MAX;
        for (int i = 0; i < (int)a1.size(); i++) minEnd = std::min(minEnd, a1[i] + t1[i]);
        int ans = INT_MAX;
        for (int i = 0; i < (int)a2.size(); i++) ans = std::min(ans, std::max(minEnd, a2[i]) + t2[i]);
        return ans;
    }

public:
    int earliestFinishTime(std::vector<int>& landStartTime, std::vector<int>& landDuration,
                           std::vector<int>& waterStartTime, std::vector<int>& waterDuration) {
        return std::min(calc(landStartTime, landDuration, waterStartTime, waterDuration),
                        calc(waterStartTime, waterDuration, landStartTime, landDuration));
    }
};


// ========== 024 3636_threshold_majority_queries ==========
// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> subarrayMajority(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int l = queries[qi][0], r = queries[qi][1], thresh = queries[qi][2];
            std::unordered_map<int, int> freq;
            for (int i = l; i <= r; i++) freq[nums[i]]++;
            int bestVal = -1, bestCnt = 0;
            for (auto& [v, c] : freq) {
                if (c >= thresh && (c > bestCnt || (c == bestCnt && (bestVal == -1 || v < bestVal)))) {
                    bestCnt = c;
                    bestVal = v;
                }
            }
            ans[qi] = bestVal;
        }
        return ans;
    }
};


// ========== 025 3637_trionic_array_i ==========
// LeetCode 3637 - Trionic Array I
// https://leetcode.com/problems/trionic-array-i/

#include <vector>

class Solution {
public:
    bool isTrionic(std::vector<int>& nums) {
        int n = (int)nums.size(), p = 0;
        while (p < n - 2 && nums[p] < nums[p + 1]) p++;
        if (p == 0) return false;
        int q = p;
        while (q < n - 1 && nums[q] > nums[q + 1]) q++;
        if (q == p || q == n - 1) return false;
        while (q < n - 1 && nums[q] < nums[q + 1]) q++;
        return q == n - 1;
    }
};


// ========== 026 3638_maximum_balanced_shipments ==========
// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxBalancedShipments(std::vector<int>& weight) {
        int ans = 0, mx = 0;
        for (int x : weight) {
            mx = std::max(mx, x);
            if (x < mx) {
                ans++;
                mx = 0;
            }
        }
        return ans;
    }
};


// ========== 027 3639_minimum_time_to_activate_string ==========
// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

#include <string>
#include <vector>

class Solution {
public:
    int minTime(std::string s, std::vector<int>& order, int k) {
        int n = (int)s.size();
        long long total = 1LL * n * (n + 1) / 2;
        if (k > total) return -1;
        auto countValid = [&](int t) {
            std::vector<bool> star(n);
            for (int i = 0; i <= t; i++) star[order[i]] = true;
            long long invalid = 0;
            for (int i = 0; i < n;) {
                if (star[i]) {
                    i++;
                    continue;
                }
                int j = i;
                while (j < n && !star[j]) j++;
                long long L = j - i;
                invalid += L * (L + 1) / 2;
                i = j;
            }
            return total - invalid;
        };
        int lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (countValid(mid) >= k) {
                ans = mid;
                hi = mid - 1;
            } else lo = mid + 1;
        }
        return ans;
    }
};


// ========== 028 3640_trionic_array_ii ==========
// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long maxSumTrionic(std::vector<int>& nums) {
        int n = (int)nums.size(), i = 0;
        long long ans = LLONG_MIN;
        while (i < n) {
            int l = i;
            for (i++; i < n && nums[i - 1] < nums[i];) i++;
            if (i == l + 1) continue;
            int p = i - 1;
            long long s = (long long)nums[p - 1] + nums[p];
            while (i < n && nums[i - 1] > nums[i]) {
                s += nums[i];
                i++;
            }
            if (i == p + 1 || i == n || nums[i - 1] == nums[i]) continue;
            int q = i - 1;
            s += nums[i];
            i++;
            long long mx = 0, t = 0;
            while (i < n && nums[i - 1] < nums[i]) {
                t += nums[i];
                i++;
                mx = std::max(mx, t);
            }
            s += mx;
            mx = t = 0;
            for (int j = p - 2; j >= l; j--) {
                t += nums[j];
                mx = std::max(mx, t);
            }
            s += mx;
            ans = std::max(ans, s);
            i = q;
        }
        return ans;
    }
};


// ========== 029 3641_longest_semi_repeating_subarray ==========
// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> cnt;
        int ans = 0, cur = 0, l = 0;
        for (int r = 0; r < (int)nums.size(); r++) {
            if (++cnt[nums[r]] == 2) cur++;
            while (cur > k) {
                if (--cnt[nums[l]] == 1) cur--;
                l++;
            }
            ans = std::max(ans, r - l + 1);
        }
        return ans;
    }
};


// ========== 030 3643_flip_square_submatrix_vertically ==========
// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> reverseSubmatrix(std::vector<std::vector<int>>& grid, int x, int y, int k) {
        for (int i = x; i < x + k / 2; i++) {
            int i2 = x + k - 1 - (i - x);
            for (int j = y; j < y + k; j++) std::swap(grid[i][j], grid[i2][j]);
        }
        return grid;
    }
};


// ========== 031 3644_maximum_k_to_sort_a_permutation ==========
// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

#include <algorithm>
#include <vector>

class Solution {
public:
    int sortPermutation(std::vector<int>& nums) {
        int ans = -1;
        for (int i = 0; i < (int)nums.size(); i++)
            if (i != nums[i]) ans &= nums[i];
        return std::max(ans, 0);
    }
};


// ========== 032 3645_maximum_total_from_optimal_activation_order ==========
// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maxTotal(std::vector<int>& value, std::vector<int>& limit) {
        std::unordered_map<int, std::vector<int>> g;
        for (int i = 0; i < (int)value.size(); i++) g[limit[i]].push_back(value[i]);
        long long ans = 0;
        for (auto& [lim, vs] : g) {
            std::sort(vs.begin(), vs.end(), std::greater<int>());
            for (int i = 0; i < std::min(lim, (int)vs.size()); i++) ans += vs[i];
        }
        return ans;
    }
};


// ========== 033 3646_next_special_palindrome_number ==========
// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    long long specialPalindrome(long long n) {
        std::vector<long long> cands;
        auto gen = [&](auto&& self, int mask) -> void {
            int total = 0, odd = 0;
            for (int d = 1; d <= 9; d++) {
                if ((mask >> d) & 1) {
                    total += d;
                    if (d % 2 == 1) odd++;
                }
            }
            if (total == 0 || total > 18 || odd > 1) return;
            int halfCnt[10] = {};
            int mid = 0;
            for (int d = 1; d <= 9; d++) {
                if (((mask >> d) & 1) == 0) continue;
                halfCnt[d] = d / 2;
                if (d % 2 == 1) mid = d;
            }
            int halfLen = total / 2;
            auto dfs = [&](auto&& dfs_self, int pos, std::vector<int>& cur) -> void {
                if (pos == halfLen) {
                    std::string left, s;
                    for (int x : cur) left += char('0' + x);
                    s = left;
                    if (mid > 0) s += char('0' + mid);
                    for (int i = (int)left.size() - 1; i >= 0; i--) s += left[i];
                    cands.push_back(std::stoll(s));
                    return;
                }
                for (int d = 1; d <= 9; d++) {
                    if (halfCnt[d] == 0) continue;
                    halfCnt[d]--;
                    cur.push_back(d);
                    dfs_self(dfs_self, pos + 1, cur);
                    cur.pop_back();
                    halfCnt[d]++;
                }
            };
            std::vector<int> cur;
            dfs(dfs, 0, cur);
        };
        for (int mask = 1; mask < (1 << 10); mask++) {
            if (mask & 1) continue;
            gen(gen, mask);
        }
        std::sort(cands.begin(), cands.end());
        for (long long v : cands)
            if (v > n) return v;
        return -1;
    }
};


// ========== 034 3647_maximum_weight_in_two_bags ==========
// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxWeight(std::vector<int>& weights, int w1, int w2) {
        std::vector<std::vector<int>> f(w1 + 1, std::vector<int>(w2 + 1));
        for (int x : weights) {
            for (int j = w1; j >= 0; j--) {
                for (int k = w2; k >= 0; k--) {
                    if (x <= j) f[j][k] = std::max(f[j][k], f[j - x][k] + x);
                    if (x <= k) f[j][k] = std::max(f[j][k], f[j][k - x] + x);
                }
            }
        }
        return f[w1][w2];
    }
};


// ========== 035 3648_minimum_sensors_to_cover_grid ==========
// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/


class Solution {
public:
    int minSensors(int n, int m, int k) {
        int cover = 2 * k + 1;
        return ((n + cover - 1) / cover) * ((m + cover - 1) / cover);
    }
};


// ========== 036 3649_number_of_perfect_pairs ==========
// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    long long perfectPairs(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> absNums(n);
        for (int i = 0; i < n; i++) absNums[i] = std::abs(nums[i]);
        std::sort(absNums.begin(), absNums.end());
        long long ans = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (j < i + 1) j = i + 1;
            while (j < n && absNums[j] <= 2 * absNums[i]) j++;
            ans += j - i - 1;
        }
        return ans;
    }
};


// ========== 037 3650_minimum_cost_path_with_edge_reversals ==========
// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

#include <climits>
#include <queue>
#include <vector>

class Solution {
public:
    int minCost(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w * 2});
        }
        const int inf = INT_MAX / 2;
        std::vector<int> dist(n, inf);
        dist[0] = 0;
        using P = std::pair<int, int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u]) continue;
            if (u == n - 1) return d;
            for (auto [v, w] : g[u]) {
                int nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        return -1;
    }
};


// ========== 038 3651_minimum_cost_path_with_teleportations ==========
// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

#include <algorithm>
#include <climits>
#include <map>
#include <vector>

class Solution {
public:
    int minCost(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        const int inf = INT_MAX / 4;
        std::vector<std::vector<std::vector<int>>> f(k + 1, std::vector<std::vector<int>>(m, std::vector<int>(n, inf)));
        f[0][0][0] = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) f[0][i][j] = std::min(f[0][i][j], f[0][i - 1][j] + grid[i][j]);
                if (j > 0) f[0][i][j] = std::min(f[0][i][j], f[0][i][j - 1] + grid[i][j]);
            }
        }
        std::map<int, std::vector<std::pair<int, int>>, std::greater<int>> g;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) g[grid[i][j]].push_back({i, j});
        for (int t = 1; t <= k; t++) {
            int mn = inf;
            for (auto& [key, pos] : g) {
                for (auto& [pi, pj] : pos) mn = std::min(mn, f[t - 1][pi][pj]);
                for (auto& [pi, pj] : pos) f[t][pi][pj] = mn;
            }
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i > 0) f[t][i][j] = std::min(f[t][i][j], f[t][i - 1][j] + grid[i][j]);
                    if (j > 0) f[t][i][j] = std::min(f[t][i][j], f[t][i][j - 1] + grid[i][j]);
                }
            }
        }
        int ans = inf;
        for (int t = 0; t <= k; t++) ans = std::min(ans, f[t][m - 1][n - 1]);
        return ans;
    }
};


// ========== 039 3652_best_time_to_buy_and_sell_stock_using_strategy ==========
// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxProfit(std::vector<int>& prices, std::vector<int>& strategy, int k) {
        int n = (int)prices.size();
        std::vector<long long> s(n + 1), t(n + 1);
        for (int i = 1; i <= n; i++) {
            s[i] = s[i - 1] + 1LL * prices[i - 1] * strategy[i - 1];
            t[i] = t[i - 1] + prices[i - 1];
        }
        long long ans = s[n];
        for (int i = k; i <= n; i++) ans = std::max(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2]));
        return ans;
    }
};


// ========== 040 3653_xor_after_range_multiplication_queries_i ==========
// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

#include <vector>

class Solution {
public:
    int xorAfterQueries(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        const int mod = 1000000007;
        for (auto& q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            for (int idx = l; idx <= r; idx += k) nums[idx] = 1LL * nums[idx] * v % mod;
        }
        int ans = 0;
        for (int x : nums) ans ^= x;
        return ans;
    }
};


// ========== 041 3654_minimum_sum_after_divisible_sum_deletions ==========
// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

#include <climits>
#include <vector>

class Solution {
public:
    long long minArraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> prefix(n + 1);
        for (int i = 0; i < n; i++) prefix[i + 1] = (prefix[i] + nums[i]) % k;
        const long long inf = 1LL << 62;
        std::vector<long long> dp(n + 1), best(k, inf);
        best[0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + nums[i - 1];
            if (best[prefix[i]] < dp[i]) dp[i] = best[prefix[i]];
            if (dp[i] < best[prefix[i]]) best[prefix[i]] = dp[i];
        }
        return dp[n];
    }
};


// ========== 042 3655_xor_after_range_multiplication_queries_ii ==========
// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int xorAfterQueries(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        const int MOD = 1000000007;
        int n = (int)nums.size();
        struct Upd { int l, r, k, v; };
        std::unordered_map<int, std::vector<Upd>> byK;
        for (auto& q : queries) byK[q[2]].push_back({q[0], q[1], q[2], q[3]});
        std::vector<int> res = nums;
        for (auto& [k, ups] : byK) {
            std::vector<int> fac(n, 1);
            for (auto& u : ups)
                for (int i = u.l; i <= u.r; i += k) fac[i] = 1LL * fac[i] * u.v % MOD;
            for (int i = 0; i < n; i++) res[i] = 1LL * res[i] * fac[i] % MOD;
        }
        int ans = 0;
        for (int v : res) ans ^= v;
        return ans;
    }
};


// ========== 043 3656_determine_if_a_simple_graph_exists ==========
// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool simpleGraphExists(std::vector<int>& degrees) {
        int n = (int)degrees.size();
        std::vector<int> d = degrees;
        std::sort(d.begin(), d.end(), std::greater<int>());
        long long sum = 0;
        for (int x : d) {
            if (x < 0 || x >= n) return false;
            sum += x;
        }
        if (sum % 2 == 1) return false;
        std::vector<long long> prefix(n + 1);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + d[i];
        for (int k = 1; k <= n; k++) {
            long long right = 0;
            for (int i = k; i < n; i++) right += d[i] < k ? d[i] : k;
            if (prefix[k] > 1LL * k * (k - 1) + right) return false;
        }
        return true;
    }
};


// ========== 044 3658_gcd_of_odd_and_even_sums ==========
// LeetCode 3658 - GCD of Odd and Even Sums
// https://leetcode.com/problems/gcd-of-odd-and-even-sums/


class Solution {
public:
    int gcdOfOddEvenSums(int n) { return n; }
};


// ========== 045 3659_partition_array_into_k_distinct_groups ==========
// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool partitionArray(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (n % k != 0) return false;
        int m = n / k;
        int mx = *std::max_element(nums.begin(), nums.end());
        std::vector<int> cnt(mx + 1);
        for (int x : nums)
            if (++cnt[x] > m) return false;
        return true;
    }
};


// ========== 046 3660_jump_game_ix ==========
// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    std::vector<int> maxValue(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(n), preMax(n);
        preMax[0] = nums[0];
        for (int i = 1; i < n; i++) preMax[i] = std::max(preMax[i - 1], nums[i]);
        int sufMin = INT_MAX / 2;
        for (int i = n - 1; i >= 0; i--) {
            if (preMax[i] > sufMin) ans[i] = ans[i + 1];
            else ans[i] = preMax[i];
            sufMin = std::min(sufMin, nums[i]);
        }
        return ans;
    }
};


// ========== 047 3661_maximum_walls_destroyed_by_robots ==========
// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

#include <algorithm>
#include <map>
#include <vector>

class Solution {
public:
    int maxWalls(std::vector<int>& robots, std::vector<int>& distance, std::vector<int>& walls) {
        int n = (int)robots.size();
        std::vector<std::pair<int, int>> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {robots[i], distance[i]};
        std::sort(arr.begin(), arr.end());
        std::sort(walls.begin(), walls.end());
        std::map<std::pair<int, int>, int> f;
        auto dfs = [&](auto&& self, int i, int j) -> int {
            if (i < 0) return 0;
            auto key = std::make_pair(i, j);
            if (f.count(key)) return f[key];
            int left = arr[i].first - arr[i].second;
            if (i > 0) left = std::max(left, arr[i - 1].first + 1);
            int l = (int)(std::lower_bound(walls.begin(), walls.end(), left) - walls.begin());
            int r = (int)(std::lower_bound(walls.begin(), walls.end(), arr[i].first + 1) - walls.begin());
            int ans = self(self, i - 1, 0) + (r - l);
            int right = arr[i].first + arr[i].second;
            if (i + 1 < n) {
                if (j == 0) right = std::min(right, arr[i + 1].first - arr[i + 1].second - 1);
                else right = std::min(right, arr[i + 1].first - 1);
            }
            l = (int)(std::lower_bound(walls.begin(), walls.end(), arr[i].first) - walls.begin());
            r = (int)(std::lower_bound(walls.begin(), walls.end(), right + 1) - walls.begin());
            ans = std::max(ans, self(self, i - 1, 1) + (r - l));
            return f[key] = ans;
        };
        return dfs(dfs, n - 1, 1);
    }
};


// ========== 048 3662_filter_characters_by_frequency ==========
// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

#include <string>

class Solution {
public:
    std::string filterCharacters(std::string s, int k) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        std::string ans;
        for (char c : s)
            if (cnt[c - 'a'] < k) ans += c;
        return ans;
    }
};


// ========== 049 3663_find_the_least_frequent_digit ==========
// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/


class Solution {
public:
    int getLeastFrequentDigit(int n) {
        int cnt[10] = {}, ans = 0, f = 1 << 30;
        for (; n > 0; n /= 10) cnt[n % 10]++;
        for (int x = 0; x < 10; x++) {
            if (cnt[x] > 0 && cnt[x] < f) {
                f = cnt[x];
                ans = x;
            }
        }
        return ans;
    }
};


// ========== 050 3664_two_letter_card_game ==========
// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int score(std::vector<std::string>& cards, char x) {
        int xx = 0;
        int left[26] = {}, right[26] = {};
        for (auto& c : cards) {
            char a = c[0], b = c[1];
            if (a == x && b == x) xx++;
            else if (a == x) left[b - 'a']++;
            else if (b == x) right[a - 'a']++;
        }
        auto pairGroup = [](int* arr) {
            int total = 0, mx = 0;
            for (int i = 0; i < 26; i++) {
                total += arr[i];
                mx = std::max(mx, arr[i]);
            }
            int pairs = total / 2;
            if (total - mx < pairs) pairs = total - mx;
            return std::make_pair(pairs, total - 2 * pairs);
        };
        auto [lp, lr] = pairGroup(left);
        auto [rp, rr] = pairGroup(right);
        int ans = lp + rp;
        int rem = lr + rr;
        int use = std::min(xx, rem);
        ans += use;
        xx -= use;
        ans += xx / 2;
        return ans;
    }
};


// ========== 051 3665_twisted_mirror_path_count ==========
// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

#include <vector>

class Solution {
public:
    int uniquePaths(std::vector<std::vector<int>>& grid) {
        const int MOD = 1000000007;
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> dp(m, std::vector<int>(n));
        if (grid[0][0] == 1) return 0;
        dp[0][0] = 1;
        auto nextCell = [&](int i, int j, int di, int dj) -> std::tuple<int, int, bool> {
            int ni = i + di, nj = j + dj;
            while (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1) {
                if (dj == 1) {
                    di = 1;
                    dj = 0;
                } else {
                    di = 0;
                    dj = 1;
                }
                ni += di;
                nj += dj;
            }
            if (ni < 0 || nj < 0 || ni >= m || nj >= n) return {0, 0, false};
            return {ni, nj, true};
        };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 || dp[i][j] == 0) continue;
                auto [ni, nj, ok] = nextCell(i, j, 0, 1);
                if (ok) dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD;
                auto [ni2, nj2, ok2] = nextCell(i, j, 1, 0);
                if (ok2) dp[ni2][nj2] = (dp[ni2][nj2] + dp[i][j]) % MOD;
            }
        }
        return dp[m - 1][n - 1];
    }
};


// ========== 052 3666_minimum_operations_to_equalize_binary_string ==========
// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

#include <algorithm>
#include <set>
#include <string>
#include <vector>

class Solution {
public:
    int minOperations(std::string s, int k) {
        int n = (int)s.size();
        std::set<int> ts[2];
        for (int i = 0; i <= n; i++) ts[i % 2].insert(i);
        int cnt0 = (int)std::count(s.begin(), s.end(), '0');
        ts[cnt0 % 2].erase(cnt0);
        std::vector<int> q{cnt0};
        int ans = 0;
        while (!q.empty()) {
            std::vector<int> nq;
            for (int cur : q) {
                if (cur == 0) return ans;
                int l = cur + k - 2 * std::min(cur, k);
                int r = cur + k - 2 * std::max(k - n + cur, 0);
                auto& t = ts[l % 2];
                auto it = t.lower_bound(l);
                while (it != t.end() && *it <= r) {
                    nq.push_back(*it);
                    it = t.erase(it);
                }
            }
            q = std::move(nq);
            ans++;
        }
        return -1;
    }
};


// ========== 053 3667_sort_array_by_absolute_value ==========
// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<int> sortByAbsoluteValue(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int a, int b) { return std::abs(a) < std::abs(b); });
        return nums;
    }
};


// ========== 054 3668_restore_finishing_order ==========
// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> recoverOrder(std::vector<int>& order, std::vector<int>& friends) {
        int n = (int)order.size();
        std::vector<int> d(n + 1);
        for (int i = 0; i < n; i++) d[order[i]] = i;
        std::sort(friends.begin(), friends.end(), [&](int a, int b) {
            return d[a] < d[b];
        });
        return friends;
    }
};


// ========== 055 3669_balanced_k_factor_decomposition ==========
// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
    static constexpr int MX = 100001;
    static std::vector<std::vector<int>> g;
    static bool inited;
    int cur;
    std::vector<int> ans, path;

    static void ensureInit() {
        if (inited) return;
        g.assign(MX, {});
        for (int i = 1; i < MX; i++) {
            for (int j = i; j < MX; j += i) g[j].push_back(i);
        }
        inited = true;
    }

    void dfs(int i, int x, int mi, int mx) {
        if (i == 0) {
            int d = std::max(mx, x) - std::min(mi, x);
            if (d < cur) {
                cur = d;
                path[i] = x;
                ans = path;
            }
            return;
        }
        for (int y : g[x]) {
            path[i] = y;
            dfs(i - 1, x / y, std::min(mi, y), std::max(mx, y));
        }
    }

public:
    std::vector<int> minDifference(int n, int k) {
        ensureInit();
        cur = INT_MAX;
        ans.clear();
        path.assign(k, 0);
        dfs(k - 1, n, INT_MAX, 0);
        return ans;
    }
};

std::vector<std::vector<int>> Solution::g;
bool Solution::inited = false;


// ========== 056 3670_maximum_product_of_two_integers_with_no_common_bits ==========
// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxProduct(std::vector<int>& nums) {
        int maxV = 0;
        for (int v : nums) if (v > maxV) maxV = v;
        int bitsN = 0;
        for (int x = maxV; x > 0; x >>= 1) bitsN++;
        if (bitsN == 0) bitsN = 1;
        int size = 1 << bitsN;
        std::vector<int> best(size, 0);
        for (int v : nums) if (v > best[v]) best[v] = v;
        for (int mask = 0; mask < size; mask++) {
            for (int b = 0; b < bitsN; b++) {
                if (mask & (1 << b)) {
                    int sub = mask ^ (1 << b);
                    if (best[sub] > best[mask]) best[mask] = best[sub];
                }
            }
        }
        long long ans = 0;
        for (int v : nums) {
            int comp = (size - 1) ^ v;
            if (best[comp] > 0) {
                long long p = (long long)v * best[comp];
                if (p > ans) ans = p;
            }
        }
        return ans;
    }
};


// ========== 057 3671_sum_of_beautiful_subsequences ==========
// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

#include <algorithm>
#include <vector>

class Solution {
public:
    int totalBeauty(std::vector<int>& nums) {
        const int MOD = 1000000007;
        int mx = 0;
        for (int v : nums) if (v > mx) mx = v;
        std::vector<std::vector<int>> pos(mx + 1);
        for (int i = 0; i < (int)nums.size(); i++) pos[nums[i]].push_back(i);
        std::vector<int> cnt(mx + 1, 0);
        for (int g = 1; g <= mx; g++) {
            std::vector<int> seq;
            for (int m = g; m <= mx; m += g) {
                seq.insert(seq.end(), pos[m].begin(), pos[m].end());
            }
            if (seq.empty()) continue;
            std::sort(seq.begin(), seq.end());
            int ways = 1;
            for (size_t i = 0; i < seq.size(); i++) ways = (int)((ways * 2LL) % MOD);
            cnt[g] = (ways - 1 + MOD) % MOD;
        }
        int ans = 0;
        for (int g = mx; g >= 1; g--) {
            for (int m = 2 * g; m <= mx; m += g) {
                cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD;
            }
            ans = (int)((ans + 1LL * cnt[g] * g) % MOD);
        }
        return ans;
    }
};


// ========== 058 3672_sum_of_weighted_modes_in_subarrays ==========
// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    long long modeWeight(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> cnt;
        // pair: {freq, -val} so higher freq first, then smaller val
        using P = std::pair<int, int>;
        std::priority_queue<P> pq;

        for (int i = 0; i < k; i++) {
            int x = nums[i];
            cnt[x]++;
            pq.push({cnt[x], -x});
        }

        auto getMode = [&]() -> long long {
            while (true) {
                auto [freq, negVal] = pq.top();
                int val = -negVal;
                if (cnt[val] == freq) return 1LL * freq * val;
                pq.pop();
            }
        };

        long long ans = getMode();
        for (int i = k; i < (int)nums.size(); i++) {
            int x = nums[i], y = nums[i - k];
            cnt[x]++;
            cnt[y]--;
            pq.push({cnt[x], -x});
            pq.push({cnt[y], -y});
            ans += getMode();
        }
        return ans;
    }
};


// ========== 059 3674_minimum_operations_to_equalize_array ==========
// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        for (int x : nums) if (x != nums[0]) return 1;
        return 0;
    }
};


// ========== 060 3675_minimum_operations_to_transform_string ==========
// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

#include <algorithm>
#include <string>

class Solution {
public:
    int minOperations(std::string s) {
        int ans = 0;
        for (char c : s) {
            if (c != 'a') ans = std::max(ans, 26 - (c - 'a'));
        }
        return ans;
    }
};


// ========== 061 3676_count_bowl_subarrays ==========
// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

#include <vector>

class Solution {
public:
    long long bowlSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long ans = 0;
        std::vector<int> ngr(n, -1), ngl(n, -1), stack;
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty() && nums[stack.back()] < nums[i]) stack.pop_back();
            if (!stack.empty()) ngr[i] = stack.back();
            stack.push_back(i);
        }
        stack.clear();
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && nums[stack.back()] < nums[i]) stack.pop_back();
            if (!stack.empty()) ngl[i] = stack.back();
            stack.push_back(i);
        }
        for (int i = 0; i < n; i++) {
            if (ngr[i] != -1 && ngr[i] - i >= 2) ans++;
            if (ngl[i] != -1 && i - ngl[i] >= 2) ans++;
        }
        return ans;
    }
};


// ========== 062 3677_count_binary_palindromic_numbers ==========
// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

#include <algorithm>
#include <string>

class Solution {
public:
    int countBinaryPalindromes(long long n) {
        if (n == 0) return 1;
        int ans = 1;
        std::string s;
        {
            long long x = n;
            while (x > 0) {
                s.push_back(char('0' + (x & 1)));
                x >>= 1;
            }
            std::reverse(s.begin(), s.end());
        }
        int L = (int)s.size();
        for (int len_ = 1; len_ < L; len_++) {
            int half = (len_ + 1) / 2;
            ans += 1 << (half - 1);
        }
        int half = (L + 1) / 2;
        std::string prefix = s.substr(0, half);
        int start = 1 << (half - 1);
        long long prefVal = 0;
        for (char c : prefix) prefVal = (prefVal << 1) | (c - '0');
        ans += (int)prefVal - start;
        std::string pal = prefix;
        for (int i = half - 1 - (L % 2); i >= 0; i--) pal.push_back(prefix[i]);
        long long pval = 0;
        for (char c : pal) pval = (pval << 1) | (c - '0');
        if (pval <= n) ans++;
        return ans;
    }
};


// ========== 063 3678_smallest_absent_positive_greater_than_average ==========
// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int smallestAbsent(std::vector<int>& nums) {
        std::unordered_set<int> s;
        int sum = 0;
        for (int x : nums) {
            s.insert(x);
            sum += x;
        }
        int ans = std::max(1, sum / (int)nums.size() + 1);
        while (s.count(ans)) ans++;
        return ans;
    }
};


// ========== 064 3679_minimum_discards_to_balance_inventory ==========
// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minArrivalsToDiscard(std::vector<int>& arrivals, int w, int m) {
        std::unordered_map<int, int> cnt;
        int n = (int)arrivals.size();
        std::vector<int> marked(n, 0);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x = arrivals[i];
            if (i >= w) cnt[arrivals[i - w]] -= marked[i - w];
            if (cnt[x] >= m) ans++;
            else {
                marked[i] = 1;
                cnt[x]++;
            }
        }
        return ans;
    }
};


// ========== 065 3680_generate_schedule ==========
// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generateSchedule(int n) {
        if (n < 5) return {};
        std::vector<std::vector<int>> matches;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) matches.push_back({i, j});
            }
        }
        std::vector<bool> used(matches.size(), false);
        std::vector<std::vector<int>> sched;
        int last0 = -1, last1 = -1;
        std::function<bool()> dfs = [&]() -> bool {
            if ((int)sched.size() == (int)matches.size()) return true;
            for (int i = 0; i < (int)matches.size(); i++) {
                if (used[i]) continue;
                auto& m = matches[i];
                if (m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1) continue;
                used[i] = true;
                sched.push_back(m);
                int p0 = last0, p1 = last1;
                last0 = m[0]; last1 = m[1];
                if (dfs()) return true;
                last0 = p0; last1 = p1;
                sched.pop_back();
                used[i] = false;
            }
            return false;
        };
        if (dfs()) return sched;
        return {};
    }
};


// ========== 066 3681_maximum_xor_of_subsequences ==========
// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

#include <vector>

class Solution {
public:
    int maxXorSubsequences(std::vector<int>& nums) {
        std::vector<int> basis(32, 0);
        for (int x : nums) {
            int cur = x;
            for (int b = 31; b >= 0; b--) {
                if ((cur & (1 << b)) == 0) continue;
                if (basis[b] == 0) {
                    basis[b] = cur;
                    break;
                }
                cur ^= basis[b];
            }
        }
        int ans = 0;
        for (int b = 31; b >= 0; b--) {
            if ((ans ^ basis[b]) > ans) ans ^= basis[b];
        }
        return ans;
    }
};


// ========== 067 3682_minimum_index_sum_of_common_elements ==========
// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumSum(std::vector<int>& nums1, std::vector<int>& nums2) {
        const int inf = 1 << 30;
        std::unordered_map<int, int> d;
        for (int i = 0; i < (int)nums2.size(); i++) {
            if (!d.count(nums2[i])) d[nums2[i]] = i;
        }
        int ans = inf;
        for (int i = 0; i < (int)nums1.size(); i++) {
            auto it = d.find(nums1[i]);
            if (it != d.end()) ans = std::min(ans, i + it->second);
        }
        return ans == inf ? -1 : ans;
    }
};


// ========== 068 3683_earliest_time_to_finish_one_task ==========
// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

#include <algorithm>
#include <vector>

class Solution {
public:
    int earliestTime(std::vector<std::vector<int>>& tasks) {
        int ans = 200;
        for (auto& task : tasks) ans = std::min(ans, task[0] + task[1]);
        return ans;
    }
};


// ========== 069 3684_maximize_sum_of_at_most_k_distinct_elements ==========
// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> maxKDistinct(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::vector<int> ans;
        for (int i = n - 1; i >= 0; i--) {
            if (i + 1 < n && nums[i] == nums[i + 1]) continue;
            ans.push_back(nums[i]);
            if (--k == 0) break;
        }
        return ans;
    }
};


// ========== 070 3685_subsequence_sum_after_capping_elements ==========
// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<bool> subsequenceSumAfterCapping(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        std::vector<bool> ans(n), reach(k + 1, false);
        reach[0] = true;
        int idx = 0;
        for (int x = 1; x <= n; x++) {
            while (idx < n && sorted[idx] <= x) {
                int v = sorted[idx];
                for (int s = k; s >= v; s--) {
                    if (reach[s - v]) reach[s] = true;
                }
                idx++;
            }
            std::vector<bool> tmp = reach;
            int rem = n - idx;
            for (int s = 0; s <= k; s++) {
                if (!reach[s]) continue;
                for (int t = 1; t <= rem && s + t * x <= k; t++) tmp[s + t * x] = true;
            }
            ans[x - 1] = tmp[k];
        }
        return ans;
    }
};


// ========== 071 3686_number_of_stable_subsequences ==========
// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

#include <vector>

class Solution {
public:
    int countStableSubsequences(std::vector<int>& nums) {
        const int MOD = 1000000007;
        int a1 = 0, a2 = 0, b1 = 0, b2 = 0;
        for (int x : nums) {
            if (x % 2 == 1) {
                int na1 = (1 + b1 + b2) % MOD;
                int na2 = a1;
                a1 = (a1 + na1) % MOD;
                a2 = (a2 + na2) % MOD;
            } else {
                int nb1 = (1 + a1 + a2) % MOD;
                int nb2 = b1;
                b1 = (b1 + nb1) % MOD;
                b2 = (b2 + nb2) % MOD;
            }
        }
        return (((a1 + a2) % MOD + b1) % MOD + b2) % MOD;
    }
};


// ========== 072 3687_library_late_fee_calculator ==========
// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

#include <vector>

class Solution {
public:
    int lateFee(std::vector<int>& daysLate) {
        auto f = [](int x) {
            if (x == 1) return 1;
            if (x > 5) return 3 * x;
            return 2 * x;
        };
        int ans = 0;
        for (int x : daysLate) ans += f(x);
        return ans;
    }
};


// ========== 073 3688_bitwise_or_of_even_numbers_in_an_array ==========
// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

#include <vector>

class Solution {
public:
    int evenNumberBitwiseORs(std::vector<int>& nums) {
        int ans = 0;
        for (int x : nums) if (x % 2 == 0) ans |= x;
        return ans;
    }
};


// ========== 074 3689_maximum_total_subarray_value_i ==========
// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxTotalValue(std::vector<int>& nums, int k) {
        auto [mn, mx] = std::minmax_element(nums.begin(), nums.end());
        return 1LL * k * (*mx - *mn);
    }
};


// ========== 075 3690_split_and_merge_array_transformation ==========
// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

#include <array>
#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
    struct ArrHash {
        size_t operator()(const std::array<int, 6>& a) const {
            size_t h = 0;
            for (int x : a) h = h * 31 + (size_t)x;
            return h;
        }
    };

public:
    int minSplitMerge(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size();
        auto toArr = [&](const std::vector<int>& nums) {
            std::array<int, 6> t{};
            for (int i = 0; i < n; i++) t[i] = nums[i];
            return t;
        };
        auto start = toArr(nums1);
        auto target = toArr(nums2);
        std::unordered_set<std::array<int, 6>, ArrHash> vis{start};
        std::vector<std::array<int, 6>> q{start};
        for (int ans = 0;; ans++) {
            std::vector<std::array<int, 6>> nq;
            for (auto& cur : q) {
                if (cur == target) return ans;
                for (int l = 0; l < n; l++) {
                    for (int r = l; r < n; r++) {
                        std::vector<int> remain, sub;
                        for (int i = 0; i < l; i++) remain.push_back(cur[i]);
                        for (int i = r + 1; i < n; i++) remain.push_back(cur[i]);
                        for (int i = l; i <= r; i++) sub.push_back(cur[i]);
                        for (int pos = 0; pos <= (int)remain.size(); pos++) {
                            std::vector<int> nxtSlice;
                            nxtSlice.insert(nxtSlice.end(), remain.begin(), remain.begin() + pos);
                            nxtSlice.insert(nxtSlice.end(), sub.begin(), sub.end());
                            nxtSlice.insert(nxtSlice.end(), remain.begin() + pos, remain.end());
                            auto nxt = toArr(nxtSlice);
                            if (!vis.count(nxt)) {
                                vis.insert(nxt);
                                nq.push_back(nxt);
                            }
                        }
                    }
                }
            }
            q = std::move(nq);
        }
    }
};


// ========== 076 3691_maximum_total_subarray_value_ii ==========
// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
    struct SparseTableRMQ {
        int n, maxLog;
        std::vector<std::vector<int>> fMax, fMin;
        std::vector<int> lg;

        explicit SparseTableRMQ(const std::vector<int>& data) {
            n = (int)data.size();
            maxLog = 0;
            while ((1 << maxLog) <= n) maxLog++;
            maxLog++;
            fMax.assign(n, std::vector<int>(maxLog));
            fMin.assign(n, std::vector<int>(maxLog));
            lg.assign(n + 1, 0);
            for (int i = 2; i <= n; i++) lg[i] = lg[i >> 1] + 1;
            for (int i = 0; i < n; i++) {
                fMax[i][0] = data[i];
                fMin[i][0] = data[i];
            }
            for (int j = 1; j < maxLog; j++) {
                for (int i = 0; i <= n - (1 << j); i++) {
                    fMax[i][j] = std::max(fMax[i][j - 1], fMax[i + (1 << (j - 1))][j - 1]);
                    fMin[i][j] = std::min(fMin[i][j - 1], fMin[i + (1 << (j - 1))][j - 1]);
                }
            }
        }

        int queryMax(int l, int r) {
            int k = lg[r - l + 1];
            return std::max(fMax[l][k], fMax[r - (1 << k) + 1][k]);
        }

        int queryMin(int l, int r) {
            int k = lg[r - l + 1];
            return std::min(fMin[l][k], fMin[r - (1 << k) + 1][k]);
        }
    };

public:
    long long maxTotalValue(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        SparseTableRMQ st(nums);
        using Item = std::tuple<long long, int, int>;
        std::priority_queue<Item> pq;
        for (int l = 0; l < n; l++) {
            long long val = (long long)st.queryMax(l, n - 1) - st.queryMin(l, n - 1);
            pq.emplace(val, l, n - 1);
        }
        long long ans = 0;
        for (int i = 0; i < k; i++) {
            auto [val, l, r] = pq.top();
            pq.pop();
            ans += val;
            if (r > l) {
                long long nextVal = (long long)st.queryMax(l, r - 1) - st.queryMin(l, r - 1);
                pq.emplace(nextVal, l, r - 1);
            }
        }
        return ans;
    }
};


// ========== 077 3692_majority_frequency_characters ==========
// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::string majorityFrequencyGroup(std::string s) {
        std::vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        std::unordered_map<int, std::string> f;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] > 0) f[cnt[i]].push_back(char('a' + i));
        }
        int mx = 0, mv = 0;
        std::string ans;
        for (auto& [v, cs] : f) {
            if ((int)cs.size() > mx || ((int)cs.size() == mx && v > mv)) {
                mx = (int)cs.size();
                mv = v;
                ans = cs;
            }
        }
        return ans;
    }
};


// ========== 078 3693_climbing_stairs_ii ==========
// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int climbStairs(int n, std::vector<int>& costs) {
        const int inf = (int)1e9;
        std::vector<int> f(n + 1, inf);
        f[0] = 0;
        for (int i = 1; i <= n; i++) {
            int x = costs[i - 1];
            for (int j = std::max(0, i - 3); j < i; j++) {
                f[i] = std::min(f[i], f[j] + x + (i - j) * (i - j));
            }
        }
        return f[n];
    }
};


// ========== 079 3694_distinct_points_reachable_after_substring_removal ==========
// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int distinctPoints(std::string s, int k) {
        int n = (int)s.size();
        std::vector<int> f(n + 1), g(n + 1);
        int x = 0, y = 0;
        for (int i = 1; i <= n; i++) {
            char c = s[i - 1];
            if (c == 'U') y++;
            else if (c == 'D') y--;
            else if (c == 'L') x--;
            else x++;
            f[i] = x;
            g[i] = y;
        }
        std::unordered_set<long long> st;
        for (int i = k; i <= n; i++) {
            int a = f[n] - (f[i] - f[i - k]);
            int b = g[n] - (g[i] - g[i - k]);
            long long key = (long long)a * n + b;
            st.insert(key);
        }
        return (int)st.size();
    }
};


// ========== 080 3695_maximize_alternating_sum_using_swaps ==========
// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

#include <algorithm>
#include <functional>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maxAlternatingSum(std::vector<int>& nums, std::vector<std::vector<int>>& swaps) {
        int n = (int)nums.size();
        std::vector<int> parent(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        std::function<int(int)> find = [&](int x) -> int {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        for (auto& s : swaps) {
            int a = find(s[0]), b = find(s[1]);
            if (a != b) parent[a] = b;
        }
        std::unordered_map<int, std::vector<int>> compVals, compIdx;
        for (int i = 0; i < n; i++) {
            int r = find(i);
            compVals[r].push_back(nums[i]);
            compIdx[r].push_back(i);
        }
        std::vector<int> arr(n);
        for (auto& [r, vals] : compVals) {
            auto& idxs = compIdx[r];
            std::sort(vals.begin(), vals.end(), std::greater<int>());
            std::vector<int> even, odd;
            for (int i : idxs) {
                if (i % 2 == 0) even.push_back(i);
                else odd.push_back(i);
            }
            std::sort(even.begin(), even.end());
            std::sort(odd.begin(), odd.end());
            int ei = 0;
            for (int v : vals) {
                if (ei < (int)even.size()) {
                    arr[even[ei]] = v;
                    ei++;
                } else {
                    arr[odd[ei - (int)even.size()]] = v;
                    ei++;
                }
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) ans += arr[i];
            else ans -= arr[i];
        }
        return ans;
    }
};


// ========== 081 3696_maximum_distance_between_unequal_words_in_array_i ==========
// LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int maxDistance(std::vector<std::string>& words) {
        int n = (int)words.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            if (words[i] != words[0]) ans = std::max(ans, i + 1);
            if (words[i] != words[n - 1]) ans = std::max(ans, n - i);
        }
        return ans;
    }
};


// ========== 082 3697_compute_decimal_representation ==========
// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> decimalRepresentation(int n) {
        std::vector<int> ans;
        int p = 1;
        while (n > 0) {
            int v = n % 10;
            n /= 10;
            if (v != 0) ans.push_back(p * v);
            p *= 10;
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};


// ========== 083 3698_split_array_with_minimum_difference ==========
// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

#include <algorithm>
#include <climits>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long splitArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<long long> s(n);
        std::vector<bool> f(n, true), g(n, true);
        s[0] = nums[0];
        for (int i = 1; i < n; i++) {
            s[i] = s[i - 1] + nums[i];
            f[i] = f[i - 1];
            if (nums[i] <= nums[i - 1]) f[i] = false;
        }
        for (int i = n - 2; i >= 0; i--) {
            g[i] = g[i + 1];
            if (nums[i] <= nums[i + 1]) g[i] = false;
        }
        const long long inf = LLONG_MAX / 4;
        long long ans = inf;
        for (int i = 0; i < n - 1; i++) {
            if (f[i] && g[i + 1]) {
                long long s1 = s[i], s2 = s[n - 1] - s[i];
                ans = std::min(ans, std::llabs(s1 - s2));
            }
        }
        return ans < inf ? ans : -1;
    }
};


// ========== 084 3699_number_of_zigzag_arrays_i ==========
// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

#include <vector>

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const int MOD = 1000000007;
        int m = r - l + 1;
        if (n == 1) return m % MOD;
        std::vector<int> up(m, 1), down(m, 1);
        for (int len_ = 2; len_ <= n; len_++) {
            std::vector<int> prefDown(m + 1, 0);
            for (int j = 0; j < m; j++) prefDown[j + 1] = (prefDown[j] + down[j]) % MOD;
            std::vector<int> nup(m);
            for (int j = 0; j < m; j++) nup[j] = prefDown[j];
            std::vector<int> sufUp(m + 1, 0);
            for (int j = m - 1; j >= 0; j--) sufUp[j] = (sufUp[j + 1] + up[j]) % MOD;
            std::vector<int> ndown(m);
            for (int j = 0; j < m; j++) ndown[j] = sufUp[j + 1];
            up.swap(nup);
            down.swap(ndown);
        }
        int ans = 0;
        for (int j = 0; j < m; j++) {
            ans = (ans + up[j]) % MOD;
            ans = (ans + down[j]) % MOD;
        }
        return ans;
    }
};


// ========== 085 3700_number_of_zigzag_arrays_ii ==========
// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

#include <vector>

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const int MOD = 1000000007;
        int m = r - l + 1;
        if (n == 1) return m % MOD;
        std::vector<int> up(m, 1), down(m, 1);
        for (int length = 2; length <= n; length++) {
            std::vector<int> pref(m + 1, 0);
            for (int j = 0; j < m; j++) pref[j + 1] = (pref[j] + down[j]) % MOD;
            std::vector<int> nup(m);
            for (int j = 0; j < m; j++) nup[j] = pref[j];
            std::vector<int> suf(m + 1, 0);
            for (int j = m - 1; j >= 0; j--) suf[j] = (suf[j + 1] + up[j]) % MOD;
            std::vector<int> ndown(m);
            for (int j = 0; j < m; j++) ndown[j] = suf[j + 1];
            up.swap(nup);
            down.swap(ndown);
        }
        int ans = 0;
        for (int j = 0; j < m; j++) {
            ans = (ans + up[j]) % MOD;
            ans = (ans + down[j]) % MOD;
        }
        return ans;
    }
};


// ========== 086 3701_compute_alternating_sum ==========
// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

#include <vector>

class Solution {
public:
    int alternatingSum(std::vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i % 2 == 0) ans += nums[i];
            else ans -= nums[i];
        }
        return ans;
    }
};


// ========== 087 3702_longest_subsequence_with_non_zero_bitwise_xor ==========
// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

#include <vector>

class Solution {
public:
    int longestSubsequence(std::vector<int>& nums) {
        int xorv = 0, cnt0 = 0;
        for (int x : nums) {
            xorv ^= x;
            if (x == 0) cnt0++;
        }
        int n = (int)nums.size();
        if (xorv != 0) return n;
        if (cnt0 == n) return 0;
        return n - 1;
    }
};


// ========== 088 3703_remove_k_balanced_substrings ==========
// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::string removeSubstring(std::string s, int k) {
        std::vector<std::pair<char, int>> stk;
        for (char c : s) {
            if (!stk.empty() && stk.back().first == c) stk.back().second++;
            else stk.push_back({c, 1});
            if (c == ')' && stk.size() > 1) {
                auto& top = stk.back();
                auto& prev = stk[stk.size() - 2];
                if (top.second == k && prev.second >= k) {
                    stk.pop_back();
                    prev.second -= k;
                    if (prev.second == 0) stk.pop_back();
                }
            }
        }
        std::string res;
        for (auto& [ch, count] : stk) {
            res.append(count, ch);
        }
        return res;
    }
};


// ========== 089 3704_count_no_zero_pairs_that_sum_to_n ==========
// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

#include <string>
#include <vector>

class Solution {
public:
    long long countNoZeroPairs(long long n) {
        std::string s = std::to_string(n);
        int m = (int)s.size();
        std::vector<int> digits(m + 1, 0);
        for (int i = 0; i < m; i++) digits[i] = s[m - 1 - i] - '0';

        long long dp[2][2][2] = {};
        dp[0][1][1] = 1;

        for (int pos = 0; pos < m + 1; pos++) {
            long long ndp[2][2][2] = {};
            int target = digits[pos];
            for (int carry = 0; carry <= 1; carry++) {
                for (int aliveA = 0; aliveA <= 1; aliveA++) {
                    for (int aliveB = 0; aliveB <= 1; aliveB++) {
                        long long ways = dp[carry][aliveA][aliveB];
                        if (ways == 0) continue;
                        int A[10][2], aLen = 0;
                        if (aliveA == 1) {
                            for (int d = 1; d <= 9; d++) {
                                A[aLen][0] = d; A[aLen][1] = 1; aLen++;
                            }
                            if (pos > 0) { A[aLen][0] = 0; A[aLen][1] = 0; aLen++; }
                        } else {
                            A[0][0] = 0; A[0][1] = 0; aLen = 1;
                        }
                        int B[10][2], bLen = 0;
                        if (aliveB == 1) {
                            for (int d = 1; d <= 9; d++) {
                                B[bLen][0] = d; B[bLen][1] = 1; bLen++;
                            }
                            if (pos > 0) { B[bLen][0] = 0; B[bLen][1] = 0; bLen++; }
                        } else {
                            B[0][0] = 0; B[0][1] = 0; bLen = 1;
                        }
                        for (int ai = 0; ai < aLen; ai++) {
                            int da = A[ai][0], na = A[ai][1];
                            for (int bi = 0; bi < bLen; bi++) {
                                int db = B[bi][0], nb = B[bi][1];
                                int sum = da + db + carry;
                                if (sum % 10 != target) continue;
                                int ncarry = sum / 10;
                                ndp[ncarry][na][nb] += ways;
                            }
                        }
                    }
                }
            }
            for (int c = 0; c < 2; c++)
                for (int a = 0; a < 2; a++)
                    for (int b = 0; b < 2; b++)
                        dp[c][a][b] = ndp[c][a][b];
        }
        return dp[0][0][0];
    }
};


// ========== 090 3706_maximum_distance_between_unequal_words_in_array_ii ==========
// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int maxDistance(std::vector<std::string>& words) {
        int n = (int)words.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            if (words[i] != words[0]) ans = std::max(ans, i + 1);
            if (words[i] != words[n - 1]) ans = std::max(ans, n - i);
        }
        return ans;
    }
};


// ========== 091 3707_equal_score_substrings ==========
// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

#include <string>

class Solution {
public:
    bool scoreBalance(std::string s) {
        int l = 0, r = 0;
        for (char c : s) r += (c - 'a') + 1;
        for (int i = 0; i + 1 < (int)s.size(); i++) {
            int x = (s[i] - 'a') + 1;
            l += x;
            r -= x;
            if (l == r) return true;
        }
        return false;
    }
};


// ========== 092 3708_longest_fibonacci_subarray ==========
// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        int f = 2, ans = f;
        for (int i = 2; i < (int)nums.size(); i++) {
            if (nums[i] == nums[i - 1] + nums[i - 2]) {
                f++;
                ans = std::max(ans, f);
            } else f = 2;
        }
        return ans;
    }
};


// ========== 093 3709_design_exam_scores_tracker ==========
// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

#include <algorithm>
#include <vector>

class ExamTracker {
    std::vector<int> times;
    std::vector<long long> pre;
public:
    ExamTracker() : times{0}, pre{0} {}

    void record(int time, int score) {
        times.push_back(time);
        pre.push_back(pre.back() + score);
    }

    long long totalScore(int startTime, int endTime) {
        int l = (int)(std::lower_bound(times.begin(), times.end(), startTime) - times.begin()) - 1;
        int r = (int)(std::lower_bound(times.begin(), times.end(), endTime + 1) - times.begin()) - 1;
        return pre[r] - pre[l];
    }
};


// ========== 094 3710_maximum_partition_factor ==========
// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

#include <cstdlib>
#include <queue>
#include <vector>

class Solution {
public:
    int maxPartitionFactor(std::vector<std::vector<int>>& points) {
        int n = (int)points.size();
        if (n == 2) return 0;
        auto dist = [&](int i, int j) {
            return std::abs(points[i][0] - points[j][0]) + std::abs(points[i][1] - points[j][1]);
        };
        auto ok = [&](int d) {
            std::vector<std::vector<int>> g(n);
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (dist(i, j) < d) {
                        g[i].push_back(j);
                        g[j].push_back(i);
                    }
                }
            }
            std::vector<int> color(n, -1);
            for (int i = 0; i < n; i++) {
                if (color[i] != -1) continue;
                std::queue<int> q;
                q.push(i);
                color[i] = 0;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    for (int v : g[u]) {
                        if (color[v] == -1) {
                            color[v] = color[u] ^ 1;
                            q.push(v);
                        } else if (color[v] == color[u]) return false;
                    }
                }
            }
            return true;
        };
        int lo = 0, hi = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                hi = std::max(hi, dist(i, j));
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};


// ========== 095 3711_maximum_transactions_without_negative_balance ==========
// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

#include <set>
#include <vector>

class Solution {
public:
    int maxTransactions(std::vector<int>& transactions) {
        std::multiset<int> tm;
        int ans = (int)transactions.size();
        long long s = 0;
        for (int x : transactions) {
            s += x;
            tm.insert(x);
            while (s < 0) {
                int y = *tm.begin();
                s -= y;
                ans--;
                tm.erase(tm.begin());
            }
        }
        return ans;
    }
};


// ========== 096 3712_sum_of_elements_with_frequency_divisible_by_k ==========
// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int sumDivisibleByK(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        int ans = 0;
        for (auto& [x, v] : cnt) {
            if (v % k == 0) ans += x * v;
        }
        return ans;
    }
};


// ========== 097 3713_longest_balanced_substring_i ==========
// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

#include <algorithm>
#include <string>

class Solution {
public:
    int longestBalanced(std::string s) {
        int n = (int)s.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            int cnt[26] = {};
            int mx = 0, v = 0;
            for (int j = i; j < n; j++) {
                int c = s[j] - 'a';
                cnt[c]++;
                if (cnt[c] == 1) v++;
                mx = std::max(mx, cnt[c]);
                if (mx * v == j - i + 1) ans = std::max(ans, j - i + 1);
            }
        }
        return ans;
    }
};


// ========== 098 3714_longest_balanced_substring_ii ==========
// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <utility>

class Solution {
    int calc1(const std::string& s) {
        int res = 0, n = (int)s.size(), i = 0;
        while (i < n) {
            int j = i + 1;
            while (j < n && s[j] == s[i]) j++;
            res = std::max(res, j - i);
            i = j;
        }
        return res;
    }

    int calc2(const std::string& s, char a, char b) {
        int res = 0, n = (int)s.size(), i = 0;
        while (i < n) {
            while (i < n && s[i] != a && s[i] != b) i++;
            std::unordered_map<int, int> pos{{0, i - 1}};
            int d = 0;
            while (i < n && (s[i] == a || s[i] == b)) {
                if (s[i] == a) d++;
                else d--;
                auto it = pos.find(d);
                if (it != pos.end()) res = std::max(res, i - it->second);
                else pos[d] = i;
                i++;
            }
        }
        return res;
    }

    int calc3(const std::string& s) {
        struct KeyHash {
            size_t operator()(const std::pair<int, int>& p) const {
                return (size_t)p.first * 1000003u + (size_t)p.second;
            }
        };
        std::unordered_map<std::pair<int, int>, int, KeyHash> pos;
        pos[{0, 0}] = -1;
        int cnt[3] = {}, res = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            cnt[s[i] - 'a']++;
            int x = cnt[0] - cnt[1], y = cnt[1] - cnt[2];
            auto k = std::make_pair(x, y);
            auto it = pos.find(k);
            if (it != pos.end()) res = std::max(res, i - it->second);
            else pos[k] = i;
        }
        return res;
    }

public:
    int longestBalanced(std::string s) {
        int x = calc1(s);
        int y = std::max({calc2(s, 'a', 'b'), calc2(s, 'b', 'c'), calc2(s, 'a', 'c')});
        int z = calc3(s);
        return std::max({x, y, z});
    }
};


// ========== 099 3715_sum_of_perfect_square_ancestors ==========
// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

#include <functional>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long sumOfAncestors(int n, std::vector<std::vector<int>>& edges, std::vector<int>& nums) {
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        auto kernel = [](int x) {
            int res = 1;
            for (int p = 2; p * p <= x; p++) {
                int cnt = 0;
                while (x % p == 0) { x /= p; cnt++; }
                if (cnt % 2 == 1) res *= p;
            }
            if (x > 1) res *= x;
            return res;
        };
        std::vector<int> ks(n);
        for (int i = 0; i < n; i++) ks[i] = kernel(nums[i]);
        std::unordered_map<int, int> freq;
        long long ans = 0;
        std::function<void(int, int)> dfs = [&](int u, int p) {
            ans += freq[ks[u]];
            freq[ks[u]]++;
            for (int v : graph[u]) if (v != p) dfs(v, u);
            freq[ks[u]]--;
        };
        dfs(0, -1);
        return ans;
    }
};
