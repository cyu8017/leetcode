================================================================================
FOLDER: 3820_pythagorean_distance_nodes_in_a_tree
// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

#include <algorithm>
#include <cstdint>
#include <queue>
#include <vector>

class Solution {
public:
    int specialNodes(int n, std::vector<std::vector<int>>& edges, int x, int y, int z) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        const int INF = 1e9;
        auto bfs = [&](int start) {
            std::vector<int> dist(n, INF);
            std::queue<int> q;
            dist[start] = 0;
            q.push(start);
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : g[u]) {
                    if (dist[v] > dist[u] + 1) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            return dist;
        };
        auto d1 = bfs(x), d2 = bfs(y), d3 = bfs(z);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int a[3] = {d1[i], d2[i], d3[i]};
            std::sort(a, a + 3);
            int64_t x0 = a[0], x1 = a[1], x2 = a[2];
            if (x0 * x0 + x1 * x1 == x2 * x2) ans++;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3821_find_nth_smallest_integer_with_k_one_bits
// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

#include <cstdint>

class Solution {
    static constexpr int MX = 50;
    static int64_t C[MX][MX + 1];
    static bool inited;

    static void init() {
        if (inited) return;
        for (int i = 0; i < MX; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
        inited = true;
    }

public:
    long long nthSmallest(long long n, int k) {
        init();
        int64_t ans = 0;
        for (int i = 49; i >= 0; i--) {
            if (n > C[i][k]) {
                n -= C[i][k];
                ans |= 1LL << i;
                k--;
                if (k == 0) break;
            }
        }
        return ans;
    }
};

int64_t Solution::C[Solution::MX][Solution::MX + 1];
bool Solution::inited = false;


================================================================================
FOLDER: 3822_design_order_management_system
// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

class OrderManagementSystem {
    struct Key {
        std::string orderType;
        int price;
        bool operator==(const Key& o) const {
            return orderType == o.orderType && price == o.price;
        }
    };
    struct KeyHash {
        size_t operator()(const Key& k) const {
            return std::hash<std::string>()(k.orderType) ^ (std::hash<int>()(k.price) << 1);
        }
    };
    std::unordered_map<int, std::string> orderTypeMap;
    std::unordered_map<int, int> priceMap;
    std::unordered_map<Key, std::vector<int>, KeyHash> t;

public:
    OrderManagementSystem() {}

    void addOrder(int orderId, std::string orderType, int price) {
        orderTypeMap[orderId] = orderType;
        priceMap[orderId] = price;
        t[{orderType, price}].push_back(orderId);
    }

    void modifyOrder(int orderId, int newPrice) {
        std::string orderType = orderTypeMap[orderId];
        int oldPrice = priceMap[orderId];
        priceMap[orderId] = newPrice;
        Key oldKey{orderType, oldPrice};
        auto& oldList = t[oldKey];
        for (int i = 0; i < (int)oldList.size(); i++) {
            if (oldList[i] == orderId) {
                oldList.erase(oldList.begin() + i);
                break;
            }
        }
        t[{orderType, newPrice}].push_back(orderId);
    }

    void cancelOrder(int orderId) {
        std::string orderType = orderTypeMap[orderId];
        int price = priceMap[orderId];
        orderTypeMap.erase(orderId);
        priceMap.erase(orderId);
        Key key{orderType, price};
        auto& list = t[key];
        for (int i = 0; i < (int)list.size(); i++) {
            if (list[i] == orderId) {
                list.erase(list.begin() + i);
                break;
            }
        }
    }

    std::vector<int> getOrdersAtPrice(std::string orderType, int price) {
        return t[{orderType, price}];
    }
};


================================================================================
FOLDER: 3823_reverse_letters_then_special_characters_in_a_string
// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    std::string reverseByType(std::string s) {
        std::vector<char> a, b;
        for (char c : s) {
            if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) a.push_back(c);
            else b.push_back(c);
        }
        int j = (int)a.size(), k = (int)b.size();
        for (int i = 0; i < (int)s.size(); i++) {
            if ((s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= 'a' && s[i] <= 'z')) s[i] = a[--j];
            else s[i] = b[--k];
        }
        return s;
    }
};


================================================================================
FOLDER: 3824_minimum_k_to_reduce_array_within_limit
// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

#include <vector>

class Solution {
public:
    int minimumK(std::vector<int>& nums) {
        auto check = [&](int k) {
            long long t = 0;
            for (int x : nums) t += (x + k - 1) / k;
            return t <= 1LL * k * k;
        };
        int lo = 1, hi = 100000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (check(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};


================================================================================
FOLDER: 3825_longest_strictly_increasing_subsequence_with_non_zero_bitwise_and
// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

#include <algorithm>
#include <vector>

class Solution {
    static int bitLen(unsigned x) {
        return x == 0 ? 0 : 32 - __builtin_clz(x);
    }

    static int lis(const std::vector<int>& arr) {
        std::vector<int> g;
        for (int x : arr) {
            auto it = std::lower_bound(g.begin(), g.end(), x);
            if (it == g.end()) g.push_back(x);
            else *it = x;
        }
        return (int)g.size();
    }

public:
    int longestSubsequence(std::vector<int>& nums) {
        int ans = 0;
        int mx = *std::max_element(nums.begin(), nums.end());
        int m = bitLen((unsigned)mx);
        for (int i = 0; i < m; i++) {
            std::vector<int> arr;
            for (int x : nums) {
                if ((x >> i) & 1) arr.push_back(x);
            }
            ans = std::max(ans, lis(arr));
        }
        return ans;
    }
};


================================================================================
FOLDER: 3826_minimum_partition_score
// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

#include <algorithm>
#include <cstdint>
#include <functional>
#include <vector>

class Solution {
public:
    long long minPartitionScore(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int64_t> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        auto value = [&](int left, int right) {
            int64_t sum = prefix[right] - prefix[left];
            return sum * (sum + 1) / 2;
        };
        const int64_t INF = 1LL << 62;
        std::vector<int64_t> previous(n + 1, INF);
        previous[0] = 0;
        for (int parts = 1; parts <= k; parts++) {
            std::vector<int64_t> current(n + 1, INF);
            std::function<void(int, int, int, int)> compute = [&](int lo, int hi, int optLo, int optHi) {
                if (lo > hi) return;
                int mid = (lo + hi) / 2;
                int bestIndex = -1;
                int end = std::min(optHi, mid - 1);
                for (int split = optLo; split <= end; split++) {
                    if (previous[split] == INF) continue;
                    int64_t candidate = previous[split] + value(split, mid);
                    if (candidate < current[mid]) {
                        current[mid] = candidate;
                        bestIndex = split;
                    }
                }
                if (bestIndex == -1) bestIndex = optLo;
                compute(lo, mid - 1, optLo, bestIndex);
                compute(mid + 1, hi, bestIndex, optHi);
            };
            compute(parts, n, parts - 1, n - 1);
            previous = std::move(current);
        }
        return previous[n];
    }
};


================================================================================
FOLDER: 3827_count_monobit_integers
// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

class Solution {
public:
    int countMonobit(int n) {
        int ans = 1;
        for (int i = 1, x = 1; x <= n; i++) {
            ans++;
            x += (1 << i);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3828_final_element_after_subarray_deletions
// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

#include <algorithm>
#include <vector>

class Solution {
public:
    int finalElement(std::vector<int>& nums) {
        return std::max(nums.front(), nums.back());
    }
};


================================================================================
FOLDER: 3829_design_ride_sharing_system
// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

#include <map>
#include <unordered_map>
#include <vector>

class RideSharingSystem {
    int t = 0;
    std::map<int, int> riders;
    std::map<int, int> drivers;
    std::unordered_map<int, int> d;

public:
    RideSharingSystem() {}

    void addRider(int riderId) {
        d[riderId] = t;
        riders[t] = riderId;
        t++;
    }

    void addDriver(int driverId) {
        drivers[t] = driverId;
        t++;
    }

    std::vector<int> matchDriverWithRider() {
        if (riders.empty() || drivers.empty()) return {-1, -1};
        auto dit = drivers.begin();
        auto rit = riders.begin();
        int driverId = dit->second, riderId = rit->second;
        drivers.erase(dit);
        riders.erase(rit);
        return {driverId, riderId};
    }

    void cancelRider(int riderId) {
        auto it = d.find(riderId);
        if (it == d.end()) return;
        riders.erase(it->second);
    }
};


================================================================================
FOLDER: 3830_longest_alternating_subarray_after_removing_at_most_one_element
// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestAlternating(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> l1(n, 1), l2(n, 1), r1(n, 1), r2(n, 1);
        int ans = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i - 1] < nums[i]) l1[i] = l2[i - 1] + 1;
            else if (nums[i - 1] > nums[i]) l2[i] = l1[i - 1] + 1;
            ans = std::max({ans, l1[i], l2[i]});
        }
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i + 1] > nums[i]) r1[i] = r2[i + 1] + 1;
            else if (nums[i + 1] < nums[i]) r2[i] = r1[i + 1] + 1;
        }
        for (int i = 1; i < n - 1; i++) {
            if (nums[i - 1] < nums[i + 1]) ans = std::max(ans, l2[i - 1] + r2[i + 1]);
            else if (nums[i - 1] > nums[i + 1]) ans = std::max(ans, l1[i - 1] + r1[i + 1]);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3831_median_of_a_binary_search_tree_level
// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

#include <functional>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int levelMedian(TreeNode* root, int level) {
        std::vector<int> nums;
        std::function<void(TreeNode*, int)> dfs = [&](TreeNode* node, int i) {
            if (!node) return;
            dfs(node->left, i + 1);
            if (i == level) nums.push_back(node->val);
            dfs(node->right, i + 1);
        };
        dfs(root, 0);
        if (nums.empty()) return -1;
        return nums[nums.size() / 2];
    }
};


================================================================================
FOLDER: 3833_count_dominant_indices
// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

#include <vector>

class Solution {
public:
    int dominantIndices(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0, suf = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] * (n - i - 1) > suf) ans++;
            suf += nums[i];
        }
        return ans;
    }
};


================================================================================
FOLDER: 3834_merge_adjacent_equal_elements
// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<long long> mergeAdjacent(std::vector<int>& nums) {
        std::vector<int64_t> stk;
        for (int x : nums) {
            stk.push_back(x);
            while (stk.size() > 1 && stk.back() == stk[stk.size() - 2]) {
                int64_t a = stk.back();
                stk.pop_back();
                int64_t b = stk.back();
                stk.pop_back();
                stk.push_back(a + b);
            }
        }
        return std::vector<long long>(stk.begin(), stk.end());
    }
};


================================================================================
FOLDER: 3835_count_subarrays_with_cost_less_than_or_equal_to_k
// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

#include <cstdint>
#include <deque>
#include <vector>

class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, long long k) {
        int64_t ans = 0;
        std::deque<int> q1, q2;
        int l = 0;
        for (int r = 0; r < (int)nums.size(); r++) {
            int x = nums[r];
            while (!q1.empty() && nums[q1.back()] <= x) q1.pop_back();
            while (!q2.empty() && nums[q2.back()] >= x) q2.pop_back();
            q1.push_back(r);
            q2.push_back(r);
            while (l < r && (int64_t)(nums[q1.front()] - nums[q2.front()]) * (r - l + 1) > k) {
                l++;
                if (q1.front() < l) q1.pop_front();
                if (q2.front() < l) q2.pop_front();
            }
            ans += r - l + 1;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3836_maximum_score_using_exactly_k_pairs
// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

#include <algorithm>
#include <cstdint>
#include <limits>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& nums1, std::vector<int>& nums2, int K) {
        int n = (int)nums1.size(), m = (int)nums2.size();
        const int64_t NEG = std::numeric_limits<int64_t>::min() / 4;
        std::vector<std::vector<std::vector<int64_t>>> f(
            n + 1, std::vector<std::vector<int64_t>>(m + 1, std::vector<int64_t>(K + 1, NEG)));
        f[0][0][0] = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= K; k++) {
                    if (i > 0) f[i][j][k] = std::max(f[i][j][k], f[i - 1][j][k]);
                    if (j > 0) f[i][j][k] = std::max(f[i][j][k], f[i][j - 1][k]);
                    if (i > 0 && j > 0 && k > 0) {
                        f[i][j][k] = std::max(f[i][j][k],
                            f[i - 1][j - 1][k - 1] + (int64_t)nums1[i - 1] * nums2[j - 1]);
                    }
                }
            }
        }
        return f[n][m][K];
    }
};


================================================================================
FOLDER: 3837_delayed_count_of_equal_elements
// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> delayedCount(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::unordered_map<int, int> cnt;
        std::vector<int> ans(n, 0);
        for (int i = n - k - 2; i >= 0; i--) {
            cnt[nums[i + k + 1]]++;
            ans[i] = cnt[nums[i]];
        }
        return ans;
    }
};


================================================================================
FOLDER: 3838_weighted_word_mapping
// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

#include <string>
#include <vector>

class Solution {
public:
    std::string mapWordWeights(std::vector<std::string>& words, std::vector<int>& weights) {
        std::string ans;
        ans.reserve(words.size());
        for (auto& w : words) {
            int s = 0;
            for (char c : w) s = (s + weights[c - 'a']) % 26;
            ans.push_back(char('a' + (25 - s)));
        }
        return ans;
    }
};


================================================================================
FOLDER: 3839_number_of_prefix_connected_groups
// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int prefixConnected(std::vector<std::string>& words, int k) {
        std::unordered_map<std::string, int> cnt;
        for (auto& w : words) {
            if ((int)w.size() >= k) cnt[w.substr(0, k)]++;
        }
        int ans = 0;
        for (auto& [_, v] : cnt) if (v > 1) ans++;
        return ans;
    }
};


================================================================================
FOLDER: 3840_house_robber_v
// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long rob(std::vector<int>& nums, std::vector<int>& colors) {
        int n = (int)nums.size();
        int64_t f = 0, g = nums[0];
        for (int i = 1; i < n; i++) {
            if (colors[i - 1] == colors[i]) {
                int64_t nf = std::max(f, g);
                g = f + nums[i];
                f = nf;
            } else {
                int64_t nf = std::max(f, g);
                g = nf + nums[i];
                f = nf;
            }
        }
        return std::max(f, g);
    }
};


================================================================================
FOLDER: 3841_palindromic_path_queries_in_a_tree
// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<bool> palindromicPathQueries(int n, std::vector<std::vector<int>>& edges,
                                             std::string s, std::vector<std::string>& queries) {
        std::vector<std::vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        std::vector<int> parent(n, -2), depth(n, 0);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    depth[v] = depth[u] + 1;
                    order.push_back(v);
                }
            }
        }
        std::vector<int> size(n), heavy(n, -1);
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            size[u] = 1;
            for (int v : graph[u]) {
                if (parent[v] == u) {
                    size[u] += size[v];
                    if (heavy[u] == -1 || size[v] > size[heavy[u]]) heavy[u] = v;
                }
            }
        }
        std::vector<int> head(n), position(n);
        struct Chain { int node, h; };
        std::vector<Chain> stack = {{0, 0}};
        int nextPosition = 0;
        while (!stack.empty()) {
            Chain chain = stack.back();
            stack.pop_back();
            for (int u = chain.node; u != -1; u = heavy[u]) {
                head[u] = chain.h;
                position[u] = nextPosition++;
                for (int v : graph[u]) {
                    if (parent[v] == u && v != heavy[u]) stack.push_back({v, v});
                }
            }
        }
        std::vector<int> bit(n + 1, 0);
        auto update = [&](int index, int value) {
            for (index++; index <= n; index += index & -index) bit[index] ^= value;
        };
        auto prefix = [&](int index) {
            int result = 0;
            for (; index > 0; index -= index & -index) result ^= bit[index];
            return result;
        };
        auto pathMask = [&](int u, int v) {
            int result = 0;
            while (head[u] != head[v]) {
                if (depth[head[u]] < depth[head[v]]) std::swap(u, v);
                result ^= prefix(position[u] + 1) ^ prefix(position[head[u]]);
                u = parent[head[u]];
            }
            if (position[u] > position[v]) std::swap(u, v);
            return result ^ prefix(position[v] + 1) ^ prefix(position[u]);
        };
        std::string current = s;
        for (int node = 0; node < n; node++) update(position[node], 1 << (current[node] - 'a'));
        std::vector<bool> answer;
        for (auto& query : queries) {
            std::istringstream iss(query);
            std::string op;
            int node;
            iss >> op >> node;
            if (op == "update") {
                std::string nc;
                iss >> nc;
                char newCharacter = nc[0];
                int delta = (1 << (current[node] - 'a')) ^ (1 << (newCharacter - 'a'));
                update(position[node], delta);
                current[node] = newCharacter;
            } else {
                int other;
                iss >> other;
                int mask = pathMask(node, other);
                answer.push_back((mask & (mask - 1)) == 0);
            }
        }
        return answer;
    }
};


================================================================================
FOLDER: 3842_toggle_light_bulbs
// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

#include <vector>

class Solution {
public:
    std::vector<int> toggleLightBulbs(std::vector<int>& bulbs) {
        int st[101] = {};
        for (int x : bulbs) st[x] ^= 1;
        std::vector<int> ans;
        for (int i = 0; i < 101; i++) if (st[i] == 1) ans.push_back(i);
        return ans;
    }
};


================================================================================
FOLDER: 3843_first_element_with_unique_frequency
// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int firstUniqueFreq(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        std::unordered_map<int, int> freq;
        for (auto& [_, v] : cnt) freq[v]++;
        for (int x : nums) {
            if (freq[cnt[x]] == 1) return x;
        }
        return -1;
    }
};


================================================================================
FOLDER: 3844_longest_almost_palindromic_substring
// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

#include <algorithm>
#include <string>

class Solution {
public:
    int almostPalindromic(std::string s) {
        int n = (int)s.size();
        auto f = [&](int l, int r) {
            while (l >= 0 && r < n && s[l] == s[r]) {
                l--;
                r++;
            }
            int l1 = l - 1, r1 = r, l2 = l, r2 = r + 1;
            while (l1 >= 0 && r1 < n && s[l1] == s[r1]) {
                l1--;
                r1++;
            }
            while (l2 >= 0 && r2 < n && s[l2] == s[r2]) {
                l2--;
                r2++;
            }
            return std::min(n, std::max(r1 - l1 - 1, r2 - l2 - 1));
        };
        int ans = 0;
        for (int i = 0; i < n; i++) ans = std::max({ans, f(i, i), f(i, i + 1)});
        return ans;
    }
};


================================================================================
FOLDER: 3845_maximum_subarray_xor_with_bounded_range
// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

#include <vector>

class Solution {
    struct Node {
        int next[2]{0, 0};
        int count = 0;
    };

    std::vector<Node> nodes;

    void add(int x, int delta) {
        int u = 0;
        nodes[u].count += delta;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            if (nodes[u].next[bit] == 0) {
                nodes[u].next[bit] = (int)nodes.size();
                nodes.push_back(Node{});
            }
            u = nodes[u].next[bit];
            nodes[u].count += delta;
        }
    }

    int query(int x) {
        int u = 0, res = 0;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            int want = bit ^ 1;
            int v = nodes[u].next[want];
            if (v != 0 && nodes[v].count > 0) {
                res |= 1 << b;
                u = v;
            } else {
                u = nodes[u].next[bit];
            }
        }
        return res;
    }

public:
    int maxSubarrayXor(std::vector<int>& nums, int k) {
        nodes.assign(1, Node{});
        int n = (int)nums.size();
        std::vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] ^ nums[i];
        std::vector<int> maxQ, minQ;
        int left = 0, trieLeft = 0, ans = 0;
        for (int r = 0; r < n; r++) {
            int x = nums[r];
            while (!maxQ.empty() && nums[maxQ.back()] <= x) maxQ.pop_back();
            maxQ.push_back(r);
            while (!minQ.empty() && nums[minQ.back()] >= x) minQ.pop_back();
            minQ.push_back(r);
            while (nums[maxQ[0]] - nums[minQ[0]] > k) {
                if (maxQ[0] == left) maxQ.erase(maxQ.begin());
                if (minQ[0] == left) minQ.erase(minQ.begin());
                left++;
            }
            add(pref[r], 1);
            while (trieLeft < left) {
                add(pref[trieLeft], -1);
                trieLeft++;
            }
            int cur = query(pref[r + 1]);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3846_total_distance_to_type_a_string_using_one_finger
// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

#include <cstdlib>
#include <string>
#include <unordered_map>
#include <utility>

class Solution {
    static std::unordered_map<char, std::pair<int, int>> buildPos() {
        std::unordered_map<char, std::pair<int, int>> pos;
        const char* keys[] = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; keys[i][j]; j++) pos[keys[i][j]] = {i, j};
        }
        return pos;
    }

public:
    int totalDistance(std::string s) {
        static auto pos = buildPos();
        char pre = 'a';
        int ans = 0;
        for (char cur : s) {
            auto p1 = pos[pre], p2 = pos[cur];
            ans += std::abs(p1.first - p2.first) + std::abs(p1.second - p2.second);
            pre = cur;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3847_find_the_score_difference_in_a_game
// LeetCode 3847 - Find The Score Difference In A Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

#include <vector>

class Solution {
public:
    int scoreDifference(std::vector<int>& nums) {
        int ans = 0, k = 1;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] % 2 != 0) k = -k;
            if (i % 6 == 5) k = -k;
            ans += k * nums[i];
        }
        return ans;
    }
};


================================================================================
FOLDER: 3848_check_digitorial_permutation
// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

#include <algorithm>
#include <string>

class Solution {
public:
    bool isDigitorialPermutation(int n) {
        int f[10];
        f[0] = 1;
        for (int i = 1; i < 10; i++) f[i] = f[i - 1] * i;
        int x = 0, y = n;
        while (y > 0) {
            x += f[y % 10];
            y /= 10;
        }
        std::string a = std::to_string(x), b = std::to_string(n);
        std::sort(a.begin(), a.end());
        std::sort(b.begin(), b.end());
        return a == b;
    }
};


================================================================================
FOLDER: 3849_maximum_bitwise_xor_after_rearrangement
// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

#include <string>

class Solution {
public:
    std::string maximumXor(std::string s, std::string t) {
        int cnt[2] = {};
        for (char c : t) cnt[c - '0']++;
        std::string ans(s.size(), '0');
        for (int i = 0; i < (int)s.size(); i++) {
            int x = s[i] - '0';
            if (cnt[x ^ 1] > 0) {
                cnt[x ^ 1]--;
                ans[i] = '1';
            } else {
                cnt[x]--;
                ans[i] = '0';
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3850_count_sequences_to_k
// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

#include <cstdint>
#include <functional>
#include <map>
#include <tuple>
#include <vector>

class Solution {
public:
    int countSequences(std::vector<int>& nums, long long k) {
        int n = (int)nums.size();
        std::map<std::tuple<int, int64_t, int64_t>, int> f;
        auto gcd = [](int64_t a, int64_t b) {
            while (b) {
                int64_t t = a % b;
                a = b;
                b = t;
            }
            return a;
        };
        std::function<int(int, int64_t, int64_t)> dfs = [&](int i, int64_t p, int64_t q) {
            if (i == n) return (p == k && q == 1) ? 1 : 0;
            auto key = std::make_tuple(i, p, q);
            if (f.count(key)) return f[key];
            int res = dfs(i + 1, p, q);
            int64_t x = nums[i];
            int64_t g1 = gcd(p * x, q);
            res += dfs(i + 1, (p * x) / g1, q / g1);
            int64_t g2 = gcd(p, q * x);
            res += dfs(i + 1, p / g2, (q * x) / g2);
            return f[key] = res;
        };
        return dfs(0, 1, 1);
    }
};


================================================================================
FOLDER: 3851_maximum_requests_without_violating_the_limit
// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxRequests(std::vector<std::vector<int>>& requests, int k, int window) {
        std::unordered_map<int, std::vector<int>> g;
        for (auto& r : requests) g[r[0]].push_back(r[1]);
        int ans = (int)requests.size();
        for (auto& [_, ts] : g) {
            std::sort(ts.begin(), ts.end());
            std::vector<int> kept;
            for (int t : ts) {
                while (!kept.empty() && t - kept.front() > window) kept.erase(kept.begin());
                if ((int)kept.size() < k) kept.push_back(t);
                else ans--;
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3852_smallest_pair_with_different_frequencies
// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> minDistinctFreqPair(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int v : nums) cnt[v]++;
        int x = *std::min_element(nums.begin(), nums.end());
        int minY = INT_MAX;
        for (auto& [y, _] : cnt) {
            if (y < minY && cnt[x] != cnt[y]) minY = y;
        }
        if (minY == INT_MAX) return {-1, -1};
        return {x, minY};
    }
};


================================================================================
FOLDER: 3853_merge_close_characters
// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

#include <string>
#include <unordered_map>

class Solution {
public:
    std::string mergeCharacters(std::string s, int k) {
        std::unordered_map<char, int> last;
        std::string ans;
        for (char c : s) {
            int cur = (int)ans.size();
            auto it = last.find(c);
            if (it != last.end() && cur - it->second <= k) continue;
            ans.push_back(c);
            last[c] = cur;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3854_minimum_operations_to_make_array_parity_alternating
// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    std::vector<int> makeParityAlternating(std::vector<int>& nums) {
        if (nums.size() == 1) return {0, 0};
        int mn = *std::min_element(nums.begin(), nums.end());
        int mx = *std::max_element(nums.begin(), nums.end());
        auto f = [&](int k) {
            int cnt = 0, a = INT_MAX, b = INT_MIN;
            for (int i = 0; i < (int)nums.size(); i++) {
                int x = nums[i];
                if (((x - i) & 1) != k) {
                    cnt++;
                    if (x == mn) x++;
                    else if (x == mx) x--;
                }
                a = std::min(a, x);
                b = std::max(b, x);
            }
            return std::vector<int>{cnt, std::max(1, b - a)};
        };
        auto r0 = f(0), r1 = f(1);
        if (r0[0] != r1[0]) return r0[0] < r1[0] ? r0 : r1;
        return r0[1] <= r1[1] ? r0 : r1;
    }
};


================================================================================
FOLDER: 3855_sum_of_k_digit_numbers_in_a_range
// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

#include <cstdint>

class Solution {
    static int64_t qpow(int64_t a, int64_t n, int64_t mod) {
        a %= mod;
        int64_t ans = 1;
        while (n > 0) {
            if (n & 1) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ans;
    }

public:
    int sumOfNumbers(int l, int r, int k) {
        const int64_t MOD = 1000000007;
        int64_t n = r - l + 1;
        int64_t sum = (int64_t)(l + r) * n / 2 % MOD;
        int64_t part1 = qpow(n % MOD, k - 1, MOD);
        int64_t part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD;
        int64_t inv9 = qpow(9, MOD - 2, MOD);
        int64_t ans = sum;
        ans = ans * part1 % MOD;
        ans = ans * part2 % MOD;
        ans = ans * inv9 % MOD;
        return (int)ans;
    }
};


================================================================================
FOLDER: 3856_trim_trailing_vowels
// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

#include <string>

class Solution {
public:
    std::string trimTrailingVowels(std::string s) {
        int i = (int)s.size() - 1;
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        while (i >= 0 && isVowel(s[i])) i--;
        return s.substr(0, i + 1);
    }
};


================================================================================
FOLDER: 3857_minimum_cost_to_split_into_ones
// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

class Solution {
public:
    int minCost(int n) {
        return n * (n - 1) / 2;
    }
};


================================================================================
FOLDER: 3858_minimum_bitwise_or_from_grid
// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

#include <algorithm>
#include <vector>

class Solution {
    static int bitLen(unsigned x) {
        return x == 0 ? 0 : 32 - __builtin_clz(x);
    }

public:
    int minimumOR(std::vector<std::vector<int>>& grid) {
        int mx = 0;
        for (auto& row : grid) mx = std::max(mx, *std::max_element(row.begin(), row.end()));
        int m = bitLen((unsigned)mx);
        int ans = 0;
        for (int i = m - 1; i >= 0; i--) {
            int mask = ans | ((1 << i) - 1);
            for (auto& row : grid) {
                bool found = false;
                for (int x : row) {
                    if ((x | mask) == mask) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    ans |= 1 << i;
                    break;
                }
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3859_count_subarrays_with_k_distinct_integers
// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

#include <cstdint>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, int k, int m) {
        auto f = [&](int lim) {
            std::unordered_map<int, int> cnt;
            int64_t ans = 0;
            int l = 0, t = 0;
            for (int x : nums) {
                if (++cnt[x] == m) t++;
                while ((int)cnt.size() >= lim && t >= k) {
                    int y = nums[l++];
                    if (--cnt[y] == m - 1) t--;
                    if (cnt[y] == 0) cnt.erase(y);
                }
                ans += l;
            }
            return ans;
        };
        return f(k) - f(k + 1);
    }
};


================================================================================
FOLDER: 3860_unique_email_groups
// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

#include <cctype>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int uniqueEmailGroups(std::vector<std::string>& emails) {
        std::unordered_set<std::string> st;
        for (auto& email : emails) {
            auto at = email.find('@');
            std::string local = email.substr(0, at);
            std::string domain = email.substr(at + 1);
            auto plus = local.find('+');
            if (plus != std::string::npos) local = local.substr(0, plus);
            std::string cleaned;
            for (char c : local) if (c != '.') cleaned.push_back(std::tolower(static_cast<unsigned char>(c)));
            for (char& c : domain) c = std::tolower(static_cast<unsigned char>(c));
            st.insert(cleaned + domain);
        }
        return (int)st.size();
    }
};


================================================================================
FOLDER: 3861_minimum_capacity_box
// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

#include <vector>

class Solution {
public:
    int minimumIndex(std::vector<int>& capacity, int itemSize) {
        int ans = -1;
        for (int i = 0; i < (int)capacity.size(); i++) {
            if (capacity[i] >= itemSize && (ans == -1 || capacity[i] < capacity[ans])) ans = i;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3862_find_the_smallest_balanced_index
// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

#include <vector>

class Solution {
public:
    int smallestBalancedIndex(std::vector<int>& nums) {
        long long s = 0, p = 1;
        for (int x : nums) s += x;
        for (int i = (int)nums.size() - 1; i >= 0; i--) {
            s -= nums[i];
            if (s == p) return i;
            p *= nums[i];
            if (p >= s) break;
        }
        return -1;
    }
};


================================================================================
FOLDER: 3863_minimum_operations_to_sort_a_string
// LeetCode 3863 - Minimum Operations To Sort A String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

#include <algorithm>
#include <string>

class Solution {
public:
    int minOperations(std::string s) {
        int n = (int)s.size();
        bool sorted = true;
        for (int i = 1; i < n; i++) {
            if (s[i] < s[i - 1]) {
                sorted = false;
                break;
            }
        }
        if (sorted) return 0;
        if (n == 2) return -1;
        char mn = *std::min_element(s.begin(), s.end());
        char mx = *std::max_element(s.begin(), s.end());
        if (s[0] == mn || s[n - 1] == mx) return 1;
        for (int i = 1; i < n - 1; i++) {
            if (s[i] == mn || s[i] == mx) return 2;
        }
        return 3;
    }
};


================================================================================
FOLDER: 3864_minimum_cost_to_partition_a_binary_string
// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

#include <algorithm>
#include <cstdint>
#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    long long minCost(std::string s, int encCost, int flatCost) {
        int n = (int)s.size();
        std::vector<int> pre(n + 1, 0);
        for (int i = 1; i <= n; i++) pre[i] = pre[i - 1] + (s[i - 1] - '0');
        std::function<int64_t(int, int)> dfs = [&](int l, int r) {
            int x = pre[r] - pre[l];
            int64_t res = x != 0 ? (int64_t)(r - l) * x * encCost : flatCost;
            if ((r - l) % 2 == 0) {
                int m = (l + r) / 2;
                res = std::min(res, dfs(l, m) + dfs(m, r));
            }
            return res;
        };
        return dfs(0, n);
    }
};


================================================================================
FOLDER: 3865_reverse_k_subarrays
// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> reverseSubarrays(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        int m = n / k;
        for (int i = 0; i < n; i += m) {
            std::reverse(nums.begin() + i, nums.begin() + i + m);
        }
        return nums;
    }
};


================================================================================
FOLDER: 3866_first_unique_even_element
// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

#include <vector>

class Solution {
public:
    int firstUniqueEven(std::vector<int>& nums) {
        int cnt[101] = {};
        for (int x : nums) cnt[x]++;
        for (int x : nums) {
            if (x % 2 == 0 && cnt[x] == 1) return x;
        }
        return -1;
    }
};


================================================================================
FOLDER: 3867_sum_of_gcd_of_formed_pairs
// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
    static int gcd(int a, int b) {
        while (b) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

public:
    long long gcdSum(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> prefixGcd(n);
        int mx = 0;
        for (int i = 0; i < n; i++) {
            mx = std::max(mx, nums[i]);
            prefixGcd[i] = gcd(nums[i], mx);
        }
        std::sort(prefixGcd.begin(), prefixGcd.end());
        int64_t ans = 0;
        for (int i = 0; i < n / 2; i++) ans += gcd(prefixGcd[i], prefixGcd[n - i - 1]);
        return ans;
    }
};


================================================================================
FOLDER: 3868_minimum_cost_to_equalize_arrays_using_swaps
// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minCost(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, int> cnt2;
        for (int x : nums2) cnt2[x]++;
        std::unordered_map<int, int> cnt1;
        for (int x : nums1) {
            if (cnt2[x] > 0) cnt2[x]--;
            else cnt1[x]++;
        }
        int ans = 0;
        for (auto& [_, v] : cnt1) {
            if (v % 2 == 1) return -1;
            ans += v / 2;
        }
        for (auto& [_, v] : cnt2) {
            if (v % 2 == 1) return -1;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3869_count_fancy_numbers_in_a_range
// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

#include <cstdint>
#include <functional>
#include <string>
#include <vector>

class Solution {
    static bool check(int s) {
        if (s < 100) return s % 11 != 0;
        int mid = (s / 10) % 10;
        int last = s % 10;
        return mid > 1 && mid < last;
    }

public:
    long long countFancy(long long l, long long r) {
        auto calc = [&](int64_t x) {
            std::string num = std::to_string(x);
            int n = (int)num.size();
            std::vector f(n, std::vector(9 * n + 1, std::vector(10, std::vector<int64_t>(4, -1))));
            std::function<int64_t(int, int, int, int, bool)> dfs =
                [&](int pos, int s, int prev, int st, bool lim) -> int64_t {
                if (pos >= n) {
                    if (st != 3) return 1;
                    return check(s) ? 1 : 0;
                }
                if (!lim && f[pos][s][prev][st] != -1) return f[pos][s][prev][st];
                int up = lim ? num[pos] - '0' : 9;
                int64_t res = 0;
                for (int i = 0; i <= up; i++) {
                    int nxtSt = st;
                    if (st == 0) {
                        if (prev == 0) nxtSt = 0;
                        else if (i > prev) nxtSt = 1;
                        else if (i < prev) nxtSt = 2;
                        else nxtSt = 3;
                    } else if (st == 1) {
                        nxtSt = i > prev ? 1 : 3;
                    } else if (st == 2) {
                        nxtSt = i < prev ? 2 : 3;
                    } else {
                        nxtSt = 3;
                    }
                    res += dfs(pos + 1, s + i, i, nxtSt, lim && i == up);
                }
                if (!lim) f[pos][s][prev][st] = res;
                return res;
            };
            return dfs(0, 0, 0, 0, true);
        };
        return calc(r) - calc(l - 1);
    }
};


================================================================================
FOLDER: 3870_count_commas_in_range
// LeetCode 3870 - Count Commas In Range
// https://leetcode.com/problems/count-commas-in-range/

#include <algorithm>

class Solution {
public:
    int countCommas(int n) {
        return std::max(0, n - 999);
    }
};


================================================================================
FOLDER: 3871_count_commas_in_range_ii
// LeetCode 3871 - Count Commas In Range Ii
// https://leetcode.com/problems/count-commas-in-range-ii/

#include <cstdint>

class Solution {
public:
    long long countCommas(long long n) {
        int64_t ans = 0;
        for (int64_t x = 1000; x <= n; x *= 1000) ans += n - x + 1;
        return ans;
    }
};


================================================================================
FOLDER: 3872_longest_arithmetic_sequence_after_changing_at_most_one_element
// LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestArithmetic(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> d(n);
        for (int i = 1; i < n; i++) d[i] = nums[i] - nums[i - 1];
        std::vector<int> f(n, 2), g(n, 2);
        f[0] = 1;
        g[n - 1] = 1;
        for (int i = 2; i < n; i++) {
            if (d[i] == d[i - 1]) f[i] = f[i - 1] + 1;
        }
        for (int i = n - 3; i >= 0; i--) {
            if (d[i + 1] == d[i + 2]) g[i] = g[i + 1] + 1;
        }
        int ans = 3;
        for (int i = 0; i < n; i++) {
            ans = std::max({ans, f[i], g[i]});
            if (i > 0) ans = std::max(ans, f[i - 1] + 1);
            if (i + 1 < n) ans = std::max(ans, g[i + 1] + 1);
            if (i > 0 && i < n - 1) {
                int diff = nums[i + 1] - nums[i - 1];
                if (diff % 2 == 0) {
                    diff /= 2;
                    int k = 3;
                    if (i > 1 && diff == d[i - 1]) k += f[i - 1] - 1;
                    if (i < n - 2 && diff == d[i + 2]) k += g[i + 1] - 1;
                    ans = std::max(ans, k);
                }
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3873_maximum_points_activated_with_one_addition
// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

#include <cstdint>
#include <unordered_map>
#include <vector>

class Solution {
    struct UnionFind {
        std::unordered_map<int64_t, int64_t> p;
        std::unordered_map<int64_t, int> size;
        int64_t find(int64_t x) {
            if (!p.count(x)) {
                p[x] = x;
                size[x] = 1;
            }
            if (p[x] != x) p[x] = find(p[x]);
            return p[x];
        }
        bool unite(int64_t a, int64_t b) {
            int64_t pa = find(a), pb = find(b);
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
    int maxActivated(std::vector<std::vector<int>>& points) {
        UnionFind uf;
        const int64_t m = 3000000000LL;
        for (auto& pt : points) uf.unite(pt[0], pt[1] + m);
        std::unordered_map<int64_t, int> cnt;
        for (auto& pt : points) cnt[uf.find(pt[0])]++;
        int mx1 = 0, mx2 = 0;
        for (auto& [_, x] : cnt) {
            if (mx1 < x) {
                mx2 = mx1;
                mx1 = x;
            } else if (mx2 < x) {
                mx2 = x;
            }
        }
        return mx1 + mx2 + 1;
    }
};


================================================================================
FOLDER: 3874_valid_subarrays_with_exactly_one_peak
// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long validSubarrays(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> peaks;
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) peaks.push_back(i);
        }
        int64_t ans = 0;
        for (int j = 0; j < (int)peaks.size(); j++) {
            int p = peaks[j];
            int leftMin = std::max(p - k, 0);
            if (j > 0) leftMin = std::max(leftMin, peaks[j - 1] + 1);
            int rightMax = std::min(p + k, n - 1);
            if (j < (int)peaks.size() - 1) rightMax = std::min(rightMax, peaks[j + 1] - 1);
            ans += (int64_t)(p - leftMin + 1) * (rightMax - p + 1);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3875_construct_uniform_parity_array_i
// LeetCode 3875 - Construct Uniform Parity Array I
// https://leetcode.com/problems/construct-uniform-parity-array-i/

#include <vector>

class Solution {
public:
    bool uniformArray(std::vector<int>& nums1) {
        return true;
    }
};


================================================================================
FOLDER: 3876_construct_uniform_parity_array_ii
// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

#include <climits>
#include <vector>

class Solution {
public:
    bool uniformArray(std::vector<int>& nums1) {
        int mn = INT_MAX;
        for (int x : nums1) {
            if (x % 2 == 1 && x < mn) mn = x;
        }
        for (int x : nums1) {
            if (x % 2 == 0 && mn != INT_MAX && x < mn) return false;
        }
        return true;
    }
};


================================================================================
FOLDER: 3877_minimum_removals_to_achieve_target_xor
// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minRemovals(std::vector<int>& nums, int target) {
        int mx = *std::max_element(nums.begin(), nums.end());
        int m = 0;
        if (mx > 0) {
            unsigned int u = (unsigned int)mx;
            while (u) {
                m++;
                u >>= 1;
            }
        }
        if ((1 << m) <= target) return -1;

        int n = (int)nums.size();
        int N = 1 << m;
        std::vector<std::vector<int>> f(n + 1, std::vector<int>(N, INT_MIN));
        f[0][0] = 0;

        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            for (int j = 0; j < N; j++) {
                f[i][j] = f[i - 1][j];
                if (f[i - 1][j ^ x] != INT_MIN) {
                    f[i][j] = std::max(f[i][j], f[i - 1][j ^ x] + 1);
                }
            }
        }

        if (f[n][target] < 0) return -1;
        return n - f[n][target];
    }
};


================================================================================
FOLDER: 3878_count_good_subarrays
// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

#include <vector>

class Solution {
public:
    long long countGoodSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> l(n, -1), stk;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (!stk.empty() && nums[stk.back()] < x && (nums[stk.back()] | x) == x) {
                stk.pop_back();
            }
            if (!stk.empty()) l[i] = stk.back();
            stk.push_back(i);
        }
        std::vector<int> r(n, n);
        stk.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stk.empty() && (nums[stk.back()] | nums[i]) == nums[i]) {
                stk.pop_back();
            }
            if (!stk.empty()) r[i] = stk.back();
            stk.push_back(i);
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += (long long)(i - l[i]) * (r[i] - i);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3879_maximum_distinct_path_sum_in_a_binary_tree
// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    std::unordered_map<TreeNode*, std::vector<TreeNode*>> g;
    std::unordered_map<int, bool> vis;

    void dfs(TreeNode* node, TreeNode* p) {
        if (!node) return;
        g[node] = {p, node->left, node->right};
        dfs(node->left, node);
        dfs(node->right, node);
    }

    int dfs2(TreeNode* node) {
        if (!node || vis[node->val]) return 0;
        vis[node->val] = true;
        int res = node->val;
        int best = 0;
        for (TreeNode* nxt : g[node]) {
            best = std::max(best, dfs2(nxt));
        }
        vis[node->val] = false;
        return res + best;
    }

public:
    int maxSum(TreeNode* root) {
        g.clear();
        vis.clear();
        dfs(root, nullptr);
        int ans = INT_MIN;
        for (auto& [node, _] : g) {
            ans = std::max(ans, dfs2(node));
            vis.clear();
        }
        return ans;
    }
};


================================================================================
FOLDER: 3880_minimum_absolute_difference_between_two_values
// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minAbsoluteDifference(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = n + 1;
        int last[3] = {-ans, -ans, -ans};
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (x != 0) {
                ans = std::min(ans, i - last[3 - x]);
                last[x] = i;
            }
        }
        if (ans > n) return -1;
        return ans;
    }
};


================================================================================
FOLDER: 3881_direction_assignments_with_exactly_k_visible_people
// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

#include <algorithm>
#include <vector>

class Solution {
    static constexpr int N = 100001;
    static constexpr int MOD = 1000000007;
    static inline std::vector<long long> fact;
    static inline std::vector<long long> invFact;
    static inline bool ready = false;

    static long long qmi(long long a, long long k, long long p) {
        long long res = 1;
        while (k) {
            if (k & 1) res = res * a % p;
            k >>= 1;
            a = a * a % p;
        }
        return res;
    }

    static void init() {
        if (ready) return;
        fact.assign(N, 0);
        invFact.assign(N, 0);
        fact[0] = invFact[0] = 1;
        for (int i = 1; i < N; i++) {
            fact[i] = fact[i - 1] * i % MOD;
            invFact[i] = qmi(fact[i], MOD - 2, MOD);
        }
        ready = true;
    }

    static long long comb(int n, int k) {
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
    }

public:
    int countVisiblePeople(int n, int pos, int k) {
        init();
        int l = pos, r = n - pos - 1;
        long long ans = 0;
        for (int a = 0; a <= std::min(k, l); a++) {
            int b = k - a;
            if (b <= r) {
                ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD;
            }
        }
        return (int)ans;
    }
};


================================================================================
FOLDER: 3882_minimum_xor_path_in_a_grid
// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

#include <array>
#include <vector>

class Solution {
public:
    int minXor(std::vector<std::vector<int>>& grid) {
        int rows = (int)grid.size(), cols = (int)grid[0].size();
        std::vector<std::array<bool, 1024>> dp(cols);
        for (int row = 0; row < rows; row++) {
            std::array<bool, 1024> left{};
            for (int col = 0; col < cols; col++) {
                std::array<bool, 1024> next{};
                int value = grid[row][col];
                if (row == 0 && col == 0) {
                    next[value] = true;
                } else {
                    for (int xorv = 0; xorv < 1024; xorv++) {
                        if (dp[col][xorv] || left[xorv]) next[xorv ^ value] = true;
                    }
                }
                dp[col] = next;
                left = next;
            }
        }
        for (int xorv = 0; xorv < 1024; xorv++) {
            if (dp[cols - 1][xorv]) return xorv;
        }
        return -1;
    }
};


================================================================================
FOLDER: 3883_count_non_decreasing_arrays_with_given_digit_sums
// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

#include <vector>

class Solution {
public:
    int countNonDecreasingArrays(std::vector<int>& digitSum) {
        const int mod = 1000000007;
        std::vector<std::vector<int>> groups(51);
        for (int x = 0; x <= 5000; x++) {
            int s = 0;
            for (int y = x; y > 0; y /= 10) s += y % 10;
            groups[s].push_back(x);
        }
        std::vector<int> prevVals = groups[digitSum[0]];
        std::vector<int> dp(prevVals.size(), 1);
        for (int pos = 1; pos < (int)digitSum.size(); pos++) {
            std::vector<int>& curVals = groups[digitSum[pos]];
            std::vector<int> next(curVals.size(), 0);
            int j = 0, prefix = 0;
            for (int i = 0; i < (int)curVals.size(); i++) {
                int x = curVals[i];
                while (j < (int)prevVals.size() && prevVals[j] <= x) {
                    prefix += dp[j];
                    if (prefix >= mod) prefix -= mod;
                    j++;
                }
                next[i] = prefix;
            }
            prevVals = curVals;
            dp = next;
        }
        int ans = 0;
        for (int x : dp) {
            ans += x;
            if (ans >= mod) ans -= mod;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3884_first_matching_character_from_both_ends
// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

#include <string>

class Solution {
public:
    int firstMatchingIndex(std::string s) {
        int n = (int)s.size();
        for (int i = 0; i < n / 2 + 1; i++) {
            if (s[i] == s[n - i - 1]) return i;
        }
        return -1;
    }
};


================================================================================
FOLDER: 3885_design_event_manager
// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

#include <set>
#include <unordered_map>
#include <utility>
#include <vector>

class EventManager {
    std::set<std::pair<int, int>> sl;
    std::unordered_map<int, int> d;

public:
    EventManager(std::vector<std::vector<int>>& events) {
        for (auto& e : events) {
            int eventId = e[0], priority = e[1];
            sl.insert({-priority, eventId});
            d[eventId] = priority;
        }
    }

    void updatePriority(int eventId, int newPriority) {
        int old = d[eventId];
        sl.erase({-old, eventId});
        sl.insert({-newPriority, eventId});
        d[eventId] = newPriority;
    }

    int pollHighest() {
        if (sl.empty()) return -1;
        auto top = *sl.begin();
        int eventId = top.second;
        sl.erase(sl.begin());
        d.erase(eventId);
        return eventId;
    }
};


================================================================================
FOLDER: 3886_sum_of_sortable_integers
// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

#include <algorithm>
#include <vector>

class Solution {
    bool rotationMatches(const std::vector<int>& block, const std::vector<int>& target) {
        int k = (int)block.size();
        std::vector<int> prefix(k, 0);
        for (int i = 1; i < k; i++) {
            int j = prefix[i - 1];
            while (j > 0 && target[i] != target[j]) j = prefix[j - 1];
            if (target[i] == target[j]) j++;
            prefix[i] = j;
        }
        int matched = 0;
        for (int i = 0; i < 2 * k - 1; i++) {
            int x = block[i % k];
            while (matched > 0 && x != target[matched]) matched = prefix[matched - 1];
            if (x == target[matched]) matched++;
            if (matched == k) return true;
        }
        return false;
    }

public:
    int sumOfSortableIntegers(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        std::vector<int> divisors;
        for (int d = 1; d * d <= n; d++) {
            if (n % d == 0) {
                divisors.push_back(d);
                if (d * d != n) divisors.push_back(n / d);
            }
        }
        int answer = 0;
        for (int k : divisors) {
            bool ok = true;
            for (int start = 0; start < n; start += k) {
                std::vector<int> block(nums.begin() + start, nums.begin() + start + k);
                std::vector<int> target(sorted.begin() + start, sorted.begin() + start + k);
                if (!rotationMatches(block, target)) {
                    ok = false;
                    break;
                }
            }
            if (ok) answer += k;
        }
        return answer;
    }
};


================================================================================
FOLDER: 3887_incremental_even_weighted_cycle_queries
// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

#include <utility>
#include <vector>

class Solution {
public:
    int countValidEdges(int n, std::vector<std::vector<int>>& edges) {
        std::vector<int> parent(n), size(n, 1), parity(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;

        auto find = [&](auto&& self, int x) -> std::pair<int, int> {
            if (parent[x] == x) return {x, 0};
            auto [root, p] = self(self, parent[x]);
            parity[x] ^= p;
            parent[x] = root;
            return {root, parity[x]};
        };

        int ans = 0;
        for (auto& e : edges) {
            auto [ru, pu] = find(find, e[0]);
            auto [rv, pv] = find(find, e[1]);
            if (ru == rv) {
                if ((pu ^ pv) == e[2]) ans++;
                continue;
            }
            if (size[ru] < size[rv]) {
                std::swap(ru, rv);
                std::swap(pu, pv);
            }
            parent[rv] = ru;
            parity[rv] = pu ^ pv ^ e[2];
            size[ru] += size[rv];
            ans++;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3888_minimum_operations_to_make_all_grid_elements_equal
// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int maxVal = grid[0][0];
        for (auto& row : grid) {
            maxVal = std::max(maxVal, *std::max_element(row.begin(), row.end()));
        }

        auto check = [&](int target) -> long long {
            std::vector<std::vector<long long>> diff(m + 2, std::vector<long long>(n + 2, 0));
            long long totalOps = 0;
            for (int i = 1; i <= m; i++) {
                for (int j = 1; j <= n; j++) {
                    diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
                    long long curVal = (long long)grid[i - 1][j - 1] + diff[i][j];
                    if (curVal > target) return -1;
                    if (curVal < target) {
                        if (i + k - 1 > m || j + k - 1 > n) return -1;
                        long long needed = target - curVal;
                        totalOps += needed;
                        diff[i][j] += needed;
                        diff[i + k][j] -= needed;
                        diff[i][j + k] -= needed;
                        diff[i + k][j + k] += needed;
                    }
                }
            }
            return totalOps;
        };

        for (int t = maxVal; t <= maxVal + 1; t++) {
            long long res = check(t);
            if (res != -1) return res;
        }
        return -1;
    }
};


================================================================================
FOLDER: 3889_mirror_frequency_distance
// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

#include <cmath>
#include <string>
#include <unordered_map>

class Solution {
public:
    int mirrorFrequency(std::string s) {
        std::unordered_map<char, int> freq;
        for (char c : s) freq[c]++;
        int ans = 0;
        std::unordered_map<char, bool> vis;
        for (auto& [c, v] : freq) {
            char m;
            if (c >= 'a' && c <= 'z') m = (char)('a' + 25 - (c - 'a'));
            else m = (char)('0' + (9 - (c - '0')));
            if (vis[m]) continue;
            vis[c] = true;
            int mv = freq.count(m) ? freq[m] : 0;
            ans += std::abs(v - mv);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3890_integers_with_multiple_sum_of_two_cubes
// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
    static inline std::vector<int> GOOD;
    static inline bool ready = false;

    static void init() {
        if (ready) return;
        const long long LIMIT = 1000000000LL;
        std::unordered_map<int, int> cnt;
        std::vector<long long> cubes(1001);
        for (int i = 0; i <= 1000; i++) cubes[i] = 1LL * i * i * i;
        for (int a = 1; a <= 1000; a++) {
            for (int b = a; b <= 1000; b++) {
                long long x = cubes[a] + cubes[b];
                if (x > LIMIT) break;
                cnt[(int)x]++;
            }
        }
        for (auto& [x, v] : cnt) {
            if (v > 1) GOOD.push_back(x);
        }
        std::sort(GOOD.begin(), GOOD.end());
        ready = true;
    }

public:
    std::vector<int> findGoodIntegers(int n) {
        init();
        auto it = std::upper_bound(GOOD.begin(), GOOD.end(), n);
        return std::vector<int>(GOOD.begin(), it);
    }
};


================================================================================
FOLDER: 3891_minimum_increase_to_maximize_special_indices
// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    long long minIncrease(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<std::vector<long long>> f(n, std::vector<long long>(2, -1));

        std::function<long long(int, int)> dfs = [&](int i, int j) -> long long {
            if (i >= n - 1) return 0;
            if (f[i][j] != -1) return f[i][j];
            int cost = std::max(0, std::max(nums[i - 1], nums[i + 1]) + 1 - nums[i]);
            long long ans = (long long)cost + dfs(i + 2, j);
            if (j > 0) ans = std::min(ans, dfs(i + 1, 0));
            return f[i][j] = ans;
        };

        return dfs(1, (n & 1) ^ 1);
    }
};


================================================================================
FOLDER: 3892_minimum_operations_to_achieve_at_least_k_peaks
// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (k == 0) return 0;
        if (k > n / 2) return -1;
        std::vector<long long> cost(n, 0);
        for (int i = 0; i < n; i++) {
            int left = nums[(i + n - 1) % n], right = nums[(i + 1) % n];
            int need = std::max(left, right);
            if (need >= nums[i]) cost[i] = (long long)need - nums[i] + 1;
        }
        const long long inf = 1LL << 60;

        auto line = [&](int left, int right, int choose) -> long long {
            if (choose == 0) return 0;
            if (left > right || choose > (right - left + 2) / 2) return inf;
            std::vector<long long> prev2(choose + 1, inf), prev1(choose + 1, inf);
            prev2[0] = prev1[0] = 0;
            for (int i = left; i <= right; i++) {
                std::vector<long long> current = prev1;
                for (int j = 1; j <= choose; j++) {
                    if (prev2[j - 1] != inf && prev2[j - 1] + cost[i] < current[j]) {
                        current[j] = prev2[j - 1] + cost[i];
                    }
                }
                prev2.swap(prev1);
                prev1.swap(current);
            }
            return prev1[choose];
        };

        long long answer = line(1, n - 1, k);
        long long withFirst = line(2, n - 2, k - 1);
        if (withFirst != inf) {
            withFirst += cost[0];
            answer = std::min(answer, withFirst);
        }
        if (answer == inf) return -1;
        return answer;
    }
};


================================================================================
FOLDER: 3893_maximum_team_size_with_overlapping_intervals
// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumTeamSize(std::vector<int>& startTime, std::vector<int>& endTime) {
        int n = (int)startTime.size();
        std::vector<std::pair<int, int>> intervals(n);
        for (int i = 0; i < n; i++) intervals[i] = {startTime[i], endTime[i]};
        std::vector<int> st = startTime, en = endTime;
        std::sort(st.begin(), st.end());
        std::sort(en.begin(), en.end());
        int ans = 0;
        for (auto& it : intervals) {
            int l = it.first, r = it.second;
            int i = (int)(std::upper_bound(en.begin(), en.end(), l - 1) - en.begin());
            int j = (int)(std::upper_bound(st.begin(), st.end(), r) - st.begin());
            ans = std::max(ans, j - i);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3894_traffic_signal_color
// LeetCode 3894 - Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/

#include <string>

class Solution {
public:
    std::string trafficSignal(int timer) {
        if (timer == 0) return "Green";
        if (timer == 30) return "Orange";
        if (timer > 30 && timer <= 90) return "Red";
        return "Invalid";
    }
};


================================================================================
FOLDER: 3895_count_digit_appearances
// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

#include <vector>

class Solution {
public:
    int countDigitOccurrences(std::vector<int>& nums, int digit) {
        int ans = 0;
        for (int x : nums) {
            for (; x > 0; x /= 10) {
                if (x % 10 == digit) ans++;
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3896_minimum_operations_to_transform_array_into_alternating_prime
// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

#include <algorithm>
#include <vector>

class Solution {
    static constexpr int MX = 200000;
    static inline std::vector<bool> isPrime;
    static inline std::vector<int> primes;
    static inline bool ready = false;

    static void init() {
        if (ready) return;
        isPrime.assign(MX + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i <= MX / i; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= MX; j += i) isPrime[j] = false;
            }
        }
        for (int i = 2; i <= MX; i++) {
            if (isPrime[i]) primes.push_back(i);
        }
        ready = true;
    }

public:
    int minOperations(std::vector<int>& nums) {
        init();
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            int x = nums[i];
            if (i % 2 == 0) {
                auto it = std::lower_bound(primes.begin(), primes.end(), x);
                ans += *it - x;
            } else if (isPrime[x]) {
                ans += (x == 2) ? 2 : 1;
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3897_maximum_value_of_concatenated_binary_segments
// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

#include <algorithm>
#include <utility>
#include <vector>

class Solution {
    static constexpr int MOD = 1000000007;

    static int group(const std::pair<int, int>& p) {
        if (p.second == 0) return 0;
        if (p.first > 0) return 1;
        return 2;
    }

public:
    int maxValue(std::vector<int>& nums1, std::vector<int>& nums0) {
        int n = (int)nums1.size();
        std::vector<std::pair<int, int>> pairs(n);
        int b = 0;
        for (int i = 0; i < n; i++) {
            pairs[i] = {nums1[i], nums0[i]};
            b += nums1[i] + nums0[i];
        }
        std::sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
            int g1 = group(a), g2 = group(b);
            if (g1 != g2) return g1 < g2;
            if (g1 == 0) return a.first > b.first;
            if (g1 == 1) {
                if (a.first != b.first) return a.first > b.first;
                return a.second < b.second;
            }
            return a.second < b.second;
        });
        std::vector<int> p(b);
        p[0] = 1;
        for (int i = 1; i < b; i++) p[i] = (int)(2LL * p[i - 1] % MOD);
        int ans = 0;
        b--;
        for (auto& pr : pairs) {
            int cnt1 = pr.first, cnt0 = pr.second;
            while (cnt1 > 0) {
                ans = (ans + p[b]) % MOD;
                b--;
                cnt1--;
            }
            b -= cnt0;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3898_find_the_degree_of_each_vertex
// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

#include <vector>

class Solution {
public:
    std::vector<int> findDegrees(std::vector<std::vector<int>>& matrix) {
        std::vector<int> ans(matrix.size(), 0);
        for (int i = 0; i < (int)matrix.size(); i++) {
            for (int x : matrix[i]) ans[i] += x;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3899_angles_of_a_triangle
// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<double> internalAngles(std::vector<int>& sides) {
        std::sort(sides.begin(), sides.end());
        int a = sides[0], b = sides[1], c = sides[2];
        if (a + b <= c) return {};
        const double PI = std::acos(-1.0);
        double A = std::acos((double)(b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / PI;
        double B = std::acos((double)(a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / PI;
        double C = 180.0 - A - B;
        return {A, B, C};
    }
};


================================================================================
FOLDER: 3900_longest_balanced_substring_after_one_swap
// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestBalanced(std::string s) {
        int cnt0 = 0;
        for (char c : s) if (c == '0') cnt0++;
        int cnt1 = (int)s.size() - cnt0;
        std::unordered_map<int, std::vector<int>> pos;
        pos[0].push_back(-1);
        int ans = 0, pre = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            if (s[i] == '1') pre++;
            else pre--;
            pos[pre].push_back(i);
            ans = std::max(ans, i - pos[pre][0]);
            if (pos.count(pre - 2)) {
                auto& p = pos[pre - 2];
                if ((i - p[0] - 2) / 2 < cnt0) ans = std::max(ans, i - p[0]);
                else if ((int)p.size() > 1) ans = std::max(ans, i - p[1]);
            }
            if (pos.count(pre + 2)) {
                auto& p = pos[pre + 2];
                if ((i - p[0] - 2) / 2 < cnt1) ans = std::max(ans, i - p[0]);
                else if ((int)p.size() > 1) ans = std::max(ans, i - p[1]);
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3901_good_subsequence_queries
// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

#include <numeric>
#include <vector>

class Solution {
    struct Node {
        int l = 0, r = 0, g = 0;
    };

    struct SegmentTree {
        std::vector<Node> tr;
        explicit SegmentTree(int n) : tr(n << 2) { build(1, 1, n); }

        void build(int u, int l, int r) {
            tr[u] = {l, r, 0};
            if (l == r) return;
            int mid = (l + r) >> 1;
            build(u << 1, l, mid);
            build(u << 1 | 1, mid + 1, r);
        }

        void pushup(int u) { tr[u].g = std::gcd(tr[u << 1].g, tr[u << 1 | 1].g); }

        void modify(int u, int x, int v) {
            if (tr[u].l == tr[u].r) {
                tr[u].g = v;
                return;
            }
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (x <= mid) modify(u << 1, x, v);
            else modify(u << 1 | 1, x, v);
            pushup(u);
        }

        int query(int u, int l, int r) {
            if (l > r) return 0;
            if (tr[u].l >= l && tr[u].r <= r) return tr[u].g;
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (r <= mid) return query(u << 1, l, r);
            if (l > mid) return query(u << 1 | 1, l, r);
            return std::gcd(query(u << 1, l, mid), query(u << 1 | 1, mid + 1, r));
        }
    };

public:
    int countGoodSubseq(std::vector<int>& nums, int p, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        SegmentTree tree(n);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] % p == 0) {
                tree.modify(1, i + 1, nums[i]);
                cnt++;
            }
        }
        int ans = 0;
        for (auto& q : queries) {
            int idx = q[0], val = q[1];
            if (nums[idx] % p == 0) {
                tree.modify(1, idx + 1, 0);
                cnt--;
            }
            if (val % p == 0) {
                tree.modify(1, idx + 1, val);
                cnt++;
            }
            nums[idx] = val;
            if (tree.tr[1].g != p) continue;
            if (cnt < n || n > 6) {
                ans++;
                continue;
            }
            for (int i = 1; i <= n; i++) {
                int leftG = tree.query(1, 1, i - 1);
                int rightG = tree.query(1, i + 1, n);
                if (std::gcd(leftG, rightG) == p) {
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3902_zigzag_level_sum_of_binary_tree
// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    std::vector<long long> zigzagLevelSum(TreeNode* root) {
        std::vector<long long> ans;
        std::vector<TreeNode*> q = {root};
        bool left = true;
        while (!q.empty()) {
            std::vector<TreeNode*> nq;
            for (TreeNode* node : q) {
                if (node->left) nq.push_back(node->left);
                if (node->right) nq.push_back(node->right);
            }
            int m = (int)q.size();
            long long s = 0;
            for (int i = 0; i < m; i++) {
                TreeNode* node = left ? q[i] : q[m - i - 1];
                TreeNode* child = left ? node->left : node->right;
                if (!child) break;
                s += node->val;
            }
            ans.push_back(s);
            left = !left;
            q.swap(nq);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3903_smallest_stable_index_i
// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int firstStableIndex(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> right(n);
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = std::min(right[i + 1], nums[i]);
        int left = 0;
        for (int i = 0; i < n; i++) {
            left = std::max(left, nums[i]);
            if (left - right[i] <= k) return i;
        }
        return -1;
    }
};


================================================================================
FOLDER: 3904_smallest_stable_index_ii
// LeetCode 3904 - Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int firstStableIndex(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> right(n);
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = std::min(right[i + 1], nums[i]);
        int left = 0;
        for (int i = 0; i < n; i++) {
            left = std::max(left, nums[i]);
            if (left - right[i] <= k) return i;
        }
        return -1;
    }
};


================================================================================
FOLDER: 3905_multi_source_flood_fill
// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

#include <map>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> colorGrid(int n, int m, std::vector<std::vector<int>>& sources) {
        std::vector<std::vector<int>> ans(n, std::vector<int>(m, 0));
        std::vector<std::vector<int>> q = sources;
        int dirs[5] = {-1, 0, 1, 0, -1};
        for (auto& s : q) ans[s[0]][s[1]] = s[2];
        while (!q.empty()) {
            std::map<std::pair<int, int>, int> vis;
            for (auto& curr : q) {
                int r = curr[0], c = curr[1], color = curr[2];
                for (int i = 0; i < 4; i++) {
                    int x = r + dirs[i], y = c + dirs[i + 1];
                    if (x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0) {
                        auto key = std::make_pair(x, y);
                        if (color > vis[key]) vis[key] = color;
                    }
                }
            }
            q.clear();
            for (auto& [pos, color] : vis) {
                ans[pos.first][pos.second] = color;
                q.push_back({pos.first, pos.second, color});
            }
        }
        return ans;
    }
};


================================================================================
FOLDER: 3906_count_good_integers_on_a_grid_path
// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

#include <array>
#include <string>
#include <vector>

class Solution {
public:
    long long countGoodIntegersOnPath(long long l, long long r, std::string directions) {
        std::array<bool, 16> key{};
        int row = 0, col = 0;
        key[0] = true;
        for (char c : directions) {
            if (c == 'D') row++;
            else col++;
            key[row * 4 + col] = true;
        }

        std::string s;
        std::array<std::array<long long, 10>, 16> f{};

        auto dfs = [&](auto&& self, int pos, int last, bool lim) -> long long {
            if (pos == 16) return 1;
            if (!lim && f[pos][last] != -1) return f[pos][last];
            long long res = 0;
            int start = key[pos] ? last : 0;
            int end = lim ? (s[pos] - '0') : 9;
            for (int i = start; i <= end; i++) {
                int nextLast = key[pos] ? i : last;
                res += self(self, pos + 1, nextLast, lim && (i == end));
            }
            if (!lim) f[pos][last] = res;
            return res;
        };

        auto calc = [&](long long x) -> long long {
            if (x < 0) return 0;
            std::string t = std::to_string(x);
            s = std::string(16 - (int)t.size(), '0') + t;
            for (int i = 0; i < 16; i++) {
                for (int j = 0; j < 10; j++) f[i][j] = -1;
            }
            return dfs(dfs, 0, 0, true);
        };

        return calc(r) - calc(l - 1);
    }
};


================================================================================
FOLDER: 3907_count_smaller_elements_with_opposite_parity
// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

#include <algorithm>
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
    std::vector<int> countSmallerOppositeParity(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        sorted.erase(std::unique(sorted.begin(), sorted.end()), sorted.end());
        int m = (int)sorted.size();
        BIT bits[2] = {BIT(m), BIT(m)};
        std::vector<int> ans(n);
        for (int i = n - 1; i >= 0; i--) {
            int x = (int)(std::lower_bound(sorted.begin(), sorted.end(), nums[i]) - sorted.begin()) + 1;
            ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1);
            bits[nums[i] & 1].update(x, 1);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3908_valid_digit_number
// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

class Solution {
public:
    bool validDigit(int n, int x) {
        bool hasX = false;
        while (n > 9) {
            hasX = hasX || (n % 10 == x);
            n /= 10;
        }
        return hasX && (n != x);
    }
};


================================================================================
FOLDER: 3909_compare_sums_of_bitonic_parts
// LeetCode 3909 - Compare Sums Of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

#include <vector>

class Solution {
public:
    int compareBitonicSums(std::vector<int>& nums) {
        long long l = nums[0], r = 0;
        for (int x : nums) r += x;
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i - 1] > nums[i]) break;
            l += nums[i];
            r -= nums[i - 1];
        }
        if (l == r) return -1;
        if (l > r) return 0;
        return 1;
    }
};


================================================================================
FOLDER: 3910_count_connected_subgraphs_with_even_node_sum
// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

#include <functional>
#include <vector>

class Solution {
public:
    int evenSumSubgraphs(std::vector<int>& nums, std::vector<std::vector<int>>& edges) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int m = (1 << n) - 1;
        int ans = 0;
        int vis = 0;

        std::function<void(int)> dfs = [&](int u) {
            vis |= 1 << u;
            for (int v : g[u]) {
                if (((vis >> v) & 1) == 0) dfs(v);
            }
        };

        for (int sub = 1; sub <= m; sub++) {
            int s = 0;
            for (int i = 0; i < n; i++) {
                if ((sub >> i) & 1) s += nums[i];
            }
            if (s % 2 != 0) continue;
            vis = m ^ sub;
            int start = 31 - __builtin_clz(sub);
            dfs(start);
            if (vis == m) ans++;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3911_k_th_smallest_remaining_even_integer_in_subarray_queries
// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> kthSmallestEven(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> evenPrefix(n + 1, 0);
        for (int i = 0; i < n; i++) {
            evenPrefix[i + 1] = evenPrefix[i] + (nums[i] % 2 == 0);
        }
        std::vector<long long> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int l = queries[qi][0], r = queries[qi][1];
            long long k = queries[qi][2];
            long long lo = 1, hi = k + (r - l + 1);
            while (lo < hi) {
                long long mid = (lo + hi) / 2;
                int pos = (int)(std::upper_bound(nums.begin(), nums.end(), 2 * mid) - nums.begin());
                if (pos > r + 1) pos = r + 1;
                int removed = 0;
                if (pos > l) removed = evenPrefix[pos] - evenPrefix[l];
                if (mid - removed >= k) hi = mid;
                else lo = mid + 1;
            }
            ans[qi] = 2 * lo;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3912_valid_elements_in_an_array
// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> findValidElements(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> right(n);
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = std::max(right[i + 1], nums[i]);
        int left = 0;
        std::vector<int> ans;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (x > left || i == n - 1 || x > right[i + 1]) ans.push_back(x);
            left = std::max(left, x);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3913_sort_vowels_by_frequency
// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string sortVowels(std::string s) {
        std::unordered_set<char> st = {'a', 'e', 'i', 'o', 'u'};
        std::vector<char> vowels;
        std::unordered_map<char, int> cnt;
        for (char c : s) {
            if (!st.count(c)) continue;
            if (!cnt.count(c)) vowels.push_back(c);
            cnt[c]++;
        }
        std::sort(vowels.begin(), vowels.end(), [&](char a, char b) {
            return cnt[a] > cnt[b];
        });
        std::string ans = s;
        int i = 0;
        for (int k = 0; k < (int)s.size(); k++) {
            if (!st.count(s[k])) continue;
            char ch = vowels[i];
            ans[k] = ch;
            if (--cnt[ch] == 0) i++;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3914_minimum_operations_to_make_array_non_decreasing
// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums) {
        long long ans = 0;
        for (int i = 1; i < (int)nums.size(); i++) {
            ans += std::max(0LL, (long long)nums[i - 1] - nums[i]);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3915_maximum_sum_of_alternating_subsequence_with_distance_at_least_k
// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

#include <algorithm>
#include <vector>

class Solution {
    struct Fenwick {
        std::vector<long long> f;
        explicit Fenwick(int n) : f(n, 0) {}
        void update(int i, long long val) {
            for (; i < (int)f.size(); i += i & -i) f[i] = std::max(f[i], val);
        }
        long long preMax(int i) {
            long long res = 0;
            for (; i > 0; i &= i - 1) res = std::max(res, f[i]);
            return res;
        }
    };

public:
    long long maxAlternatingSum(std::vector<int>& nums, int k) {
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        sorted.erase(std::unique(sorted.begin(), sorted.end()), sorted.end());
        int n = (int)nums.size();
        int m = (int)sorted.size();
        std::vector<long long> fInc(n), fDec(n);
        Fenwick inc(m + 1), dec(m + 1);
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (i >= k) {
                int j = nums[i - k];
                inc.update(m - j, fInc[i - k]);
                dec.update(j + 1, fDec[i - k]);
            }
            int j = (int)(std::lower_bound(sorted.begin(), sorted.end(), x) - sorted.begin());
            nums[i] = j;
            fInc[i] = dec.preMax(j) + x;
            fDec[i] = inc.preMax(m - 1 - j) + x;
            ans = std::max({ans, fInc[i], fDec[i]});
        }
        return ans;
    }
};


================================================================================
FOLDER: 3916_number_of_zigzag_arrays_iii
// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

#include <vector>

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const long long mod = 1000000007;
        int points = n + 1;
        std::vector<long long> values(points + 1, 0);
        for (int m = 1; m <= points; m++) {
            std::vector<long long> up(m), down(m);
            for (int value = 0; value < m; value++) {
                up[value] = value;
                down[value] = m - 1 - value;
            }
            for (int length = 3; length <= n; length++) {
                std::vector<long long> nextUp(m), nextDown(m);
                long long prefix = 0;
                for (int value = 0; value < m; value++) {
                    nextUp[value] = prefix;
                    prefix = (prefix + down[value]) % mod;
                }
                long long suffix = 0;
                for (int value = m - 1; value >= 0; value--) {
                    nextDown[value] = suffix;
                    suffix = (suffix + up[value]) % mod;
                }
                up.swap(nextUp);
                down.swap(nextDown);
            }
            for (int value = 0; value < m; value++) {
                values[m] = (values[m] + up[value] + down[value]) % mod;
            }
        }
        long long x = (r - l + 1) % mod;
        if (r - l + 1 <= points) return (int)values[r - l + 1];
        std::vector<long long> prefix(points + 2), suffix(points + 2);
        prefix[0] = 1;
        for (int i = 1; i <= points; i++) {
            prefix[i] = prefix[i - 1] * ((x - i + mod) % mod) % mod;
        }
        suffix[points + 1] = 1;
        for (int i = points; i >= 1; i--) {
            suffix[i] = suffix[i + 1] * ((x - i + mod) % mod) % mod;
        }
        std::vector<long long> factorial(points + 1);
        factorial[0] = 1;
        for (int i = 1; i <= points; i++) factorial[i] = factorial[i - 1] * i % mod;
        auto powm = [&](long long a, long long e) {
            long long res = 1;
            while (e > 0) {
                if (e & 1) res = res * a % mod;
                a = a * a % mod;
                e >>= 1;
            }
            return res;
        };
        long long answer = 0;
        for (int i = 1; i <= points; i++) {
            long long numerator = prefix[i - 1] * suffix[i + 1] % mod;
            long long denominator = factorial[i - 1] * factorial[points - i] % mod;
            long long term = values[i] * numerator % mod * powm(denominator, mod - 2) % mod;
            if ((points - i) % 2 == 1) answer -= term;
            else answer += term;
            answer %= mod;
        }
        if (answer < 0) answer += mod;
        return (int)answer;
    }
};


================================================================================
FOLDER: 3917_count_indices_with_opposite_parity
// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

#include <vector>

class Solution {
public:
    std::vector<int> countOppositeParity(std::vector<int>& nums) {
        int cnt[2] = {0, 0};
        for (int x : nums) cnt[x & 1]++;
        int n = (int)nums.size();
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            cnt[x & 1]--;
            ans[i] = cnt[(x & 1) ^ 1];
        }
        return ans;
    }
};


================================================================================
FOLDER: 3918_sum_of_primes_between_number_and_its_reverse
// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

#include <algorithm>
#include <vector>

class Solution {
    static inline bool ready = false;
    static inline bool isPrime[1001];

    static void init() {
        if (ready) return;
        for (int i = 0; i <= 1000; i++) isPrime[i] = true;
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= 1000; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= 1000; j += i) isPrime[j] = false;
            }
        }
        ready = true;
    }

public:
    int sumOfPrimesInRange(int n) {
        init();
        int r = 0;
        for (int x = n; x > 0; x /= 10) r = r * 10 + x % 10;
        int low = std::min(n, r), high = std::max(n, r);
        int ans = 0;
        for (int x = low; x <= high; x++) {
            if (isPrime[x]) ans += x;
        }
        return ans;
    }
};


================================================================================
FOLDER: 3919_minimum_cost_to_move_between_indices
// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

#include <vector>

class Solution {
public:
    std::vector<int> minCost(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> s1(n, 0), s2(n, 0);
        for (int i = 1; i < n; i++) {
            int c1 = 1;
            if (i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]) c1 = nums[i] - nums[i - 1];
            int c2 = 1;
            if (i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i]) c2 = nums[i] - nums[i - 1];
            s1[i] = s1[i - 1] + c1;
            s2[i] = s2[i - 1] + c2;
        }
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int l = queries[i][0], r = queries[i][1];
            ans[i] = (l < r) ? (s1[r] - s1[l]) : (s2[l] - s2[r]);
        }
        return ans;
    }
};


================================================================================
FOLDER: 3920_maximize_fixed_points_after_deletions
// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxFixedPoints(std::vector<int>& nums) {
        std::vector<int> tails;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i < nums[i]) continue;
            int d = i - nums[i];
            auto it = std::lower_bound(tails.begin(), tails.end(), d);
            if (it == tails.end()) tails.push_back(d);
            else *it = d;
        }
        return (int)tails.size();
    }
};

