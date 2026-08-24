===== 2618_check_if_object_instance_of_class (11 lines) =====
// LeetCode 2618 - Check if Object Instance of Class
// https://leetcode.com/problems/check-if-object-instance-of-class/

// JavaScript problem; C++ stand-in mirrors Go stand-in.
class Solution {
public:
    bool checkIfInstanceOf(void* obj, void* classFunction) {
        if (obj == nullptr || classFunction == nullptr) return false;
        return true;
    }
};

===== 2619_array_prototype_last (13 lines) =====
// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    int last(std::vector<int>& nums) {
        if (nums.empty()) return -1;
        return nums.back();
    }
};

===== 2620_counter (14 lines) =====
// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

#include <functional>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::function<int()> createCounter(int n) {
        return [cur = n]() mutable {
            return cur++;
        };
    }
};

===== 2621_sleep (13 lines) =====
// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

#include <chrono>
#include <thread>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    void sleep(int millis) {
        std::this_thread::sleep_for(std::chrono::milliseconds(millis));
    }
};

===== 2622_cache_with_time_limit (51 lines) =====
// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

#include <chrono>
#include <unordered_map>

// JavaScript problem; C++ stand-in of TimeLimitedCache.
class TimeLimitedCache {
    struct Entry {
        int value = 0;
        long long expire = 0;
    };
    std::unordered_map<int, Entry> data;

    static long long nowMs() {
        using namespace std::chrono;
        return duration_cast<milliseconds>(steady_clock::now().time_since_epoch()).count();
    }

public:
    TimeLimitedCache() {}

    bool set(int key, int value, int duration) {
        long long now = nowMs();
        auto it = data.find(key);
        bool alive = it != data.end() && it->second.expire > now;
        data[key] = {value, now + duration};
        return alive;
    }

    int get(int key) {
        long long now = nowMs();
        auto it = data.find(key);
        if (it == data.end() || it->second.expire <= now) return -1;
        return it->second.value;
    }

    int count() {
        long long now = nowMs();
        int cnt = 0;
        for (auto it = data.begin(); it != data.end();) {
            if (it->second.expire > now) {
                cnt++;
                ++it;
            } else {
                it = data.erase(it);
            }
        }
        return cnt;
    }
};

===== 2623_memoize (21 lines) =====
// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

#include <functional>
#include <memory>
#include <unordered_map>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::function<int(int)> memoize(std::function<int(int)> fn) {
        auto cache = std::make_shared<std::unordered_map<int, int>>();
        return [fn, cache](int x) {
            auto it = cache->find(x);
            if (it != cache->end()) return it->second;
            int v = fn(x);
            (*cache)[x] = v;
            return v;
        };
    }
};

===== 2624_snail_traversal (22 lines) =====
// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::vector<std::vector<int>> snail(std::vector<int>& nums, int rowsCount, int colsCount) {
        if (rowsCount * colsCount != (int)nums.size()) return {};
        std::vector<std::vector<int>> ans(rowsCount, std::vector<int>(colsCount));
        int idx = 0;
        for (int c = 0; c < colsCount; ++c) {
            if (c % 2 == 0) {
                for (int r = 0; r < rowsCount; ++r) ans[r][c] = nums[idx++];
            } else {
                for (int r = rowsCount - 1; r >= 0; --r) ans[r][c] = nums[idx++];
            }
        }
        return ans;
    }
};

===== 2625_flatten_deeply_nested_array (12 lines) =====
// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

#include <vector>

// JavaScript problem; C++ stand-in using int vectors as a simplified model.
class Solution {
public:
    std::vector<int> flat(std::vector<int>& arr, int /*n*/) {
        return arr;
    }
};

===== 2626_array_reduce_transformation (15 lines) =====
// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    int reduce(std::vector<int>& nums, std::function<int(int, int)> fn, int init) {
        int acc = init;
        for (int x : nums) acc = fn(acc, x);
        return acc;
    }
};

===== 2627_debounce (12 lines) =====
// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

#include <functional>

// JavaScript problem; C++ stand-in (immediate invoke; no timer runtime).
class Solution {
public:
    std::function<void()> debounce(std::function<void()> fn, int /*t*/) {
        return [fn]() { fn(); };
    }
};

===== 2628_json_deep_equal (12 lines) =====
// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

#include <string>

// JavaScript problem; C++ stand-in comparing stringified forms.
class Solution {
public:
    bool areDeeplyEqual(const std::string& o1, const std::string& o2) {
        return o1 == o2;
    }
};

===== 2629_function_composition (16 lines) =====
// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::function<int(int)> compose(std::vector<std::function<int(int)>> functions) {
        return [functions](int x) {
            for (int i = (int)functions.size() - 1; i >= 0; --i) x = functions[i](x);
            return x;
        };
    }
};

===== 2630_memoize_ii (25 lines) =====
// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

#include <functional>
#include <memory>
#include <string>
#include <unordered_map>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::function<int(const std::vector<int>&)> memoizeII(std::function<int(const std::vector<int>&)> fn) {
        auto cache = std::make_shared<std::unordered_map<std::string, int>>();
        return [fn, cache](const std::vector<int>& args) {
            std::string k;
            for (int a : args) k += "|" + std::to_string(a);
            auto it = cache->find(k);
            if (it != cache->end()) return it->second;
            int v = fn(args);
            (*cache)[k] = v;
            return v;
        };
    }
};

===== 2631_group_by (17 lines) =====
// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

#include <functional>
#include <string>
#include <unordered_map>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::unordered_map<std::string, std::vector<int>> groupBy(std::vector<int>& arr, std::function<std::string(int)> fn) {
        std::unordered_map<std::string, std::vector<int>> out;
        for (int x : arr) out[fn(x)].push_back(x);
        return out;
    }
};

===== 2632_curry (13 lines) =====
// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in applying all args at once.
class Solution {
public:
    std::function<int(const std::vector<int>&)> curry(std::function<int(const std::vector<int>&)> fn, int /*arity*/) {
        return [fn](const std::vector<int>& args) { return fn(args); };
    }
};

===== 2633_convert_object_to_json_string (12 lines) =====
// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

#include <string>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::string jsonStringify(const std::string& object) {
        return object;
    }
};

===== 2634_filter_elements_from_array (17 lines) =====
// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::vector<int> filter(std::vector<int>& arr, std::function<bool(int, int)> fn) {
        std::vector<int> out;
        for (int i = 0; i < (int)arr.size(); ++i) {
            if (fn(arr[i], i)) out.push_back(arr[i]);
        }
        return out;
    }
};

===== 2635_apply_transform_over_each_element_in_array (15 lines) =====
// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::vector<int> map(std::vector<int>& arr, std::function<int(int, int)> fn) {
        std::vector<int> out(arr.size());
        for (int i = 0; i < (int)arr.size(); ++i) out[i] = fn(arr[i], i);
        return out;
    }
};

===== 2636_promise_pool (15 lines) =====
// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in (sequential execution).
class Solution {
public:
    std::vector<int> promisePool(std::vector<std::function<int()>>& functions, int /*n*/) {
        std::vector<int> ans(functions.size());
        for (size_t i = 0; i < functions.size(); ++i) ans[i] = functions[i]();
        return ans;
    }
};

===== 2637_promise_time_limit (13 lines) =====
// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

#include <functional>
#include <stdexcept>

// JavaScript problem; C++ stand-in (no real timeout).
class Solution {
public:
    std::function<int()> timeLimit(std::function<int()> fn, int /*t*/) {
        return [fn]() { return fn(); };
    }
};

===== 2638_count_the_number_of_k_free_subsets (30 lines) =====
// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countTheNumOfKFreeSubsets(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        std::unordered_map<int, std::vector<int>> groups;
        for (int x : nums) groups[x % k].push_back(x);
        long long ans = 1;
        for (auto& [_, g] : groups) {
            int prevVal = -1;
            long long prevTake = 0, prevSkip = 1;
            for (int v : g) {
                long long take = 0, skip = prevTake + prevSkip;
                if (prevVal + k == v) take = prevSkip;
                else take = prevTake + prevSkip;
                prevTake = take;
                prevSkip = skip;
                prevVal = v;
            }
            ans *= prevTake + prevSkip;
        }
        return ans;
    }
};

===== 2639_find_the_width_of_columns_of_a_grid (32 lines) =====
// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

#include <vector>

class Solution {
public:
    std::vector<int> findColumnWidth(std::vector<std::vector<int>>& grid) {
        int n = (int)grid[0].size();
        std::vector<int> ans(n);
        auto width = [](int x) {
            if (x == 0) return 1;
            int w = 0;
            if (x < 0) {
                w++;
                x = -x;
            }
            while (x > 0) {
                w++;
                x /= 10;
            }
            return w;
        };
        for (auto& row : grid) {
            for (int j = 0; j < n; ++j) {
                int w = width(row[j]);
                if (w > ans[j]) ans[j] = w;
            }
        }
        return ans;
    }
};

===== 2640_find_the_score_of_all_prefixes_of_an_array (19 lines) =====
// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

#include <vector>

class Solution {
public:
    std::vector<long long> findPrefixScore(std::vector<int>& nums) {
        std::vector<long long> ans(nums.size());
        int mx = 0;
        long long sum = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] > mx) mx = nums[i];
            sum += nums[i] + mx;
            ans[i] = sum;
        }
        return ans;
    }
};

===== 2641_cousins_in_binary_tree_ii (50 lines) =====
// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* replaceValueInTree(TreeNode* root) {
        if (!root) return nullptr;
        root->val = 0;
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = (int)q.size();
            int levelSum = 0;
            std::vector<TreeNode*> level;
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node);
                if (node->left) levelSum += node->left->val;
                if (node->right) levelSum += node->right->val;
            }
            for (TreeNode* node : level) {
                int cousin = levelSum;
                if (node->left) cousin -= node->left->val;
                if (node->right) cousin -= node->right->val;
                if (node->left) {
                    node->left->val = cousin;
                    q.push(node->left);
                }
                if (node->right) {
                    node->right->val = cousin;
                    q.push(node->right);
                }
            }
        }
        return root;
    }
};

===== 2642_design_graph_with_shortest_path_calculator (44 lines) =====
// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

#include <queue>
#include <vector>

class Graph {
    struct Edge {
        int to, w;
    };
    std::vector<std::vector<Edge>> g;

public:
    Graph(int n, std::vector<std::vector<int>>& edges) : g(n) {
        for (auto& e : edges) g[e[0]].push_back({e[1], e[2]});
    }

    void addEdge(std::vector<int> edge) {
        g[edge[0]].push_back({edge[1], edge[2]});
    }

    int shortestPath(int node1, int node2) {
        int n = (int)g.size();
        std::vector<int> dist(n, 1 << 30);
        dist[node1] = 0;
        using Item = std::pair<int, int>;
        std::priority_queue<Item, std::vector<Item>, std::greater<Item>> h;
        h.push({0, node1});
        while (!h.empty()) {
            auto [d, u] = h.top();
            h.pop();
            if (u == node2) return d;
            if (d > dist[u]) continue;
            for (auto& e : g[u]) {
                int nd = d + e.w;
                if (nd < dist[e.to]) {
                    dist[e.to] = nd;
                    h.push({nd, e.to});
                }
            }
        }
        return -1;
    }
};

===== 2643_row_with_maximum_ones (17 lines) =====
// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

#include <vector>

class Solution {
public:
    std::vector<int> rowAndMaximumOnes(std::vector<std::vector<int>>& mat) {
        int bestRow = 0, bestCnt = -1;
        for (int i = 0; i < (int)mat.size(); i++) {
            int cnt = 0;
            for (int v : mat[i]) cnt += v;
            if (cnt > bestCnt) { bestCnt = cnt; bestRow = i; }
        }
        return {bestRow, bestCnt};
    }
};

===== 2644_find_the_maximum_divisibility_score (19 lines) =====
// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

#include <vector>

class Solution {
public:
    int maxDivScore(std::vector<int>& nums, std::vector<int>& divisors) {
        int best = divisors[0], bestScore = -1;
        for (int d : divisors) {
            int score = 0;
            for (int x : nums) if (x % d == 0) score++;
            if (score > bestScore || (score == bestScore && d < best)) {
                bestScore = score; best = d;
            }
        }
        return best;
    }
};

===== 2645_minimum_additions_to_make_valid_string (19 lines) =====
// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

#include <string>

class Solution {
public:
    int addMinimum(std::string word) {
        int ans = 0, expect = 0, i = 0, n = (int)word.size();
        while (i < n) {
            char need = 'a' + expect;
            if (word[i] == need) i++;
            else ans++;
            expect = (expect + 1) % 3;
        }
        ans += (3 - expect) % 3;
        return ans;
    }
};

===== 2646_minimize_the_total_price_of_the_trips (36 lines) =====
// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    int minimumTotalPrice(int n, std::vector<std::vector<int>>& edges, std::vector<int>& price, std::vector<std::vector<int>>& trips) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        std::vector<int> cnt(n);
        std::function<bool(int,int,int)> path = [&](int u, int p, int target) -> bool {
            if (u == target) { cnt[u]++; return true; }
            for (int v : g[u]) {
                if (v == p) continue;
                if (path(v, u, target)) { cnt[u]++; return true; }
            }
            return false;
        };
        for (auto& t : trips) path(t[0], -1, t[1]);
        std::function<std::pair<int,int>(int,int)> dfs = [&](int u, int p) -> std::pair<int,int> {
            int full = price[u] * cnt[u], half = full / 2;
            for (int v : g[u]) {
                if (v == p) continue;
                auto [nf, hf] = dfs(v, u);
                full += std::min(nf, hf);
                half += nf;
            }
            return {full, half};
        };
        auto [a, b] = dfs(0, -1);
        return std::min(a, b);
    }
};

===== 2647_color_the_triangle_red (16 lines) =====
// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> colorRed(int n) {
        std::vector<std::vector<int>> ans;
        for (int i = 1; i <= n; i++) ans.push_back({i, 1});
        for (int i = n % 2 + 2; i <= n; i += 2)
            for (int j = 2; j <= 2 * (n - i) + 2; j++)
                ans.push_back({i, j});
        return ans;
    }
};

===== 2648_generate_fibonacci_sequence (19 lines) =====
// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

#include <functional>

class Solution {
public:
    // JS generator stand-in
    std::function<int()> fibGenerator() {
        int a = 0, b = 1;
        return [a, b]() mutable {
            int v = a;
            int na = b;
            b = a + b;
            a = na;
            return v;
        };
    }
};

===== 2649_nested_array_generator (13 lines) =====
// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

#include <vector>
#include <functional>

class Solution {
public:
    // JS nested generator stand-in: flatten nested integer arrays
    std::vector<int> inorderTraversal(std::vector<int>& arr) {
        return arr;
    }
};

===== 2650_design_cancellable_function (23 lines) =====
// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

#include <functional>
#include <utility>

class Solution {
public:
    // JS cancellable generator stand-in
    std::pair<std::function<void()>, std::function<std::pair<int,bool>()>> cancellable(std::function<int()> generator) {
        bool cancelled = false;
        bool done = false;
        int result = 0;
        auto cancel = [&cancelled]() { cancelled = true; };
        auto run = [&, generator]() -> std::pair<int,bool> {
            if (done) return {result, true};
            result = generator();
            done = true;
            return {result, !cancelled};
        };
        return {cancel, run};
    }
};

===== 2651_calculate_delayed_arrival_time (9 lines) =====
// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        return (arrivalTime + delayedTime) % 24;
    }
};

===== 2652_sum_multiples (12 lines) =====
// LeetCode 2652 - Sum Multiples
// https://leetcode.com/problems/sum-multiples/

class Solution {
public:
    int sumOfMultiples(int n) {
        int ans = 0;
        for (int i = 1; i <= n; i++)
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) ans += i;
        return ans;
    }
};

===== 2653_sliding_subarray_beauty (25 lines) =====
// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

#include <vector>

class Solution {
public:
    std::vector<int> getSubarrayBeauty(std::vector<int>& nums, int k, int x) {
        int freq[101] = {};
        std::vector<int> ans(nums.size() - k + 1);
        for (int i = 0; i < (int)nums.size(); i++) {
            freq[nums[i] + 50]++;
            if (i >= k) freq[nums[i - k] + 50]--;
            if (i >= k - 1) {
                int need = x, val = 0;
                for (int j = 0; j < 50; j++) {
                    need -= freq[j];
                    if (need <= 0) { val = j - 50; break; }
                }
                ans[i - k + 1] = val;
            }
        }
        return ans;
    }
};

===== 2654_minimum_number_of_operations_to_make_all_array_elements_equal_to_1 (26 lines) =====
// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = (int)nums.size(), ones = 0;
        for (int x : nums) if (x == 1) ones++;
        if (ones > 0) return n - ones;
        auto gcd = [](int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; };
        int best = n + 1;
        for (int i = 0; i < n; i++) {
            int g = 0;
            for (int j = i; j < n; j++) {
                g = gcd(g, nums[j]);
                if (g == 1) { best = std::min(best, j - i); break; }
            }
        }
        if (best == n + 1) return -1;
        return best + n - 1;
    }
};

===== 2655_find_maximal_uncovered_ranges (20 lines) =====
// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> findMaximalUncoveredRanges(int n, std::vector<std::vector<int>>& ranges) {
        std::sort(ranges.begin(), ranges.end());
        std::vector<std::vector<int>> ans;
        int cur = 0;
        for (auto& r : ranges) {
            if (r[0] > cur) ans.push_back({cur, r[0] - 1});
            if (r[1] + 1 > cur) cur = r[1] + 1;
        }
        if (cur < n) ans.push_back({cur, n - 1});
        return ans;
    }
};

===== 2656_maximum_sum_with_exactly_k_elements (13 lines) =====
// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximizeSum(std::vector<int>& nums, int k) {
        int mx = *std::max_element(nums.begin(), nums.end());
        return k * mx + k * (k - 1) / 2;
    }
};

===== 2657_find_the_prefix_common_array_of_two_arrays (22 lines) =====
// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

#include <vector>

class Solution {
public:
    std::vector<int> findThePrefixCommonArray(std::vector<int>& A, std::vector<int>& B) {
        int n = (int)A.size();
        std::vector<char> seenA(n + 1), seenB(n + 1);
        std::vector<int> ans(n);
        int common = 0;
        for (int i = 0; i < n; i++) {
            if (seenB[A[i]]) common++;
            seenA[A[i]] = 1;
            if (seenA[B[i]]) common++;
            seenB[B[i]] = 1;
            ans[i] = common;
        }
        return ans;
    }
};

===== 2658_maximum_number_of_fish_in_a_grid (24 lines) =====
// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    int findMaxFish(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::function<int(int,int)> dfs = [&](int r, int c) -> int {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return 0;
            int fish = grid[r][c];
            grid[r][c] = 0;
            return fish + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1);
        };
        int best = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] > 0) best = std::max(best, dfs(i, j));
        return best;
    }
};

===== 2659_make_array_empty (20 lines) =====
// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

#include <vector>
#include <algorithm>
#include <numeric>

class Solution {
public:
    long long countOperationsToEmptyArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> idx(n);
        std::iota(idx.begin(), idx.end(), 0);
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return nums[a] < nums[b]; });
        long long ans = n;
        for (int i = 1; i < n; i++)
            if (idx[i] < idx[i - 1]) ans += n - i;
        return ans;
    }
};

===== 2660_determine_the_winner_of_a_bowling_game (23 lines) =====
// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

#include <vector>

class Solution {
public:
    int isWinner(std::vector<int>& player1, std::vector<int>& player2) {
        auto score = [](std::vector<int>& p) {
            int s = 0;
            for (int i = 0; i < (int)p.size(); i++) {
                int mul = 1;
                if ((i > 0 && p[i-1] == 10) || (i > 1 && p[i-2] == 10)) mul = 2;
                s += mul * p[i];
            }
            return s;
        };
        int a = score(player1), b = score(player2);
        if (a > b) return 1;
        if (b > a) return 2;
        return 0;
    }
};

===== 2661_first_completely_painted_row_or_column (22 lines) =====
// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

#include <vector>

class Solution {
public:
    int firstCompleteIndex(std::vector<int>& arr, std::vector<std::vector<int>>& mat) {
        int m = (int)mat.size(), n = (int)mat[0].size();
        std::vector<std::pair<int,int>> pos(m * n + 1);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                pos[mat[i][j]] = {i, j};
        std::vector<int> rowCnt(m), colCnt(n);
        for (int i = 0; i < (int)arr.size(); i++) {
            auto [r, c] = pos[arr[i]];
            rowCnt[r]++; colCnt[c]++;
            if (rowCnt[r] == n || colCnt[c] == m) return i;
        }
        return -1;
    }
};

===== 2662_minimum_cost_of_a_path_with_special_roads (50 lines) =====
// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

#include <vector>
#include <queue>
#include <cmath>
#include <climits>

class Solution {
public:
    int minimumCost(std::vector<int>& start, std::vector<int>& target, std::vector<std::vector<int>>& specialRoads) {
        std::vector<std::vector<int>> points = {start, target};
        for (auto& r : specialRoads) {
            points.push_back({r[0], r[1]});
            points.push_back({r[2], r[3]});
        }
        int N = (int)points.size();
        auto distMan = [](std::vector<int>& a, std::vector<int>& b) {
            return std::abs(a[0]-b[0]) + std::abs(a[1]-b[1]);
        };
        std::vector<std::vector<std::pair<int,int>>> g(N);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (i != j) g[i].push_back({j, distMan(points[i], points[j])});
        for (auto& r : specialRoads) {
            int u = -1, v = -1;
            for (int i = 0; i < N; i++) {
                if (points[i][0] == r[0] && points[i][1] == r[1]) u = i;
                if (points[i][0] == r[2] && points[i][1] == r[3]) v = i;
            }
            if (u >= 0 && v >= 0) g[u].push_back({v, r[4]});
        }
        std::vector<int> dist(N, INT_MAX / 4);
        dist[0] = 0;
        using P = std::pair<int,int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [cost, id] = pq.top(); pq.pop();
            if (cost > dist[id]) continue;
            for (auto [to, w] : g[id]) {
                if (cost + w < dist[to]) {
                    dist[to] = cost + w;
                    pq.push({dist[to], to});
                }
            }
        }
        return dist[1];
    }
};

===== 2663_lexicographically_smallest_beautiful_string (27 lines) =====
// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

#include <string>

class Solution {
public:
    std::string smallestBeautifulString(std::string s, int k) {
        int n = (int)s.size();
        std::string b = s;
        for (int i = n - 1; i >= 0; i--) {
            for (char c = b[i] + 1; c < 'a' + k; c++) {
                if ((i > 0 && c == b[i-1]) || (i > 1 && c == b[i-2])) continue;
                b[i] = c;
                for (int j = i + 1; j < n; j++) {
                    for (char nc = 'a'; nc < 'a' + k; nc++) {
                        if ((j > 0 && nc == b[j-1]) || (j > 1 && nc == b[j-2])) continue;
                        b[j] = nc;
                        break;
                    }
                }
                return b;
            }
        }
        return "";
    }
};

===== 2664_the_knights_tour (26 lines) =====
// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

#include <vector>
#include <functional>

class Solution {
public:
    std::vector<std::vector<int>> tourOfKnight(int m, int n, int r, int c) {
        std::vector<std::vector<int>> ans(m, std::vector<int>(n, -1));
        int dirs[8][2] = {{1,2},{1,-2},{-1,2},{-1,-2},{2,1},{2,-1},{-2,1},{-2,-1}};
        std::function<bool(int,int,int)> dfs = [&](int x, int y, int step) -> bool {
            ans[x][y] = step;
            if (step == m * n - 1) return true;
            for (auto& d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1)
                    if (dfs(nx, ny, step + 1)) return true;
            }
            ans[x][y] = -1;
            return false;
        };
        dfs(r, c, 0);
        return ans;
    }
};

===== 2665_counter_ii (21 lines) =====
// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

#include <memory>

// JS Counter II stand-in
class CounterII {
    int init_, cur_;
public:
    CounterII(int init) : init_(init), cur_(init) {}
    int increment() { return ++cur_; }
    int decrement() { return --cur_; }
    int reset() { cur_ = init_; return cur_; }
};

class Solution {
public:
    CounterII* createCounter(int init) {
        return new CounterII(init);
    }
};

===== 2666_allow_one_function_call (20 lines) =====
// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

#include <functional>
#include <optional>

class Solution {
public:
    // JS once stand-in
    std::function<std::optional<int>(int)> once(std::function<int(int)> fn) {
        bool called = false;
        int res = 0;
        return [fn, called, res](int arg) mutable -> std::optional<int> {
            if (called) return std::nullopt;
            called = true;
            res = fn(arg);
            return res;
        };
    }
};

===== 2667_create_hello_world_function (13 lines) =====
// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

#include <functional>
#include <string>

class Solution {
public:
    // JS hello world stand-in
    std::function<std::string()> createHelloWorld() {
        return []() { return std::string("Hello World"); };
    }
};

===== 2670_find_the_distinct_difference_array (25 lines) =====
// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<int> distinctDifferenceArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> suf(n + 1);
        std::unordered_set<int> seen;
        for (int i = n - 1; i >= 0; i--) {
            seen.insert(nums[i]);
            suf[i] = (int)seen.size();
        }
        seen.clear();
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            seen.insert(nums[i]);
            ans[i] = (int)seen.size() - suf[i + 1];
        }
        return ans;
    }
};

===== 2671_frequency_tracker (26 lines) =====
// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

#include <unordered_map>

class FrequencyTracker {
    std::unordered_map<int, int> freq, count;
public:
    FrequencyTracker() {}
    void add(int number) {
        int old = freq[number];
        if (old > 0) count[old]--;
        freq[number] = old + 1;
        count[old + 1]++;
    }
    void deleteOne(int number) {
        int old = freq[number];
        if (old == 0) return;
        count[old]--;
        freq[number] = old - 1;
        if (old - 1 > 0) count[old - 1]++;
    }
    bool hasFrequency(int frequency) {
        return count[frequency] > 0;
    }
};

===== 2672_number_of_adjacent_elements_with_the_same_color (24 lines) =====
// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

#include <vector>

class Solution {
public:
    std::vector<int> colorTheArray(int n, std::vector<std::vector<int>>& queries) {
        std::vector<int> colors(n), ans(queries.size());
        int same = 0;
        for (int i = 0; i < (int)queries.size(); i++) {
            int idx = queries[i][0], color = queries[i][1];
            if (colors[idx] != 0) {
                if (idx > 0 && colors[idx] == colors[idx - 1]) same--;
                if (idx + 1 < n && colors[idx] == colors[idx + 1]) same--;
            }
            colors[idx] = color;
            if (idx > 0 && colors[idx] == colors[idx - 1]) same++;
            if (idx + 1 < n && colors[idx] == colors[idx + 1]) same++;
            ans[i] = same;
        }
        return ans;
    }
};

===== 2673_make_costs_of_paths_equal_in_a_binary_tree (18 lines) =====
// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

#include <vector>
#include <cstdlib>

class Solution {
public:
    int minIncrements(int n, std::vector<int>& cost) {
        int ans = 0;
        for (int i = n / 2 - 1; i >= 0; i--) {
            int l = 2 * i + 1, r = 2 * i + 2;
            ans += std::abs(cost[l] - cost[r]);
            cost[i] += std::max(cost[l], cost[r]);
        }
        return ans;
    }
};

===== 2674_split_a_circular_linked_list (29 lines) =====
// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    std::vector<ListNode*> splitCircularLinkedList(ListNode* list) {
        if (!list) return {nullptr, nullptr};
        ListNode *slow = list, *fast = list;
        while (fast->next != list && fast->next->next != list) {
            slow = slow->next;
            fast = fast->next->next;
        }
        if (fast->next->next == list) fast = fast->next;
        ListNode* head2 = slow->next;
        slow->next = list;
        fast->next = head2;
        return {list, head2};
    }
};

===== 2675_array_of_objects_to_matrix (28 lines) =====
// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>

class Solution {
public:
    // JS array-of-objects-to-matrix stand-in
    std::vector<std::vector<std::string>> jsonToMatrix(std::vector<std::map<std::string, std::string>>& arr) {
        std::set<std::string> keys;
        for (auto& obj : arr) for (auto& [k, _] : obj) keys.insert(k);
        std::vector<std::vector<std::string>> mat;
        mat.push_back(std::vector<std::string>(keys.begin(), keys.end()));
        for (auto& obj : arr) {
            std::vector<std::string> row;
            for (auto& k : keys) {
                auto it = obj.find(k);
                row.push_back(it == obj.end() ? "" : it->second);
            }
            mat.push_back(row);
        }
        return mat;
    }
};

===== 2676_throttle (20 lines) =====
// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

#include <functional>
#include <chrono>

class Solution {
public:
    // JS throttle stand-in: calls fn at most once per t ms (wall clock)
    std::function<void()> throttle(std::function<void()> fn, int t) {
        auto last = std::chrono::steady_clock::now() - std::chrono::hours(24);
        return [fn, t, last]() mutable {
            auto now = std::chrono::steady_clock::now();
            if (std::chrono::duration_cast<std::chrono::milliseconds>(now - last).count() >= t) {
                last = now;
                fn();
            }
        };
    }
};

===== 2677_chunk_array (17 lines) =====
// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> chunk(std::vector<int>& arr, int size) {
        std::vector<std::vector<int>> ans;
        for (int i = 0; i < (int)arr.size(); i += size) {
            std::vector<int> part;
            for (int j = i; j < (int)arr.size() && j < i + size; j++) part.push_back(arr[j]);
            ans.push_back(part);
        }
        return ans;
    }
};

===== 2678_number_of_senior_citizens (17 lines) =====
// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

#include <vector>
#include <string>

class Solution {
public:
    int countSeniors(std::vector<std::string>& details) {
        int ans = 0;
        for (auto& d : details) {
            int age = (d[11] - '0') * 10 + (d[12] - '0');
            if (age > 60) ans++;
        }
        return ans;
    }
};

===== 2679_sum_in_a_matrix (19 lines) =====
// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

#include <vector>
#include <algorithm>

class Solution {
public:
    int matrixSum(std::vector<std::vector<int>>& nums) {
        for (auto& row : nums) std::sort(row.begin(), row.end());
        int ans = 0, n = (int)nums[0].size();
        for (int j = 0; j < n; j++) {
            int mx = 0;
            for (auto& row : nums) mx = std::max(mx, row[j]);
            ans += mx;
        }
        return ans;
    }
};

===== 2680_maximum_or (20 lines) =====
// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

#include <vector>

class Solution {
public:
    long long maximumOr(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1), suf(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] | nums[i];
        for (int i = n - 1; i >= 0; i--) suf[i] = suf[i + 1] | nums[i];
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long cur = pref[i] | ((long long)nums[i] << k) | suf[i + 1];
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};

===== 2681_power_of_heroes (19 lines) =====
// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

#include <vector>
#include <algorithm>

class Solution {
public:
    int sumOfPower(std::vector<int>& nums) {
        const int MOD = 1000000007;
        std::sort(nums.begin(), nums.end());
        long long ans = 0, s = 0;
        for (int x : nums) {
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD;
            s = (s * 2 + x) % MOD;
        }
        return (int)ans;
    }
};

===== 2682_find_the_losers_of_the_circular_game (20 lines) =====
// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

#include <vector>

class Solution {
public:
    std::vector<int> circularGameLosers(int n, int k) {
        std::vector<char> seen(n + 1);
        int cur = 1, step = 1;
        while (!seen[cur]) {
            seen[cur] = 1;
            cur = (cur - 1 + step * k) % n + 1;
            step++;
        }
        std::vector<int> ans;
        for (int i = 1; i <= n; i++) if (!seen[i]) ans.push_back(i);
        return ans;
    }
};

===== 2683_neighboring_bitwise_xor (13 lines) =====
// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

#include <vector>

class Solution {
public:
    bool doesValidArrayExist(std::vector<int>& derived) {
        int x = 0;
        for (int v : derived) x ^= v;
        return x == 0;
    }
};

===== 2684_maximum_number_of_moves_in_a_grid (27 lines) =====
// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxMoves(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<int> dp(m, 0);
        for (int c = n - 2; c >= 0; c--) {
            std::vector<int> ndp(m, 0);
            for (int r = 0; r < m; r++) {
                int best = 0;
                for (int dr = -1; dr <= 1; dr++) {
                    int nr = r + dr;
                    if (nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c])
                        best = std::max(best, 1 + dp[nr]);
                }
                ndp[r] = best;
            }
            dp.swap(ndp);
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};

===== 2685_count_the_number_of_complete_components (30 lines) =====
// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

#include <vector>
#include <functional>

class Solution {
public:
    int countCompleteComponents(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        std::vector<char> vis(n);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (vis[i]) continue;
            std::vector<int> nodes;
            std::function<void(int)> dfs = [&](int u) {
                vis[u] = 1; nodes.push_back(u);
                for (int v : g[u]) if (!vis[v]) dfs(v);
            };
            dfs(i);
            int ecount = 0;
            for (int u : nodes) ecount += (int)g[u].size();
            ecount /= 2;
            int sz = (int)nodes.size();
            if (ecount == sz * (sz - 1) / 2) ans++;
        }
        return ans;
    }
};

===== 2689_extract_kth_character_from_the_rope_tree (24 lines) =====
// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

struct RopeTreeNode {
    int len;
    char val;
    RopeTreeNode* left;
    RopeTreeNode* right;
    RopeTreeNode() : len(0), val(0), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    char getKthCharacter(RopeTreeNode* root, int k) {
        auto dfs = [&](auto&& self, RopeTreeNode* node, int kk) -> char {
            if (!node->left && !node->right) return node->val;
            int leftLen = 0;
            if (node->left) leftLen = node->left->len > 0 ? node->left->len : 1;
            if (kk <= leftLen) return self(self, node->left, kk);
            return self(self, node->right, kk - leftLen);
        };
        return dfs(dfs, root, k);
    }
};

===== 2690_infinite_method_object (13 lines) =====
// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

#include <functional>
#include <string>

class Solution {
public:
    // JS infinite method object stand-in
    std::function<std::string(std::string)> createInfiniteObject() {
        return [](std::string) { return std::string("Hello World"); };
    }
};

===== 2691_immutability_helper (23 lines) =====
// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

#include <map>
#include <string>
#include <vector>
#include <functional>

class Solution {
public:
    // JS immutability helper stand-in
    std::vector<std::map<std::string, int>> immutableHelper(
        std::map<std::string, int> obj,
        std::vector<std::function<void(std::map<std::string, int>&)>> mutators) {
        std::vector<std::map<std::string, int>> out;
        for (auto& m : mutators) {
            auto copy = obj;
            m(copy);
            out.push_back(copy);
        }
        return out;
    }
};

===== 2692_make_object_immutable (13 lines) =====
// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

#include <map>
#include <string>

class Solution {
public:
    // JS makeImmutable stand-in: return copy
    std::map<std::string, int> makeImmutable(std::map<std::string, int> obj) {
        return obj;
    }
};

===== 2693_call_function_with_custom_context (13 lines) =====
// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

#include <functional>

class Solution {
public:
    // JS call stand-in
    int call(std::function<int(int, int)> fn, int ctx, int arg) {
        (void)ctx;
        return fn(ctx, arg);
    }
};

===== 2694_event_emitter (38 lines) =====
// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

#include <unordered_map>
#include <vector>
#include <string>
#include <functional>

// JS EventEmitter stand-in
class EventEmitter {
    std::unordered_map<std::string, std::vector<std::function<void(const std::vector<int>&)>>> handlers;
public:
    EventEmitter() {}
    std::function<void()> subscribe(std::string eventName, std::function<void(const std::vector<int>&)> callback) {
        handlers[eventName].push_back(callback);
        int idx = (int)handlers[eventName].size() - 1;
        return [this, eventName, idx]() mutable {
            auto& v = handlers[eventName];
            if (idx >= 0 && idx < (int)v.size()) {
                v.erase(v.begin() + idx);
                idx = -1;
            }
        };
    }
    std::vector<int> emit(std::string eventName, std::vector<int> args) {
        std::vector<int> res;
        for (auto& cb : handlers[eventName]) {
            cb(args);
            res.push_back(0);
        }
        return res;
    }
};

class Solution {
public:
    EventEmitter createEmitter() { return EventEmitter(); }
};

===== 2695_array_wrapper (33 lines) =====
// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

#include <vector>
#include <string>
#include <sstream>

// JS ArrayWrapper stand-in
class ArrayWrapper {
    std::vector<int> nums;
public:
    ArrayWrapper(std::vector<int> nums) : nums(std::move(nums)) {}
    int valueOf() const {
        int s = 0;
        for (int x : nums) s += x;
        return s;
    }
    std::string toString() const {
        std::ostringstream oss;
        oss << '[';
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i) oss << ',';
            oss << nums[i];
        }
        oss << ']';
        return oss.str();
    }
};

class Solution {
public:
    ArrayWrapper ArrayWrapperCreate(std::vector<int> nums) { return ArrayWrapper(std::move(nums)); }
};

===== 2696_minimum_string_length_after_removing_substrings (17 lines) =====
// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

#include <string>

class Solution {
public:
    int minLength(std::string s) {
        std::string st;
        for (char c : s) {
            if (!st.empty() && ((st.back() == 'A' && c == 'B') || (st.back() == 'C' && c == 'D')))
                st.pop_back();
            else st.push_back(c);
        }
        return (int)st.size();
    }
};

===== 2697_lexicographically_smallest_palindrome (17 lines) =====
// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

#include <string>
#include <algorithm>

class Solution {
public:
    std::string makeSmallestPalindrome(std::string s) {
        int n = (int)s.size();
        for (int i = 0; i < n / 2; i++) {
            char c = std::min(s[i], s[n - 1 - i]);
            s[i] = s[n - 1 - i] = c;
        }
        return s;
    }
};

===== 2698_find_the_punishment_number_of_an_integer (32 lines) =====
// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

#include <string>
#include <functional>

class Solution {
public:
    int punishmentNumber(int n) {
        auto can = [](int sq, int target) {
            std::string s = std::to_string(sq);
            int m = (int)s.size();
            std::function<bool(int,int)> dfs = [&](int i, int sum) -> bool {
                if (i == m) return sum == target;
                int cur = 0;
                for (int j = i; j < m; j++) {
                    cur = cur * 10 + (s[j] - '0');
                    if (sum + cur > target) break;
                    if (dfs(j + 1, sum + cur)) return true;
                }
                return false;
            };
            return dfs(0, 0);
        };
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int sq = i * i;
            if (can(sq, i)) ans += sq;
        }
        return ans;
    }
};

===== 2699_modify_graph_edge_weights (54 lines) =====
// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

#include <vector>
#include <queue>
#include <climits>

class Solution {
public:
    std::vector<std::vector<int>> modifiedGraphEdges(int n, std::vector<std::vector<int>>& edges, int source, int destination, int target) {
        const int INF = 2000000000;
        auto dijkstra = [&](bool ignoreNeg) {
            std::vector<int> dist(n, INF);
            dist[source] = 0;
            using P = std::pair<int,int>;
            std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
            pq.push({0, source});
            while (!pq.empty()) {
                auto [d, u] = pq.top(); pq.pop();
                if (d != dist[u]) continue;
                for (int i = 0; i < (int)edges.size(); i++) {
                    int a = edges[i][0], b = edges[i][1], w = edges[i][2];
                    if (a != u && b != u) continue;
                    int to = a == u ? b : a;
                    if (w == -1) {
                        if (ignoreNeg) continue;
                        w = 1;
                    }
                    if (d + w < dist[to]) {
                        dist[to] = d + w;
                        pq.push({dist[to], to});
                    }
                }
            }
            return dist;
        };
        auto d = dijkstra(true);
        if (d[destination] < target) return {};
        bool matched = d[destination] == target;
        for (int i = 0; i < (int)edges.size(); i++) {
            if (edges[i][2] != -1) continue;
            if (matched) { edges[i][2] = INF; continue; }
            edges[i][2] = 1;
            d = dijkstra(false);
            if (d[destination] <= target) {
                edges[i][2] += target - d[destination];
                matched = true;
            }
        }
        d = dijkstra(false);
        if (d[destination] != target) return {};
        return edges;
    }
};

===== 2700_differences_between_two_objects (19 lines) =====
// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

#include <map>
#include <string>
#include <vector>

class Solution {
public:
    // JS objDiff stand-in: keys where values differ
    std::map<std::string, std::vector<int>> objDiff(std::map<std::string, int>& obj1, std::map<std::string, int>& obj2) {
        std::map<std::string, std::vector<int>> diff;
        for (auto& [k, v] : obj1) {
            auto it = obj2.find(k);
            if (it != obj2.end() && it->second != v) diff[k] = {v, it->second};
        }
        return diff;
    }
};

===== 2702_minimum_operations_to_make_numbers_non_positive (31 lines) =====
// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int x, int y) {
        auto ok = [&](int ops) {
            long long extra = 0;
            for (int v : nums) {
                long long remain = v - 1LL * ops * y;
                if (remain > 0) extra += (remain + (x - y) - 1) / (x - y);
            }
            return extra <= ops;
        };
        int lo = 0, hi = 0;
        for (int v : nums) {
            hi = std::max(hi, (v + y - 1) / y);
            hi = std::max(hi, (v + x - 1) / x);
        }
        hi += (int)nums.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};

===== 2703_return_length_of_arguments_passed (12 lines) =====
// LeetCode 2703 - Return Length of Arguments Passed
// https://leetcode.com/problems/return-length-of-arguments-passed/

#include <vector>

class Solution {
public:
    // JS argumentsLength stand-in
    int argumentsLength(std::vector<int>& args) {
        return (int)args.size();
    }
};

===== 2704_to_be_or_not_to_be (23 lines) =====
// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

#include <stdexcept>

class Expect {
    int val;
public:
    Expect(int v) : val(v) {}
    bool toBe(int other) {
        if (val == other) return true;
        throw std::runtime_error("Not Equal");
    }
    bool notToBe(int other) {
        if (val != other) return true;
        throw std::runtime_error("Equal");
    }
};

class Solution {
public:
    Expect expect(int val) { return Expect(val); }
};

===== 2705_compact_object (16 lines) =====
// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

#include <vector>
#include <map>
#include <string>

class Solution {
public:
    // JS compactObject stand-in for int vectors: drop zeros
    std::vector<int> compactObject(std::vector<int>& obj) {
        std::vector<int> out;
        for (int x : obj) if (x) out.push_back(x);
        return out;
    }
};

===== 2706_buy_two_chocolates (14 lines) =====
// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

#include <vector>
#include <algorithm>

class Solution {
public:
    int buyChoco(std::vector<int>& prices, int money) {
        std::sort(prices.begin(), prices.end());
        int cost = prices[0] + prices[1];
        return cost <= money ? money - cost : money;
    }
};

===== 2707_extra_characters_in_a_string (25 lines) =====
// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int minExtraChar(std::string s, std::vector<std::string>& dictionary) {
        std::unordered_set<std::string> dict(dictionary.begin(), dictionary.end());
        int n = (int)s.size();
        std::vector<int> dp(n + 1, n);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            dp[i + 1] = std::min(dp[i + 1], dp[i] + 1);
            for (int j = i + 1; j <= n; j++) {
                if (dict.count(s.substr(i, j - i)))
                    dp[j] = std::min(dp[j], dp[i]);
            }
        }
        return dp[n];
    }
};

===== 2708_maximum_strength_of_a_group (34 lines) =====
// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxStrength(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        if (n == 1) return nums[0];
        long long prod = 1;
        bool used = false;
        int i = 0;
        while (i + 1 < n && nums[i] < 0 && nums[i + 1] < 0) {
            prod *= 1LL * nums[i] * nums[i + 1];
            used = true;
            i += 2;
        }
        bool negLeft = i < n && nums[i] < 0;
        for (; i < n; i++) {
            if (nums[i] > 0) { prod *= nums[i]; used = true; }
        }
        if (!used) {
            if (negLeft) {
                for (int x : nums) if (x == 0) return 0;
                return nums[n - 1];
            }
            return 0;
        }
        return prod;
    }
};

===== 2709_greatest_common_divisor_traversal (42 lines) =====
// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    bool canTraverseAllPairs(std::vector<int>& nums) {
        int n = (int)nums.size();
        if (n == 1) return true;
        int mx = *std::max_element(nums.begin(), nums.end());
        std::vector<int> parent(mx + 1);
        for (int i = 0; i <= mx; i++) parent[i] = i;
        std::function<int(int)> find = [&](int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra != rb) parent[ra] = rb;
        };
        std::vector<char> has(mx + 1);
        for (int x : nums) {
            if (x == 1) return false;
            has[x] = 1;
        }
        std::vector<int> sieve(mx + 1);
        for (int i = 2; i <= mx; i++) {
            if (sieve[i] == 0) {
                for (int j = i; j <= mx; j += i) {
                    if (sieve[j] == 0) sieve[j] = i;
                    if (has[j]) unite(i, j);
                }
            }
        }
        int root = find(nums[0]);
        for (int x : nums) if (find(x) != root) return false;
        return true;
    }
};

===== 2710_remove_trailing_zeros_from_a_string (12 lines) =====
// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

#include <string>

class Solution {
public:
    std::string removeTrailingZeros(std::string num) {
        while (!num.empty() && num.back() == '0') num.pop_back();
        return num;
    }
};

===== 2711_difference_of_number_of_distinct_values_on_diagonals (23 lines) =====
// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

#include <vector>
#include <unordered_set>
#include <cstdlib>

class Solution {
public:
    std::vector<std::vector<int>> differenceOfDistinctValues(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> ans(m, std::vector<int>(n));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                std::unordered_set<int> top, bot;
                for (int r = i - 1, c = j - 1; r >= 0 && c >= 0; r--, c--) top.insert(grid[r][c]);
                for (int r = i + 1, c = j + 1; r < m && c < n; r++, c++) bot.insert(grid[r][c]);
                ans[i][j] = std::abs((int)top.size() - (int)bot.size());
            }
        }
        return ans;
    }
};

===== 2712_minimum_cost_to_make_all_characters_equal (17 lines) =====
// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

#include <string>
#include <algorithm>

class Solution {
public:
    long long minimumCost(std::string s) {
        int n = (int)s.size();
        long long ans = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] != s[i - 1]) ans += std::min(i, n - i);
        }
        return ans;
    }
};

===== 2713_maximum_strictly_increasing_cells_in_a_matrix (40 lines) =====
// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxIncreasingCells(std::vector<std::vector<int>>& mat) {
        int m = (int)mat.size(), n = (int)mat[0].size();
        struct Cell { int v, r, c; };
        std::vector<Cell> cells;
        cells.reserve(m * n);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                cells.push_back({mat[i][j], i, j});
        std::sort(cells.begin(), cells.end(), [](auto& a, auto& b) { return a.v < b.v; });
        std::vector<int> rowMax(m), colMax(n);
        std::vector<std::vector<int>> dp(m, std::vector<int>(n));
        int ans = 0;
        for (int i = 0; i < (int)cells.size(); ) {
            int j = i;
            while (j < (int)cells.size() && cells[j].v == cells[i].v) j++;
            std::vector<std::tuple<int,int,int>> buf;
            for (int k = i; k < j; k++) {
                int r = cells[k].r, c = cells[k].c;
                int best = std::max(rowMax[r], colMax[c]);
                dp[r][c] = best + 1;
                ans = std::max(ans, dp[r][c]);
                buf.push_back({r, c, dp[r][c]});
            }
            for (auto [r, c, val] : buf) {
                rowMax[r] = std::max(rowMax[r], val);
                colMax[c] = std::max(colMax[c], val);
            }
            i = j;
        }
        return ans;
    }
};

===== 2714_find_shortest_path_with_k_hops (39 lines) =====
// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

#include <vector>
#include <queue>
#include <climits>
#include <tuple>

class Solution {
public:
    int shortestPathWithHops(int n, std::vector<std::vector<int>>& edges, int s, int d, int k) {
        std::vector<std::vector<std::pair<int,int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        std::vector<std::vector<int>> dist(n, std::vector<int>(k + 1, INT_MAX / 4));
        dist[s][0] = 0;
        using T = std::tuple<int,int,int>; // dist, node, hops
        std::priority_queue<T, std::vector<T>, std::greater<T>> pq;
        pq.push({0, s, 0});
        while (!pq.empty()) {
            auto [cd, u, hops] = pq.top(); pq.pop();
            if (u == d) return cd;
            if (cd > dist[u][hops]) continue;
            for (auto [to, w] : g[u]) {
                if (cd + w < dist[to][hops]) {
                    dist[to][hops] = cd + w;
                    pq.push({dist[to][hops], to, hops});
                }
                if (hops < k && cd < dist[to][hops + 1]) {
                    dist[to][hops + 1] = cd;
                    pq.push({cd, to, hops + 1});
                }
            }
        }
        return -1;
    }
};

===== 2715_timeout_cancellation (20 lines) =====
// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

#include <functional>
#include <optional>

class Solution {
public:
    // JS timeout cancellation stand-in
    std::pair<std::function<void()>, std::function<std::optional<int>()>> cancellable(
        std::function<int()> fn, int /*t*/) {
        bool cancelled = false;
        auto cancel = [&cancelled]() { cancelled = true; };
        auto result = [fn, &cancelled]() -> std::optional<int> {
            if (cancelled) return std::nullopt;
            return fn();
        };
        return {cancel, result};
    }
};

===== 2716_minimize_string_length (12 lines) =====
// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

#include <string>
#include <unordered_set>

class Solution {
public:
    int minimizedStringLength(std::string s) {
        return (int)std::unordered_set<char>(s.begin(), s.end()).size();
    }
};

===== 2717_semi_ordered_permutation (18 lines) =====
// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

#include <vector>

class Solution {
public:
    int semiOrderedPermutation(std::vector<int>& nums) {
        int n = (int)nums.size(), p1 = 0, pn = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) p1 = i;
            if (nums[i] == n) pn = i;
        }
        int ans = p1 + (n - 1 - pn);
        if (p1 > pn) ans--;
        return ans;
    }
};

===== 2718_sum_of_matrix_after_queries (30 lines) =====
// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

#include <vector>

class Solution {
public:
    long long matrixSumQueries(int n, std::vector<std::vector<int>>& queries) {
        std::vector<char> rowDone(n), colDone(n);
        int rowsLeft = n, colsLeft = n;
        long long ans = 0;
        for (int i = (int)queries.size() - 1; i >= 0; i--) {
            int type = queries[i][0], idx = queries[i][1], val = queries[i][2];
            if (type == 0) {
                if (!rowDone[idx]) {
                    ans += 1LL * val * colsLeft;
                    rowDone[idx] = 1;
                    rowsLeft--;
                }
            } else {
                if (!colDone[idx]) {
                    ans += 1LL * val * rowsLeft;
                    colDone[idx] = 1;
                    colsLeft--;
                }
            }
        }
        return ans;
    }
};

===== 2719_count_of_integers (39 lines) =====
// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

#include <string>
#include <functional>
#include <map>
#include <array>

class Solution {
public:
    int count(std::string num1, std::string num2, int min_sum, int max_sum) {
        const int MOD = 1000000007;
        auto dec = [](std::string s) {
            int i = (int)s.size() - 1;
            while (i >= 0 && s[i] == '0') { s[i] = '9'; i--; }
            if (i >= 0) s[i]--;
            int j = 0;
            while (j < (int)s.size() - 1 && s[j] == '0') j++;
            return s.substr(j);
        };
        auto dp = [&](std::string s) {
            int n = (int)s.size();
            std::map<std::array<int,3>, int> memo;
            std::function<int(int,int,bool)> dfs = [&](int pos, int sum, bool tight) -> int {
                if (sum > max_sum) return 0;
                if (pos == n) return sum >= min_sum ? 1 : 0;
                std::array<int,3> key = {pos, sum, tight ? 1 : 0};
                if (memo.count(key)) return memo[key];
                int up = tight ? s[pos] - '0' : 9;
                int res = 0;
                for (int d = 0; d <= up; d++)
                    res = (res + dfs(pos + 1, sum + d, tight && d == up)) % MOD;
                return memo[key] = res;
            };
            return dfs(0, 0, true);
        };
        return (dp(num2) - dp(dec(num1)) + MOD) % MOD;
    }
};

===== 2721_execute_asynchronous_functions_in_parallel (15 lines) =====
// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

#include <vector>
#include <functional>

class Solution {
public:
    // JS promiseAll stand-in: run sync functions in order
    std::vector<int> promiseAll(std::vector<std::function<int()>>& functions) {
        std::vector<int> out;
        for (auto& f : functions) out.push_back(f());
        return out;
    }
};

===== 2722_join_two_arrays_by_id (28 lines) =====
// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

#include <vector>
#include <map>
#include <string>
#include <algorithm>

class Solution {
public:
    // JS join-by-id stand-in for maps with int id
    std::vector<std::map<std::string, int>> join(
        std::vector<std::map<std::string, int>>& arr1,
        std::vector<std::map<std::string, int>>& arr2) {
        std::map<int, std::map<std::string, int>> byId;
        auto merge = [&](std::vector<std::map<std::string, int>>& arr) {
            for (auto& obj : arr) {
                int id = obj.at("id");
                auto& dest = byId[id];
                for (auto& [k, v] : obj) dest[k] = v;
            }
        };
        merge(arr1); merge(arr2);
        std::vector<std::map<std::string, int>> out;
        for (auto& [_, obj] : byId) out.push_back(obj);
        return out;
    }
};

===== 2723_add_two_promises (12 lines) =====
// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

#include <functional>

class Solution {
public:
    // JS addTwoPromises stand-in
    int addTwoPromises(std::function<int()> promise1, std::function<int()> promise2) {
        return promise1() + promise2();
    }
};

===== 2724_sort_by (16 lines) =====
// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    // JS sortBy stand-in
    std::vector<int> sortBy(std::vector<int>& arr, std::function<double(int)> fn) {
        std::vector<int> out = arr;
        std::sort(out.begin(), out.end(), [&](int a, int b) { return fn(a) < fn(b); });
        return out;
    }
};

