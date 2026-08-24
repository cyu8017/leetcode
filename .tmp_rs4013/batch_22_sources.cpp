

================================================================================
// FILE: 3921_score_validator (1059 bytes)
================================================================================
// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> scoreValidator(std::vector<std::string>& events) {
        int score = 0, counter = 0;
        for (auto& event : events) {
            bool isNum = !event.empty();
            int num = 0;
            int start = 0;
            if (isNum && event[0] == '-') start = 1;
            for (int i = start; i < (int)event.size(); i++) {
                if (event[i] < '0' || event[i] > '9') {
                    isNum = false;
                    break;
                }
                num = num * 10 + (event[i] - '0');
            }
            if (isNum && !(start == 1 && event.size() == 1)) {
                if (start == 1) num = -num;
                score += num;
            } else if (event == "W") {
                counter++;
                if (counter == 10) break;
            } else {
                score++;
            }
        }
        return {score, counter};
    }
};


================================================================================
// FILE: 3922_minimum_flips_to_make_binary_string_coherent (797 bytes)
================================================================================
// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

#include <algorithm>
#include <string>

class Solution {
public:
    int minFlips(std::string s) {
        int ones = 0;
        for (char c : s) if (c == '1') ones++;
        int answer = ones;
        if (ones > 0) answer = ones - 1;
        int zeros = (int)s.size() - ones;
        answer = std::min(answer, zeros);
        if ((int)s.size() >= 2) {
            int cost = 0;
            for (int i = 0; i < (int)s.size(); i++) {
                char want = (i == 0 || i == (int)s.size() - 1) ? '1' : '0';
                if (s[i] != want) cost++;
            }
            answer = std::min(answer, cost);
        }
        return answer;
    }
};


================================================================================
// FILE: 3923_minimum_generations_to_target_point (1597 bytes)
================================================================================
// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

#include <array>
#include <map>
#include <vector>

class Solution {
public:
    int minGenerations(std::vector<std::vector<int>>& points, std::vector<int>& target) {
        using Point = std::array<int, 3>;
        Point targetPoint = {target[0], target[1], target[2]};
        std::map<Point, int> generation;
        std::vector<Point> all;
        for (auto& values : points) {
            Point p = {values[0], values[1], values[2]};
            generation[p] = 0;
            all.push_back(p);
        }
        if (generation.count(targetPoint)) return generation[targetPoint];
        for (int current = 1;; current++) {
            int limit = (int)all.size();
            std::vector<Point> added;
            for (int i = 0; i < limit; i++) {
                for (int j = i + 1; j < limit; j++) {
                    if (all[i] == all[j]) continue;
                    Point p = {
                        (all[i][0] + all[j][0]) / 2,
                        (all[i][1] + all[j][1]) / 2,
                        (all[i][2] + all[j][2]) / 2
                    };
                    if (!generation.count(p)) {
                        generation[p] = current;
                        added.push_back(p);
                    }
                }
            }
            if (generation.count(targetPoint)) return generation[targetPoint];
            if (added.empty()) return -1;
            all.insert(all.end(), added.begin(), added.end());
        }
    }
};


================================================================================
// FILE: 3924_minimum_threshold_path_with_limited_heavy_edges (1629 bytes)
================================================================================
// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

#include <algorithm>
#include <deque>
#include <vector>

class Solution {
public:
    int minThreshold(int n, std::vector<std::vector<int>>& edges, int source, int target, int k) {
        if (source == target) return 0;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        int maxWeight = 0;
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
            maxWeight = std::max(maxWeight, e[2]);
        }
        auto can = [&](int threshold) {
            const int inf = 1000000000;
            std::vector<int> dist(n, inf);
            dist[source] = 0;
            std::deque<int> dq;
            dq.push_back(source);
            while (!dq.empty()) {
                int u = dq.front();
                dq.pop_front();
                for (auto& [to, weight] : g[u]) {
                    int cost = weight > threshold ? 1 : 0;
                    if (dist[u] + cost >= dist[to] || dist[u] + cost > k) continue;
                    dist[to] = dist[u] + cost;
                    if (cost == 0) dq.push_front(to);
                    else dq.push_back(to);
                }
            }
            return dist[target] <= k;
        };
        if (!can(maxWeight)) return -1;
        int lo = 0, hi = maxWeight;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};


================================================================================
// FILE: 3925_concatenate_array_with_reverse (445 bytes)
================================================================================
// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

#include <vector>

class Solution {
public:
    std::vector<int> concatWithReverse(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(2 * n);
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[n - i - 1];
        }
        return ans;
    }
};


================================================================================
// FILE: 3926_count_valid_word_occurrences (999 bytes)
================================================================================
// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> countWordOccurrences(std::vector<std::string>& chunks, std::vector<std::string>& queries) {
        std::string s;
        for (auto& c : chunks) s += c;
        int n = (int)s.size();
        std::unordered_map<std::string, int> cnt;
        int i = 0;
        while (i < n) {
            if (s[i] == ' ' || s[i] == '-') {
                i++;
                continue;
            }
            int j = i;
            while (j < n && s[j] != ' ' && (s[j] != '-' || (j + 1 < n && s[j + 1] != ' ' && s[j + 1] != '-'))) {
                j++;
            }
            cnt[s.substr(i, j - i)]++;
            i = j;
        }
        std::vector<int> ans(queries.size());
        for (int k = 0; k < (int)queries.size(); k++) ans[k] = cnt[queries[k]];
        return ans;
    }
};


================================================================================
// FILE: 3927_minimize_array_sum_using_divisible_replacements (896 bytes)
================================================================================
// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

#include <vector>

class Solution {
public:
    long long minArraySum(std::vector<int>& nums) {
        int maximum = 0;
        std::vector<bool> present(100001, false);
        for (int value : nums) {
            present[value] = true;
            if (value > maximum) maximum = value;
        }
        std::vector<int> best(maximum + 1, 0);
        for (int divisor = 1; divisor <= maximum; divisor++) {
            if (!present[divisor]) continue;
            for (int multiple = divisor; multiple <= maximum; multiple += divisor) {
                if (best[multiple] == 0) best[multiple] = divisor;
            }
        }
        long long answer = 0;
        for (int value : nums) answer += best[value];
        return answer;
    }
};


================================================================================
// FILE: 3928_minimum_cost_to_buy_apples_ii (2075 bytes)
================================================================================
// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

#include <queue>
#include <utility>
#include <vector>

class Solution {
    struct Edge {
        int to, empty, full;
    };

public:
    std::vector<long long> minCostToBuyApples(int n, std::vector<int>& prices, std::vector<std::vector<int>>& roads) {
        std::vector<std::vector<Edge>> g(n);
        for (auto& road : roads) {
            Edge e{road[1], road[2], road[2] * road[3]};
            g[road[0]].push_back(e);
            e.to = road[0];
            g[road[1]].push_back(e);
        }
        const long long inf = 1LL << 62;
        auto dijkstra = [&](int source, bool carrying) {
            std::vector<long long> dist(n, inf);
            dist[source] = 0;
            using P = std::pair<long long, int>;
            std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
            pq.push({0, source});
            while (!pq.empty()) {
                auto [d, node] = pq.top();
                pq.pop();
                if (d != dist[node]) continue;
                for (auto& e : g[node]) {
                    int weight = carrying ? e.full : e.empty;
                    long long next = d + weight;
                    if (next < dist[e.to]) {
                        dist[e.to] = next;
                        pq.push({next, e.to});
                    }
                }
            }
            return dist;
        };
        std::vector<long long> answer(n);
        for (int source = 0; source < n; source++) {
            auto emptyDist = dijkstra(source, false);
            auto fullDist = dijkstra(source, true);
            long long best = prices[source];
            for (int shop = 0; shop < n; shop++) {
                if (emptyDist[shop] == inf || fullDist[shop] == inf) continue;
                long long total = emptyDist[shop] + fullDist[shop] + prices[shop];
                if (total < best) best = total;
            }
            answer[source] = best;
        }
        return answer;
    }
};


================================================================================
// FILE: 3929_minimum_partition_score_ii (3426 bytes)
================================================================================
// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

#include <vector>

class Solution {
    struct Line {
        long long slope = 0, intercept = 0;
        int count = 0;
        bool valid = false;
    };
    struct State {
        long long value = 0;
        int count = 0;
        bool valid = false;
    };

    static State better(State a, State b) {
        if (!a.valid) return b;
        if (!b.valid) return a;
        if (a.value != b.value) return a.value < b.value ? a : b;
        return a.count >= b.count ? a : b;
    }

    static State evaluate(const Line& line, long long x) {
        if (!line.valid) return {};
        return {line.slope * x + line.intercept, line.count, true};
    }

public:
    long long minPartitionScore(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        auto run = [&](long long penalty) -> State {
            std::vector<Line> tree(4 * (n + 1));
            auto insert = [&](auto&& self, int node, int left, int right, Line line) -> void {
                if (!tree[node].valid) {
                    tree[node] = line;
                    return;
                }
                int mid = (left + right) / 2;
                long long xLeft = prefix[left], xMid = prefix[mid];
                State leftBetter = better(evaluate(line, xLeft), evaluate(tree[node], xLeft));
                State midBetter = better(evaluate(line, xMid), evaluate(tree[node], xMid));
                bool lineWinsLeft = leftBetter.value == evaluate(line, xLeft).value && leftBetter.count == line.count;
                bool lineWinsMid = midBetter.value == evaluate(line, xMid).value && midBetter.count == line.count;
                if (lineWinsMid) std::swap(tree[node], line);
                if (left == right) return;
                if (lineWinsLeft != lineWinsMid) self(self, node * 2, left, mid, line);
                else self(self, node * 2 + 1, mid + 1, right, line);
            };
            auto query = [&](auto&& self, int node, int left, int right, int index) -> State {
                State result = evaluate(tree[node], prefix[index]);
                if (left == right) return result;
                int mid = (left + right) / 2;
                if (index <= mid) return better(result, self(self, node * 2, left, mid, index));
                return better(result, self(self, node * 2 + 1, mid + 1, right, index));
            };
            insert(insert, 1, 0, n, Line{0, 0, 0, true});
            State current;
            for (int i = 1; i <= n; i++) {
                State best = query(query, 1, 0, n, i);
                long long x = prefix[i];
                current = State{best.value + x * x + x + penalty, best.count + 1, true};
                insert(insert, 1, 0, n, Line{-2 * x, current.value + x * x - x, current.count, true});
            }
            return current;
        };

        long long bound = prefix[n] * prefix[n] + prefix[n] + 1;
        long long low = 0, high = bound;
        while (low < high) {
            long long mid = low + (high - low + 1) / 2;
            if (run(mid).count >= k) low = mid;
            else high = mid - 1;
        }
        State state = run(low);
        return (state.value - low * k) / 2;
    }
};


================================================================================
// FILE: 3930_power_update_after_k_th_largest_insertion_ii (1997 bytes)
================================================================================
// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> powerUpdate(std::vector<int>& nums, int p, std::vector<std::vector<int>>& queries) {
        const long long mod = 1000000007;
        std::vector<int> vals = nums;
        for (auto& q : queries) vals.push_back(q[0]);
        std::sort(vals.begin(), vals.end());
        vals.erase(std::unique(vals.begin(), vals.end()), vals.end());
        std::vector<int> bit(vals.size() + 1, 0);
        auto add = [&](int i) {
            for (; i < (int)bit.size(); i += i & -i) bit[i]++;
        };
        auto kth = [&](int rank) {
            int idx = 0;
            int step = 1;
            while ((step << 1) < (int)bit.size()) step <<= 1;
            for (; step > 0; step >>= 1) {
                int next = idx + step;
                if (next < (int)bit.size() && bit[next] < rank) {
                    idx = next;
                    rank -= bit[next];
                }
            }
            return vals[idx];
        };
        for (int x : nums) {
            add((int)(std::lower_bound(vals.begin(), vals.end(), x) - vals.begin()) + 1);
        }
        auto powm = [&](long long a, long long e) {
            long long res = 1;
            while (e > 0) {
                if (e & 1) res = res * a % mod;
                a = a * a % mod;
                e >>= 1;
            }
            return res;
        };
        std::vector<int> ans(queries.size());
        int size = (int)nums.size();
        long long cur = p;
        for (int i = 0; i < (int)queries.size(); i++) {
            add((int)(std::lower_bound(vals.begin(), vals.end(), queries[i][0]) - vals.begin()) + 1);
            size++;
            int x = kth(size - queries[i][1] + 1);
            cur = powm(cur, x);
            ans[i] = (int)cur;
        }
        return ans;
    }
};


================================================================================
// FILE: 3931_check_adjacent_digit_differences (392 bytes)
================================================================================
// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/

#include <cmath>
#include <string>

class Solution {
public:
    bool isAdjacentDiffAtMostTwo(std::string s) {
        for (int i = 1; i < (int)s.size(); i++) {
            if (std::abs((int)s[i - 1] - (int)s[i]) > 2) return false;
        }
        return true;
    }
};


================================================================================
// FILE: 3932_count_k_th_roots_in_a_range (707 bytes)
================================================================================
// LeetCode 3932 - Count K Th Roots In A Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/

class Solution {
public:
    int countKthRoots(int l, int r, int k) {
        if (k == 1) return r - l + 1;
        int ans = 0;
        for (long long x = 0;; x++) {
            long long y = 1;
            bool tooBig = false;
            for (int i = 0; i < k; i++) {
                if (x != 0 && y > (long long)r / x) {
                    tooBig = true;
                    break;
                }
                y *= x;
                if (y > r) break;
            }
            if (tooBig || y > r) break;
            if (l <= y && y <= r) ans++;
        }
        return ans;
    }
};


================================================================================
// FILE: 3933_largest_local_values_in_a_matrix_ii (1964 bytes)
================================================================================
// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countLocalMaximums(std::vector<std::vector<int>>& matrix) {
        int rows = (int)matrix.size(), cols = (int)matrix[0].size();
        std::vector<std::vector<std::pair<int, int>>> positions(201);
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                int value = matrix[row][col];
                if (value > 0) positions[value].push_back({row, col});
            }
        }
        int answer = 0;
        for (int value = 1; value <= 200; value++) {
            if (positions[value].empty()) continue;
            std::vector<std::vector<int>> prefix(rows + 1, std::vector<int>(cols + 1, 0));
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    int add = matrix[row][col] > value ? 1 : 0;
                    prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add;
                }
            }
            for (auto& [row, col] : positions[value]) {
                int top = std::max(0, row - value), bottom = std::min(rows - 1, row + value);
                int left = std::max(0, col - value), right = std::min(cols - 1, col + value);
                int greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left];
                for (int dr : {-value, value}) {
                    for (int dc : {-value, value}) {
                        int rr = row + dr, cc = col + dc;
                        if (rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value) greater--;
                    }
                }
                if (greater == 0) answer++;
            }
        }
        return answer;
    }
};


================================================================================
// FILE: 3934_smallest_unique_subarray (2086 bytes)
================================================================================
// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int smallestUniqueSubarray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> sa(n), rank = nums;
        for (int i = 0; i < n; i++) sa[i] = i;
        for (int width = 1; width < n; width <<= 1) {
            std::sort(sa.begin(), sa.end(), [&](int a, int b) {
                if (rank[a] != rank[b]) return rank[a] < rank[b];
                int ra = a + width < n ? rank[a + width] : -1;
                int rb = b + width < n ? rank[b + width] : -1;
                return ra < rb;
            });
            std::vector<int> next(n, 0);
            for (int i = 1; i < n; i++) {
                int a = sa[i - 1], b = sa[i];
                bool different = rank[a] != rank[b];
                int ra = a + width < n ? rank[a + width] : -1;
                int rb = b + width < n ? rank[b + width] : -1;
                next[b] = (different || ra != rb) ? next[a] + 1 : next[a];
            }
            rank.swap(next);
            if (rank[sa[n - 1]] == n - 1) break;
        }
        std::vector<int> pos(n);
        for (int i = 0; i < n; i++) pos[sa[i]] = i;
        std::vector<int> lcp(std::max(0, n - 1), 0);
        int height = 0;
        for (int i = 0; i < n; i++) {
            int p = pos[i];
            if (p == n - 1) {
                height = 0;
                continue;
            }
            int j = sa[p + 1];
            while (i + height < n && j + height < n && nums[i + height] == nums[j + height]) height++;
            lcp[p] = height;
            if (height > 0) height--;
        }
        int ans = n;
        for (int p = 0; p < n; p++) {
            int start = sa[p];
            int need = 1;
            if (p > 0 && lcp[p - 1] + 1 > need) need = lcp[p - 1] + 1;
            if (p + 1 < n && lcp[p] + 1 > need) need = lcp[p] + 1;
            if (need <= n - start && need < ans) ans = need;
        }
        return ans;
    }
};


================================================================================
// FILE: 3935_power_update_after_k_th_largest_insertion_i (1774 bytes)
================================================================================
// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

#include <map>
#include <vector>

class Solution {
    static void merge(std::map<int, int>& st, int x, int v) {
        int c = st.count(x) ? st[x] : 0;
        if (c + v == 0) st.erase(x);
        else st[x] = c + v;
    }

public:
    std::vector<int> powerUpdate(std::vector<int>& nums, int p, std::vector<std::vector<int>>& queries) {
        std::map<int, int> L, R;
        int sz1 = 0, sz2 = (int)nums.size();
        for (int x : nums) merge(R, x, 1);
        const int mod = 1000000007;
        auto qpow = [&](long long a, int b) {
            long long ans = 1;
            while (b > 0) {
                if (b & 1) ans = ans * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return (int)ans;
        };
        std::vector<int> ans;
        ans.reserve(queries.size());
        for (auto& q : queries) {
            int val = q[0], k = q[1];
            merge(R, val, 1);
            sz2++;
            int node = R.begin()->first;
            merge(R, node, -1);
            sz2--;
            merge(L, node, 1);
            sz1++;
            while (sz2 < k) {
                node = L.rbegin()->first;
                merge(L, node, -1);
                sz1--;
                merge(R, node, 1);
                sz2++;
            }
            while (sz2 > k) {
                node = R.begin()->first;
                merge(R, node, -1);
                sz2--;
                merge(L, node, 1);
                sz1++;
            }
            int x = R.begin()->first;
            p = qpow(p, x);
            ans.push_back(p);
        }
        return ans;
    }
};


================================================================================
// FILE: 3936_minimum_swaps_to_move_zeros_to_end (507 bytes)
================================================================================
// LeetCode 3936 - Minimum Swaps To Move Zeros To End
// https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

#include <vector>

class Solution {
public:
    int minimumSwaps(std::vector<int>& nums) {
        int ans = 0;
        int n = (int)nums.size();
        for (int i = 0, j = n - 1; i < j; i++, j--) {
            while (i < n && nums[i] != 0) i++;
            while (j > 0 && nums[j] == 0) j--;
            if (i >= j) break;
            ans++;
        }
        return ans;
    }
};


================================================================================
// FILE: 3937_minimum_operations_to_make_array_modulo_alternating_i (864 bytes)
================================================================================
// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

#include <algorithm>
#include <climits>
#include <cmath>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        for (int& v : nums) v %= k;
        int ans = INT_MAX;
        for (int x = 0; x < k; x++) {
            for (int y = 0; y < k; y++) {
                if (x == y) continue;
                int cnt = 0;
                for (int i = 0; i < (int)nums.size(); i++) {
                    int target = (i & 1) ? y : x;
                    int diff = std::abs(target - nums[i]);
                    cnt += std::min(diff, k - diff);
                }
                ans = std::min(ans, cnt);
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 3938_maximum_path_intersection_sum_in_a_grid (1307 bytes)
================================================================================
// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

#include <climits>
#include <functional>
#include <vector>

class Solution {
public:
    int maxPathSum(std::vector<std::vector<int>>& grid) {
        int rows = (int)grid.size(), cols = (int)grid[0].size();
        int answer = INT_MIN;
        auto checkLine = [&](int length, auto value) {
            int bestEnding = value(0) + value(1);
            if (bestEnding > answer) answer = bestEnding;
            for (int i = 2; i < length; i++) {
                if (value(i - 1) + value(i) > bestEnding + value(i)) bestEnding = value(i - 1) + value(i);
                else bestEnding += value(i);
                if (bestEnding > answer) answer = bestEnding;
            }
        };
        for (int row = 0; row < rows; row++) {
            checkLine(cols, [&](int col) { return grid[row][col]; });
        }
        for (int col = 0; col < cols; col++) {
            checkLine(rows, [&](int row) { return grid[row][col]; });
        }
        for (int row = 1; row + 1 < rows; row++) {
            for (int col = 1; col + 1 < cols; col++) {
                if (grid[row][col] > answer) answer = grid[row][col];
            }
        }
        return answer;
    }
};


================================================================================
// FILE: 3939_count_non_adjacent_subsets_in_a_rooted_tree (1434 bytes)
================================================================================
// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

#include <vector>

class Solution {
public:
    int countNonAdjacentSubsets(std::vector<int>& parent, std::vector<int>& nums, int k) {
        const long long mod = 1000000007;
        int n = (int)parent.size();
        std::vector<std::vector<int>> children(n);
        for (int i = 1; i < n; i++) children[parent[i]].push_back(i);
        std::vector<std::vector<long long>> dp0(n), dp1(n);
        for (int u = n - 1; u >= 0; u--) {
            std::vector<long long> a(k, 0), b(k, 0);
            a[0] = 1;
            b[((nums[u] % k) + k) % k] = 1;
            for (int v : children[u]) {
                std::vector<long long> na(k, 0), nb(k, 0);
                for (int x = 0; x < k; x++) {
                    for (int y = 0; y < k; y++) {
                        long long allChild = (dp0[v][y] + dp1[v][y]) % mod;
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % mod;
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod;
                    }
                }
                a.swap(na);
                b.swap(nb);
            }
            dp0[u] = a;
            dp1[u] = b;
        }
        long long ans = (dp0[0][0] + dp1[0][0] - 1) % mod;
        if (ans < 0) ans += mod;
        return (int)ans;
    }
};


================================================================================
// FILE: 3940_limit_occurrences_in_sorted_array (572 bytes)
================================================================================
// LeetCode 3940 - Limit Occurrences In Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/

#include <vector>

class Solution {
public:
    std::vector<int> limitOccurrences(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        int cnt = 1, l = 1;
        for (int r = 1; r < n; r++) {
            if (nums[r] != nums[r - 1]) cnt = 1;
            else cnt++;
            if (cnt <= k) {
                nums[l] = nums[r];
                l++;
            }
        }
        nums.resize(l);
        return nums;
    }
};


================================================================================
// FILE: 3941_password_strength (600 bytes)
================================================================================
// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

#include <cctype>
#include <string>
#include <unordered_set>

class Solution {
public:
    int passwordStrength(std::string password) {
        std::unordered_set<char> st(password.begin(), password.end());
        int ans = 0;
        for (char ch : st) {
            if (std::islower((unsigned char)ch)) ans += 1;
            else if (std::isupper((unsigned char)ch)) ans += 2;
            else if (std::isdigit((unsigned char)ch)) ans += 3;
            else ans += 5;
        }
        return ans;
    }
};


================================================================================
// FILE: 3942_minimum_operations_to_sort_a_permutation (1117 bytes)
================================================================================
// LeetCode 3942 - Minimum Operations To Sort A Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = (int)nums.size();
        int zero = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                zero = i;
                break;
            }
        }
        auto check = [&](int step) {
            for (int i = 1; i < n; i++) {
                int prev = ((zero + (i - 1) * step) % n + n) % n;
                int curr = ((zero + i * step) % n + n) % n;
                if (nums[prev] > nums[curr]) return false;
            }
            return true;
        };
        int ans = INT_MAX;
        if (check(1)) {
            ans = std::min(ans, zero);
            ans = std::min(ans, n - zero + 2);
        }
        if (check(-1)) {
            ans = std::min(ans, zero + 2);
            ans = std::min(ans, n - zero);
        }
        if (ans == INT_MAX) return -1;
        return ans;
    }
};


================================================================================
// FILE: 3943_number_of_pairs_after_increment (2472 bytes)
================================================================================
// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<long long> numberOfPairs(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<std::vector<int>>& queries) {
        const int blockSize = 225;
        int n = (int)nums2.size();
        int blocks = (n + blockSize - 1) / blockSize;
        std::vector<int> lazy(blocks, 0);
        std::vector<std::unordered_map<int, int>> freq(blocks);
        auto rebuild = [&](int b) {
            freq[b].clear();
            int end = std::min((b + 1) * blockSize, n);
            for (int i = b * blockSize; i < end; i++) freq[b][nums2[i]]++;
        };
        auto push = [&](int b) {
            if (lazy[b] != 0) {
                int end = std::min((b + 1) * blockSize, n);
                for (int i = b * blockSize; i < end; i++) nums2[i] += lazy[b];
                lazy[b] = 0;
            }
        };
        for (int b = 0; b < blocks; b++) rebuild(b);
        std::unordered_map<int, int> fixed;
        for (int x : nums1) fixed[x]++;
        std::vector<long long> answer;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int l = q[1], r = q[2], delta = q[3];
                int first = l / blockSize, last = r / blockSize;
                if (first == last) {
                    push(first);
                    for (int i = l; i <= r; i++) nums2[i] += delta;
                    rebuild(first);
                    continue;
                }
                push(first);
                for (int i = l; i < (first + 1) * blockSize; i++) nums2[i] += delta;
                rebuild(first);
                push(last);
                for (int i = last * blockSize; i <= r; i++) nums2[i] += delta;
                rebuild(last);
                for (int b = first + 1; b < last; b++) lazy[b] += delta;
            } else {
                long long total = 0;
                for (auto& [a, countA] : fixed) {
                    int target = q[1] - a;
                    for (int b = 0; b < blocks; b++) {
                        auto it = freq[b].find(target - lazy[b]);
                        if (it != freq[b].end()) total += (long long)countA * it->second;
                    }
                }
                answer.push_back(total);
            }
        }
        return answer;
    }
};


================================================================================
// FILE: 3944_minimum_operations_to_make_array_modulo_alternating_ii (2348 bytes)
================================================================================
// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums, int k) {
        std::vector<long long> evenFreq(k), oddFreq(k);
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i % 2 == 0) evenFreq[nums[i] % k]++;
            else oddFreq[nums[i] % k]++;
        }
        auto costs = [&](const std::vector<long long>& freq) {
            std::vector<long long> dbl(2 * k);
            for (int i = 0; i < 2 * k; i++) dbl[i] = freq[i % k];
            std::vector<long long> countPrefix(2 * k + 1), weightedPrefix(2 * k + 1);
            for (int i = 0; i < 2 * k; i++) {
                countPrefix[i + 1] = countPrefix[i] + dbl[i];
                weightedPrefix[i + 1] = weightedPrefix[i] + (long long)i * dbl[i];
            }
            auto rangeStats = [&](int l, int r) {
                return std::pair<long long, long long>{
                    countPrefix[r + 1] - countPrefix[l],
                    weightedPrefix[r + 1] - weightedPrefix[l]
                };
            };
            std::vector<long long> res(k);
            int cw = k / 2, cc = (k - 1) / 2;
            for (int t = 0; t < k; t++) {
                auto [cnt, sum] = rangeStats(t, t + cw);
                res[t] += sum - (long long)t * cnt;
                if (cc > 0) {
                    auto [cnt2, sum2] = rangeStats(t + k - cc, t + k - 1);
                    res[t] += (long long)(t + k) * cnt2 - sum2;
                }
            }
            return res;
        };
        auto evenCost = costs(evenFreq);
        auto oddCost = costs(oddFreq);
        long long best1 = 1LL << 62, best2 = 1LL << 62;
        int bestIndex = -1;
        for (int i = 0; i < k; i++) {
            long long x = oddCost[i];
            if (x < best1) {
                best2 = best1;
                best1 = x;
                bestIndex = i;
            } else if (x < best2) best2 = x;
        }
        long long ans = 1LL << 62;
        for (int x = 0; x < k; x++) {
            long long other = (x == bestIndex) ? best2 : best1;
            ans = std::min(ans, evenCost[x] + other);
        }
        return ans;
    }
};


================================================================================
// FILE: 3945_digit_frequency_score (256 bytes)
================================================================================
// LeetCode 3945 - Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/

class Solution {
public:
    int digitFrequencyScore(int n) {
        int ans = 0;
        for (; n > 0; n /= 10) ans += n % 10;
        return ans;
    }
};


================================================================================
// FILE: 3946_maximum_number_of_items_from_sale_i (939 bytes)
================================================================================
// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maximumSaleItems(std::vector<std::vector<int>>& items, int budget) {
        std::vector<int> f(budget + 1, 0);
        int mn = INT_MAX;
        for (auto& item : items) {
            int factor = item[0], price = item[1];
            mn = std::min(mn, price);
            int cnt = 0;
            for (auto& jItem : items) {
                if (jItem[0] % factor == 0) cnt++;
            }
            for (int j = budget; j >= price; j--) {
                f[j] = std::max(f[j], f[j - price] + cnt);
            }
        }
        int ans = 0;
        for (int i = 0; i <= budget; i++) {
            int extra = (budget - i) / mn;
            ans = std::max(ans, f[i] + extra);
        }
        return ans;
    }
};


================================================================================
// FILE: 3947_maximum_number_of_items_from_sale_ii (1639 bytes)
================================================================================
// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxItems(std::vector<std::vector<int>>& items, int budget) {
        int n = (int)items.size();
        std::vector<int> frequency(n + 1, 0);
        int minimumPrice = items[0][1];
        for (auto& item : items) {
            frequency[item[0]]++;
            minimumPrice = std::min(minimumPrice, item[1]);
        }
        struct Batch { int price, count; };
        std::vector<Batch> batches;
        for (auto& item : items) {
            int gain = 0;
            for (int multiple = item[0]; multiple <= n; multiple += item[0]) gain += frequency[multiple];
            gain--;
            if (gain > 0 && item[1] < 2 * minimumPrice) batches.push_back({item[1], gain});
        }
        std::sort(batches.begin(), batches.end(), [](const Batch& a, const Batch& b) {
            return a.price < b.price;
        });
        long long remaining = budget;
        long long answer = budget / minimumPrice;
        long long boosted = 0;
        for (auto& current : batches) {
            long long count = current.count;
            long long affordable = remaining / current.price;
            if (affordable < count) count = affordable;
            remaining -= count * current.price;
            boosted += count;
            long long total = 2 * boosted + remaining / minimumPrice;
            if (total > answer) answer = total;
            if (count < current.count) break;
        }
        return (int)answer;
    }
};


================================================================================
// FILE: 3948_lexicographically_maximum_mex_array (1288 bytes)
================================================================================
// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

#include <vector>

class Solution {
public:
    std::vector<int> maxMexArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> remaining(n + 2, 0);
        for (int x : nums) {
            if (x <= n + 1) remaining[x]++;
        }
        int mex = 0;
        while (remaining[mex] > 0) mex++;
        std::vector<int> answer;
        std::vector<int> seen(n + 2, 0);
        int stamp = 0, index = 0;
        while (index < n) {
            if (mex == 0) {
                answer.push_back(0);
                int x = nums[index];
                if (x <= n + 1) remaining[x]--;
                index++;
                continue;
            }
            stamp++;
            int need = mex;
            while (need > 0) {
                int x = nums[index];
                if (x < mex && seen[x] != stamp) {
                    seen[x] = stamp;
                    need--;
                }
                if (x <= n + 1) remaining[x]--;
                index++;
            }
            answer.push_back(mex);
            mex = 0;
            while (remaining[mex] > 0) mex++;
        }
        return answer;
    }
};


================================================================================
// FILE: 3949_subtree_inversion_sum_ii (2819 bytes)
================================================================================
// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxSubtreeInversionSum(std::vector<std::vector<int>>& edges, std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        std::vector<int> parent(n, -2);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.push_back(v);
                }
            }
        }
        const long long infinity = 1LL << 60;
        std::vector<std::vector<long long>> maximum(n), minimum(n);
        for (int oi = n - 1; oi >= 0; oi--) {
            int u = order[oi];
            std::vector<long long> currentMax(k + 1, -infinity), currentMin(k + 1, infinity);
            currentMax[k] = currentMin[k] = nums[u];
            for (int v : graph[u]) {
                if (parent[v] != u) continue;
                std::vector<long long> nextMax(k + 1, -infinity), nextMin(k + 1, infinity);
                for (int first = 0; first <= k; first++) {
                    if (currentMax[first] == -infinity) continue;
                    for (int childDistance = 0; childDistance <= k; childDistance++) {
                        if (maximum[v][childDistance] == -infinity) continue;
                        int second = childDistance + 1;
                        if (second > k) second = k;
                        if (first < k && second < k && first + second < k) continue;
                        int distance = std::min(first, second);
                        long long maxValue = currentMax[first] + maximum[v][childDistance];
                        long long minValue = currentMin[first] + minimum[v][childDistance];
                        nextMax[distance] = std::max(nextMax[distance], maxValue);
                        nextMin[distance] = std::min(nextMin[distance], minValue);
                    }
                }
                currentMax.swap(nextMax);
                currentMin.swap(nextMin);
            }
            if (-currentMin[k] > currentMax[0]) currentMax[0] = -currentMin[k];
            if (-currentMax[k] < currentMin[0]) currentMin[0] = -currentMax[k];
            maximum[u] = currentMax;
            minimum[u] = currentMin;
        }
        long long answer = -(1LL << 60);
        for (long long value : maximum[0]) answer = std::max(answer, value);
        return answer;
    }
};


================================================================================
// FILE: 3950_exactly_one_consecutive_set_bits_pair (476 bytes)
================================================================================
// LeetCode 3950 - Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

class Solution {
public:
    bool consecutiveSetBits(int n) {
        bool vis = false;
        for (int pre = 0; n > 0; n >>= 1) {
            int cur = n & 1;
            if (pre == cur && cur == 1) {
                if (vis) return false;
                vis = true;
            }
            pre = cur;
        }
        return vis;
    }
};


================================================================================
// FILE: 3951_minimum_energy_to_maintain_brightness (939 bytes)
================================================================================
// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minEnergy(int n, int brightness, std::vector<std::vector<int>>& intervals) {
        (void)n;
        std::sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) {
            return a[0] < b[0];
        });
        std::vector<std::vector<int>> merged = {intervals[0]};
        for (int i = 1; i < (int)intervals.size(); i++) {
            auto& x = intervals[i];
            if (merged.back()[1] < x[0]) merged.push_back(x);
            else if (x[1] > merged.back()[1]) merged.back()[1] = x[1];
        }
        long long ans = 0;
        for (auto& interval : merged) {
            int m = interval[1] - interval[0] + 1;
            ans += (long long)((brightness + 2) / 3) * m;
        }
        return ans;
    }
};


================================================================================
// FILE: 3952_maximum_total_value_of_covered_indices (1023 bytes)
================================================================================
// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

#include <string>
#include <vector>

class Solution {
public:
    int maxTotalValue(std::vector<int>& nums, std::string s) {
        int answer = 0;
        for (int i = 0; i < (int)s.size();) {
            if (s[i] == '0') {
                i++;
                continue;
            }
            int start = i;
            while (i < (int)s.size() && s[i] == '1') i++;
            int end = i - 1;
            if (start == 0) {
                for (int index = start; index <= end; index++) answer += nums[index];
                continue;
            }
            int minimum = nums[start - 1];
            int total = 0;
            for (int index = start - 1; index <= end; index++) {
                total += nums[index];
                if (nums[index] < minimum) minimum = nums[index];
            }
            answer += total - minimum;
        }
        return answer;
    }
};


================================================================================
// FILE: 3953_maximum_score_with_co_prime_element (2242 bytes)
================================================================================
// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

#include <vector>

class Solution {
public:
    int maxScore(std::vector<int>& nums, int maxVal) {
        int limit = maxVal;
        std::vector<int> frequency(100001, 0);
        for (int x : nums) {
            frequency[x]++;
            if (x > limit) limit = x;
        }
        std::vector<int> divisible(limit + 1, 0);
        for (int d = 1; d <= limit; d++) {
            for (int multiple = d; multiple <= limit; multiple += d) {
                if (multiple < (int)frequency.size()) divisible[d] += frequency[multiple];
            }
        }
        auto badCount = [&](int x) {
            std::vector<int> primes;
            int y = x;
            for (int p = 2; 1LL * p * p <= y; p++) {
                if (y % p == 0) {
                    primes.push_back(p);
                    while (y % p == 0) y /= p;
                }
            }
            if (y > 1) primes.push_back(y);
            int bad = 0;
            int psz = (int)primes.size();
            for (int mask = 1; mask < (1 << psz); mask++) {
                int product = 1, bits = 0;
                for (int i = 0; i < psz; i++) {
                    if ((mask >> i) & 1) {
                        product *= primes[i];
                        bits++;
                    }
                }
                if (bits % 2 == 1) bad += divisible[product];
                else bad -= divisible[product];
            }
            return bad;
        };
        int best = -(int)nums.size();
        std::vector<bool> checked(limit + 1, false);
        auto evaluate = [&](int x, bool exists) {
            if (checked[x]) return;
            checked[x] = true;
            int bad = badCount(x);
            int cost = 0;
            if (exists) {
                if (x > 1) cost = bad - 1;
            } else if (bad > 0) cost = bad;
            else cost = 1;
            if (x - cost > best) best = x - cost;
        };
        for (int x = 1; x <= maxVal; x++) {
            evaluate(x, x < (int)frequency.size() && frequency[x] > 0);
        }
        for (int x : nums) evaluate(x, true);
        return best;
    }
};


================================================================================
// FILE: 3954_sum_of_compatible_numbers_in_range_i (427 bytes)
================================================================================
// LeetCode 3954 - Sum Of Compatible Numbers In Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

#include <algorithm>

class Solution {
public:
    int sumOfGoodIntegers(int n, int k) {
        int start = std::max(1, n - k);
        int end = n + k;
        int ans = 0;
        for (int x = start; x <= end; x++) {
            if ((n & x) == 0) ans += x;
        }
        return ans;
    }
};


================================================================================
// FILE: 3955_valid_binary_strings_with_cost_limit (877 bytes)
================================================================================
// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> generateValidStrings(int n, int k) {
        std::vector<std::string> ans;
        std::string path;
        path.reserve(n);
        std::function<void(int, int)> dfs = [&](int i, int tot) {
            if (i >= n) {
                ans.push_back(path);
                return;
            }
            path.push_back('0');
            dfs(i + 1, tot);
            path.pop_back();
            if ((path.empty() || path.back() == '0') && tot + i <= k) {
                path.push_back('1');
                dfs(i + 1, tot + i);
                path.pop_back();
            }
        };
        dfs(0, 0);
        return ans;
    }
};


================================================================================
// FILE: 3956_maximum_sum_of_m_non_overlapping_subarrays_i (1724 bytes)
================================================================================
// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

#include <vector>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, int m, int l, int r) {
        int n = (int)nums.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        std::vector<long long> dp(n + 1, 0);
        long long bestSelected = -(1LL << 62);
        for (int count = 1; count <= m; count++) {
            std::vector<long long> next = dp;
            std::vector<int> deque;
            for (int end = 1; end <= n; end++) {
                int addIndex = end - l;
                if (addIndex >= 0) {
                    long long value = dp[addIndex] - prefix[addIndex];
                    while (!deque.empty()) {
                        int last = deque.back();
                        if (dp[last] - prefix[last] > value) break;
                        deque.pop_back();
                    }
                    deque.push_back(addIndex);
                }
                int minIndex = end - r;
                while (!deque.empty() && deque.front() < minIndex) deque.erase(deque.begin());
                if (!deque.empty()) {
                    long long candidate = prefix[end] + dp[deque.front()] - prefix[deque.front()];
                    if (candidate > next[end]) next[end] = candidate;
                    if (candidate > bestSelected) bestSelected = candidate;
                }
                if (next[end - 1] > next[end]) next[end] = next[end - 1];
            }
            dp.swap(next);
        }
        return bestSelected;
    }
};


================================================================================
// FILE: 3957_maximum_sum_of_m_non_overlapping_subarrays_ii (3145 bytes)
================================================================================
// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

#include <vector>

class Solution {
    struct State {
        long long value = 0;
        int count = 0;
    };

    static bool better(State a, State b) {
        return a.value > b.value || (a.value == b.value && a.count > b.count);
    }

public:
    long long maxSum(std::vector<int>& nums, int m, int l, int r) {
        int n = (int)nums.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        auto run = [&](long long penalty) -> State {
            std::vector<State> dp(n + 1);
            std::vector<int> deque;
            auto candidateBetter = [&](int a, int b) {
                State left{dp[a].value - prefix[a], dp[a].count};
                State right{dp[b].value - prefix[b], dp[b].count};
                return better(left, right);
            };
            for (int end = 1; end <= n; end++) {
                int addIndex = end - l;
                if (addIndex >= 0) {
                    while (!deque.empty() && candidateBetter(addIndex, deque.back())) deque.pop_back();
                    deque.push_back(addIndex);
                }
                int minIndex = end - r;
                while (!deque.empty() && deque.front() < minIndex) deque.erase(deque.begin());
                dp[end] = dp[end - 1];
                if (!deque.empty()) {
                    int start = deque.front();
                    State take{dp[start].value + prefix[end] - prefix[start] - penalty, dp[start].count + 1};
                    if (better(take, dp[end])) dp[end] = take;
                }
            }
            return dp[n];
        };

        State unconstrained = run(0);
        if (unconstrained.count > 0 && unconstrained.count <= m) return unconstrained.value;
        if (unconstrained.count > m) {
            long long bound = 0;
            for (int value : nums) bound += value >= 0 ? value : -value;
            long long low = 0, high = bound + 1;
            while (low < high) {
                long long mid = low + (high - low + 1) / 2;
                if (run(mid).count >= m) low = mid;
                else high = mid - 1;
            }
            State state = run(low);
            return state.value + low * m;
        }
        const long long infinity = 1LL << 60;
        long long bestSingle = -infinity;
        std::vector<int> deque;
        for (int end = 1; end <= n; end++) {
            int addIndex = end - l;
            if (addIndex >= 0) {
                while (!deque.empty() && prefix[deque.back()] >= prefix[addIndex]) deque.pop_back();
                deque.push_back(addIndex);
            }
            int minIndex = end - r;
            while (!deque.empty() && deque.front() < minIndex) deque.erase(deque.begin());
            if (!deque.empty()) {
                long long sum = prefix[end] - prefix[deque.front()];
                if (sum > bestSingle) bestSingle = sum;
            }
        }
        return bestSingle;
    }
};


================================================================================
// FILE: 3958_minimum_cost_to_split_into_ones_ii (227 bytes)
================================================================================
// LeetCode 3958 - Minimum Cost To Split Into Ones II
// https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

class Solution {
public:
    long long minCost(int n) {
        return 1LL * n * (n - 1) / 2;
    }
};


================================================================================
// FILE: 3959_check_good_integer (305 bytes)
================================================================================
// LeetCode 3959 - Check Good Integer
// https://leetcode.com/problems/check-good-integer/

class Solution {
public:
    bool checkGoodInteger(int n) {
        int s = 0;
        for (; n > 0; n /= 10) {
            int x = n % 10;
            s += x * (x - 1);
        }
        return s >= 50;
    }
};


================================================================================
// FILE: 3960_frequency_balance_subarray (952 bytes)
================================================================================
// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int getLength(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = 1;
        for (int l = 0; l < n; l++) {
            std::unordered_map<int, int> cnt, freq;
            for (int r = l; r < n; r++) {
                int x = nums[r];
                int c = cnt[x];
                if (freq[c] > 0) {
                    if (--freq[c] == 0) freq.erase(c);
                }
                cnt[x] = c + 1;
                freq[cnt[x]]++;
                int cx = cnt[x];
                if ((int)cnt.size() == 1 || ((int)freq.size() == 2 && (freq[cx * 2] > 0 || (cx % 2 == 0 && freq[cx / 2] > 0)))) {
                    ans = std::max(ans, r - l + 1);
                }
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 3961_maximize_sum_of_device_ratings (733 bytes)
================================================================================
// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long maxRatings(std::vector<std::vector<int>>& units) {
        int n = (int)units[0].size();
        if (n == 1) {
            long long ans = 0;
            for (auto& x : units) ans += x[0];
            return ans;
        }
        long long ans = 0;
        int mn = INT_MAX, mn2 = INT_MAX;
        for (auto& x : units) {
            std::sort(x.begin(), x.end());
            ans += x[1];
            mn2 = std::min(mn2, x[1]);
            mn = std::min(mn, x[0]);
        }
        return ans - (mn2 - mn);
    }
};


================================================================================
// FILE: 3962_maximum_subarray_sum_after_at_most_k_swaps (4292 bytes)
================================================================================
// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxSubarraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> unique = nums;
        std::sort(unique.begin(), unique.end());
        unique.erase(std::unique(unique.begin(), unique.end()), unique.end());
        std::vector<int> rank(n);
        std::vector<int> globalCount(unique.size() + 1, 0);
        std::vector<long long> globalSum(unique.size() + 1, 0);
        auto add = [&](std::vector<int>& count, std::vector<long long>& sum, int index, int delta) {
            long long value = unique[index - 1];
            for (; index < (int)count.size(); index += index & -index) {
                count[index] += delta;
                sum[index] += (long long)delta * value;
            }
        };
        for (int i = 0; i < n; i++) {
            rank[i] = (int)(std::lower_bound(unique.begin(), unique.end(), nums[i]) - unique.begin()) + 1;
            add(globalCount, globalSum, rank[i], 1);
        }
        auto queryCount = [](std::vector<int>& bit, int index) {
            int result = 0;
            for (; index > 0; index -= index & -index) result += bit[index];
            return result;
        };
        auto querySum = [](std::vector<long long>& bit, int index) {
            long long result = 0;
            for (; index > 0; index -= index & -index) result += bit[index];
            return result;
        };
        auto kth = [](std::vector<int>& bit, int order) {
            int index = 0, step = 1;
            while ((step << 1) < (int)bit.size()) step <<= 1;
            for (; step > 0; step >>= 1) {
                int next = index + step;
                if (next < (int)bit.size() && bit[next] < order) {
                    index = next;
                    order -= bit[next];
                }
            }
            return index + 1;
        };
        auto sumSmallest = [&](std::vector<int>& count, std::vector<long long>& sum, int amount) {
            if (amount <= 0) return 0LL;
            int index = kth(count, amount);
            int countBefore = queryCount(count, index - 1);
            long long sumBefore = querySum(sum, index - 1);
            return sumBefore + (long long)(amount - countBefore) * unique[index - 1];
        };
        long long answer = -(1LL << 60);
        for (int left = 0; left < n; left++) {
            std::vector<int> insideCount(unique.size() + 1, 0);
            std::vector<long long> insideSum(unique.size() + 1, 0);
            std::vector<int> outsideCount = globalCount;
            std::vector<long long> outsideSum = globalSum;
            long long subarraySum = 0;
            for (int right = left; right < n; right++) {
                add(outsideCount, outsideSum, rank[right], -1);
                add(insideCount, insideSum, rank[right], 1);
                subarraySum += nums[right];
                int insideSize = right - left + 1;
                int outsideSize = n - insideSize;
                int limit = std::min({k, insideSize, outsideSize});
                int low = 0, high = limit;
                while (low < high) {
                    int mid = (low + high + 1) / 2;
                    int insideValue = unique[kth(insideCount, mid) - 1];
                    int outsideOrder = outsideSize - mid + 1;
                    int outsideValue = unique[kth(outsideCount, outsideOrder) - 1];
                    if (outsideValue > insideValue) low = mid;
                    else high = mid - 1;
                }
                int swaps = low;
                long long gain = 0;
                if (swaps > 0) {
                    long long smallInside = sumSmallest(insideCount, insideSum, swaps);
                    long long totalOutside = querySum(outsideSum, (int)unique.size());
                    long long largeOutside = totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize - swaps);
                    gain = largeOutside - smallInside;
                }
                answer = std::max(answer, subarraySum + gain);
            }
        }
        return answer;
    }
};


================================================================================
// FILE: 3963_create_grid_with_exactly_one_path (433 bytes)
================================================================================
// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> createGrid(int m, int n) {
        std::vector<std::string> g(m, std::string(n, '#'));
        for (int j = 0; j < n; j++) g[0][j] = '.';
        for (int i = 0; i < m; i++) g[i][n - 1] = '.';
        return g;
    }
};


================================================================================
// FILE: 3964_minimum_lights_to_illuminate_a_road (863 bytes)
================================================================================
// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minLights(std::vector<int>& lights) {
        int n = (int)lights.size();
        std::vector<int> d(n, 0);
        for (int i = 0; i < n; i++) {
            int v = lights[i];
            if (v > 0) {
                int l = std::max(0, i - v);
                int r = std::min(n - 1, i + v);
                d[l]++;
                if (r + 1 < n) d[r + 1]--;
            }
        }
        int s = 0, cnt = 0, ans = 0;
        for (int x : d) {
            s += x;
            if (s == 0) cnt++;
            else {
                ans += (cnt + 2) / 3;
                cnt = 0;
            }
        }
        ans += (cnt + 2) / 3;
        return ans;
    }
};


================================================================================
// FILE: 3965_finish_time_of_tasks_i (940 bytes)
================================================================================
// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    long long finishTime(int n, std::vector<std::vector<int>>& edges, std::vector<int>& baseTime) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) g[e[0]].push_back(e[1]);
        std::function<long long(int)> dfs = [&](int i) -> long long {
            if (g[i].empty()) return baseTime[i];
            const long long INF = 1LL << 62;
            long long earliest = INF, latest = -INF;
            for (int j : g[i]) {
                long long a = dfs(j);
                earliest = std::min(earliest, a);
                latest = std::max(latest, a);
            }
            long long ownDuration = (latest - earliest) + baseTime[i];
            return latest + ownDuration;
        };
        return dfs(0);
    }
};


================================================================================
// FILE: 3966_count_good_integers_in_a_range (1666 bytes)
================================================================================
// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

#include <cmath>
#include <functional>
#include <map>
#include <string>
#include <tuple>
#include <vector>

class Solution {
public:
    long long countGoodIntegers(long long l, long long r, int k) {
        auto count = [&](long long bound) -> long long {
            if (bound <= 0) return 0;
            std::string digits = std::to_string(bound);
            std::map<std::tuple<int, int, bool>, long long> memo;
            std::function<long long(int, int, bool, bool)> dfs = [&](int position, int previous, bool started, bool tight) -> long long {
                if (position == (int)digits.size()) return started ? 1 : 0;
                auto key = std::make_tuple(position, previous, started);
                if (!tight) {
                    auto it = memo.find(key);
                    if (it != memo.end()) return it->second;
                }
                int limit = tight ? digits[position] - '0' : 9;
                long long result = 0;
                for (int digit = 0; digit <= limit; digit++) {
                    bool nextStarted = started || digit != 0;
                    if (started && std::abs(previous - digit) > k) continue;
                    int nextPrevious = nextStarted ? digit : previous;
                    result += dfs(position + 1, nextPrevious, nextStarted, tight && digit == limit);
                }
                if (!tight) memo[key] = result;
                return result;
            };
            return dfs(0, 0, false, true);
        };
        return count(r) - count(l - 1);
    }
};


================================================================================
// FILE: 3967_finish_time_of_tasks_ii (3686 bytes)
================================================================================
// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

#include <algorithm>
#include <vector>

class Solution {
    struct Edge {
        int to, reverse;
    };

    static long long combine(long long minimum, long long maximum, int count, int base) {
        if (count == 0) return base;
        return 2 * maximum - minimum + base;
    }

public:
    long long minFinishTime(int n, std::vector<std::vector<int>>& edges, std::vector<int>& baseTime) {
        std::vector<std::vector<Edge>> graph(n);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            int iu = (int)graph[u].size(), iv = (int)graph[v].size();
            graph[u].push_back({v, iv});
            graph[v].push_back({u, iu});
        }
        std::vector<int> parent(n, -2), parentEdge(n, 0);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (auto& edge : graph[u]) {
                if (parent[edge.to] == -2) {
                    parent[edge.to] = u;
                    parentEdge[edge.to] = edge.reverse;
                    order.push_back(edge.to);
                }
            }
        }
        std::vector<std::vector<long long>> incoming(n);
        for (int i = 0; i < n; i++) incoming[i].assign(graph[i].size(), 0);
        for (int oi = n - 1; oi > 0; oi--) {
            int u = order[oi];
            long long minimum = 1LL << 62, maximum = -1;
            int count = 0;
            for (int edgeIndex = 0; edgeIndex < (int)incoming[u].size(); edgeIndex++) {
                if (edgeIndex == parentEdge[u]) continue;
                long long value = incoming[u][edgeIndex];
                minimum = std::min(minimum, value);
                maximum = std::max(maximum, value);
                count++;
            }
            long long value = combine(minimum, maximum, count, baseTime[u]);
            int parentNode = parent[u];
            int reverseIndex = graph[u][parentEdge[u]].reverse;
            incoming[parentNode][reverseIndex] = value;
        }
        long long answer = 1LL << 62;
        for (int u : order) {
            long long min1 = 1LL << 62, min2 = 1LL << 62;
            int minIndex = -1;
            long long max1 = -1, max2 = -1;
            int maxIndex = -1;
            for (int i = 0; i < (int)incoming[u].size(); i++) {
                long long value = incoming[u][i];
                if (value < min1) {
                    min2 = min1;
                    min1 = value;
                    minIndex = i;
                } else if (value < min2) min2 = value;
                if (value > max1) {
                    max2 = max1;
                    max1 = value;
                    maxIndex = i;
                } else if (value > max2) max2 = value;
            }
            long long rootValue = combine(min1, max1, (int)graph[u].size(), baseTime[u]);
            answer = std::min(answer, rootValue);
            for (int i = 0; i < (int)graph[u].size(); i++) {
                auto& edge = graph[u][i];
                if (edge.to == parent[u]) continue;
                if ((int)graph[u].size() == 1) {
                    incoming[edge.to][edge.reverse] = baseTime[u];
                    continue;
                }
                long long minimum = min1, maximum = max1;
                if (i == minIndex) minimum = min2;
                if (i == maxIndex) maximum = max2;
                incoming[edge.to][edge.reverse] = combine(minimum, maximum, (int)graph[u].size() - 1, baseTime[u]);
            }
        }
        return answer;
    }
};


================================================================================
// FILE: 3968_maximum_manhattan_distance_after_all_moves (547 bytes)
================================================================================
// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

#include <cmath>
#include <string>

class Solution {
public:
    int maxDistance(std::string moves) {
        int x = 0, y = 0, z = 0;
        for (char c : moves) {
            if (c == 'U') x -= 1;
            else if (c == 'D') x += 1;
            else if (c == 'L') y -= 1;
            else if (c == 'R') y += 1;
            else z += 1;
        }
        return std::abs(x) + std::abs(y) + z;
    }
};


================================================================================
// FILE: 3969_valid_subarrays_with_matching_sum_digits_i (666 bytes)
================================================================================
// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

#include <string>
#include <vector>

class Solution {
public:
    int countValidSubarrays(std::vector<int>& nums, int x) {
        int n = (int)nums.size();
        int ans = 0;
        for (int l = 0; l < n; l++) {
            long long s = 0;
            for (int r = l; r < n; r++) {
                s += nums[r];
                if (s % 10 == x) {
                    std::string t = std::to_string(s);
                    if (t[0] - '0' == x) ans++;
                }
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 3970_shortest_path_with_at_most_k_consecutive_identical_characters (1606 bytes)
================================================================================
// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

#include <queue>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    long long shortestPath(int n, std::vector<std::vector<int>>& edges, std::string labels, int k) {
        std::vector<std::vector<std::pair<int, int>>> graph(n);
        for (auto& edge : edges) graph[edge[0]].push_back({edge[1], edge[2]});
        const long long infinity = (long long)((~0ULL) >> 2);
        std::vector<std::vector<long long>> distances(n, std::vector<long long>(k + 1, infinity));
        distances[0][1] = 0;
        using State = std::tuple<long long, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> queue;
        queue.push({0, 0, 1});
        while (!queue.empty()) {
            auto [distance, node, run] = queue.top();
            queue.pop();
            if (distance != distances[node][run]) continue;
            if (node == n - 1) return distance;
            for (auto& [to, weight] : graph[node]) {
                int nextRun = 1;
                if (labels[node] == labels[to]) nextRun = run + 1;
                if (nextRun > k) continue;
                long long nextDistance = distance + weight;
                if (nextDistance < distances[to][nextRun]) {
                    distances[to][nextRun] = nextDistance;
                    queue.push({nextDistance, to, nextRun});
                }
            }
        }
        return -1;
    }
};


================================================================================
// FILE: 3971_maximum_total_value (1750 bytes)
================================================================================
// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

#include <vector>

class Solution {
public:
    int maximumTotalValue(std::vector<int>& value, std::vector<int>& decay, long long m) {
        const long long mod = 1000000007;
        auto countAtLeast = [&](long long threshold) {
            long long count = 0;
            for (int i = 0; i < (int)value.size(); i++) {
                if (value[i] >= threshold) {
                    count += (value[i] - threshold) / decay[i] + 1;
                }
            }
            return count;
        };
        if (countAtLeast(1) <= m) {
            long long sum = 0;
            for (int i = 0; i < (int)value.size(); i++) {
                long long terms = (value[i] - 1LL) / decay[i] + 1;
                sum = (sum + terms * value[i] - (long long)decay[i] * terms * (terms - 1) / 2) % mod;
            }
            return (int)sum;
        }
        long long high = 0;
        for (int v : value) if (v > high) high = v;
        long long low = 1;
        while (low < high) {
            long long mid = (low + high + 1) / 2;
            if (countAtLeast(mid) >= m) low = mid;
            else high = mid - 1;
        }
        long long threshold = low;
        long long count = 0, sum = 0;
        for (int i = 0; i < (int)value.size(); i++) {
            if (value[i] < threshold) continue;
            long long terms = (value[i] - threshold) / decay[i] + 1;
            count += terms;
            sum = (sum + (terms * value[i] - (long long)decay[i] * terms * (terms - 1) / 2) % mod) % mod;
        }
        sum = (sum - ((count - m) % mod) * (threshold % mod)) % mod;
        if (sum < 0) sum += mod;
        return (int)sum;
    }
};


================================================================================
// FILE: 3972_valid_subarrays_with_matching_sum_digits_ii (1254 bytes)
================================================================================
// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long countValidSubarrays(std::vector<int>& nums, int x) {
        std::vector<std::vector<long long>> byRemainder(10);
        byRemainder[0].push_back(0);
        long long prefix = 0, answer = 0;
        for (int value : nums) {
            prefix += value;
            int required = (int)((prefix - x) % 10 + 10) % 10;
            auto& values = byRemainder[required];
            for (long long power = 1; (long long)x * power <= prefix; power *= 10) {
                long long low = (long long)x * power;
                long long high = (long long)(x + 1) * power - 1;
                long long minPrefix = prefix - high, maxPrefix = prefix - low;
                auto left = std::lower_bound(values.begin(), values.end(), minPrefix);
                auto right = std::upper_bound(values.begin(), values.end(), maxPrefix);
                answer += right - left;
                if (power > prefix / 10) break;
            }
            byRemainder[(int)(prefix % 10)].push_back(prefix);
        }
        return answer;
    }
};


================================================================================
// FILE: 3973_distinct_gate_paths_to_lca (3802 bytes)
================================================================================
// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

#include <array>
#include <vector>

class Solution {
    using Mat = std::array<std::array<long long, 2>, 2>;
    static constexpr long long MOD = 1000000007;

    static Mat multiply(const Mat& a, const Mat& b) {
        Mat c{};
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return c;
    }

public:
    int gatePathXor(int n, std::vector<int>& parent, std::vector<std::vector<int>>& gates, std::vector<std::vector<int>>& queries) {
        int logn = 1;
        while ((1 << logn) <= n) logn++;
        std::vector<std::vector<int>> up(logn, std::vector<int>(n));
        std::vector<std::vector<Mat>> product(logn, std::vector<Mat>(n));
        std::vector<std::vector<int>> children(n);
        for (int node = 1; node < n; node++) children[parent[node]].push_back(node);
        std::vector<int> depth(n, 0);
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : children[u]) {
                depth[v] = depth[u] + 1;
                order.push_back(v);
            }
        }
        for (int u = 0; u < n; u++) {
            up[0][u] = (u == 0) ? 0 : parent[u];
            product[0][u] = Mat{{
                {(long long)gates[u][1], (long long)gates[u][2]},
                {(long long)gates[u][2], (long long)gates[u][0]}
            }};
        }
        for (int level = 1; level < logn; level++) {
            for (int u = 0; u < n; u++) {
                int mid = up[level - 1][u];
                up[level][u] = up[level - 1][mid];
                product[level][u] = multiply(product[level - 1][u], product[level - 1][mid]);
            }
        }
        auto liftNode = [&](int node, int distance) {
            for (int level = 0; distance > 0; level++) {
                if (distance & 1) node = up[level][node];
                distance >>= 1;
            }
            return node;
        };
        auto lca = [&](int a, int b) {
            if (depth[a] > depth[b]) a = liftNode(a, depth[a] - depth[b]);
            else if (depth[b] > depth[a]) b = liftNode(b, depth[b] - depth[a]);
            if (a == b) return a;
            for (int level = logn - 1; level >= 0; level--) {
                if (up[level][a] != up[level][b]) {
                    a = up[level][a];
                    b = up[level][b];
                }
            }
            return up[0][a];
        };
        auto ways = [&](int node, int card, int distance) {
            std::array<long long, 2> vector{};
            vector[card] = 1;
            for (int level = 0; distance > 0; level++) {
                if (distance & 1) {
                    Mat matrix = product[level][node];
                    vector = {
                        (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                        (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD
                    };
                    node = up[level][node];
                }
                distance >>= 1;
            }
            return (vector[0] + vector[1]) % MOD;
        };
        int answer = 0;
        for (auto& query : queries) {
            int ancestor = lca(query[0], query[2]);
            long long alice = ways(query[0], query[1], depth[query[0]] - depth[ancestor]);
            long long bob = ways(query[2], query[3], depth[query[2]] - depth[ancestor]);
            int total = (int)(alice * bob % MOD);
            answer ^= total;
        }
        return answer;
    }
};


================================================================================
// FILE: 3974_maximum_total_sum_of_k_selected_elements (556 bytes)
================================================================================
// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, int k, int mul) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = n - 1; i >= n - k; i--) {
            int m = std::max(1, mul);
            ans += (long long)nums[i] * m;
            mul--;
        }
        return ans;
    }
};


================================================================================
// FILE: 3975_filter_occupied_intervals (1181 bytes)
================================================================================
// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> filterOccupiedIntervals(std::vector<std::vector<int>>& occupiedIntervals, int freeStart, int freeEnd) {
        std::sort(occupiedIntervals.begin(), occupiedIntervals.end(), [](auto& a, auto& b) {
            return a[0] < b[0];
        });
        std::vector<std::vector<int>> busy = {occupiedIntervals[0]};
        for (int i = 1; i < (int)occupiedIntervals.size(); i++) {
            auto& cur = occupiedIntervals[i];
            auto& last = busy.back();
            if (last[1] + 1 < cur[0]) busy.push_back(cur);
            else if (cur[1] > last[1]) last[1] = cur[1];
        }
        std::vector<std::vector<int>> ans;
        for (auto& it : busy) {
            int s = it[0], e = it[1];
            if (e < freeStart || s > freeEnd) ans.push_back({s, e});
            else {
                if (s < freeStart) ans.push_back({s, freeStart - 1});
                if (e > freeEnd) ans.push_back({freeEnd + 1, e});
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 3976_maximum_subarray_sum_after_multiplier (1047 bytes)
================================================================================
// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

#include <algorithm>
#include <array>
#include <climits>
#include <vector>

class Solution {
public:
    long long maxSubarraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        const long long inf = LLONG_MIN / 4;
        std::vector<std::array<long long, 4>> f(n + 1);
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < 4; j++) f[i][j] = inf;
        }
        f[0][0] = 0;
        long long ans = inf;
        for (int i = 1; i <= n; i++) {
            long long x = nums[i - 1];
            f[i][0] = std::max(f[i - 1][0], 0LL) + x;
            f[i][1] = std::max({f[i - 1][0], f[i - 1][1], 0LL}) + x * k;
            f[i][2] = std::max({f[i - 1][0], f[i - 1][2], 0LL}) + x / k;
            f[i][3] = std::max({f[i - 1][1], f[i - 1][2], f[i - 1][3]}) + x;
            ans = std::max({ans, f[i][0], f[i][1], f[i][2], f[i][3]});
        }
        return ans;
    }
};


================================================================================
// FILE: 3977_minimum_time_to_reach_target_with_limited_power (1584 bytes)
================================================================================
// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

#include <cstdint>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<long long> minTimeMaxPower(int n, std::vector<std::vector<int>>& edges, int power,
                                           std::vector<int>& cost, int source, int target) {
        const long long INF = 1LL << 62;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
        }

        std::vector<std::vector<long long>> dist(n, std::vector<long long>(power + 1, INF));
        // state: {d, -p, u} so smaller d first, then larger remaining power (smaller -p)
        using State = std::tuple<long long, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> pq;
        pq.emplace(0, -power, source);
        dist[source][power] = 0;

        while (!pq.empty()) {
            auto [d, negP, u] = pq.top();
            pq.pop();
            int p = -negP;
            if (u == target) {
                return {d, (long long)p};
            }
            if (d > dist[u][p] || p < cost[u]) continue;
            p -= cost[u];
            for (auto [v, t] : g[u]) {
                long long nd = d + t;
                if (nd < dist[v][p]) {
                    dist[v][p] = nd;
                    pq.emplace(nd, -p, v);
                }
            }
        }
        return {-1, -1};
    }
};


================================================================================
// FILE: 3978_unique_middle_element (367 bytes)
================================================================================
// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

#include <vector>

class Solution {
public:
    bool isMiddleElementUnique(std::vector<int>& nums) {
        int mid = nums[nums.size() / 2];
        int cnt = 0;
        for (int x : nums) {
            if (x == mid) cnt++;
        }
        return cnt == 1;
    }
};


================================================================================
// FILE: 3979_maximum_valid_pair_sum (453 bytes)
================================================================================
// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxValidPairSum(std::vector<int>& nums, int k) {
        int ans = 0, x = 0;
        for (int j = k; j < (int)nums.size(); j++) {
            int y = nums[j];
            x = std::max(x, nums[j - k]);
            ans = std::max(ans, x + y);
        }
        return ans;
    }
};


================================================================================
// FILE: 3980_minimum_operations_to_transform_binary_string (1356 bytes)
================================================================================
// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

#include <algorithm>
#include <array>
#include <string>

class Solution {
public:
    int minOperations(std::string s1, std::string s2) {
        const int infinity = 1000000000;
        std::array<int, 2> dp{0, infinity};
        int n = (int)s1.size();
        for (int i = 0; i < n; i++) {
            std::array<int, 2> next{infinity, infinity};
            for (int forcedZero = 0; forcedZero <= 1; forcedZero++) {
                if (dp[forcedZero] == infinity) continue;
                char current = s1[i];
                if (forcedZero == 1) current = '0';

                int direct = dp[forcedZero];
                if (current == '0' && s2[i] == '1') direct++;
                else if (current == '1' && s2[i] == '0') direct = infinity;
                next[0] = std::min(next[0], direct);

                if (i + 1 < n) {
                    int cost = dp[forcedZero] + 1;
                    if (current == '0') cost++;
                    if (s1[i + 1] == '0') cost++;
                    if (s2[i] == '1') cost++;
                    next[1] = std::min(next[1], cost);
                }
            }
            dp = next;
        }
        return dp[0] == infinity ? -1 : dp[0];
    }
};


================================================================================
// FILE: 3981_count_distinct_ways_to_form_target_from_two_strings (2471 bytes)
================================================================================
// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

#include <string>
#include <vector>

class Solution {
public:
    int countWays(std::string word1, std::string word2, std::string target) {
        const int mod = 1000000007;
        int n1 = (int)word1.size();
        int n2 = (int)word2.size();
        int size = (n1 + 1) * (n2 + 1) * 4;
        auto index = [&](int i, int j, int mask) {
            return ((i * (n2 + 1) + j) * 4) + mask;
        };
        std::vector<int> dp(size, 0), next(size, 0);
        dp[index(0, 0, 0)] = 1;
        for (char ch : target) {
            std::fill(next.begin(), next.end(), 0);
            for (int j = 0; j <= n2; j++) {
                int prefix[4] = {0, 0, 0, 0};
                for (int a = 0; a < n1; a++) {
                    for (int mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[index(a, j, mask)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word1[a] == ch) {
                        for (int mask = 0; mask < 4; mask++) {
                            int at = index(a + 1, j, mask | 1);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            for (int i = 0; i <= n1; i++) {
                int prefix[4] = {0, 0, 0, 0};
                for (int b = 0; b < n2; b++) {
                    for (int mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[index(i, b, mask)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word2[b] == ch) {
                        for (int mask = 0; mask < 4; mask++) {
                            int at = index(i, b + 1, mask | 2);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            dp.swap(next);
        }
        int answer = 0;
        for (int i = 0; i <= n1; i++) {
            for (int j = 0; j <= n2; j++) {
                answer += dp[index(i, j, 3)];
                if (answer >= mod) answer -= mod;
            }
        }
        return answer;
    }
};


================================================================================
// FILE: 3982_sum_of_integers_with_maximum_digit_range (717 bytes)
================================================================================
// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxDigitRange(std::vector<int>& nums) {
        int mx = 0, ans = 0;
        for (int x : nums) {
            int a = 10, b = 0;
            for (int y = x; y > 0; y /= 10) {
                int v = y % 10;
                a = std::min(a, v);
                b = std::max(b, v);
            }
            int r = b - a;
            if (mx < r) {
                mx = r;
                ans = x;
            } else if (mx == r) {
                ans += x;
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 3983_subsequence_after_one_replacement (533 bytes)
================================================================================
// LeetCode 3983 - Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/

#include <string>

class Solution {
public:
    bool canMakeSubsequence(std::string s, std::string t) {
        int m = (int)s.size();
        int n = (int)t.size();
        int i0 = 0, i1 = 0, j = 0;
        while (i1 < m && j < n) {
            if (s[i1] == t[j]) i1++;
            if (i1 < i0 + 1) i1 = i0 + 1;
            if (s[i0] == t[j]) i0++;
            j++;
        }
        return i1 == m;
    }
};


================================================================================
// FILE: 3984_divisible_game (1515 bytes)
================================================================================
// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

#include <cstdint>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int divisibleGame(std::vector<int>& nums) {
        std::unordered_set<int> candidates{2};
        for (int value : nums) {
            for (int divisor = 2; divisor * divisor <= value; divisor++) {
                if (value % divisor != 0) continue;
                candidates.insert(divisor);
                candidates.insert(value / divisor);
            }
            if (value > 1) candidates.insert(value);
        }

        long long bestScore = -(1LL << 62);
        int bestK = 0;
        for (int k : candidates) {
            long long ending = 0, score = 0;
            for (int i = 0; i < (int)nums.size(); i++) {
                int value = nums[i];
                long long contribution = -((long long)value);
                if (value % k == 0) contribution = value;
                if (i == 0 || ending + contribution < contribution) ending = contribution;
                else ending += contribution;
                if (i == 0 || ending > score) score = ending;
            }
            if (score > bestScore || (score == bestScore && k < bestK)) {
                bestScore = score;
                bestK = k;
            }
        }

        const long long mod = 1000000007LL;
        long long answer = (bestScore % mod) * bestK % mod;
        if (answer < 0) answer += mod;
        return (int)answer;
    }
};


================================================================================
// FILE: 3985_palindromic_subarray_sum (1989 bytes)
================================================================================
// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

#include <vector>

class Solution {
public:
    long long maxPalindromicSubarraySum(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        std::vector<int> odd(n);
        int left = 0, right = -1;
        for (int i = 0; i < n; i++) {
            int radius = 1;
            if (i <= right) {
                int mirror = left + right - i;
                radius = odd[mirror];
                if (right - i + 1 < radius) radius = right - i + 1;
            }
            while (i - radius >= 0 && i + radius < n && nums[i - radius] == nums[i + radius]) radius++;
            odd[i] = radius;
            if (i + radius - 1 > right) {
                left = i - radius + 1;
                right = i + radius - 1;
            }
        }

        std::vector<int> even(n);
        left = 0;
        right = -1;
        for (int i = 0; i < n; i++) {
            int radius = 0;
            if (i <= right) {
                int mirror = left + right - i + 1;
                radius = even[mirror];
                if (right - i + 1 < radius) radius = right - i + 1;
            }
            while (i - radius - 1 >= 0 && i + radius < n && nums[i - radius - 1] == nums[i + radius]) radius++;
            even[i] = radius;
            if (i + radius - 1 > right) {
                left = i - radius;
                right = i + radius - 1;
            }
        }

        long long answer = 0;
        for (int i = 0; i < n; i++) {
            long long sum = prefix[i + odd[i]] - prefix[i - odd[i] + 1];
            if (sum > answer) answer = sum;
            if (even[i] > 0) {
                sum = prefix[i + even[i]] - prefix[i - even[i]];
                if (sum > answer) answer = sum;
            }
        }
        return answer;
    }
};


================================================================================
// FILE: 3986_number_of_elapsed_seconds_between_two_times (575 bytes)
================================================================================
// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

#include <string>

class Solution {
    static int toSeconds(const std::string& s) {
        int h = (s[0] - '0') * 10 + (s[1] - '0');
        int m = (s[3] - '0') * 10 + (s[4] - '0');
        int sec = (s[6] - '0') * 10 + (s[7] - '0');
        return h * 3600 + m * 60 + sec;
    }

public:
    int secondsBetweenTimes(std::string startTime, std::string endTime) {
        return toSeconds(endTime) - toSeconds(startTime);
    }
};


================================================================================
// FILE: 3987_minimum_total_cost_to_process_all_elements (691 bytes)
================================================================================
// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

#include <vector>

class Solution {
public:
    int minimumCost(std::vector<int>& nums, int k) {
        const long long mod = 1000000007LL;
        long long cnt = 0;
        long long cur = k;
        for (int x0 : nums) {
            long long x = x0;
            long long diff = x - cur;
            if (diff > 0) {
                long long m = (diff + k - 1) / k;
                cur += m * k;
                cnt += m;
            }
            cur -= x;
        }
        cnt %= mod;
        return (int)((cnt + 1) * cnt / 2 % mod);
    }
};


================================================================================
// FILE: 3988_create_grid_with_exactly_k_paths_i (1299 bytes)
================================================================================
// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> createGrid(int m, int n, int k) {
        std::vector<std::vector<std::string>> cands;
        if (k == 1) {
            cands.push_back({"."});
        } else if (k == 2) {
            cands.push_back({"..", ".."});
        } else if (k == 3) {
            cands.push_back({"..", "..", ".."});
            cands.push_back({"...", "..."});
        } else if (k == 4) {
            cands.push_back({"..", "..", "..", ".."});
            cands.push_back({"....", "...."});
            cands.push_back({"..#", "...", "#.."});
        }

        for (auto& pat : cands) {
            int pr = (int)pat.size();
            int pc = (int)pat[0].size();
            if (pr > m || pc > n) continue;
            std::vector<std::string> result(m, std::string(n, '#'));
            for (int i = 0; i < pr; i++) {
                for (int j = 0; j < pc; j++) result[i][j] = pat[i][j];
            }
            for (int i = pr; i < m; i++) result[i][pc - 1] = '.';
            for (int j = pc; j < n; j++) result[m - 1][j] = '.';
            return result;
        }
        return {};
    }
};


================================================================================
// FILE: 3989_maximum_consistent_columns_in_a_grid (973 bytes)
================================================================================
// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int maxConsistentColumns(std::vector<std::vector<int>>& grid, int limit) {
        int m = (int)grid.size();
        int n = (int)grid[0].size();
        std::vector<int> dp(n, 1);
        int ans = 1;
        for (int j = 0; j < n; j++) {
            dp[j] = 1;
            for (int i = 0; i < j; i++) {
                if (dp[i] + 1 <= dp[j]) continue;
                bool ok = true;
                for (int r = 0; r < m; r++) {
                    int d = std::abs(grid[r][j] - grid[r][i]);
                    if (d > limit) {
                        ok = false;
                        break;
                    }
                }
                if (ok) dp[j] = dp[i] + 1;
            }
            if (dp[j] > ans) ans = dp[j];
        }
        return ans;
    }
};


================================================================================
// FILE: 3990_create_grid_with_exactly_k_paths_ii (930 bytes)
================================================================================
// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

#include <string>
#include <vector>

class Solution {
    static int bitWidth(unsigned k) {
        int w = 0;
        while (k) {
            ++w;
            k >>= 1;
        }
        return w;
    }

public:
    std::vector<std::string> createGrid(int k) {
        if (k <= 0) return {};
        int l = bitWidth((unsigned)k);
        int m = 2 * l, n = l + 3;
        std::vector<std::string> result(m, std::string(n, '#'));
        for (int i = 0; i < l; i++) {
            int r = 2 * i;
            result[r][i] = result[r][i + 1] = result[r + 1][i] = result[r + 1][i + 1] = '.';
            if (k & (1 << i)) {
                for (int c = i + 2; c < n; c++) result[r][c] = '.';
            }
        }
        for (int r = 0; r < m; r++) result[r][n - 1] = '.';
        return result;
    }
};


================================================================================
// FILE: 3992_rearrange_string_to_avoid_character_pair (471 bytes)
================================================================================
// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

#include <string>

class Solution {
public:
    std::string rearrangeString(std::string s, char x, char y) {
        (void)x;
        int i = 0;
        for (int j = 0; j < (int)s.size(); j++) {
            if (s[j] == y) {
                std::swap(s[i], s[j]);
                i++;
            }
        }
        return s;
    }
};


================================================================================
// FILE: 3993_maximum_value_of_an_alternating_sequence (314 bytes)
================================================================================
// LeetCode 3993 - Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

class Solution {
public:
    long long maximumValue(int n, int s, int m) {
        if (n == 1) return s;
        return (long long)s + (long long)(n / 2) * (m - 1) + 1;
    }
};


================================================================================
// FILE: 3994_minimum_adjacent_swaps_to_partition_array (642 bytes)
================================================================================
// LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

#include <vector>

class Solution {
public:
    int minAdjacentSwaps(std::vector<int>& nums, int a, int b) {
        const int MOD = 1000000007;
        int result = 0, cnt1 = 0, cnt2 = 0;
        for (int x : nums) {
            if (x < a) {
                result = (result + cnt1 + cnt2) % MOD;
            } else if (x <= b) {
                ++cnt1;
                result = (result + cnt2) % MOD;
            } else {
                ++cnt2;
            }
        }
        return result;
    }
};


================================================================================
// FILE: 3995_minimum_cost_to_convert_string_iii (1585 bytes)
================================================================================
// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

#include <climits>
#include <string>
#include <vector>

class Solution {
public:
    int minCost(std::string source, std::string target, std::vector<std::vector<std::string>>& rules,
                std::vector<int>& costs) {
        int n = (int)source.size();
        if ((int)target.size() != n) return -1;
        std::vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == INT_MAX) continue;
            if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
            for (int j = 0; j < (int)rules.size(); j++) {
                const std::string& p = rules[j][0];
                const std::string& r = rules[j][1];
                int plen = (int)p.size();
                if (i + plen > n) continue;
                int c = costs[j];
                bool ok = true;
                for (int k = 0; k < plen; k++) {
                    if (r[k] != target[i + k]) {
                        ok = false;
                        break;
                    }
                    if (p[k] == '*') ++c;
                    else if (p[k] != source[i + k]) {
                        ok = false;
                        break;
                    }
                }
                if (ok && dp[i] <= INT_MAX - c && dp[i] + c < dp[i + plen]) {
                    dp[i + plen] = dp[i] + c;
                }
            }
        }
        return dp[n] == INT_MAX ? -1 : dp[n];
    }
};


================================================================================
// FILE: 3996_even_number_of_knight_moves (311 bytes)
================================================================================
// LeetCode 3996 - Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/

#include <vector>

class Solution {
public:
    bool canReach(std::vector<int>& start, std::vector<int>& target) {
        return ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2);
    }
};


================================================================================
// FILE: 3997_count_dominant_nodes_in_a_binary_tree (852 bytes)
================================================================================
// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

#include <algorithm>
#include <climits>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int ans = 0;

    int dfs(TreeNode* node) {
        if (!node) return INT_MIN;
        int l = dfs(node->left);
        int r = dfs(node->right);
        int mx = std::max({l, r, node->val});
        if (mx == node->val) ans++;
        return mx;
    }

public:
    int countDominantNodes(TreeNode* root) {
        ans = 0;
        dfs(root);
        return ans;
    }
};


================================================================================
// FILE: 3998_transform_binary_string_using_subsequence_sort (1134 bytes)
================================================================================
// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<bool> transformStr(std::string s, std::vector<std::string>& strs) {
        int n = (int)s.size();
        std::vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + (s[i] == '1' ? 1 : 0);
        std::vector<bool> result(strs.size());
        for (int i = 0; i < (int)strs.size(); i++) {
            int left = 0, right = 0;
            bool ok = true;
            for (int j = 0; j < n; j++) {
                left += (strs[i][j] == '1' ? 1 : 0);
                int add = (strs[i][j] != '0' ? 1 : 0);
                right = right + add;
                if (right > prefix[j + 1]) right = prefix[j + 1];
                if (left > right) {
                    ok = false;
                    break;
                }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right;
        }
        return result;
    }
};


================================================================================
// FILE: 3999_minimum_number_of_string_groups_through_transformations (1713 bytes)
================================================================================
// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
    static int leastRotation(const std::string& s) {
        int n = (int)s.size();
        int i = 0, j = 1, k = 0;
        while (i < n && j < n && k < n) {
            char a = s[(i + k) % n];
            char b = s[(j + k) % n];
            if (a == b) ++k;
            else {
                if (a > b) i += k + 1;
                else j += k + 1;
                if (i == j) ++j;
                k = 0;
            }
        }
        return i < j ? i : j;
    }

    static std::string canonicalRotate(std::string s) {
        int n = (int)s.size();
        if (n <= 1) return s;
        int r = leastRotation(s);
        if (r == 0) return s;
        return s.substr(r) + s.substr(0, r);
    }

public:
    int minimumGroups(std::vector<std::string>& words) {
        std::vector<std::string> keys;
        keys.reserve(words.size());
        for (const std::string& w : words) {
            int n = (int)w.size();
            std::string even, odd;
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0) even.push_back(w[i]);
                else odd.push_back(w[i]);
            }
            even = canonicalRotate(even);
            odd = canonicalRotate(odd);
            keys.push_back(even + "#" + odd);
        }
        std::sort(keys.begin(), keys.end());
        int groups = 0;
        for (int i = 0; i < (int)keys.size(); i++) {
            if (i == 0 || keys[i] != keys[i - 1]) ++groups;
        }
        return groups;
    }
};


================================================================================
// FILE: 4000_largest_integer_with_given_digit_sum (411 bytes)
================================================================================
// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

class Solution {
public:
    int largestInteger(int n, int s) {
        if (n * 9 < s) return -1;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x = s < 9 ? s : 9;
            ans = ans * 10 + x;
            s -= x;
        }
        return ans;
    }
};


================================================================================
// FILE: 4001_aggregate_two_time_series (1155 bytes)
================================================================================
// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> aggregateTimeSeries(std::vector<std::vector<int>>& series1,
                                                      std::vector<std::vector<int>>& series2) {
        int m = (int)series1.size(), n = (int)series2.size();
        int i = 0, j = 0;
        std::vector<std::vector<int>> ans;

        while (i < m && j < n) {
            int t1 = series1[i][0], v1 = series1[i][1];
            int t2 = series2[j][0], v2 = series2[j][1];
            if (t1 == t2) {
                ans.push_back({t1, v1 + v2});
                i++;
                j++;
            } else if (t1 < t2) {
                ans.push_back({t1, v1 + v2});
                i++;
            } else {
                ans.push_back({t2, v1 + v2});
                j++;
            }
        }
        while (i < m) {
            ans.push_back(series1[i]);
            i++;
        }
        while (j < n) {
            ans.push_back(series2[j]);
            j++;
        }
        return ans;
    }
};


================================================================================
// FILE: 4002_count_valid_sequences (1310 bytes)
================================================================================
// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

#include <cstdint>

class Solution {
    static constexpr int MX = 500001;
    static constexpr int64_t MOD = 1000000007LL;

    static int64_t f[MX];
    static int64_t g[MX];
    static bool inited;

    static int64_t modPow(int64_t a, int64_t b) {
        int64_t res = 1;
        a %= MOD;
        while (b > 0) {
            if (b & 1) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    static void ensureInit() {
        if (inited) return;
        inited = true;
        f[0] = 1;
        g[0] = 1;
        for (int i = 1; i < MX; i++) {
            f[i] = f[i - 1] * (int64_t)i % MOD;
            g[i] = modPow(f[i], MOD - 2);
        }
    }

    static int64_t comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        return f[n] * g[k] % MOD * g[n - k] % MOD;
    }

public:
    int countValidSequences(int n, int k) {
        ensureInit();
        int64_t ans = comb(n - 1, k - 1);
        if ((n + k) % 2 == 0) {
            ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD;
        }
        return (int)ans;
    }
};

int64_t Solution::f[Solution::MX];
int64_t Solution::g[Solution::MX];
bool Solution::inited = false;


================================================================================
// FILE: 4003_minimum_cost_path_with_alternating_directions_iii (1708 bytes)
================================================================================
// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

#include <cstdint>
#include <functional>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
    static constexpr int64_t INF = (int64_t)1 << 60;

public:
    long long minCost(int m, int n, std::vector<std::vector<int>>& penalty) {
        std::vector<std::vector<std::vector<int64_t>>> dist(
            m, std::vector<std::vector<int64_t>>(n, std::vector<int64_t>(2, INF)));
        dist[0][0][1] = 1;

        using Tup = std::tuple<int64_t, int, int, int>;
        std::priority_queue<Tup, std::vector<Tup>, std::greater<Tup>> pq;
        pq.emplace(1, 0, 0, 1);

        int dirs[4][2] = {{-1, 0}, {0, 1}, {0, -1}, {1, 0}};

        while (!pq.empty()) {
            auto [d, i, j, k] = pq.top();
            pq.pop();
            if (i == m - 1 && j == n - 1) return d;
            if (d > dist[i][j][k]) continue;

            int p = penalty[i][j];
            int64_t nd = d + (int64_t)p;
            if (nd < dist[i][j][k ^ 1]) {
                dist[i][j][k ^ 1] = nd;
                pq.emplace(nd, i, j, k ^ 1);
            }
            for (int idx = 0; idx < 4; idx++) {
                int x = i + dirs[idx][0], y = j + dirs[idx][1];
                if (0 <= x && x < m && 0 <= y && y < n) {
                    nd = d + (int64_t)((x + 1) * (y + 1) + (((idx & 1) ^ k) * p));
                    if (nd < dist[x][y][k ^ 1]) {
                        dist[x][y][k ^ 1] = nd;
                        pq.emplace(nd, x, y, k ^ 1);
                    }
                }
            }
        }
        return -1;
    }
};


================================================================================
// FILE: 4004_minimum_moves_to_balance_circular_array_ii (3482 bytes)
================================================================================
// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

#include <cstdint>
#include <queue>
#include <vector>

class Solution {
    static constexpr int INF = 1000000000;

    struct Edge {
        int to, cap, cost, rev;
    };

    struct MinCostMaxFlow {
        int n;
        std::vector<std::vector<Edge>> graph;

        explicit MinCostMaxFlow(int n_) : n(n_), graph(n_) {}

        void addEdge(int u, int v, int cap, int cost) {
            graph[u].push_back({v, cap, cost, (int)graph[v].size()});
            graph[v].push_back({u, 0, -cost, (int)graph[u].size() - 1});
        }

        int64_t minCostFlow(int source, int sink, int maxFlow) {
            int64_t totalCost = 0;
            int currentFlow = 0;

            while (currentFlow < maxFlow) {
                std::vector<int> dist(n, INF), parentNode(n, -1), parentEdge(n, -1);
                std::vector<char> inQueue(n, 0);
                std::queue<int> q;
                q.push(source);
                dist[source] = 0;
                inQueue[source] = 1;

                while (!q.empty()) {
                    int u = q.front();
                    q.pop();
                    inQueue[u] = 0;
                    for (int i = 0; i < (int)graph[u].size(); i++) {
                        Edge& e = graph[u][i];
                        if (e.cap > 0 && dist[e.to] > dist[u] + e.cost) {
                            dist[e.to] = dist[u] + e.cost;
                            parentNode[e.to] = u;
                            parentEdge[e.to] = i;
                            if (!inQueue[e.to]) {
                                inQueue[e.to] = 1;
                                q.push(e.to);
                            }
                        }
                    }
                }

                if (dist[sink] == INF) return -1;

                int pushFlow = maxFlow - currentFlow;
                for (int cur = sink; cur != source; cur = parentNode[cur]) {
                    Edge& e = graph[parentNode[cur]][parentEdge[cur]];
                    if (e.cap < pushFlow) pushFlow = e.cap;
                }
                for (int cur = sink; cur != source; cur = parentNode[cur]) {
                    int p = parentNode[cur];
                    int idx = parentEdge[cur];
                    int rev = graph[p][idx].rev;
                    graph[p][idx].cap -= pushFlow;
                    graph[cur][rev].cap += pushFlow;
                }
                currentFlow += pushFlow;
                totalCost += (int64_t)pushFlow * dist[sink];
            }
            return totalCost;
        }
    };

public:
    long long minMoves(std::vector<int>& balance) {
        int totalBalance = 0, totalDeficit = 0;
        for (int x : balance) {
            totalBalance += x;
            if (x < 0) totalDeficit += -x;
        }
        if (totalBalance < 0) return -1;
        if (totalDeficit == 0) return 0;

        int n = (int)balance.size();
        int source = n, sink = n + 1;
        MinCostMaxFlow mcmf(n + 2);

        for (int i = 0; i < n; i++) {
            int x = balance[i];
            if (x > 0) mcmf.addEdge(source, i, x, 0);
            else if (x < 0) mcmf.addEdge(i, sink, -x, 0);
            mcmf.addEdge(i, (i + 1) % n, INF, 1);
            mcmf.addEdge(i, (i - 1 + n) % n, INF, 1);
        }
        return mcmf.minCostFlow(source, sink, totalDeficit);
    }
};


================================================================================
// FILE: 4005_minimum_operations_to_make_array_equal_iii (1236 bytes)
================================================================================
// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

#include <algorithm>
#include <climits>
#include <numeric>
#include <set>
#include <vector>

class Solution {
    static int cost(int x, int t) {
        if (x == t) return 0;
        if (x % t == 0 || t % x == 0) return 1;
        return 2;
    }

public:
    int minOperations(std::vector<int>& nums) {
        int n = (int)nums.size();
        if (n <= 1) return 0;

        int g = nums[0], mn = nums[0];
        for (int i = 1; i < n; i++) {
            g = std::gcd(g, nums[i]);
            mn = std::min(mn, nums[i]);
        }

        std::set<int> cands;
        for (int x : nums) cands.insert(x);
        for (int d = 1; (long long)d * d <= mn; d++) {
            if (mn % d == 0) {
                cands.insert(d);
                cands.insert(mn / d);
            }
        }
        cands.insert(g);

        int ans = INT_MAX;
        for (int t : cands) {
            int sum = 0;
            for (int x : nums) {
                sum += cost(x, t);
                if (sum >= ans) break;
            }
            ans = std::min(ans, sum);
        }
        return ans;
    }
};


================================================================================
// FILE: 4006_count_valid_prefixes (373 bytes)
================================================================================
// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

#include <string>

class Solution {
public:
    int countValidPrefixes(std::string s) {
        int ans = 0, t = 0;
        for (char c : s) {
            if (c == '1') t++;
            else t--;
            if (t >= -1 && t <= 1) ans++;
        }
        return ans;
    }
};


================================================================================
// FILE: 4007_widest_possible_fence (831 bytes)
================================================================================
// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maximumWidth(std::vector<int>& planks) {
        std::unordered_map<int, int> cnt;
        for (int x : planks) cnt[x]++;

        std::unordered_map<int, int> t;
        int ans = 0;

        for (auto& [x, v1] : cnt) {
            t[x] += v1;
            ans = std::max(ans, t[x]);

            t[x * 2] += v1 / 2;
            ans = std::max(ans, t[x * 2]);

            for (auto& [y, v2] : cnt) {
                if (y > x) {
                    int key = x + y;
                    t[key] += std::min(v1, v2);
                    ans = std::max(ans, t[key]);
                }
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 4008_minimum_initial_strength_to_defeat_all_monsters (1110 bytes)
================================================================================
// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long minInitialStrength(std::vector<int>& monsters, std::vector<std::vector<int>>& boosts) {
        int n = (int)monsters.size();
        std::vector<int64_t> d(n + 1, 0);
        for (auto& b : boosts) {
            d[b[0]] += (int64_t)b[2];
            d[b[1] + 1] -= (int64_t)b[2];
        }

        auto check = [&](int64_t v) -> bool {
            int64_t bonus = 0;
            for (int i = 0; i < n; i++) {
                bonus += d[i];
                if (v + bonus < (int64_t)monsters[i]) return false;
                v -= (int64_t)monsters[i];
                if (v < 0) v = 0;
            }
            return true;
        };

        int64_t left = 0, right = 1000000000000000LL;
        while (left < right) {
            int64_t mid = (left + right) / 2;
            if (check(mid)) right = mid;
            else left = mid + 1;
        }
        return left;
    }
};


================================================================================
// FILE: 4009_minimum_possible_maximum_waiting_time (2893 bytes)
================================================================================
// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
    std::vector<int>* dem;
    int n;
    int W;
    int bestServe;
    std::unordered_map<long long, int> memo;

    static long long packKey(int i, int f0, int f1, int d0, int d1) {
        return (((((long long)i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1);
    }

    int maxServe(int i, int f0, int f1, int d0, int d1) {
        if (i == n) return i;
        long long key = packKey(i, f0, f1, d0, d1);
        auto it = memo.find(key);
        if (it != memo.end()) return it->second;

        int need = (*dem)[i];
        bool can0 = f0 >= need;
        bool can1 = f1 >= need;
        int best = i;
        if (!can0 && !can1) {
            memo[key] = best;
            return best;
        }
        if (can0) {
            int nd1 = d1 > d0 ? d1 - d0 : 0;
            best = std::max(best, maxServe(i + 1, f0 - need, f1, need, nd1));
        }
        if (can1) {
            int nd0 = d0 > d1 ? d0 - d1 : 0;
            best = std::max(best, maxServe(i + 1, f0, f1 - need, nd0, need));
        }
        memo[key] = best;
        return best;
    }

    bool canWithW(int i, int f0, int f1, int d0, int d1) {
        if (i >= bestServe) return true;
        if (i == n) return true;
        long long key = packKey(i, f0, f1, d0, d1);
        auto it = memo.find(key);
        if (it != memo.end()) return it->second == 2;

        int need = (*dem)[i];
        bool can0 = f0 >= need;
        bool can1 = f1 >= need;
        bool ok = false;
        if (!can0 && !can1) {
            memo[key] = 1;
            return false;
        }
        if (can0 && d0 <= W) {
            int nd1 = d1 > d0 ? d1 - d0 : 0;
            if (canWithW(i + 1, f0 - need, f1, need, nd1)) ok = true;
        }
        if (!ok && can1 && d1 <= W) {
            int nd0 = d0 > d1 ? d0 - d1 : 0;
            if (canWithW(i + 1, f0, f1 - need, nd0, need)) ok = true;
        }
        memo[key] = ok ? 2 : 1;
        return ok;
    }

public:
    int minMaxWaitingTime(std::vector<int>& demand, std::vector<int>& fuel) {
        dem = &demand;
        n = (int)demand.size();
        int f0 = fuel[0], f1 = fuel[1];

        if (f0 < demand[0] && f1 < demand[0]) return -1;

        memo.clear();
        bestServe = maxServe(0, f0, f1, 0, 0);
        if (bestServe == 0) return -1;

        int lo = 0, hi = 0;
        for (int x : demand) hi += x;

        int ans = hi;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            W = mid;
            memo.clear();
            if (canWithW(0, f0, f1, 0, 0)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 4010_maximize_pair_strength_using_gcd (664 bytes)
================================================================================
// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

#include <algorithm>
#include <cstdint>
#include <numeric>
#include <vector>

class Solution {
public:
    long long maxPairStrength(std::vector<int>& nums) {
        int n = (int)nums.size();
        int64_t ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int64_t g = std::gcd((int64_t)nums[i], (int64_t)nums[j]);
                int64_t x = (int64_t)nums[i] * (int64_t)nums[j] / (g * g);
                ans = std::max(ans, x);
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 4011_count_subarrays_with_even_odd_ratio_i (682 bytes)
================================================================================
// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

#include <cstdint>
#include <vector>

class Solution {
public:
    int countRatioSubarrays(std::vector<int>& nums, int a, int b) {
        int n = (int)nums.size();
        int64_t ans = 0;
        for (int i = 0; i < n; i++) {
            int y = 0;
            for (int j = i; j < n; j++) {
                y += nums[j] % 2;
                int x = j - i + 1 - y;
                if (y > 0 && (int64_t)x * (int64_t)b <= (int64_t)y * (int64_t)a) {
                    ans++;
                }
            }
        }
        return (int)ans;
    }
};


================================================================================
// FILE: 4012_count_of_unfinished_tasks_after_each_shift (1380 bytes)
================================================================================
// LeetCode 4012 - Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<int> countTasks(std::vector<int>& tasks, std::vector<int>& shifts) {
        int m = (int)tasks.size(), n = (int)shifts.size();
        std::vector<int64_t> s(m + 1, 0);
        for (int i = 0; i < m; i++) s[i + 1] = s[i] + (int64_t)tasks[i];

        std::vector<int> ans(n, 0);
        int i = 0;
        int64_t cur = 0;

        for (int j = 0; j < n; j++) {
            if ((int64_t)shifts[j] < (int64_t)tasks[i] - cur) {
                cur += (int64_t)shifts[j];
                ans[j] = m - i;
            } else {
                int64_t t = (int64_t)shifts[j] - ((int64_t)tasks[i] - cur);
                if (t >= s[m] - s[i + 1]) {
                    i = 0;
                    cur = 0;
                } else {
                    int l = i + 1, r = m;
                    while (l < r) {
                        int mid = (l + r) >> 1;
                        if (t < s[mid + 1] - s[i + 1]) r = mid;
                        else l = mid + 1;
                    }
                    cur = t - (s[l] - s[i + 1]);
                    i = l;
                    ans[j] = m - i;
                }
            }
        }
        return ans;
    }
};


================================================================================
// FILE: 4013_count_subarrays_with_even_odd_ratio_ii (1326 bytes)
================================================================================
// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

#include <algorithm>
#include <cstdint>
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
            int sum = 0;
            for (; x > 0; x -= x & -x) sum += c[x];
            return sum;
        }
    };

public:
    long long countRatioSubarrays(std::vector<int>& nums, int a, int b) {
        int n = (int)nums.size();
        std::vector<int64_t> s(n + 1, 0);
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 1) s[i + 1] = s[i] + (int64_t)a;
            else s[i + 1] = s[i] - (int64_t)b;
        }

        std::vector<int64_t> st = s;
        std::sort(st.begin(), st.end());
        st.erase(std::unique(st.begin(), st.end()), st.end());

        BIT bit((int)st.size() + 1);
        int64_t ans = 0;
        for (int64_t v : s) {
            int x = (int)(std::lower_bound(st.begin(), st.end(), v) - st.begin()) + 1;
            ans += (int64_t)bit.query(x);
            bit.update(x, 1);
        }
        return ans;
    }
};
