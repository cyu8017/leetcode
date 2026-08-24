
================================================================================
FOLDER 0678_valid_parenthesis_string
================================================================================
// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

#include <algorithm>
#include <string>

class Solution {
public:
    bool checkValidString(std::string s) {
        int lo = 0;
        int hi = 0;
        for (char ch : s) {
            if (ch == '(') {
                ++lo;
                ++hi;
            } else if (ch == ')') {
                lo = std::max(lo - 1, 0);
                --hi;
                if (hi < 0) {
                    return false;
                }
            } else {
                lo = std::max(lo - 1, 0);
                ++hi;
            }
        }
        return lo == 0;
    }
};


================================================================================
FOLDER 0679_24_game
================================================================================
// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

#include <cmath>
#include <vector>

class Solution {
    static constexpr double eps = 1e-6;

    bool dfs(std::vector<double> nums) {
        if (nums.size() == 1) {
            return std::fabs(nums[0] - 24.0) < eps;
        }
        for (std::size_t i = 0; i < nums.size(); ++i) {
            for (std::size_t j = 0; j < nums.size(); ++j) {
                if (i == j) {
                    continue;
                }
                std::vector<double> rest;
                for (std::size_t k = 0; k < nums.size(); ++k) {
                    if (k != i && k != j) {
                        rest.push_back(nums[k]);
                    }
                }
                const double a = nums[i];
                const double b = nums[j];
                std::vector<double> candidates = {a + b, a - b, a * b};
                if (std::fabs(b) > eps) {
                    candidates.push_back(a / b);
                }
                for (double value : candidates) {
                    rest.push_back(value);
                    if (dfs(rest)) {
                        return true;
                    }
                    rest.pop_back();
                }
            }
        }
        return false;
    }

public:
    bool judgePoint24(std::vector<int>& cards) {
        std::vector<double> nums;
        for (int card : cards) {
            nums.push_back(static_cast<double>(card));
        }
        return dfs(nums);
    }
};


================================================================================
FOLDER 0680_valid_palindrome_ii
================================================================================
// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

#include <string>

class Solution {
    bool isPalindrome(const std::string& s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            ++left;
            --right;
        }
        return true;
    }

public:
    bool validPalindrome(std::string s) {
        int left = 0;
        int right = static_cast<int>(s.size()) - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return isPalindrome(s, left + 1, right) ||
                       isPalindrome(s, left, right - 1);
            }
            ++left;
            --right;
        }
        return true;
    }
};


================================================================================
FOLDER 0681_next_closest_time
================================================================================
// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

#include <set>
#include <string>

class Solution {
public:
    std::string nextClosestTime(std::string time) {
        std::set<char> digits = {time[0], time[1], time[3], time[4]};
        const int start = std::stoi(time.substr(0, 2)) * 60 + std::stoi(time.substr(3, 2));
        for (int delta = 1; delta <= 24 * 60; ++delta) {
            const int mins = (start + delta) % (24 * 60);
            const int hh = mins / 60;
            const int mm = mins % 60;
            char candidate[5];
            candidate[0] = static_cast<char>('0' + hh / 10);
            candidate[1] = static_cast<char>('0' + hh % 10);
            candidate[2] = static_cast<char>('0' + mm / 10);
            candidate[3] = static_cast<char>('0' + mm % 10);
            candidate[4] = '\0';
            bool valid = true;
            for (int i = 0; i < 4; ++i) {
                if (!digits.count(candidate[i])) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                std::string result;
                result += candidate[0];
                result += candidate[1];
                result += ':';
                result += candidate[2];
                result += candidate[3];
                return result;
            }
        }
        return time;
    }
};


================================================================================
FOLDER 0682_baseball_game
================================================================================
// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

#include <string>
#include <vector>

class Solution {
public:
    int calPoints(std::vector<std::string>& operations) {
        std::vector<int> stack;
        for (const std::string& op : operations) {
            if (op == "C") {
                stack.pop_back();
            } else if (op == "D") {
                stack.push_back(stack.back() * 2);
            } else if (op == "+") {
                stack.push_back(stack.back() + stack[stack.size() - 2]);
            } else {
                stack.push_back(std::stoi(op));
            }
        }
        int total = 0;
        for (int value : stack) {
            total += value;
        }
        return total;
    }
};


================================================================================
FOLDER 0683_k_empty_slots
================================================================================
// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int kEmptySlots(std::vector<int>& bulbs, int k) {
        const int n = static_cast<int>(bulbs.size());
        std::vector<int> days(n);
        for (int day = 1; day <= n; ++day) {
            days[bulbs[day - 1] - 1] = day;
        }

        int ans = INT_MAX;
        int i = 0;
        while (i < n - k - 1) {
            const int left = i;
            const int right = i + k + 1;
            int j = left + 1;
            while (j < right && days[j] > days[left] && days[j] > days[right]) {
                ++j;
            }
            if (j == right) {
                ans = std::min(ans, std::max(days[left], days[right]));
                ++i;
            } else {
                i = j;
            }
        }
        return ans == INT_MAX ? -1 : ans;
    }
};


================================================================================
FOLDER 0684_redundant_connection
================================================================================
// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

#include <numeric>
#include <vector>

class Solution {
    int find(std::vector<int>& parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

public:
    std::vector<int> findRedundantConnection(std::vector<std::vector<int>>& edges) {
        std::vector<int> parent(edges.size() + 1);
        std::iota(parent.begin(), parent.end(), 0);
        for (const auto& edge : edges) {
            const int u = edge[0];
            const int v = edge[1];
            const int pu = find(parent, u);
            const int pv = find(parent, v);
            if (pu == pv) {
                return {u, v};
            }
            parent[pu] = pv;
        }
        return {};
    }
};


================================================================================
FOLDER 0685_redundant_connection_ii
================================================================================
// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

#include <numeric>
#include <vector>

class Solution {
    int find(std::vector<int>& uf, int x) {
        while (uf[x] != x) {
            uf[x] = uf[uf[x]];
            x = uf[x];
        }
        return x;
    }

public:
    std::vector<int> findRedundantDirectedConnection(std::vector<std::vector<int>>& edges) {
        const int n = static_cast<int>(edges.size());
        std::vector<int> parent(n + 1, 0);
        std::vector<int> cand1;
        std::vector<int> cand2;
        for (int i = 0; i < n; ++i) {
            const int u = edges[i][0];
            const int v = edges[i][1];
            if (parent[v] == 0) {
                parent[v] = u;
            } else {
                cand1 = {parent[v], v};
                cand2 = {u, v};
                edges[i] = {-1, -1};
                break;
            }
        }

        std::vector<int> uf(n + 1);
        std::iota(uf.begin(), uf.end(), 0);
        for (const auto& edge : edges) {
            if (edge[0] < 0) {
                continue;
            }
            const int pu = find(uf, edge[0]);
            const int pv = find(uf, edge[1]);
            if (pu == pv) {
                return cand1.empty() ? std::vector<int>{edge[0], edge[1]} : cand1;
            }
            uf[pu] = pv;
        }
        return cand2;
    }
};


================================================================================
FOLDER 0686_repeated_string_match
================================================================================
// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

#include <string>

class Solution {
public:
    int repeatedStringMatch(std::string a, std::string b) {
        const int repeats = static_cast<int>((b.size() + a.size() - 1) / a.size());
        std::string built;
        built.reserve(a.size() * (repeats + 1));
        for (int i = 0; i < repeats; ++i) {
            built += a;
        }
        if (built.find(b) != std::string::npos) {
            return repeats;
        }
        built += a;
        if (built.find(b) != std::string::npos) {
            return repeats + 1;
        }
        return -1;
    }
};


================================================================================
FOLDER 0687_longest_univalue_path
================================================================================
// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

#include <algorithm>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int best_ = 0;

    int dfs(TreeNode* node) {
        if (!node) {
            return 0;
        }
        const int left = dfs(node->left);
        const int right = dfs(node->right);
        const int leftPath =
            node->left && node->left->val == node->val ? left + 1 : 0;
        const int rightPath =
            node->right && node->right->val == node->val ? right + 1 : 0;
        best_ = std::max(best_, leftPath + rightPath);
        return std::max(leftPath, rightPath);
    }

public:
    int longestUnivaluePath(TreeNode* root) {
        best_ = 0;
        dfs(root);
        return best_;
    }
};


================================================================================
FOLDER 0688_knight_probability_in_chessboard
================================================================================
// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

#include <vector>

class Solution {
public:
    double knightProbability(int n, int k, int row, int column) {
        static const int moves[8][2] = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
                                        {1, -2},  {1, 2},  {2, -1},  {2, 1}};
        std::vector<std::vector<double>> dp(n, std::vector<double>(n, 0.0));
        dp[row][column] = 1.0;
        for (int step = 0; step < k; ++step) {
            std::vector<std::vector<double>> nxt(n, std::vector<double>(n, 0.0));
            for (int r = 0; r < n; ++r) {
                for (int c = 0; c < n; ++c) {
                    if (dp[r][c] == 0.0) {
                        continue;
                    }
                    for (const auto& move : moves) {
                        const int nr = r + move[0];
                        const int nc = c + move[1];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                            nxt[nr][nc] += dp[r][c] / 8.0;
                        }
                    }
                }
            }
            dp.swap(nxt);
        }
        double total = 0.0;
        for (const auto& rowVals : dp) {
            for (double value : rowVals) {
                total += value;
            }
        }
        return total;
    }
};


================================================================================
FOLDER 0689_maximum_sum_of_3_non_overlapping_subarrays
================================================================================
// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

#include <vector>

class Solution {
public:
    std::vector<int> maxSumOfThreeSubarrays(std::vector<int>& nums, int k) {
        const int n = static_cast<int>(nums.size());
        const int windows = n - k + 1;
        std::vector<int> sums(windows, 0);
        int total = 0;
        for (int i = 0; i < k; ++i) {
            total += nums[i];
        }
        sums[0] = total;
        for (int i = 1; i < windows; ++i) {
            total += nums[i + k - 1] - nums[i - 1];
            sums[i] = total;
        }

        std::vector<int> left(windows, 0);
        int best = 0;
        for (int i = 0; i < windows; ++i) {
            if (sums[i] > sums[best]) {
                best = i;
            }
            left[i] = best;
        }

        std::vector<int> right(windows, 0);
        best = windows - 1;
        for (int i = windows - 1; i >= 0; --i) {
            if (sums[i] >= sums[best]) {
                best = i;
            }
            right[i] = best;
        }

        std::vector<int> answer = {0, 0, 0};
        int bestTotal = -1;
        for (int mid = k; mid < windows - k; ++mid) {
            const int l = left[mid - k];
            const int r = right[mid + k];
            const int cur = sums[l] + sums[mid] + sums[r];
            if (cur > bestTotal) {
                bestTotal = cur;
                answer = {l, mid, r};
            }
        }
        return answer;
    }
};


================================================================================
FOLDER 0690_employee_importance
================================================================================
// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

#include <unordered_map>
#include <vector>

class Employee {
public:
    int id;
    int importance;
    std::vector<int> subordinates;
};

class Solution {
    std::unordered_map<int, Employee*> table_;

    int dfs(int eid) {
        Employee* emp = table_[eid];
        int total = emp->importance;
        for (int sub : emp->subordinates) {
            total += dfs(sub);
        }
        return total;
    }

public:
    int getImportance(std::vector<Employee*> employees, int id) {
        table_.clear();
        for (Employee* emp : employees) {
            table_[emp->id] = emp;
        }
        return dfs(id);
    }
};


================================================================================
FOLDER 0691_stickers_to_spell_word
================================================================================
// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

#include <algorithm>
#include <climits>
#include <map>
#include <string>
#include <vector>

class Solution {
    std::vector<char> chars_;
    std::vector<std::vector<int>> sticks_;
    std::map<std::vector<int>, int> memo_;

    int dfs(std::vector<int> state) {
        if (memo_.count(state)) {
            return memo_[state];
        }
        int i = 0;
        while (i < static_cast<int>(state.size()) && state[i] == 0) {
            ++i;
        }
        if (i == static_cast<int>(state.size())) {
            return memo_[state] = 0;
        }
        const char first = chars_[i];
        int best = INT_MAX / 4;
        for (const auto& stick : sticks_) {
            if (stick[first - 'a'] == 0) {
                continue;
            }
            std::vector<int> nxt = state;
            for (int j = 0; j < static_cast<int>(chars_.size()); ++j) {
                nxt[j] = std::max(0, nxt[j] - stick[chars_[j] - 'a']);
            }
            best = std::min(best, 1 + dfs(nxt));
        }
        return memo_[state] = best;
    }

public:
    int minStickers(std::vector<std::string>& stickers, std::string target) {
        std::vector<int> need(26, 0);
        for (char ch : target) {
            ++need[ch - 'a'];
        }
        chars_.clear();
        for (int i = 0; i < 26; ++i) {
            if (need[i]) {
                chars_.push_back(static_cast<char>('a' + i));
            }
        }
        sticks_.clear();
        for (const std::string& sticker : stickers) {
            std::vector<int> counts(26, 0);
            for (char ch : sticker) {
                ++counts[ch - 'a'];
            }
            bool useful = false;
            for (char ch : chars_) {
                if (counts[ch - 'a']) {
                    useful = true;
                    break;
                }
            }
            if (useful) {
                sticks_.push_back(counts);
            }
        }
        memo_.clear();
        std::vector<int> state;
        for (char ch : chars_) {
            state.push_back(need[ch - 'a']);
        }
        const int result = dfs(state);
        return result >= INT_MAX / 4 ? -1 : result;
    }
};


================================================================================
FOLDER 0692_top_k_frequent_words
================================================================================
// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> topKFrequent(std::vector<std::string>& words, int k) {
        std::unordered_map<std::string, int> counts;
        for (const std::string& word : words) {
            ++counts[word];
        }
        std::vector<std::string> ordered;
        for (const auto& [word, _] : counts) {
            ordered.push_back(word);
        }
        std::sort(ordered.begin(), ordered.end(), [&](const std::string& a, const std::string& b) {
            if (counts[a] != counts[b]) {
                return counts[a] > counts[b];
            }
            return a < b;
        });
        ordered.resize(k);
        return ordered;
    }
};


================================================================================
FOLDER 0693_binary_number_with_alternating_bits
================================================================================
// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution {
public:
    bool hasAlternatingBits(int n) {
        const unsigned x = static_cast<unsigned>(n) ^ (static_cast<unsigned>(n) >> 1);
        return (x & (x + 1)) == 0;
    }
};


================================================================================
FOLDER 0694_number_of_distinct_islands
================================================================================
// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

#include <set>
#include <utility>
#include <vector>

class Solution {
    void dfs(std::vector<std::vector<int>>& grid, int r, int c, int br, int bc,
             std::vector<std::pair<int, int>>& path) {
        if (r < 0 || r >= static_cast<int>(grid.size()) || c < 0 ||
            c >= static_cast<int>(grid[0].size()) || grid[r][c] == 0) {
            return;
        }
        grid[r][c] = 0;
        path.emplace_back(r - br, c - bc);
        dfs(grid, r + 1, c, br, bc, path);
        dfs(grid, r - 1, c, br, bc, path);
        dfs(grid, r, c + 1, br, bc, path);
        dfs(grid, r, c - 1, br, bc, path);
    }

public:
    int numDistinctIslands(std::vector<std::vector<int>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        std::set<std::vector<std::pair<int, int>>> shapes;
        for (int i = 0; i < static_cast<int>(grid.size()); ++i) {
            for (int j = 0; j < static_cast<int>(grid[0].size()); ++j) {
                if (grid[i][j] == 1) {
                    std::vector<std::pair<int, int>> path;
                    dfs(grid, i, j, i, j, path);
                    shapes.insert(path);
                }
            }
        }
        return static_cast<int>(shapes.size());
    }
};


================================================================================
FOLDER 0695_max_area_of_island
================================================================================
// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

#include <algorithm>
#include <vector>

class Solution {
    int dfs(std::vector<std::vector<int>>& grid, int r, int c) {
        if (r < 0 || r >= static_cast<int>(grid.size()) || c < 0 ||
            c >= static_cast<int>(grid[0].size()) || grid[r][c] == 0) {
            return 0;
        }
        grid[r][c] = 0;
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) +
               dfs(grid, r, c - 1);
    }

public:
    int maxAreaOfIsland(std::vector<std::vector<int>>& grid) {
        int best = 0;
        for (int i = 0; i < static_cast<int>(grid.size()); ++i) {
            for (int j = 0; j < static_cast<int>(grid[0].size()); ++j) {
                best = std::max(best, dfs(grid, i, j));
            }
        }
        return best;
    }
};


================================================================================
FOLDER 0696_count_binary_substrings
================================================================================
// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

#include <algorithm>
#include <string>

class Solution {
public:
    int countBinarySubstrings(std::string s) {
        int prev = 0;
        int cur = 1;
        int ans = 0;
        for (int i = 1; i < static_cast<int>(s.size()); ++i) {
            if (s[i] == s[i - 1]) {
                ++cur;
            } else {
                ans += std::min(prev, cur);
                prev = cur;
                cur = 1;
            }
        }
        return ans + std::min(prev, cur);
    }
};


================================================================================
FOLDER 0697_degree_of_an_array
================================================================================
// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int findShortestSubArray(std::vector<int>& nums) {
        std::unordered_map<int, int> first;
        std::unordered_map<int, int> last;
        std::unordered_map<int, int> count;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (!first.count(nums[i])) {
                first[nums[i]] = i;
            }
            last[nums[i]] = i;
            ++count[nums[i]];
        }
        int degree = 0;
        for (const auto& [_, freq] : count) {
            degree = std::max(degree, freq);
        }
        int best = INT_MAX;
        for (const auto& [num, freq] : count) {
            if (freq == degree) {
                best = std::min(best, last[num] - first[num] + 1);
            }
        }
        return best;
    }
};


================================================================================
FOLDER 0698_partition_to_k_equal_sum_subsets
================================================================================
// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
    std::vector<int> nums_;
    std::vector<int> buckets_;
    int target_ = 0;

    bool dfs(int index) {
        if (index == static_cast<int>(nums_.size())) {
            return true;
        }
        for (int i = 0; i < static_cast<int>(buckets_.size()); ++i) {
            if (buckets_[i] + nums_[index] > target_) {
                continue;
            }
            buckets_[i] += nums_[index];
            if (dfs(index + 1)) {
                return true;
            }
            buckets_[i] -= nums_[index];
            if (buckets_[i] == 0) {
                break;
            }
        }
        return false;
    }

public:
    bool canPartitionKSubsets(std::vector<int>& nums, int k) {
        const int total = std::accumulate(nums.begin(), nums.end(), 0);
        if (total % k != 0) {
            return false;
        }
        target_ = total / k;
        nums_ = nums;
        std::sort(nums_.begin(), nums_.end(), std::greater<int>());
        if (nums_[0] > target_) {
            return false;
        }
        buckets_.assign(k, 0);
        return dfs(0);
    }
};


================================================================================
FOLDER 0699_falling_squares
================================================================================
// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

#include <algorithm>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<int> fallingSquares(std::vector<std::vector<int>>& positions) {
        std::vector<std::tuple<int, int, int>> intervals;
        std::vector<int> answer;
        int maxHeight = 0;
        for (const auto& pos : positions) {
            const int left = pos[0];
            const int side = pos[1];
            const int right = left + side;
            int base = 0;
            for (const auto& [l, r, height] : intervals) {
                if (r > left && l < right) {
                    base = std::max(base, height);
                }
            }
            const int height = base + side;
            intervals.emplace_back(left, right, height);
            maxHeight = std::max(maxHeight, height);
            answer.push_back(maxHeight);
        }
        return answer;
    }
};


================================================================================
FOLDER 0700_search_in_a_binary_search_tree
================================================================================
// LeetCode 0700 - Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

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
    TreeNode* searchBST(TreeNode* root, int val) {
        while (root && root->val != val) {
            root = val < root->val ? root->left : root->right;
        }
        return root;
    }
};


================================================================================
FOLDER 0701_insert_into_a_binary_search_tree
================================================================================
// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            return new TreeNode(val);
        }
        TreeNode* node = root;
        while (true) {
            if (val < node->val) {
                if (!node->left) {
                    node->left = new TreeNode(val);
                    break;
                }
                node = node->left;
            } else {
                if (!node->right) {
                    node->right = new TreeNode(val);
                    break;
                }
                node = node->right;
            }
        }
        return root;
    }
};


================================================================================
FOLDER 0702_search_in_a_sorted_array_of_unknown_size
================================================================================
// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

#include <vector>

class ArrayReader {
public:
    explicit ArrayReader(const std::vector<int>& secret) : secret_(secret) {}

    int get(int index) const {
        if (index < 0 || index >= static_cast<int>(secret_.size())) {
            return 2147483647;
        }
        return secret_[index];
    }

private:
    std::vector<int> secret_;
};

class Solution {
public:
    // Harness passes the secret array directly; wrap it as ArrayReader.
    int search(const std::vector<int>& secret, int target) {
        return search(ArrayReader(secret), target);
    }

    int search(const ArrayReader& reader, int target) {
        int right = 1;
        while (reader.get(right) < target) {
            right <<= 1;
        }
        int left = right >> 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int value = reader.get(mid);
            if (value == target) {
                return mid;
            }
            if (value > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
};


================================================================================
FOLDER 0703_kth_largest_element_in_a_stream
================================================================================
// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

#include <queue>
#include <vector>

class KthLargest {
public:
    KthLargest(int k, std::vector<int>& nums) : k_(k) {
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        heap_.push(val);
        if (static_cast<int>(heap_.size()) > k_) {
            heap_.pop();
        }
        return heap_.top();
    }

private:
    int k_;
    std::priority_queue<int, std::vector<int>, std::greater<int>> heap_;
};


================================================================================
FOLDER 0704_binary_search
================================================================================
// LeetCode 0704 - Binary Search
// https://leetcode.com/problems/binary-search/

#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int left = 0;
        int right = static_cast<int>(nums.size()) - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
};


================================================================================
FOLDER 0705_design_hashset
================================================================================
// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

#include <unordered_set>

class MyHashSet {
public:
    MyHashSet() = default;

    void add(int key) { data_.insert(key); }

    void remove(int key) { data_.erase(key); }

    bool contains(int key) { return data_.count(key) > 0; }

private:
    std::unordered_set<int> data_;
};


================================================================================
FOLDER 0706_design_hashmap
================================================================================
// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

#include <unordered_map>

class MyHashMap {
public:
    MyHashMap() = default;

    void put(int key, int value) { data_[key] = value; }

    int get(int key) {
        auto it = data_.find(key);
        return it == data_.end() ? -1 : it->second;
    }

    void remove(int key) { data_.erase(key); }

private:
    std::unordered_map<int, int> data_;
};


================================================================================
FOLDER 0707_design_linked_list
================================================================================
// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList {
    struct Node {
        int val;
        Node* next;
        Node(int v = 0) : val(v), next(nullptr) {}
    };

    Node* dummy_;
    int size_;

public:
    MyLinkedList() : dummy_(new Node()), size_(0) {}

    int get(int index) {
        if (index < 0 || index >= size_) {
            return -1;
        }
        Node* node = dummy_->next;
        for (int i = 0; i < index; ++i) {
            node = node->next;
        }
        return node->val;
    }

    void addAtHead(int val) { addAtIndex(0, val); }

    void addAtTail(int val) { addAtIndex(size_, val); }

    void addAtIndex(int index, int val) {
        if (index < 0 || index > size_) {
            return;
        }
        Node* prev = dummy_;
        for (int i = 0; i < index; ++i) {
            prev = prev->next;
        }
        Node* node = new Node(val);
        node->next = prev->next;
        prev->next = node;
        ++size_;
    }

    void deleteAtIndex(int index) {
        if (index < 0 || index >= size_) {
            return;
        }
        Node* prev = dummy_;
        for (int i = 0; i < index; ++i) {
            prev = prev->next;
        }
        Node* doomed = prev->next;
        prev->next = doomed->next;
        delete doomed;
        --size_;
    }
};


================================================================================
FOLDER 0708_insert_into_a_sorted_circular_linked_list
================================================================================
// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* insert(ListNode* head, int insertVal) {
        ListNode* node = new ListNode(insertVal);
        if (!head) {
            node->next = node;
            return node;
        }

        ListNode* cur = head;
        while (cur->next && cur->next != head) {
            cur = cur->next;
        }
        cur->next = head;

        ListNode* prev = head;
        ListNode* curr = head->next;
        while (true) {
            if (prev->val <= insertVal && insertVal <= curr->val) {
                break;
            }
            if (prev->val > curr->val && (insertVal >= prev->val || insertVal <= curr->val)) {
                break;
            }
            prev = curr;
            curr = curr->next;
            if (prev == head) {
                break;
            }
        }
        prev->next = node;
        node->next = curr;
        return head;
    }
};


================================================================================
FOLDER 0709_to_lower_case
================================================================================
// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

#include <string>

class Solution {
public:
    std::string toLowerCase(std::string s) {
        for (char& ch : s) {
            if (ch >= 'A' && ch <= 'Z') {
                ch = static_cast<char>(ch + 32);
            }
        }
        return s;
    }
};


================================================================================
FOLDER 0710_random_pick_with_blacklist
================================================================================
// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

#include <cstdlib>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    Solution(int n, std::vector<int>& blacklist) {
        size_ = n - static_cast<int>(blacklist.size());
        std::unordered_set<int> black(blacklist.begin(), blacklist.end());
        int white = size_;
        for (int b : blacklist) {
            if (b < size_) {
                while (black.count(white)) {
                    ++white;
                }
                mapping_[b] = white++;
            }
        }
    }

    int pick() {
        int index = std::rand() % size_;
        auto it = mapping_.find(index);
        return it == mapping_.end() ? index : it->second;
    }

private:
    int size_;
    std::unordered_map<int, int> mapping_;
};


================================================================================
FOLDER 0711_number_of_distinct_islands_ii
================================================================================
// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

#include <algorithm>
#include <set>
#include <vector>

class Solution {
public:
    int numDistinctIslands2(std::vector<std::vector<int>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        std::set<std::vector<std::pair<int, int>>> shapes;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    std::vector<std::pair<int, int>> cells;
                    dfs(grid, i, j, m, n, cells);
                    shapes.insert(canonical(cells));
                }
            }
        }
        return static_cast<int>(shapes.size());
    }

private:
    void dfs(std::vector<std::vector<int>>& grid, int r, int c, int m, int n,
             std::vector<std::pair<int, int>>& cells) {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) {
            return;
        }
        grid[r][c] = 0;
        cells.push_back({r, c});
        static const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (auto& d : dirs) {
            dfs(grid, r + d[0], c + d[1], m, n, cells);
        }
    }

    std::vector<std::pair<int, int>> canonical(const std::vector<std::pair<int, int>>& cells) {
        using Transform = std::pair<int, int> (*)(int, int);
        Transform transforms[8] = {
            [](int x, int y) { return std::pair<int, int>{x, y}; },
            [](int x, int y) { return std::pair<int, int>{x, -y}; },
            [](int x, int y) { return std::pair<int, int>{-x, y}; },
            [](int x, int y) { return std::pair<int, int>{-x, -y}; },
            [](int x, int y) { return std::pair<int, int>{y, x}; },
            [](int x, int y) { return std::pair<int, int>{y, -x}; },
            [](int x, int y) { return std::pair<int, int>{-y, x}; },
            [](int x, int y) { return std::pair<int, int>{-y, -x}; },
        };
        std::vector<std::vector<std::pair<int, int>>> norms;
        for (auto transform : transforms) {
            std::vector<std::pair<int, int>> pts;
            pts.reserve(cells.size());
            for (auto [x, y] : cells) {
                pts.push_back(transform(x, y));
            }
            int minX = pts[0].first, minY = pts[0].second;
            for (auto [x, y] : pts) {
                minX = std::min(minX, x);
                minY = std::min(minY, y);
            }
            for (auto& p : pts) {
                p.first -= minX;
                p.second -= minY;
            }
            std::sort(pts.begin(), pts.end());
            norms.push_back(std::move(pts));
        }
        return *std::min_element(norms.begin(), norms.end());
    }
};


================================================================================
FOLDER 0712_minimum_ascii_delete_sum_for_two_strings
================================================================================
// LeetCode 0712 - Minimum ASCII Delete Sum for Two Strings
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minimumDeleteSum(std::string s1, std::string s2) {
        int m = static_cast<int>(s1.size());
        int n = static_cast<int>(s2.size());
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            dp[i][0] = dp[i - 1][0] + static_cast<unsigned char>(s1[i - 1]);
        }
        for (int j = 1; j <= n; ++j) {
            dp[0][j] = dp[0][j - 1] + static_cast<unsigned char>(s2[j - 1]);
        }
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = std::min(
                        dp[i - 1][j] + static_cast<unsigned char>(s1[i - 1]),
                        dp[i][j - 1] + static_cast<unsigned char>(s2[j - 1]));
                }
            }
        }
        return dp[m][n];
    }
};


================================================================================
FOLDER 0713_subarray_product_less_than_k
================================================================================
// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

#include <vector>

class Solution {
public:
    int numSubarrayProductLessThanK(std::vector<int>& nums, int k) {
        if (k <= 1) {
            return 0;
        }
        long long product = 1;
        int left = 0;
        int ans = 0;
        for (int right = 0; right < static_cast<int>(nums.size()); ++right) {
            product *= nums[right];
            while (product >= k) {
                product /= nums[left++];
            }
            ans += right - left + 1;
        }
        return ans;
    }
};


================================================================================
FOLDER 0714_best_time_to_buy_and_sell_stock_with_transaction_fee
================================================================================
// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices, int fee) {
        int hold = -prices[0];
        int cash = 0;
        for (size_t i = 1; i < prices.size(); ++i) {
            int price = prices[i];
            hold = std::max(hold, cash - price);
            cash = std::max(cash, hold + price - fee);
        }
        return cash;
    }
};


================================================================================
FOLDER 0715_range_module
================================================================================
// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

#include <algorithm>
#include <vector>

class RangeModule {
public:
    RangeModule() = default;

    void addRange(int left, int right) {
        std::vector<std::pair<int, int>> next;
        bool placed = false;
        for (auto [start, end] : intervals_) {
            if (end < left) {
                next.push_back({start, end});
            } else if (right < start) {
                if (!placed) {
                    next.push_back({left, right});
                    placed = true;
                }
                next.push_back({start, end});
            } else {
                left = std::min(left, start);
                right = std::max(right, end);
            }
        }
        if (!placed) {
            next.push_back({left, right});
        }
        intervals_ = std::move(next);
    }

    bool queryRange(int left, int right) {
        for (auto [start, end] : intervals_) {
            if (start <= left && right <= end) {
                return true;
            }
            if (end >= right) {
                break;
            }
        }
        return false;
    }

    void removeRange(int left, int right) {
        std::vector<std::pair<int, int>> next;
        for (auto [start, end] : intervals_) {
            if (end <= left || right <= start) {
                next.push_back({start, end});
            } else {
                if (start < left) {
                    next.push_back({start, left});
                }
                if (right < end) {
                    next.push_back({right, end});
                }
            }
        }
        intervals_ = std::move(next);
    }

private:
    std::vector<std::pair<int, int>> intervals_;
};


================================================================================
FOLDER 0716_max_stack
================================================================================
// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

#include <algorithm>
#include <vector>

class MaxStack {
public:
    MaxStack() = default;

    void push(int x) {
        stack_.push_back(x);
        maxes_.push_back(maxes_.empty() ? x : std::max(x, maxes_.back()));
    }

    int pop() {
        maxes_.pop_back();
        int val = stack_.back();
        stack_.pop_back();
        return val;
    }

    int top() { return stack_.back(); }

    int peekMax() { return maxes_.back(); }

    int popMax() {
        int maxVal = peekMax();
        std::vector<int> buffer;
        while (top() != maxVal) {
            buffer.push_back(pop());
        }
        pop();
        while (!buffer.empty()) {
            push(buffer.back());
            buffer.pop_back();
        }
        return maxVal;
    }

private:
    std::vector<int> stack_;
    std::vector<int> maxes_;
};


================================================================================
FOLDER 0717_1_bit_and_2_bit_characters
================================================================================
// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

#include <vector>

class Solution {
public:
    bool isOneBitCharacter(std::vector<int>& bits) {
        int i = 0;
        int n = static_cast<int>(bits.size());
        while (i < n - 1) {
            i += bits[i] == 1 ? 2 : 1;
        }
        return i == n - 1;
    }
};


================================================================================
FOLDER 0718_maximum_length_of_repeated_subarray
================================================================================
// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findLength(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = static_cast<int>(nums1.size());
        int n = static_cast<int>(nums2.size());
        std::vector<int> dp(n + 1, 0);
        int best = 0;
        for (int i = 1; i <= m; ++i) {
            std::vector<int> next(n + 1, 0);
            for (int j = 1; j <= n; ++j) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    next[j] = dp[j - 1] + 1;
                    best = std::max(best, next[j]);
                }
            }
            dp.swap(next);
        }
        return best;
    }
};


================================================================================
FOLDER 0719_find_k_th_smallest_pair_distance
================================================================================
// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

#include <algorithm>
#include <vector>

class Solution {
public:
    int smallestDistancePair(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int lo = 0;
        int hi = nums.back() - nums.front();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (countPairs(nums, mid) >= k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

private:
    int countPairs(const std::vector<int>& nums, int distance) {
        int count = 0;
        int left = 0;
        for (int right = 0; right < static_cast<int>(nums.size()); ++right) {
            while (nums[right] - nums[left] > distance) {
                ++left;
            }
            count += right - left;
        }
        return count;
    }
};


================================================================================
FOLDER 0720_longest_word_in_dictionary
================================================================================
// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string longestWord(std::vector<std::string>& words) {
        std::sort(words.begin(), words.end());
        std::unordered_set<std::string> built{""};
        std::string best;
        for (const std::string& word : words) {
            if (built.count(word.substr(0, word.size() - 1))) {
                built.insert(word);
                if (word.size() > best.size()) {
                    best = word;
                }
            }
        }
        return best;
    }
};


================================================================================
FOLDER 0721_accounts_merge
================================================================================
// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> accountsMerge(std::vector<std::vector<std::string>>& accounts) {
        std::unordered_map<std::string, std::string> parent;
        std::unordered_map<std::string, std::string> emailName;

        auto find = [&](std::string x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        auto unite = [&](const std::string& a, const std::string& b) {
            parent[find(a)] = find(b);
        };

        for (const auto& account : accounts) {
            const std::string& name = account[0];
            const std::string& first = account[1];
            for (size_t i = 1; i < account.size(); ++i) {
                const std::string& email = account[i];
                if (!parent.count(email)) {
                    parent[email] = email;
                }
                emailName[email] = name;
                unite(first, email);
            }
        }

        std::unordered_map<std::string, std::vector<std::string>> groups;
        for (const auto& [email, _] : parent) {
            groups[find(email)].push_back(email);
        }

        std::vector<std::vector<std::string>> result;
        for (auto& [_, emails] : groups) {
            std::sort(emails.begin(), emails.end());
            std::vector<std::string> row;
            row.push_back(emailName[emails[0]]);
            row.insert(row.end(), emails.begin(), emails.end());
            result.push_back(std::move(row));
        }
        return result;
    }
};


================================================================================
FOLDER 0722_remove_comments
================================================================================
// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> removeComments(std::vector<std::string>& source) {
        std::vector<std::string> result;
        std::string buffer;
        bool inBlock = false;
        for (const std::string& line : source) {
            size_t i = 0;
            while (i < line.size()) {
                if (inBlock) {
                    if (i + 1 < line.size() && line[i] == '*' && line[i + 1] == '/') {
                        inBlock = false;
                        i += 2;
                    } else {
                        ++i;
                    }
                } else if (i + 1 < line.size() && line[i] == '/' && line[i + 1] == '*') {
                    inBlock = true;
                    i += 2;
                } else if (i + 1 < line.size() && line[i] == '/' && line[i + 1] == '/') {
                    break;
                } else {
                    buffer.push_back(line[i++]);
                }
            }
            if (!inBlock && !buffer.empty()) {
                result.push_back(buffer);
                buffer.clear();
            }
        }
        return result;
    }
};


================================================================================
FOLDER 0723_candy_crush
================================================================================
// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> candyCrush(std::vector<std::vector<int>>& board) {
        int m = static_cast<int>(board.size());
        int n = static_cast<int>(board[0].size());
        bool stable = false;
        while (!stable) {
            stable = true;
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n - 2; ++j) {
                    int value = std::abs(board[i][j]);
                    if (value && value == std::abs(board[i][j + 1]) && value == std::abs(board[i][j + 2])) {
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -value;
                        stable = false;
                    }
                }
            }
            for (int j = 0; j < n; ++j) {
                for (int i = 0; i < m - 2; ++i) {
                    int value = std::abs(board[i][j]);
                    if (value && value == std::abs(board[i + 1][j]) && value == std::abs(board[i + 2][j])) {
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -value;
                        stable = false;
                    }
                }
            }
            for (int j = 0; j < n; ++j) {
                int write = m - 1;
                for (int i = m - 1; i >= 0; --i) {
                    if (board[i][j] > 0) {
                        board[write--][j] = board[i][j];
                    }
                }
                for (int i = write; i >= 0; --i) {
                    board[i][j] = 0;
                }
            }
        }
        return board;
    }
};


================================================================================
FOLDER 0724_find_pivot_index
================================================================================
// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

#include <numeric>
#include <vector>

class Solution {
public:
    int pivotIndex(std::vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        int left = 0;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (left == total - left - nums[i]) {
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
};


================================================================================
FOLDER 0725_split_linked_list_in_parts
================================================================================
// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

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
    std::vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int length = 0;
        for (ListNode* node = head; node; node = node->next) {
            ++length;
        }
        int partSize = length / k;
        int extra = length % k;
        std::vector<ListNode*> result;
        ListNode* current = head;
        for (int i = 0; i < k; ++i) {
            result.push_back(current);
            int size = partSize + (i < extra ? 1 : 0);
            for (int j = 0; j < size - 1 && current; ++j) {
                current = current->next;
            }
            if (current) {
                ListNode* nxt = current->next;
                current->next = nullptr;
                current = nxt;
            }
        }
        return result;
    }
};


================================================================================
FOLDER 0726_number_of_atoms
================================================================================
// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

#include <cctype>
#include <map>
#include <stack>
#include <string>

class Solution {
public:
    std::string countOfAtoms(std::string formula) {
        std::stack<std::map<std::string, int>> st;
        st.push({});
        int i = 0;
        int n = static_cast<int>(formula.size());
        while (i < n) {
            if (formula[i] == '(') {
                st.push({});
                ++i;
            } else if (formula[i] == ')') {
                ++i;
                int start = i;
                while (i < n && std::isdigit(static_cast<unsigned char>(formula[i]))) {
                    ++i;
                }
                int mult = start < i ? std::stoi(formula.substr(start, i - start)) : 1;
                auto top = st.top();
                st.pop();
                for (auto& [atom, count] : top) {
                    st.top()[atom] += count * mult;
                }
            } else {
                int start = i++;
                while (i < n && std::islower(static_cast<unsigned char>(formula[i]))) {
                    ++i;
                }
                std::string atom = formula.substr(start, i - start);
                start = i;
                while (i < n && std::isdigit(static_cast<unsigned char>(formula[i]))) {
                    ++i;
                }
                int count = start < i ? std::stoi(formula.substr(start, i - start)) : 1;
                st.top()[atom] += count;
            }
        }
        std::string result;
        for (auto& [atom, count] : st.top()) {
            result += atom;
            if (count > 1) {
                result += std::to_string(count);
            }
        }
        return result;
    }
};


================================================================================
FOLDER 0727_minimum_window_subsequence
================================================================================
// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

#include <string>

class Solution {
public:
    std::string minWindow(std::string s1, std::string s2) {
        int m = static_cast<int>(s1.size());
        int n = static_cast<int>(s2.size());
        std::string best;
        int i = 0;
        while (i < m) {
            int j = 0;
            int k = i;
            while (k < m && j < n) {
                if (s1[k] == s2[j]) {
                    ++j;
                }
                ++k;
            }
            if (j < n) {
                break;
            }
            int end = k - 1;
            j = n - 1;
            k = end;
            while (j >= 0) {
                if (s1[k] == s2[j]) {
                    --j;
                }
                --k;
            }
            int start = k + 1;
            if (best.empty() || end - start + 1 < static_cast<int>(best.size())) {
                best = s1.substr(start, end - start + 1);
            }
            i = start + 1;
        }
        return best;
    }
};


================================================================================
FOLDER 0728_self_dividing_numbers
================================================================================
// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

#include <vector>

class Solution {
public:
    std::vector<int> selfDividingNumbers(int left, int right) {
        std::vector<int> result;
        for (int num = left; num <= right; ++num) {
            if (isSelfDividing(num)) {
                result.push_back(num);
            }
        }
        return result;
    }

private:
    bool isSelfDividing(int num) {
        int x = num;
        while (x) {
            int digit = x % 10;
            if (digit == 0 || num % digit != 0) {
                return false;
            }
            x /= 10;
        }
        return true;
    }
};


================================================================================
FOLDER 0729_my_calendar_i
================================================================================
// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

#include <vector>

class MyCalendar {
public:
    MyCalendar() = default;

    bool book(int startTime, int endTime) {
        for (auto [start, end] : bookings_) {
            if (start < endTime && startTime < end) {
                return false;
            }
        }
        bookings_.push_back({startTime, endTime});
        return true;
    }

private:
    std::vector<std::pair<int, int>> bookings_;
};


================================================================================
FOLDER 0730_count_different_palindromic_subsequences
================================================================================
// LeetCode 0730 - Count Different Palindromic Subsequences
// https://leetcode.com/problems/count-different-palindromic-subsequences/

#include <string>
#include <vector>

class Solution {
public:
    int countPalindromicSubsequences(std::string s) {
        const int mod = 1000000007;
        int n = static_cast<int>(s.size());
        std::vector<std::vector<long long>> dp(n, std::vector<long long>(n, 0));
        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
        }
        for (int length = 2; length <= n; ++length) {
            for (int i = 0; i <= n - length; ++i) {
                int j = i + length - 1;
                if (s[i] != s[j]) {
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1];
                } else {
                    int left = i + 1;
                    int right = j - 1;
                    while (left <= right && s[left] != s[i]) {
                        ++left;
                    }
                    while (left <= right && s[right] != s[i]) {
                        --right;
                    }
                    if (left > right) {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2;
                    } else if (left == right) {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1];
                    }
                }
                dp[i][j] = (dp[i][j] % mod + mod) % mod;
            }
        }
        return static_cast<int>(dp[0][n - 1]);
    }
};


================================================================================
FOLDER 0731_my_calendar_ii
================================================================================
// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

#include <algorithm>
#include <vector>

class MyCalendarTwo {
public:
    MyCalendarTwo() = default;

    bool book(int startTime, int endTime) {
        for (auto [start, end] : overlaps_) {
            if (start < endTime && startTime < end) {
                return false;
            }
        }
        for (auto [start, end] : booked_) {
            if (start < endTime && startTime < end) {
                overlaps_.push_back({std::max(start, startTime), std::min(end, endTime)});
            }
        }
        booked_.push_back({startTime, endTime});
        return true;
    }

private:
    std::vector<std::pair<int, int>> booked_;
    std::vector<std::pair<int, int>> overlaps_;
};


================================================================================
FOLDER 0732_my_calendar_iii
================================================================================
// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

#include <algorithm>
#include <map>

class MyCalendarThree {
public:
    MyCalendarThree() = default;

    int book(int startTime, int endTime) {
        ++delta_[startTime];
        --delta_[endTime];
        int current = 0;
        int best = 0;
        for (auto& [_, change] : delta_) {
            current += change;
            best = std::max(best, current);
        }
        return best;
    }

private:
    std::map<int, int> delta_;
};


================================================================================
FOLDER 0733_flood_fill
================================================================================
// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> floodFill(std::vector<std::vector<int>>& image, int sr, int sc, int color) {
        int original = image[sr][sc];
        if (original == color) {
            return image;
        }
        dfs(image, sr, sc, original, color);
        return image;
    }

private:
    void dfs(std::vector<std::vector<int>>& image, int r, int c, int original, int color) {
        if (r < 0 || r >= static_cast<int>(image.size()) || c < 0 ||
            c >= static_cast<int>(image[0].size()) || image[r][c] != original) {
            return;
        }
        image[r][c] = color;
        dfs(image, r + 1, c, original, color);
        dfs(image, r - 1, c, original, color);
        dfs(image, r, c + 1, original, color);
        dfs(image, r, c - 1, original, color);
    }
};


================================================================================
FOLDER 0734_sentence_similarity
================================================================================
// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool areSentencesSimilar(std::vector<std::string>& sentence1, std::vector<std::string>& sentence2,
                             std::vector<std::vector<std::string>>& similarPairs) {
        if (sentence1.size() != sentence2.size()) {
            return false;
        }
        std::unordered_set<std::string> pairs;
        for (const auto& pair : similarPairs) {
            pairs.insert(pair[0] + "#" + pair[1]);
            pairs.insert(pair[1] + "#" + pair[0]);
        }
        for (size_t i = 0; i < sentence1.size(); ++i) {
            if (sentence1[i] != sentence2[i] &&
                !pairs.count(sentence1[i] + "#" + sentence2[i])) {
                return false;
            }
        }
        return true;
    }
};


================================================================================
FOLDER 0735_asteroid_collision
================================================================================
// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

#include <vector>

class Solution {
public:
    std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
        std::vector<int> stack;
        for (int asteroid : asteroids) {
            bool alive = true;
            while (alive && !stack.empty() && asteroid < 0 && stack.back() > 0) {
                if (stack.back() < -asteroid) {
                    stack.pop_back();
                    continue;
                }
                if (stack.back() == -asteroid) {
                    stack.pop_back();
                }
                alive = false;
            }
            if (alive) {
                stack.push_back(asteroid);
            }
        }
        return stack;
    }
};


================================================================================
FOLDER 0736_parse_lisp_expression
================================================================================
// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

#include <cctype>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int evaluate(std::string expression) {
        tokens_.clear();
        std::string cur;
        for (char ch : expression) {
            if (ch == '(' || ch == ')') {
                if (!cur.empty()) {
                    tokens_.push_back(cur);
                    cur.clear();
                }
                tokens_.push_back(std::string(1, ch));
            } else if (std::isspace(static_cast<unsigned char>(ch))) {
                if (!cur.empty()) {
                    tokens_.push_back(cur);
                    cur.clear();
                }
            } else {
                cur.push_back(ch);
            }
        }
        if (!cur.empty()) {
            tokens_.push_back(cur);
        }
        pos_ = 0;
        std::vector<std::unordered_map<std::string, int>> env;
        return parse(env);
    }

private:
    std::vector<std::string> tokens_;
    int pos_ = 0;

    int parse(std::vector<std::unordered_map<std::string, int>>& env) {
        const std::string& token = tokens_[pos_];
        if (token != "(") {
            ++pos_;
            if (std::isdigit(static_cast<unsigned char>(token[0])) ||
                (token[0] == '-' && token.size() > 1)) {
                return std::stoi(token);
            }
            for (int i = static_cast<int>(env.size()) - 1; i >= 0; --i) {
                auto it = env[i].find(token);
                if (it != env[i].end()) {
                    return it->second;
                }
            }
            return 0;
        }

        ++pos_;
        std::string op = tokens_[pos_++];
        if (op == "let") {
            env.push_back({});
            while (tokens_[pos_] != ")") {
                if (tokens_[pos_] == "(" || tokens_[pos_ + 1] == ")") {
                    int value = parse(env);
                    ++pos_;
                    env.pop_back();
                    return value;
                }
                std::string var = tokens_[pos_++];
                env.back()[var] = parse(env);
            }
        }
        if (op == "add") {
            int left = parse(env);
            int right = parse(env);
            ++pos_;
            return left + right;
        }
        if (op == "mult") {
            int left = parse(env);
            int right = parse(env);
            ++pos_;
            return left * right;
        }
        return 0;
    }
};


================================================================================
FOLDER 0737_sentence_similarity_ii
================================================================================
// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool areSentencesSimilarTwo(std::vector<std::string>& sentence1, std::vector<std::string>& sentence2,
                                std::vector<std::vector<std::string>>& similarPairs) {
        if (sentence1.size() != sentence2.size()) {
            return false;
        }
        for (const auto& pair : similarPairs) {
            unite(pair[0], pair[1]);
        }
        for (size_t i = 0; i < sentence1.size(); ++i) {
            if (find(sentence1[i]) != find(sentence2[i])) {
                return false;
            }
        }
        return true;
    }

private:
    std::unordered_map<std::string, std::string> parent_;

    std::string find(const std::string& x) {
        if (!parent_.count(x)) {
            parent_[x] = x;
        }
        std::string cur = x;
        while (parent_[cur] != cur) {
            parent_[cur] = parent_[parent_[cur]];
            cur = parent_[cur];
        }
        return cur;
    }

    void unite(const std::string& a, const std::string& b) {
        parent_[find(a)] = find(b);
    }
};


================================================================================
FOLDER 0738_monotone_increasing_digits
================================================================================
// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

#include <string>

class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        std::string digits = std::to_string(n);
        int mark = static_cast<int>(digits.size());
        for (int i = static_cast<int>(digits.size()) - 1; i > 0; --i) {
            if (digits[i] < digits[i - 1]) {
                digits[i - 1] = static_cast<char>(digits[i - 1] - 1);
                mark = i;
            }
        }
        for (int i = mark; i < static_cast<int>(digits.size()); ++i) {
            digits[i] = '9';
        }
        return std::stoi(digits);
    }
};


================================================================================
FOLDER 0739_daily_temperatures
================================================================================
// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

#include <vector>

class Solution {
public:
    std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
        std::vector<int> answer(temperatures.size(), 0);
        std::vector<int> stack;
        for (int i = 0; i < static_cast<int>(temperatures.size()); ++i) {
            while (!stack.empty() && temperatures[stack.back()] < temperatures[i]) {
                int prev = stack.back();
                stack.pop_back();
                answer[prev] = i - prev;
            }
            stack.push_back(i);
        }
        return answer;
    }
};


================================================================================
FOLDER 0740_delete_and_earn
================================================================================
// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

#include <algorithm>
#include <vector>

class Solution {
public:
    int deleteAndEarn(std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        int maxNum = *std::max_element(nums.begin(), nums.end());
        std::vector<int> points(maxNum + 1, 0);
        for (int num : nums) {
            points[num] += num;
        }
        int take = 0;
        int skip = 0;
        for (int value : points) {
            int newTake = skip + value;
            int newSkip = std::max(skip, take);
            take = newTake;
            skip = newSkip;
        }
        return std::max(take, skip);
    }
};


================================================================================
FOLDER 0741_cherry_pickup
================================================================================
// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int cherryPickup(std::vector<std::vector<int>>& grid) {
        n_ = static_cast<int>(grid.size());
        grid_ = &grid;
        memo_.assign(n_, std::vector<std::vector<int>>(n_, std::vector<int>(n_, INT_MIN)));
        return std::max(0, dp(0, 0, 0));
    }

private:
    int n_;
    std::vector<std::vector<int>>* grid_;
    std::vector<std::vector<std::vector<int>>> memo_;

    int dp(int r1, int c1, int c2) {
        int r2 = r1 + c1 - c2;
        if (r1 >= n_ || c1 >= n_ || r2 >= n_ || c2 >= n_ || (*grid_)[r1][c1] == -1 ||
            (*grid_)[r2][c2] == -1) {
            return -1000000000;
        }
        if (r1 == n_ - 1 && c1 == n_ - 1) {
            return (*grid_)[r1][c1];
        }
        int& cached = memo_[r1][c1][c2];
        if (cached != INT_MIN) {
            return cached;
        }
        int cherries = (*grid_)[r1][c1];
        if (r1 != r2 || c1 != c2) {
            cherries += (*grid_)[r2][c2];
        }
        cherries += std::max({dp(r1 + 1, c1, c2), dp(r1, c1 + 1, c2), dp(r1 + 1, c1, c2 + 1),
                              dp(r1, c1 + 1, c2 + 1)});
        return cached = cherries;
    }
};


================================================================================
FOLDER 0742_closest_leaf_in_a_binary_tree
================================================================================
// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

#include <queue>
#include <unordered_map>
#include <unordered_set>
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
    int findClosestLeaf(TreeNode* root, int k) {
        std::unordered_map<int, std::vector<int>> graph;
        std::unordered_set<int> leaves;
        build(root, nullptr, graph, leaves);
        std::queue<int> q;
        std::unordered_set<int> seen{k};
        q.push(k);
        while (!q.empty()) {
            int value = q.front();
            q.pop();
            if (leaves.count(value)) {
                return value;
            }
            for (int neighbor : graph[value]) {
                if (!seen.count(neighbor)) {
                    seen.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        return -1;
    }

private:
    void build(TreeNode* node, TreeNode* parent, std::unordered_map<int, std::vector<int>>& graph,
               std::unordered_set<int>& leaves) {
        if (!node) {
            return;
        }
        if (parent) {
            graph[node->val].push_back(parent->val);
            graph[parent->val].push_back(node->val);
        }
        if (!node->left && !node->right) {
            leaves.insert(node->val);
        }
        build(node->right, node, graph, leaves);
        build(node->left, node, graph, leaves);
    }
};


================================================================================
FOLDER 0743_network_delay_time
================================================================================
// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

#include <algorithm>
#include <limits>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int networkDelayTime(std::vector<std::vector<int>>& times, int n, int k) {
        std::vector<std::vector<std::pair<int, int>>> graph(n + 1);
        for (const auto& edge : times) {
            graph[edge[0]].push_back({edge[1], edge[2]});
        }
        const int INF = std::numeric_limits<int>::max() / 4;
        std::vector<int> dist(n + 1, INF);
        dist[k] = 0;
        using Node = std::pair<int, int>;
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> heap;
        heap.push({0, k});
        while (!heap.empty()) {
            auto [d, node] = heap.top();
            heap.pop();
            if (d > dist[node]) {
                continue;
            }
            for (auto [nei, weight] : graph[node]) {
                int nd = d + weight;
                if (nd < dist[nei]) {
                    dist[nei] = nd;
                    heap.push({nd, nei});
                }
            }
        }
        int ans = *std::max_element(dist.begin() + 1, dist.end());
        return ans == INF ? -1 : ans;
    }
};


================================================================================
FOLDER 0744_find_smallest_letter_greater_than_target
================================================================================
// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

#include <vector>

class Solution {
public:
    char nextGreatestLetter(std::vector<char>& letters, char target) {
        int left = 0;
        int right = static_cast<int>(letters.size());
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (letters[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return letters[left % letters.size()];
    }
};


================================================================================
FOLDER 0745_prefix_and_suffix_search
================================================================================
// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

#include <string>
#include <unordered_map>
#include <vector>

class WordFilter {
public:
    WordFilter(std::vector<std::string>& words) {
        for (int index = 0; index < static_cast<int>(words.size()); ++index) {
            const std::string& word = words[index];
            int size = static_cast<int>(word.size());
            for (int i = 0; i <= size; ++i) {
                for (int j = 0; j <= size; ++j) {
                    lookup_[word.substr(0, i) + "#" + word.substr(j)] = index;
                }
            }
        }
    }

    int f(std::string pref, std::string suff) {
        auto it = lookup_.find(pref + "#" + suff);
        return it == lookup_.end() ? -1 : it->second;
    }

private:
    std::unordered_map<std::string, int> lookup_;
};


================================================================================
FOLDER 0746_min_cost_climbing_stairs
================================================================================
// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minCostClimbingStairs(std::vector<int>& cost) {
        int a = 0;
        int b = 0;
        for (int i = static_cast<int>(cost.size()) - 1; i >= 0; --i) {
            int nextA = cost[i] + std::min(a, b);
            b = a;
            a = nextA;
        }
        return std::min(a, b);
    }
};


================================================================================
FOLDER 0747_largest_number_at_least_twice_of_others
================================================================================
// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

#include <vector>

class Solution {
public:
    int dominantIndex(std::vector<int>& nums) {
        int first = -1;
        int second = -1;
        int index = -1;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (nums[i] > first) {
                second = first;
                first = nums[i];
                index = i;
            } else if (nums[i] > second) {
                second = nums[i];
            }
        }
        return first >= 2 * second ? index : -1;
    }
};


================================================================================
FOLDER 0748_shortest_completing_word
================================================================================
// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    std::string shortestCompletingWord(std::string licensePlate, std::vector<std::string>& words) {
        int need[26] = {};
        for (char ch : licensePlate) {
            if (std::isalpha(static_cast<unsigned char>(ch))) {
                ++need[std::tolower(static_cast<unsigned char>(ch)) - 'a'];
            }
        }
        std::string best;
        for (const std::string& word : words) {
            int counts[26] = {};
            for (char ch : word) {
                ++counts[ch - 'a'];
            }
            bool ok = true;
            for (int i = 0; i < 26; ++i) {
                if (counts[i] < need[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok && (best.empty() || word.size() < best.size())) {
                best = word;
            }
        }
        return best;
    }
};


================================================================================
FOLDER 0749_contain_virus
================================================================================
// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    int containVirus(std::vector<std::vector<int>>& isInfected) {
        int m = static_cast<int>(isInfected.size());
        int n = static_cast<int>(isInfected[0].size());
        int walls = 0;
        while (true) {
            std::set<std::pair<int, int>> seen;
            std::vector<std::set<std::pair<int, int>>> regions;
            std::vector<std::set<std::pair<int, int>>> frontiers;
            std::vector<int> perimeters;

            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (isInfected[i][j] == 1 && !seen.count({i, j})) {
                        std::vector<std::pair<int, int>> stack{{i, j}};
                        seen.insert({i, j});
                        std::set<std::pair<int, int>> region;
                        std::set<std::pair<int, int>> frontier;
                        int perimeter = 0;
                        while (!stack.empty()) {
                            auto [r, c] = stack.back();
                            stack.pop_back();
                            region.insert({r, c});
                            static const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                            for (auto& d : dirs) {
                                int nr = r + d[0];
                                int nc = c + d[1];
                                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                                    continue;
                                }
                                if (isInfected[nr][nc] == 1 && !seen.count({nr, nc})) {
                                    seen.insert({nr, nc});
                                    stack.push_back({nr, nc});
                                } else if (isInfected[nr][nc] == 0) {
                                    frontier.insert({nr, nc});
                                    ++perimeter;
                                }
                            }
                        }
                        regions.push_back(std::move(region));
                        frontiers.push_back(std::move(frontier));
                        perimeters.push_back(perimeter);
                    }
                }
            }

            if (regions.empty()) {
                break;
            }
            int quarantine = 0;
            for (int i = 1; i < static_cast<int>(regions.size()); ++i) {
                if (frontiers[i].size() > frontiers[quarantine].size()) {
                    quarantine = i;
                }
            }
            if (frontiers[quarantine].empty()) {
                break;
            }
            walls += perimeters[quarantine];
            for (auto [r, c] : regions[quarantine]) {
                isInfected[r][c] = -1;
            }
            for (int index = 0; index < static_cast<int>(frontiers.size()); ++index) {
                if (index == quarantine) {
                    continue;
                }
                for (auto [r, c] : frontiers[index]) {
                    isInfected[r][c] = 1;
                }
            }
        }
        return walls;
    }
};


================================================================================
FOLDER 0750_number_of_corner_rectangles
================================================================================
// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

#include <vector>

class Solution {
public:
    int countCornerRectangles(std::vector<std::vector<int>>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = i + 1; j < m; ++j) {
                int count = 0;
                for (int c = 0; c < n; ++c) {
                    if (grid[i][c] && grid[j][c]) {
                        ++count;
                    }
                }
                ans += count * (count - 1) / 2;
            }
        }
        return ans;
    }
};


================================================================================
FOLDER 0751_ip_to_cidr
================================================================================
// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> ipToCIDR(std::string ip, int n) {
        long long start = ipToInt(ip);
        std::vector<std::string> answer;
        while (n > 0) {
            long long lowbit = start == 0 ? (1LL << 32) : (start & -start);
            while (lowbit > n) {
                lowbit >>= 1;
            }
            int mask = 32 - (bitLength(lowbit) - 1);
            answer.push_back(intToIp(start) + "/" + std::to_string(mask));
            start += lowbit;
            n -= static_cast<int>(lowbit);
        }
        return answer;
    }

private:
    long long ipToInt(const std::string& value) {
        long long result = 0;
        std::stringstream ss(value);
        std::string part;
        while (std::getline(ss, part, '.')) {
            result = result * 256 + std::stoll(part);
        }
        return result;
    }

    std::string intToIp(long long value) {
        return std::to_string((value >> 24) & 255) + "." + std::to_string((value >> 16) & 255) +
               "." + std::to_string((value >> 8) & 255) + "." + std::to_string(value & 255);
    }

    int bitLength(long long value) {
        int len = 0;
        while (value) {
            value >>= 1;
            ++len;
        }
        return len;
    }
};


================================================================================
FOLDER 0752_open_the_lock
================================================================================
// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

#include <queue>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int openLock(std::vector<std::string>& deadends, std::string target) {
        std::unordered_set<std::string> dead(deadends.begin(), deadends.end());
        if (dead.count("0000")) {
            return -1;
        }
        std::queue<std::pair<std::string, int>> q;
        std::unordered_set<std::string> seen{"0000"};
        q.push({"0000", 0});
        while (!q.empty()) {
            auto [state, steps] = q.front();
            q.pop();
            if (state == target) {
                return steps;
            }
            for (int i = 0; i < 4; ++i) {
                int digit = state[i] - '0';
                for (int delta : {-1, 1}) {
                    std::string nxt = state;
                    nxt[i] = static_cast<char>('0' + (digit + delta + 10) % 10);
                    if (!seen.count(nxt) && !dead.count(nxt)) {
                        seen.insert(nxt);
                        q.push({nxt, steps + 1});
                    }
                }
            }
        }
        return -1;
    }
};


================================================================================
FOLDER 0753_cracking_the_safe
================================================================================
// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string crackSafe(int n, int k) {
        seen_.clear();
        path_.clear();
        std::string start(n - 1, '0');
        dfs(start, k);
        std::string result;
        for (char ch : path_) {
            result.push_back(ch);
        }
        return result + start;
    }

private:
    std::unordered_set<std::string> seen_;
    std::vector<char> path_;

    void dfs(const std::string& node, int k) {
        for (int d = 0; d < k; ++d) {
            char digit = static_cast<char>('0' + d);
            std::string edge = node + digit;
            if (!seen_.count(edge)) {
                seen_.insert(edge);
                dfs(edge.substr(1), k);
                path_.push_back(digit);
            }
        }
    }
};


================================================================================
FOLDER 0754_reach_a_number
================================================================================
// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

#include <cstdlib>

class Solution {
public:
    int reachNumber(int target) {
        target = std::abs(target);
        int steps = 0;
        int total = 0;
        while (total < target || (total - target) % 2) {
            ++steps;
            total += steps;
        }
        return steps;
    }
};


================================================================================
FOLDER 0755_pour_water
================================================================================
// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

#include <vector>

class Solution {
public:
    std::vector<int> pourWater(std::vector<int>& heights, int volume, int k) {
        for (int v = 0; v < volume; ++v) {
            int index = k;
            for (int i = k - 1; i >= 0; --i) {
                if (heights[i] > heights[index]) {
                    break;
                }
                if (heights[i] < heights[index]) {
                    index = i;
                }
            }
            if (index != k) {
                ++heights[index];
                continue;
            }
            index = k;
            for (int i = k + 1; i < static_cast<int>(heights.size()); ++i) {
                if (heights[i] > heights[index]) {
                    break;
                }
                if (heights[i] < heights[index]) {
                    index = i;
                }
            }
            ++heights[index];
        }
        return heights;
    }
};


================================================================================
FOLDER 0756_pyramid_transition_matrix
================================================================================
// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool pyramidTransition(std::string bottom, std::vector<std::string>& allowed) {
        transitions_.clear();
        memo_.clear();
        for (const std::string& triple : allowed) {
            transitions_[triple.substr(0, 2)].push_back(triple[2]);
        }
        return dfs(bottom);
    }

private:
    std::unordered_map<std::string, std::vector<char>> transitions_;
    std::unordered_map<std::string, bool> memo_;

    bool dfs(const std::string& row) {
        if (row.size() == 1) {
            return true;
        }
        auto it = memo_.find(row);
        if (it != memo_.end()) {
            return it->second;
        }
        std::vector<std::vector<char>> options;
        for (size_t i = 0; i + 1 < row.size(); ++i) {
            std::string key = row.substr(i, 2);
            auto found = transitions_.find(key);
            if (found == transitions_.end()) {
                return memo_[row] = false;
            }
            options.push_back(found->second);
        }
        std::string path;
        return memo_[row] = build(0, options, path);
    }

    bool build(size_t index, const std::vector<std::vector<char>>& options, std::string& path) {
        if (index == options.size()) {
            return dfs(path);
        }
        for (char ch : options[index]) {
            path.push_back(ch);
            if (build(index + 1, options, path)) {
                return true;
            }
            path.pop_back();
        }
        return false;
    }
};


================================================================================
FOLDER 0757_set_intersection_size_at_least_two
================================================================================
// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

#include <algorithm>
#include <vector>

class Solution {
public:
    int intersectionSizeTwo(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            if (a[1] != b[1]) {
                return a[1] < b[1];
            }
            return a[0] < b[0];
        });
        int size = 0;
        int first = -1;
        int second = -1;
        for (const auto& interval : intervals) {
            int left = interval[0];
            int right = interval[1];
            if (left <= first) {
                continue;
            }
            if (left <= second) {
                ++size;
                first = second;
                second = right;
            } else {
                size += 2;
                first = right - 1;
                second = right;
            }
        }
        return size;
    }
};


================================================================================
FOLDER 0758_bold_words_in_string
================================================================================
// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

#include <string>
#include <vector>

class Solution {
public:
    std::string boldWords(std::vector<std::string>& words, std::string s) {
        int n = static_cast<int>(s.size());
        std::vector<bool> bold(n, false);
        for (const std::string& word : words) {
            size_t start = s.find(word);
            while (start != std::string::npos) {
                for (size_t i = start; i < start + word.size(); ++i) {
                    bold[i] = true;
                }
                start = s.find(word, start + 1);
            }
        }
        std::string parts;
        int i = 0;
        while (i < n) {
            if (bold[i]) {
                parts += "**";
                while (i < n && bold[i]) {
                    parts.push_back(s[i++]);
                }
                parts += "**";
            } else {
                parts.push_back(s[i++]);
            }
        }
        return parts;
    }
};


================================================================================
FOLDER 0759_employee_free_time
================================================================================
// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> employeeFreeTime(std::vector<std::vector<std::vector<int>>>& schedule) {
        std::vector<std::vector<int>> intervals;
        for (const auto& employee : schedule) {
            for (const auto& item : employee) {
                intervals.push_back({item[0], item[1]});
            }
        }
        std::sort(intervals.begin(), intervals.end());
        std::vector<std::vector<int>> merged;
        for (const auto& iv : intervals) {
            if (merged.empty() || merged.back()[1] < iv[0]) {
                merged.push_back(iv);
            } else {
                merged.back()[1] = std::max(merged.back()[1], iv[1]);
            }
        }
        std::vector<std::vector<int>> result;
        for (size_t i = 1; i < merged.size(); ++i) {
            result.push_back({merged[i - 1][1], merged[i][0]});
        }
        return result;
    }
};


================================================================================
FOLDER 0760_find_anagram_mappings
================================================================================
// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> anagramMappings(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, std::queue<int>> positions;
        for (int i = 0; i < static_cast<int>(nums2.size()); ++i) {
            positions[nums2[i]].push(i);
        }
        std::vector<int> result;
        result.reserve(nums1.size());
        for (int value : nums1) {
            result.push_back(positions[value].front());
            positions[value].pop();
        }
        return result;
    }
};


================================================================================
FOLDER 0761_special_binary_string
================================================================================
// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string makeLargestSpecial(std::string s) {
        std::vector<std::string> parts;
        int balance = 0;
        int start = 0;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            balance += s[i] == '1' ? 1 : -1;
            if (balance == 0) {
                parts.push_back("1" + makeLargestSpecial(s.substr(start + 1, i - start - 1)) + "0");
                start = i + 1;
            }
        }
        std::sort(parts.begin(), parts.end(), std::greater<std::string>());
        std::string result;
        for (const std::string& part : parts) {
            result += part;
        }
        return result;
    }
};


================================================================================
FOLDER 0762_prime_number_of_set_bits_in_binary_representation
================================================================================
// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

#include <unordered_set>

class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        static const std::unordered_set<int> primes{2, 3, 5, 7, 11, 13, 17, 19};
        int ans = 0;
        for (int num = left; num <= right; ++num) {
            if (primes.count(__builtin_popcount(num))) {
                ++ans;
            }
        }
        return ans;
    }
};


================================================================================
FOLDER 0763_partition_labels
================================================================================
// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> partitionLabels(std::string s) {
        int last[26] = {};
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            last[s[i] - 'a'] = i;
        }
        int start = 0;
        int end = 0;
        std::vector<int> answer;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            end = std::max(end, last[s[i] - 'a']);
            if (i == end) {
                answer.push_back(end - start + 1);
                start = i + 1;
            }
        }
        return answer;
    }
};


================================================================================
FOLDER 0764_largest_plus_sign
================================================================================
// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int orderOfLargestPlusSign(int n, std::vector<std::vector<int>>& mines) {
        std::unordered_set<int> banned;
        for (const auto& mine : mines) {
            banned.insert(mine[0] * n + mine[1]);
        }
        std::vector<std::vector<int>> arms(n, std::vector<int>(n, 0));
        int best = 0;
        for (int r = 0; r < n; ++r) {
            int count = 0;
            for (int c = 0; c < n; ++c) {
                count = banned.count(r * n + c) ? 0 : count + 1;
                arms[r][c] = count;
            }
            count = 0;
            for (int c = n - 1; c >= 0; --c) {
                count = banned.count(r * n + c) ? 0 : count + 1;
                arms[r][c] = std::min(arms[r][c], count);
            }
        }
        for (int c = 0; c < n; ++c) {
            int count = 0;
            for (int r = 0; r < n; ++r) {
                count = banned.count(r * n + c) ? 0 : count + 1;
                arms[r][c] = std::min(arms[r][c], count);
            }
            count = 0;
            for (int r = n - 1; r >= 0; --r) {
                count = banned.count(r * n + c) ? 0 : count + 1;
                arms[r][c] = std::min(arms[r][c], count);
                best = std::max(best, arms[r][c]);
            }
        }
        return best;
    }
};


================================================================================
FOLDER 0765_couples_holding_hands
================================================================================
// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minSwapsCouples(std::vector<int>& row) {
        std::unordered_map<int, int> pos;
        for (int i = 0; i < static_cast<int>(row.size()); ++i) {
            pos[row[i]] = i;
        }
        int swaps = 0;
        for (int i = 0; i < static_cast<int>(row.size()); i += 2) {
            int partner = row[i] ^ 1;
            if (row[i + 1] == partner) {
                continue;
            }
            int j = pos[partner];
            pos[row[i + 1]] = j;
            row[j] = row[i + 1];
            row[i + 1] = partner;
            pos[partner] = i + 1;
            ++swaps;
        }
        return swaps;
    }
};


================================================================================
FOLDER 0766_toeplitz_matrix
================================================================================
// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

#include <vector>

class Solution {
public:
    bool isToeplitzMatrix(std::vector<std::vector<int>>& matrix) {
        for (size_t r = 1; r < matrix.size(); ++r) {
            for (size_t c = 1; c < matrix[0].size(); ++c) {
                if (matrix[r][c] != matrix[r - 1][c - 1]) {
                    return false;
                }
            }
        }
        return true;
    }
};


================================================================================
FOLDER 0767_reorganize_string
================================================================================
// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

#include <queue>
#include <string>
#include <utility>

class Solution {
public:
    std::string reorganizeString(std::string s) {
        int freq[26] = {};
        for (char ch : s) {
            ++freq[ch - 'a'];
        }
        using Item = std::pair<int, char>;
        std::priority_queue<Item> heap;
        for (int i = 0; i < 26; ++i) {
            if (freq[i]) {
                heap.push({freq[i], static_cast<char>('a' + i)});
            }
        }
        if (!heap.empty() && heap.top().first > (static_cast<int>(s.size()) + 1) / 2) {
            return "";
        }
        std::string result;
        while (heap.size() >= 2) {
            auto [c1, a] = heap.top();
            heap.pop();
            auto [c2, b] = heap.top();
            heap.pop();
            result.push_back(a);
            result.push_back(b);
            if (--c1) {
                heap.push({c1, a});
            }
            if (--c2) {
                heap.push({c2, b});
            }
        }
        if (!heap.empty()) {
            result.push_back(heap.top().second);
        }
        return result;
    }
};


================================================================================
FOLDER 0768_max_chunks_to_make_sorted_ii
================================================================================
// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxChunksToSorted(std::vector<int>& arr) {
        int n = static_cast<int>(arr.size());
        std::vector<int> maxLeft(n), minRight(n);
        maxLeft[0] = arr[0];
        for (int i = 1; i < n; ++i) {
            maxLeft[i] = std::max(maxLeft[i - 1], arr[i]);
        }
        minRight[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            minRight[i] = std::min(minRight[i + 1], arr[i]);
        }
        int chunks = 1;
        for (int i = 0; i < n - 1; ++i) {
            if (maxLeft[i] <= minRight[i + 1]) {
                ++chunks;
            }
        }
        return chunks;
    }
};


================================================================================
FOLDER 0769_max_chunks_to_make_sorted
================================================================================
// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxChunksToSorted(std::vector<int>& arr) {
        int chunks = 0;
        int maxSoFar = 0;
        for (int i = 0; i < static_cast<int>(arr.size()); ++i) {
            maxSoFar = std::max(maxSoFar, arr[i]);
            if (maxSoFar == i) {
                ++chunks;
            }
        }
        return chunks;
    }
};


================================================================================
FOLDER 0770_basic_calculator_iv
================================================================================
// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

#include <algorithm>
#include <cctype>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
    using Poly = std::map<std::vector<std::string>, int>;

public:
    std::vector<std::string> basicCalculatorIV(std::string expression, std::vector<std::string>& evalvars,
                                               std::vector<int>& evalints) {
        values_.clear();
        for (size_t i = 0; i < evalvars.size(); ++i) {
            values_[evalvars[i]] = evalints[i];
        }
        tokens_.clear();
        std::string cur;
        for (char ch : expression) {
            if (ch == '(' || ch == ')') {
                if (!cur.empty()) {
                    tokens_.push_back(cur);
                    cur.clear();
                }
                tokens_.push_back(std::string(1, ch));
            } else if (std::isspace(static_cast<unsigned char>(ch))) {
                if (!cur.empty()) {
                    tokens_.push_back(cur);
                    cur.clear();
                }
            } else {
                cur.push_back(ch);
            }
        }
        if (!cur.empty()) {
            tokens_.push_back(cur);
        }
        pos_ = 0;
        Poly poly = parseExpr();
        std::vector<std::pair<std::vector<std::string>, int>> keys(poly.begin(), poly.end());
        std::sort(keys.begin(), keys.end(), [](const auto& a, const auto& b) {
            if (a.first.size() != b.first.size()) {
                return a.first.size() > b.first.size();
            }
            return a.first < b.first;
        });
        std::vector<std::string> answer;
        for (const auto& [key, coef] : keys) {
            if (coef == 0) {
                continue;
            }
            if (key.empty()) {
                answer.push_back(std::to_string(coef));
            } else {
                std::string term = std::to_string(coef);
                for (const std::string& var : key) {
                    term += "*" + var;
                }
                answer.push_back(term);
            }
        }
        return answer;
    }

private:
    std::unordered_map<std::string, int> values_;
    std::vector<std::string> tokens_;
    int pos_ = 0;

    Poly parseExpr() {
        Poly poly = parseTerm();
        while (pos_ < static_cast<int>(tokens_.size()) &&
               (tokens_[pos_] == "+" || tokens_[pos_] == "-")) {
            std::string op = tokens_[pos_++];
            Poly right = parseTerm();
            poly = add(poly, op == "+" ? right : negate(right));
        }
        return poly;
    }

    Poly parseTerm() {
        Poly poly = parseFactor();
        while (pos_ < static_cast<int>(tokens_.size()) && tokens_[pos_] == "*") {
            ++pos_;
            poly = mul(poly, parseFactor());
        }
        return poly;
    }

    Poly parseFactor() {
        if (tokens_[pos_] == "(") {
            ++pos_;
            Poly poly = parseExpr();
            ++pos_;
            return poly;
        }
        return atom(tokens_[pos_++]);
    }

    Poly atom(const std::string& token) {
        Poly poly;
        if (std::isalpha(static_cast<unsigned char>(token[0]))) {
            auto it = values_.find(token);
            if (it != values_.end()) {
                poly[{}] = it->second;
            } else {
                poly[{token}] = 1;
            }
        } else {
            poly[{}] = std::stoi(token);
        }
        return clean(poly);
    }

    Poly add(const Poly& left, const Poly& right) {
        Poly result = left;
        for (const auto& [key, coef] : right) {
            result[key] += coef;
        }
        return clean(result);
    }

    Poly negate(const Poly& poly) {
        Poly result;
        for (const auto& [key, coef] : poly) {
            result[key] = -coef;
        }
        return result;
    }

    Poly mul(const Poly& left, const Poly& right) {
        Poly result;
        for (const auto& [lk, lv] : left) {
            for (const auto& [rk, rv] : right) {
                std::vector<std::string> key = lk;
                key.insert(key.end(), rk.begin(), rk.end());
                std::sort(key.begin(), key.end());
                result[key] += lv * rv;
            }
        }
        return clean(result);
    }

    Poly clean(Poly poly) {
        for (auto it = poly.begin(); it != poly.end();) {
            if (it->second == 0) {
                it = poly.erase(it);
            } else {
                ++it;
            }
        }
        return poly;
    }
};


================================================================================
FOLDER 0771_jewels_and_stones
================================================================================
// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

#include <string>
#include <unordered_set>

class Solution {
public:
    int numJewelsInStones(std::string jewels, std::string stones) {
        std::unordered_set<char> jewelSet(jewels.begin(), jewels.end());
        int count = 0;
        for (char stone : stones) {
            if (jewelSet.count(stone)) {
                ++count;
            }
        }
        return count;
    }
};


================================================================================
FOLDER 0772_basic_calculator_iii
================================================================================
// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    int calculate(std::string s) {
        std::string expr;
        for (char ch : s) {
            if (!std::isspace(static_cast<unsigned char>(ch))) {
                expr.push_back(ch);
            }
        }
        int i = 0;
        return parse(expr, i);
    }

private:
    int parse(const std::string& expr, int& i) {
        std::vector<long long> stack;
        long long num = 0;
        char sign = '+';
        while (i < static_cast<int>(expr.size())) {
            char ch = expr[i];
            if (std::isdigit(static_cast<unsigned char>(ch))) {
                num = num * 10 + (ch - '0');
            } else if (ch == '(') {
                ++i;
                num = parse(expr, i);
            }
            if ((!std::isdigit(static_cast<unsigned char>(ch)) && ch != '(') ||
                i == static_cast<int>(expr.size()) - 1) {
                if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' ||
                    i == static_cast<int>(expr.size()) - 1) {
                    if (sign == '+') {
                        stack.push_back(num);
                    } else if (sign == '-') {
                        stack.push_back(-num);
                    } else if (sign == '*') {
                        stack.back() *= num;
                    } else if (sign == '/') {
                        long long top = stack.back();
                        stack.pop_back();
                        stack.push_back(static_cast<long long>(top / static_cast<double>(num)));
                    }
                    if (ch == ')') {
                        long long sum = 0;
                        for (long long v : stack) {
                            sum += v;
                        }
                        return static_cast<int>(sum);
                    }
                    sign = ch;
                    num = 0;
                }
            }
            ++i;
        }
        long long sum = 0;
        for (long long v : stack) {
            sum += v;
        }
        return static_cast<int>(sum);
    }
};


================================================================================
FOLDER 0773_sliding_puzzle
================================================================================
// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    int slidingPuzzle(std::vector<std::vector<int>>& board) {
        std::string start;
        for (const auto& row : board) {
            for (int cell : row) {
                start.push_back(static_cast<char>('0' + cell));
            }
        }
        const std::string target = "123450";
        static const std::unordered_map<int, std::vector<int>> neighbors{
            {0, {1, 3}}, {1, {0, 2, 4}}, {2, {1, 5}},
            {3, {0, 4}}, {4, {1, 3, 5}}, {5, {2, 4}},
        };
        std::queue<std::pair<std::string, int>> q;
        std::unordered_set<std::string> seen{start};
        q.push({start, 0});
        while (!q.empty()) {
            auto [state, steps] = q.front();
            q.pop();
            if (state == target) {
                return steps;
            }
            int zero = static_cast<int>(state.find('0'));
            for (int nei : neighbors.at(zero)) {
                std::string nxt = state;
                std::swap(nxt[zero], nxt[nei]);
                if (!seen.count(nxt)) {
                    seen.insert(nxt);
                    q.push({nxt, steps + 1});
                }
            }
        }
        return -1;
    }
};


================================================================================
FOLDER 0774_minimize_max_distance_to_gas_station
================================================================================
// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

#include <vector>

class Solution {
public:
    double minmaxGasDist(std::vector<int>& stations, int k) {
        auto can = [&](double dist) {
            int needed = 0;
            for (size_t i = 1; i < stations.size(); ++i) {
                needed += static_cast<int>((stations[i] - stations[i - 1]) / dist);
            }
            return needed <= k;
        };
        double lo = 0.0;
        double hi = static_cast<double>(stations.back() - stations.front());
        while (hi - lo > 1e-6) {
            double mid = (lo + hi) / 2.0;
            if (can(mid)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        return hi;
    }
};


================================================================================
FOLDER 0775_global_and_local_inversions
================================================================================
// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

#include <cstdlib>
#include <vector>

class Solution {
public:
    bool isIdealPermutation(std::vector<int>& nums) {
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (std::abs(nums[i] - i) > 1) {
                return false;
            }
        }
        return true;
    }
};


================================================================================
FOLDER 0776_split_bst
================================================================================
// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

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
    std::vector<TreeNode*> splitBST(TreeNode* root, int target) {
        if (!root) {
            return {nullptr, nullptr};
        }
        if (root->val <= target) {
            auto parts = splitBST(root->right, target);
            root->right = parts[0];
            return {root, parts[1]};
        }
        auto parts = splitBST(root->left, target);
        root->left = parts[1];
        return {parts[0], root};
    }
};


================================================================================
FOLDER 0777_swap_adjacent_in_lr_string
================================================================================
// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

#include <string>

class Solution {
public:
    bool canTransform(std::string start, std::string result) {
        std::string a;
        std::string b;
        for (char ch : start) {
            if (ch != 'X') {
                a.push_back(ch);
            }
        }
        for (char ch : result) {
            if (ch != 'X') {
                b.push_back(ch);
            }
        }
        if (a != b) {
            return false;
        }
        int i = 0;
        int j = 0;
        int n = static_cast<int>(start.size());
        while (i < n && j < n) {
            while (i < n && start[i] == 'X') {
                ++i;
            }
            while (j < n && result[j] == 'X') {
                ++j;
            }
            if (i == n || j == n) {
                break;
            }
            if (start[i] != result[j]) {
                return false;
            }
            if (start[i] == 'L' && i < j) {
                return false;
            }
            if (start[i] == 'R' && i > j) {
                return false;
            }
            ++i;
            ++j;
        }
        return true;
    }
};
