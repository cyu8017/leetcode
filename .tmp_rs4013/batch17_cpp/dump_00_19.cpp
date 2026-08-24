

########## 3393_count_paths_with_the_given_xor_value ##########
// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

#include <vector>

class Solution {
public:
    int countPathsWithXorValue(std::vector<std::vector<int>>& grid, int k) {
        const int mod = 1000000007;
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<std::vector<int>>> dp(m, std::vector<std::vector<int>>(n, std::vector<int>(16, 0)));
        dp[0][0][grid[0][0]] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int x = 0; x < 16; x++) {
                    if (dp[i][j][x] == 0) continue;
                    if (i + 1 < m) {
                        int nx = x ^ grid[i + 1][j];
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod;
                    }
                    if (j + 1 < n) {
                        int nx = x ^ grid[i][j + 1];
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod;
                    }
                }
            }
        }
        return dp[m - 1][n - 1][k];
    }
};


########## 3394_check_if_grid_can_be_cut_into_sections ##########
// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

#include <algorithm>
#include <vector>

class Solution {
    bool checkCut(std::vector<std::vector<int>>& rects, int axis) {
        struct Seg { int a, b; };
        std::vector<Seg> arr;
        arr.reserve(rects.size());
        for (auto& r : rects) {
            if (axis == 0) arr.push_back({r[0], r[2]});
            else arr.push_back({r[1], r[3]});
        }
        std::sort(arr.begin(), arr.end(), [](const Seg& x, const Seg& y) {
            if (x.a == y.a) return x.b < y.b;
            return x.a < y.a;
        });
        int cuts = 0;
        int end = arr[0].b;
        for (int i = 1; i < (int)arr.size(); i++) {
            if (arr[i].a >= end) {
                cuts++;
                end = arr[i].b;
                if (cuts >= 2) return true;
            } else if (arr[i].b > end) {
                end = arr[i].b;
            }
        }
        return false;
    }

public:
    bool checkValidCuts(int n, std::vector<std::vector<int>>& rectangles) {
        (void)n;
        return checkCut(rectangles, 0) || checkCut(rectangles, 1);
    }
};


########## 3395_subsequences_with_a_unique_middle_mode_i ##########
// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

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
                            if (uniqueMode(seq)) ans++;
                        }
                    }
                }
            }
        }
        return ans % mod;
    }
};


########## 3396_minimum_number_of_operations_to_make_elements_in_array_distinct ##########
// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimumOperations(std::vector<int>& nums) {
        int ops = 0;
        while (true) {
            std::unordered_set<int> seen;
            bool dup = false;
            for (int x : nums) {
                if (seen.count(x)) { dup = true; break; }
                seen.insert(x);
            }
            if (!dup) return ops;
            if ((int)nums.size() <= 3) return ops + 1;
            nums.erase(nums.begin(), nums.begin() + 3);
            ops++;
        }
    }
};


########## 3397_maximum_number_of_distinct_elements_after_operations ##########
// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxDistinctElements(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = 0;
        long long prev = LLONG_MIN / 2;
        for (int x : nums) {
            long long cur = x - k;
            if (cur <= prev) cur = prev + 1;
            if (cur > x + k) continue;
            ans++;
            prev = cur;
        }
        return ans;
    }
};


########## 3398_smallest_substring_with_identical_characters_i ##########
// LeetCode 3398 - Smallest Substring With Identical Characters I
// https://leetcode.com/problems/smallest-substring-with-identical-characters-i/

#include <string>

class Solution {
public:
    int minLength(std::string s, int numOps) {
        int n = (int)s.size();
        auto ok = [&](int L) {
            if (L == 0) return false;
            int ops = 0;
            for (int i = 0; i < n; ) {
                int j = i;
                while (j < n && s[j] == s[i]) j++;
                ops += (j - i) / (L + 1);
                i = j;
            }
            return ops <= numOps;
        };
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};


########## 3399_smallest_substring_with_identical_characters_ii ##########
// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

#include <string>

class Solution {
public:
    int minLength(std::string s, int numOps) {
        int n = (int)s.size();
        auto ok = [&](int L) {
            int ops = 0;
            for (int i = 0; i < n; ) {
                int j = i;
                while (j < n && s[j] == s[i]) j++;
                ops += (j - i) / (L + 1);
                i = j;
            }
            return ops <= numOps;
        };
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};


########## 3400_maximum_number_of_matching_indices_after_right_shifts ##########
// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

#include <vector>

class Solution {
public:
    int maximumMatchingIndices(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size();
        int ans = 0;
        for (int shift = 0; shift < n; shift++) {
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (nums1[(i - shift + n) % n] == nums2[i]) cnt++;
            }
            if (cnt > ans) ans = cnt;
        }
        return ans;
    }
};


########## 3402_minimum_operations_to_make_columns_strictly_increasing ##########
// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

#include <vector>

class Solution {
public:
    int minimumOperations(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int ans = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 1; i < m; i++) {
                if (grid[i][j] <= grid[i - 1][j]) {
                    int need = grid[i - 1][j] + 1;
                    ans += need - grid[i][j];
                    grid[i][j] = need;
                }
            }
        }
        return ans;
    }
};


########## 3403_find_the_lexicographically_largest_string_from_the_box_i ##########
// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

#include <string>

class Solution {
public:
    std::string answerString(std::string word, int numFriends) {
        if (numFriends == 1) return word;
        int n = (int)word.size();
        int maxLen = n - (numFriends - 1);
        std::string ans;
        for (int i = 0; i < n; i++) {
            int end = i + maxLen;
            if (end > n) end = n;
            std::string cand = word.substr(i, end - i);
            if (cand > ans) ans = cand;
        }
        return ans;
    }
};


########## 3404_count_special_subsequences ##########
// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long numberOfSubsequences(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 2; j < n; j++) {
                for (int k = j + 2; k < n; k++) {
                    for (int l = k + 2; l < n; l++) {
                        if ((long long)nums[i] * nums[k] == (long long)nums[j] * nums[l]) ans++;
                    }
                }
            }
        }
        return ans;
    }
};


########## 3405_count_the_number_of_arrays_with_k_matching_adjacent_elements ##########
// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

class Solution {
    static long long modPow(long long a, long long e, int mod) {
        if (a < 0) a = 0;
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
    int countGoodArrays(int n, int m, int k) {
        const int mod = 1000000007;
        return (int)((long long)comb(n - 1, k, mod) * m % mod * modPow(m - 1, n - 1 - k, mod) % mod);
    }
};


########## 3406_find_the_lexicographically_largest_string_from_the_box_ii ##########
// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

#include <string>

class Solution {
public:
    std::string answerString(std::string word, int numFriends) {
        if (numFriends == 1) return word;
        int n = (int)word.size();
        int maxLen = n - (numFriends - 1);
        std::string ans;
        for (int i = 0; i < n; i++) {
            int end = i + maxLen;
            if (end > n) end = n;
            std::string cand = word.substr(i, end - i);
            if (cand > ans) ans = cand;
        }
        return ans;
    }
};


########## 3407_substring_matching_pattern ##########
// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

#include <string>

class Solution {
public:
    bool hasMatch(std::string s, std::string p) {
        auto i = p.find('*');
        std::string left = p.substr(0, i);
        std::string right = p.substr(i + 1);
        auto li = s.find(left);
        if (li == std::string::npos) return false;
        return s.find(right, li + left.size()) != std::string::npos;
    }
};


########## 3408_design_task_manager ##########
// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

#include <queue>
#include <unordered_map>
#include <vector>

class TaskManager {
    struct Item {
        int pri, taskId, userId;
        bool operator<(const Item& o) const {
            if (pri != o.pri) return pri < o.pri;
            return taskId < o.taskId;
        }
    };
    std::priority_queue<Item> h;
    std::unordered_map<int, int> pri;
    std::unordered_map<int, int> user;

public:
    TaskManager(std::vector<std::vector<int>>& tasks) {
        for (auto& t : tasks) add(t[0], t[1], t[2]);
    }

    void add(int userId, int taskId, int priority) {
        pri[taskId] = priority;
        user[taskId] = userId;
        h.push({priority, taskId, userId});
    }

    void edit(int taskId, int newPriority) {
        pri[taskId] = newPriority;
        h.push({newPriority, taskId, user[taskId]});
    }

    void rmv(int taskId) {
        pri.erase(taskId);
        user.erase(taskId);
    }

    int execTop() {
        while (!h.empty()) {
            Item top = h.top();
            h.pop();
            auto it = pri.find(top.taskId);
            if (it != pri.end() && it->second == top.pri && user[top.taskId] == top.userId) {
                pri.erase(top.taskId);
                int uid = user[top.taskId];
                user.erase(top.taskId);
                return uid;
            }
        }
        return -1;
    }
};


########## 3409_longest_subsequence_with_decreasing_adjacent_difference ##########
// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int longestSubsequence(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = 1;
        std::vector<std::vector<int>> dp(n, std::vector<int>(301, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int d = std::abs(nums[i] - nums[j]);
                int best = 1;
                for (int pd = d; pd <= 300; pd++) {
                    if (dp[j][pd] > best) best = dp[j][pd];
                }
                if (best + 1 > dp[i][d]) dp[i][d] = best + 1;
                if (dp[i][d] > ans) ans = dp[i][d];
            }
            if (dp[i][0] < 1) dp[i][0] = 1;
        }
        return ans;
    }
};


########## 3410_maximize_subarray_sum_after_removing_all_occurrences_of_one_element ##########
// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

#include <cstdint>
#include <unordered_set>
#include <vector>

class Solution {
    long long kadane(const std::vector<int>& a) {
        long long best = -(1LL << 62), cur = 0;
        for (int x : a) {
            cur += x;
            if (cur > best) best = cur;
            if (cur < 0) cur = 0;
        }
        bool allNeg = true;
        long long mx = a[0];
        for (int x : a) {
            if (x > mx) mx = x;
            if (x >= 0) allNeg = false;
        }
        if (allNeg) return mx;
        return best;
    }

public:
    long long maxSubarraySum(std::vector<int>& nums) {
        long long ans = kadane(nums);
        std::unordered_set<int> uniq;
        for (int x : nums) if (x < 0) uniq.insert(x);
        for (int v : uniq) {
            std::vector<int> b;
            for (int x : nums) if (x != v) b.push_back(x);
            if (b.empty()) continue;
            long long cand = kadane(b);
            if (cand > ans) ans = cand;
        }
        return ans;
    }
};


########## 3411_maximum_subarray_with_equal_products ##########
// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

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
    int maxLength(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = 1;
        for (int i = 0; i < n; i++) {
            long long prod = 1;
            int g = 0, l = 1;
            for (int j = i; j < n; j++) {
                if (prod > 1000000000LL / nums[j]) break;
                prod *= nums[j];
                if (g == 0) {
                    g = nums[j];
                    l = nums[j];
                } else {
                    g = gcd(g, nums[j]);
                    l = l / gcd(l, nums[j]) * nums[j];
                }
                if (prod == (long long)l * g && j - i + 1 > ans) ans = j - i + 1;
            }
        }
        return ans;
    }
};


########## 3412_find_mirror_score_of_a_string ##########
// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

#include <cstdint>
#include <string>
#include <vector>

class Solution {
public:
    long long calculateScore(std::string s) {
        std::vector<std::vector<int>> stacks(26);
        long long ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            int ci = s[i] - 'a';
            int mir = 25 - ci;
            if (!stacks[mir].empty()) {
                int j = stacks[mir].back();
                stacks[mir].pop_back();
                ans += i - j;
            } else {
                stacks[ci].push_back(i);
            }
        }
        return ans;
    }
};


########## 3413_maximum_coins_from_k_consecutive_bags ##########
// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long maximumCoins(std::vector<std::vector<int>>& coins, int k) {
        std::sort(coins.begin(), coins.end(), [](auto& a, auto& b) { return a[0] < b[0]; });
        long long ans = 0;
        int n = (int)coins.size();
        for (int i = 0; i < n; i++) {
            long long sum = 0;
            int start = coins[i][0];
            int end = start + k - 1;
            for (int j = i; j < n && coins[j][0] <= end; j++) {
                int l = coins[j][0];
                int r = coins[j][1];
                if (r > end) r = end;
                if (l < start) l = start;
                if (l <= r) sum += (long long)(r - l + 1) * coins[j][2];
            }
            if (sum > ans) ans = sum;
        }
        for (int i = 0; i < n; i++) {
            long long sum = 0;
            int end = coins[i][1];
            int start = end - k + 1;
            for (int j = 0; j <= i; j++) {
                int l = coins[j][0];
                int r = coins[j][1];
                if (l < start) l = start;
                if (r > end) r = end;
                if (l <= r) sum += (long long)(r - l + 1) * coins[j][2];
            }
            if (sum > ans) ans = sum;
        }
        return ans;
    }
};
