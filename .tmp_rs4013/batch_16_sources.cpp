

// ========== 3283_maximum_number_of_moves_to_kill_all_pawns ==========
// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

#include <array>
#include <functional>
#include <map>
#include <queue>
#include <utility>
#include <vector>

class Solution {
    std::vector<int> knightDist(int x, int y, const std::vector<std::array<int, 2>>& pts) {
        static const int dirs[8][2] = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};
        int np = (int)pts.size();
        std::vector<int> ans(np, -1);
        bool vis[50][50] = {};
        std::queue<std::array<int, 3>> q;
        q.push({x, y, 0});
        vis[x][y] = true;
        std::map<std::pair<int, int>, std::vector<int>> need;
        for (int i = 0; i < np; i++) need[{pts[i][0], pts[i][1]}].push_back(i);
        int found = 0;
        while (!q.empty() && found < np) {
            auto cur = q.front();
            q.pop();
            auto key = std::make_pair(cur[0], cur[1]);
            auto it = need.find(key);
            if (it != need.end()) {
                for (int i : it->second) {
                    if (ans[i] == -1) {
                        ans[i] = cur[2];
                        found++;
                    }
                }
            }
            for (auto& d : dirs) {
                int nx = cur[0] + d[0], ny = cur[1] + d[1];
                if (nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny]) continue;
                vis[nx][ny] = true;
                q.push({nx, ny, cur[2] + 1});
            }
        }
        return ans;
    }

public:
    int maxMoves(int kx, int ky, std::vector<std::vector<int>>& positions) {
        int n = (int)positions.size();
        std::vector<std::array<int, 2>> pts(n + 1);
        pts[0] = {kx, ky};
        for (int i = 0; i < n; i++) pts[i + 1] = {positions[i][0], positions[i][1]};
        std::vector<std::vector<int>> dist(n + 1);
        for (int i = 0; i <= n; i++) dist[i] = knightDist(pts[i][0], pts[i][1], pts);
        int N = 1 << n;
        std::vector<std::vector<int>> memo(N, std::vector<int>(n + 1, -1));
        std::function<int(int, int, int)> dfs = [&](int mask, int cur, int turn) -> int {
            if (mask == N - 1) return 0;
            if (memo[mask][cur] != -1) return memo[mask][cur];
            int best = turn == 0 ? -(1 << 30) : (1 << 30);
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                int d = dist[cur][i + 1];
                int v = d + dfs(mask | (1 << i), i + 1, 1 - turn);
                if (turn == 0) {
                    if (v > best) best = v;
                } else if (v < best) best = v;
            }
            return memo[mask][cur] = best;
        };
        return dfs(0, 0, 0);
    }
};


// ========== 3284_sum_of_consecutive_subarrays ==========
// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

#include <vector>

class Solution {
public:
    int rangeSum(std::vector<int>& nums) {
        const int mod = 1000000007;
        int n = (int)nums.size(), ans = 0, i = 0;
        while (i < n) {
            int j = i;
            while (j + 1 < n && (nums[j + 1] == nums[j] + 1 || nums[j + 1] == nums[j] - 1)) j++;
            for (int L = i; L <= j; L++) {
                int s = 0;
                for (int R = L; R <= j; R++) {
                    s += nums[R];
                    ans = (ans + s) % mod;
                }
            }
            i = j + 1;
        }
        return ans;
    }
};


// ========== 3285_find_indices_of_stable_mountains ==========
// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

#include <vector>

class Solution {
public:
    std::vector<int> stableMountains(std::vector<int>& height, int threshold) {
        std::vector<int> ans;
        for (int i = 1; i < (int)height.size(); i++) {
            if (height[i - 1] > threshold) ans.push_back(i);
        }
        return ans;
    }
};


// ========== 3286_find_a_safe_walk_through_a_grid ==========
// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

#include <array>
#include <queue>
#include <vector>

class Solution {
public:
    bool findSafeWalk(std::vector<std::vector<int>>& grid, int health) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> vis(m, std::vector<int>(n, -1));
        int qh = health - grid[0][0];
        if (qh <= 0) return false;
        std::queue<std::array<int, 3>> q;
        q.push({0, 0, qh});
        vis[0][0] = qh;
        const int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            if (cur[0] == m - 1 && cur[1] == n - 1) return true;
            for (auto& d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int nh = cur[2] - grid[nr][nc];
                if (nh <= 0) continue;
                if (nh > vis[nr][nc]) {
                    vis[nr][nc] = nh;
                    q.push({nr, nc, nh});
                }
            }
        }
        return false;
    }
};


// ========== 3287_find_the_maximum_sequence_value_of_array ==========
// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

#include <vector>

class Solution {
public:
    int maxValue(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        const int MAX = 128;
        std::vector<std::vector<std::vector<char>>> left(n + 1, std::vector<std::vector<char>>(k + 1, std::vector<char>(MAX, 0)));
        left[0][0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                for (int v = 0; v < MAX; v++) {
                    if (!left[i][j][v]) continue;
                    left[i + 1][j][v] = 1;
                    if (j < k) left[i + 1][j + 1][v | nums[i]] = 1;
                }
            }
        }
        std::vector<std::vector<std::vector<char>>> right(n + 1, std::vector<std::vector<char>>(k + 1, std::vector<char>(MAX, 0)));
        right[n][0][0] = 1;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= k; j++) {
                for (int v = 0; v < MAX; v++) {
                    if (!right[i + 1][j][v]) continue;
                    right[i][j][v] = 1;
                    if (j < k) right[i][j + 1][v | nums[i]] = 1;
                }
            }
        }
        int ans = 0;
        for (int mid = k; mid + k <= n; mid++) {
            for (int a = 0; a < MAX; a++) {
                if (!left[mid][k][a]) continue;
                for (int b = 0; b < MAX; b++) {
                    if (right[mid][k][b] && (a ^ b) > ans) ans = a ^ b;
                }
            }
        }
        return ans;
    }
};


// ========== 3288_length_of_the_longest_increasing_path ==========
// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

#include <algorithm>
#include <vector>

class Solution {
    int lis(const std::vector<int>& a) {
        std::vector<int> tails;
        for (int x : a) {
            auto it = std::lower_bound(tails.begin(), tails.end(), x);
            if (it == tails.end()) tails.push_back(x);
            else *it = x;
        }
        return (int)tails.size();
    }

public:
    int maxPathLength(std::vector<std::vector<int>>& coordinates, int k) {
        int n = (int)coordinates.size();
        struct Pt { int x, y, i; };
        std::vector<Pt> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {coordinates[i][0], coordinates[i][1], i};
        std::sort(arr.begin(), arr.end(), [](const Pt& a, const Pt& b) {
            if (a.x == b.x) return a.y > b.y;
            return a.x < b.x;
        });
        int kx = coordinates[k][0], ky = coordinates[k][1];
        std::vector<int> left, right;
        for (auto& p : arr) {
            if (p.x < kx && p.y < ky) left.push_back(p.y);
            if (p.x > kx && p.y > ky) right.push_back(p.y);
        }
        return lis(left) + 1 + lis(right);
    }
};


// ========== 3289_the_two_sneaky_numbers_of_digitville ==========
// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> getSneakyNumbers(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        std::vector<int> ans;
        for (int x : nums) {
            if (seen.count(x)) ans.push_back(x);
            else seen.insert(x);
        }
        return ans;
    }
};


// ========== 3290_maximum_multiplication_score ==========
// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

#include <array>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& a, std::vector<int>& b) {
        const long long neg = -(1LL << 62);
        std::array<long long, 5> dp{0, neg, neg, neg, neg};
        for (int x : b) {
            for (int k = 4; k >= 1; k--) {
                if (dp[k - 1] == neg) continue;
                long long v = dp[k - 1] + (long long)a[k - 1] * x;
                if (v > dp[k]) dp[k] = v;
            }
        }
        return dp[4];
    }
};


// ========== 3291_minimum_number_of_valid_strings_to_form_target_i ==========
// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

#include <string>
#include <vector>

class Solution {
    struct TrieNode {
        TrieNode* next[26]{};
    };

public:
    int minValidStrings(std::vector<std::string>& words, std::string target) {
        int n = (int)target.size();
        const int inf = 1000000000;
        std::vector<int> dp(n + 1, inf);
        dp[0] = 0;
        TrieNode* root = new TrieNode();
        for (auto& w : words) {
            TrieNode* cur = root;
            for (char c : w) {
                int ci = c - 'a';
                if (!cur->next[ci]) cur->next[ci] = new TrieNode();
                cur = cur->next[ci];
            }
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == inf) continue;
            TrieNode* cur = root;
            for (int j = i; j < n; j++) {
                int ci = target[j] - 'a';
                if (!cur->next[ci]) break;
                cur = cur->next[ci];
                if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
            }
        }
        return dp[n] == inf ? -1 : dp[n];
    }
};


// ========== 3292_minimum_number_of_valid_strings_to_form_target_ii ==========
// LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

#include <string>
#include <vector>

class Solution {
    struct TrieNode {
        TrieNode* next[26]{};
    };

public:
    int minValidStrings(std::vector<std::string>& words, std::string target) {
        int n = (int)target.size();
        const int inf = 1000000000;
        std::vector<int> dp(n + 1, inf);
        dp[0] = 0;
        TrieNode* root = new TrieNode();
        for (auto& w : words) {
            TrieNode* cur = root;
            for (char c : w) {
                int ci = c - 'a';
                if (!cur->next[ci]) cur->next[ci] = new TrieNode();
                cur = cur->next[ci];
            }
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == inf) continue;
            TrieNode* cur = root;
            for (int j = i; j < n; j++) {
                int ci = target[j] - 'a';
                if (!cur->next[ci]) break;
                cur = cur->next[ci];
                if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
            }
        }
        return dp[n] == inf ? -1 : dp[n];
    }
};


// ========== 3294_convert_doubly_linked_list_to_array_ii ==========
// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

#include <vector>

class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node() : val(0), prev(nullptr), next(nullptr) {}
    Node(int x) : val(x), prev(nullptr), next(nullptr) {}
};

class Solution {
public:
    std::vector<int> toArray(Node* node) {
        while (node && node->prev) node = node->prev;
        std::vector<int> ans;
        while (node) {
            ans.push_back(node->val);
            node = node->next;
        }
        return ans;
    }
};


// ========== 3295_report_spam_message ==========
// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool reportSpam(std::vector<std::string>& message, std::vector<std::string>& bannedWords) {
        std::unordered_set<std::string> ban(bannedWords.begin(), bannedWords.end());
        int cnt = 0;
        for (auto& w : message) {
            if (ban.count(w)) {
                cnt++;
                if (cnt >= 2) return true;
            }
        }
        return false;
    }
};


// ========== 3296_minimum_number_of_seconds_to_make_mountain_height_zero ==========
// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, std::vector<int>& workerTimes) {
        auto ok = [&](long long t) {
            long long total = 0;
            for (int w : workerTimes) {
                long long lo = 0, hi = mountainHeight;
                while (lo < hi) {
                    long long mid = (lo + hi + 1) / 2;
                    if ((long long)w * mid * (mid + 1) / 2 <= t) lo = mid;
                    else hi = mid - 1;
                }
                total += lo;
                if (total >= mountainHeight) return true;
            }
            return total >= mountainHeight;
        };
        long long lo = 0, hi = (long long)1e18;
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};


// ========== 3297_count_substrings_that_can_be_rearranged_to_contain_a_string_i ==========
// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

#include <array>
#include <string>

class Solution {
public:
    long long validSubstringCount(std::string word1, std::string word2) {
        std::array<int, 26> need{};
        int required = 0;
        for (char c : word2) {
            if (need[c - 'a'] == 0) required++;
            need[c - 'a']++;
        }
        std::array<int, 26> have{};
        int formed = 0;
        long long ans = 0;
        int l = 0;
        for (int r = 0; r < (int)word1.size(); r++) {
            int c = word1[r] - 'a';
            have[c]++;
            if (have[c] == need[c] && need[c] > 0) formed++;
            while (formed == required && l <= r) {
                ans += (int)word1.size() - r;
                int c2 = word1[l] - 'a';
                if (have[c2] == need[c2] && need[c2] > 0) formed--;
                have[c2]--;
                l++;
            }
        }
        return ans;
    }
};


// ========== 3298_count_substrings_that_can_be_rearranged_to_contain_a_string_ii ==========
// LeetCode 3298 - Count Substrings That Can Be Rearranged to Contain a String II
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/

#include <array>
#include <string>

class Solution {
public:
    long long validSubstringCount(std::string word1, std::string word2) {
        std::array<int, 26> need{};
        int required = 0;
        for (char c : word2) {
            if (need[c - 'a'] == 0) required++;
            need[c - 'a']++;
        }
        std::array<int, 26> have{};
        int formed = 0;
        long long ans = 0;
        int l = 0;
        for (int r = 0; r < (int)word1.size(); r++) {
            int c = word1[r] - 'a';
            have[c]++;
            if (have[c] == need[c] && need[c] > 0) formed++;
            while (formed == required && l <= r) {
                ans += (int)word1.size() - r;
                int c2 = word1[l] - 'a';
                if (have[c2] == need[c2] && need[c2] > 0) formed--;
                have[c2]--;
                l++;
            }
        }
        return ans;
    }
};


// ========== 3299_sum_of_consecutive_subsequences ==========
// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int rangeSum(std::vector<int>& nums) {
        const int mod = 1000000007;
        std::unordered_map<int, int> cnt, sum;
        int ans = 0;
        for (int x : nums) {
            int cL = cnt[x - 1], sL = sum[x - 1];
            int cR = cnt[x + 1], sR = sum[x + 1];
            int c = (1 + cL + cR) % mod;
            int s = (int)(((long long)x + sL + (long long)cL * x % mod + sR + (long long)cR * x % mod) % mod);
            if (cL > 0 && cR > 0) {
                c = (c + (int)((long long)cL * cR % mod)) % mod;
                s = (int)((s + (long long)sL * cR % mod + (long long)sR * cL % mod + (long long)cL * cR % mod * x % mod) % mod);
            }
            cnt[x] = (cnt[x] + c) % mod;
            sum[x] = (sum[x] + s) % mod;
            ans = (ans + s) % mod;
        }
        return ans;
    }
};


// ========== 3300_minimum_element_after_replacement_with_digit_sum ==========
// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

#include <vector>

class Solution {
public:
    int minElement(std::vector<int>& nums) {
        int ans = 1000000000;
        for (int x : nums) {
            int s = 0;
            while (x > 0) { s += x % 10; x /= 10; }
            if (s < ans) ans = s;
        }
        return ans;
    }
};


// ========== 3301_maximize_the_total_height_of_unique_towers ==========
// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long maximumTotalSum(std::vector<int>& maximumHeight) {
        std::sort(maximumHeight.begin(), maximumHeight.end(), std::greater<int>());
        long long ans = 0;
        long long prev = (long long)1e18;
        for (int h : maximumHeight) {
            long long cur = h;
            if (cur >= prev) cur = prev - 1;
            if (cur <= 0) return -1;
            ans += cur;
            prev = cur;
        }
        return ans;
    }
};


// ========== 3302_find_the_lexicographically_smallest_valid_sequence ==========
// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

#include <string>
#include <vector>

class Solution {
    bool canFinish(const std::string& w1, const std::string& w2, int i, int j, bool usedSkip, const std::vector<int>& right) {
        int m = (int)w2.size();
        if (j >= m) return true;
        if (!usedSkip) {
            if (right[j] >= i) return true;
            if (j + 1 <= m && right[j + 1] > i) return true;
            if (right[j] > i) return true;
            return false;
        }
        return right[j] >= i;
    }

public:
    std::vector<int> validSequence(std::string word1, std::string word2) {
        int n = (int)word1.size(), m = (int)word2.size();
        std::vector<int> right(m + 1);
        right[m] = n;
        int j = m - 1;
        for (int i = n - 1; i >= 0 && j >= 0; i--) {
            if (word1[i] == word2[j]) {
                right[j] = i;
                j--;
            }
        }
        for (; j >= 0; j--) right[j] = -1;
        std::vector<int> ans(m);
        bool usedSkip = false;
        int i = 0;
        for (j = 0; j < m; j++) {
            bool found = false;
            while (i < n) {
                if (word1[i] == word2[j]) {
                    if (canFinish(word1, word2, i + 1, j + 1, usedSkip, right)) {
                        ans[j] = i; i++; found = true; break;
                    }
                } else if (!usedSkip) {
                    if (canFinish(word1, word2, i + 1, j + 1, true, right)) {
                        ans[j] = i; i++; usedSkip = true; found = true; break;
                    }
                }
                i++;
            }
            if (!found) return {};
        }
        return ans;
    }
};


// ========== 3303_find_the_occurrence_of_first_almost_equal_substring ==========
// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

#include <string>

class Solution {
public:
    int minStartingIndex(std::string s, std::string pattern) {
        int n = (int)s.size(), m = (int)pattern.size();
        for (int i = 0; i + m <= n; i++) {
            int diff = 0;
            for (int j = 0; j < m; j++) {
                if (s[i + j] != pattern[j]) {
                    diff++;
                    if (diff > 1) break;
                }
            }
            if (diff <= 1) return i;
        }
        return -1;
    }
};


// ========== 3304_find_the_k_th_character_in_string_game_i ==========
// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

#include <string>

class Solution {
public:
    char kthCharacter(int k) {
        std::string s = "a";
        while ((int)s.size() < k) {
            int n = (int)s.size();
            for (int i = 0; i < n; i++) s.push_back(char('a' + ((s[i] - 'a' + 1) % 26)));
        }
        return s[k - 1];
    }
};


// ========== 3305_count_of_substrings_containing_every_vowel_and_k_consonants_i ==========
// LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

#include <string>
#include <unordered_map>

class Solution {
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    int atLeast(const std::string& word, int k) {
        std::unordered_map<char, int> cnt;
        int cons = 0, l = 0, ans = 0;
        for (int r = 0; r < (int)word.size(); r++) {
            char c = word[r];
            if (isVowel(c)) cnt[c]++;
            else cons++;
            while ((int)cnt.size() == 5 && cons >= k) {
                ans += (int)word.size() - r;
                char c2 = word[l];
                if (isVowel(c2)) {
                    if (--cnt[c2] == 0) cnt.erase(c2);
                } else cons--;
                l++;
            }
        }
        return ans;
    }

public:
    int countOfSubstrings(std::string word, int k) {
        return atLeast(word, k) - atLeast(word, k + 1);
    }
};


// ========== 3306_count_of_substrings_containing_every_vowel_and_k_consonants_ii ==========
// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

#include <string>
#include <unordered_map>

class Solution {
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    int atLeast(const std::string& word, int k) {
        std::unordered_map<char, int> cnt;
        int cons = 0, l = 0, ans = 0;
        for (int r = 0; r < (int)word.size(); r++) {
            char c = word[r];
            if (isVowel(c)) cnt[c]++;
            else cons++;
            while ((int)cnt.size() == 5 && cons >= k) {
                ans += (int)word.size() - r;
                char c2 = word[l];
                if (isVowel(c2)) {
                    if (--cnt[c2] == 0) cnt.erase(c2);
                } else cons--;
                l++;
            }
        }
        return ans;
    }

public:
    long long countOfSubstrings(std::string word, int k) {
        return (long long)atLeast(word, k) - atLeast(word, k + 1);
    }
};


// ========== 3307_find_the_k_th_character_in_string_game_ii ==========
// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

#include <cstdint>
#include <vector>

class Solution {
public:
    char kthCharacter(long long k, std::vector<int>& operations) {
        int shift = 0;
        std::vector<int> ops = operations;
        while (!ops.empty()) {
            int op = ops.back();
            ops.pop_back();
            long long half = 1LL << (int)ops.size();
            if (k > half) {
                k -= half;
                if (op == 1) shift++;
            }
        }
        return char('a' + shift % 26);
    }
};


// ========== 3309_maximum_possible_number_by_binary_concatenation ==========
// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

#include <string>
#include <vector>

class Solution {
    std::string toBin(int x) {
        if (x == 0) return "0";
        std::string s;
        while (x > 0) {
            s.insert(s.begin(), char('0' + (x & 1)));
            x >>= 1;
        }
        return s;
    }

public:
    int maxGoodNumber(std::vector<int>& nums) {
        std::string bs[3];
        for (int i = 0; i < 3; i++) bs[i] = toBin(nums[i]);
        int idx[3] = {0, 1, 2};
        int ans = 0;
        auto perm = [&](auto&& self, int i) -> void {
            if (i == 3) {
                std::string s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]];
                int v = 0;
                for (char c : s) v = v * 2 + (c - '0');
                if (v > ans) ans = v;
                return;
            }
            for (int j = i; j < 3; j++) {
                std::swap(idx[i], idx[j]);
                self(self, i + 1);
                std::swap(idx[i], idx[j]);
            }
        };
        perm(perm, 0);
        return ans;
    }
};


// ========== 3310_remove_methods_from_project ==========
// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> remainingMethods(int n, int k, std::vector<std::vector<int>>& invocations) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : invocations) g[e[0]].push_back(e[1]);
        std::vector<char> sus(n, 0);
        std::function<void(int)> dfs = [&](int u) {
            if (sus[u]) return;
            sus[u] = 1;
            for (int v : g[u]) dfs(v);
        };
        dfs(k);
        for (auto& e : invocations) {
            if (!sus[e[0]] && sus[e[1]]) {
                std::vector<int> ans(n);
                for (int i = 0; i < n; i++) ans[i] = i;
                return ans;
            }
        }
        std::vector<int> ans;
        for (int i = 0; i < n; i++) if (!sus[i]) ans.push_back(i);
        return ans;
    }
};


// ========== 3311_construct_2d_grid_matching_graph_layout ==========
// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> constructGridLayout(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<int> deg(n);
        for (int i = 0; i < n; i++) deg[i] = (int)g[i].size();
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (deg[i] == 1) { start = i; break; }
            if (deg[i] == 2) start = i;
        }
        std::vector<char> vis(n, 0);
        std::vector<int> row;
        int cur = start, prev = -1;
        for (;;) {
            row.push_back(cur);
            vis[cur] = 1;
            int next = -1;
            for (int v : g[cur]) {
                if (v != prev && !vis[v] && deg[v] <= 3) {
                    next = v;
                    if (deg[v] < 4) break;
                }
            }
            if (next == -1) break;
            prev = cur;
            cur = next;
        }
        int width = (int)row.size();
        int height = width ? n / width : n;
        if (width == 0 || width * height != n) {
            for (int w = 1; w <= n; w++) {
                if (n % w == 0) { width = w; height = n / w; break; }
            }
        }
        std::vector<std::vector<int>> grid(height, std::vector<int>(width, 0));
        for (int i = 0; i < n; i++) grid[i / width][i % width] = i;
        return grid;
    }
};


// ========== 3312_sorted_gcd_pair_queries ==========
// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<int> gcdValues(std::vector<int>& nums, std::vector<long long>& queries) {
        int maxV = *std::max_element(nums.begin(), nums.end());
        std::vector<int> cnt(maxV + 1);
        for (int x : nums) cnt[x]++;
        std::vector<int64_t> divCnt(maxV + 1);
        for (int g = 1; g <= maxV; g++) {
            int64_t c = 0;
            for (int m = g; m <= maxV; m += g) c += cnt[m];
            divCnt[g] = c * (c - 1) / 2;
        }
        std::vector<int64_t> exact(maxV + 1);
        for (int g = maxV; g >= 1; g--) {
            exact[g] = divCnt[g];
            for (int m = 2 * g; m <= maxV; m += g) exact[g] -= exact[m];
        }
        std::vector<int64_t> pref(maxV + 1);
        for (int g = 1; g <= maxV; g++) pref[g] = pref[g - 1] + exact[g];
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            long long q = queries[i];
            int lo = 1, hi = maxV;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (pref[mid] > q) hi = mid;
                else lo = mid + 1;
            }
            ans[i] = lo;
        }
        return ans;
    }
};


// ========== 3313_find_the_last_marked_nodes_in_tree ==========
// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> lastMarkedNodes(std::vector<std::vector<int>>& edges) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        auto bfs = [&](int start) {
            std::vector<int> dist(n, -1);
            std::queue<int> q;
            q.push(start);
            dist[start] = 0;
            int far = start;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                if (dist[u] > dist[far]) far = u;
                for (int v : g[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            return std::make_pair(far, dist);
        };
        auto [u, _] = bfs(0);
        auto [v, du] = bfs(u);
        auto [__, dv] = bfs(v);
        (void)__;
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = du[i] >= dv[i] ? u : v;
        return ans;
    }
};


// ========== 3314_construct_the_minimum_bitwise_array_i ==========
// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

#include <vector>

class Solution {
public:
    std::vector<int> minBitwiseArray(std::vector<int>& nums) {
        std::vector<int> ans(nums.size(), -1);
        for (int i = 0; i < (int)nums.size(); i++) {
            for (int x = 0; x < nums[i]; x++) {
                if ((x | (x + 1)) == nums[i]) { ans[i] = x; break; }
            }
        }
        return ans;
    }
};


// ========== 3315_construct_the_minimum_bitwise_array_ii ==========
// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

#include <vector>

class Solution {
public:
    std::vector<int> minBitwiseArray(std::vector<int>& nums) {
        std::vector<int> ans(nums.size(), -1);
        for (int i = 0; i < (int)nums.size(); i++) {
            int n = nums[i];
            if (n == 2) continue;
            for (int b = 0; b < 31; b++) {
                if (((n >> b) & 1) == 0) continue;
                int x = n ^ (1 << b);
                if ((x | (x + 1)) == n) { ans[i] = x; break; }
            }
        }
        return ans;
    }
};


// ========== 3316_find_maximum_removals_from_source_string ==========
// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

#include <string>
#include <vector>

class Solution {
public:
    int maxRemovals(std::string source, std::string pattern, std::vector<int>& targetIndices) {
        int n = (int)source.size();
        auto ok = [&](int removeFirst) {
            std::vector<char> mark(n, 0);
            for (int i = 0; i < removeFirst; i++) mark[targetIndices[i]] = 1;
            int j = 0;
            for (int i = 0; i < n && j < (int)pattern.size(); i++) {
                if (mark[i]) continue;
                if (source[i] == pattern[j]) j++;
            }
            return j == (int)pattern.size();
        };
        int lo = 0, hi = (int)targetIndices.size();
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};


// ========== 3317_find_the_number_of_possible_ways_for_an_event ==========
// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

#include <vector>

class Solution {
    int modPow(long long a, long long e, int mod) {
        long long r = 1;
        a %= mod;
        while (e > 0) {
            if (e & 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return (int)r;
    }

public:
    int numberOfWays(int n, int x, int y) {
        const int mod = 1000000007;
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(x + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= x && j <= i; j++) {
                dp[i][j] = (dp[i - 1][j - 1] + (int)((long long)j * dp[i - 1][j] % mod)) % mod;
            }
        }
        std::vector<int> fact(x + 1);
        fact[0] = 1;
        for (int i = 1; i <= x; i++) fact[i] = (int)((long long)fact[i - 1] * i % mod);
        int ans = 0, ypow = 1;
        for (int k = 1; k <= x && k <= n; k++) {
            ypow = (int)((long long)ypow * y % mod);
            int perm = (int)((long long)fact[x] * modPow(fact[x - k], mod - 2, mod) % mod);
            ans = (ans + (int)((long long)dp[n][k] * perm % mod * ypow % mod)) % mod;
        }
        return ans;
    }
};


// ========== 3318_find_x_sum_of_all_k_long_subarrays_i ==========
// LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> findXSum(std::vector<int>& nums, int k, int x) {
        int n = (int)nums.size();
        std::vector<int> ans(n - k + 1);
        for (int i = 0; i <= n - k; i++) {
            std::unordered_map<int, int> freq;
            for (int j = i; j < i + k; j++) freq[nums[j]]++;
            struct P { int v, f; };
            std::vector<P> arr;
            for (auto& p : freq) arr.push_back({p.first, p.second});
            for (int a = 0; a < (int)arr.size(); a++) {
                for (int b = a + 1; b < (int)arr.size(); b++) {
                    if (arr[b].f > arr[a].f || (arr[b].f == arr[a].f && arr[b].v > arr[a].v))
                        std::swap(arr[a], arr[b]);
                }
            }
            int lim = std::min(x, (int)arr.size());
            std::unordered_map<int, char> keep;
            for (int t = 0; t < lim; t++) keep[arr[t].v] = 1;
            int sum = 0;
            for (int j = i; j < i + k; j++) if (keep.count(nums[j])) sum += nums[j];
            ans[i] = sum;
        }
        return ans;
    }
};


// ========== 3319_k_th_largest_perfect_subtree_size_in_binary_tree ==========
// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

#include <algorithm>
#include <functional>
#include <tuple>
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
    int kthLargestPerfectSubtree(TreeNode* root, int k) {
        std::vector<int> sizes;
        std::function<std::tuple<int, int, bool>(TreeNode*)> dfs = [&](TreeNode* node) -> std::tuple<int, int, bool> {
            if (!node) return {0, 0, true};
            auto [lh, ls, lp] = dfs(node->left);
            auto [rh, rs, rp] = dfs(node->right);
            int sz = ls + rs + 1;
            bool perf = lp && rp && lh == rh;
            if (perf) sizes.push_back(sz);
            return {std::max(lh, rh) + 1, sz, perf};
        };
        dfs(root);
        std::sort(sizes.begin(), sizes.end(), std::greater<int>());
        if (k > (int)sizes.size()) return -1;
        return sizes[k - 1];
    }
};


// ========== 3320_count_the_number_of_winning_sequences ==========
// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

#include <array>
#include <string>
#include <vector>

class Solution {
public:
    int countWinningSequences(std::string s) {
        const int mod = 1000000007;
        int n = (int)s.size();
        int mp[256]{};
        mp['F'] = 0; mp['W'] = 1; mp['E'] = 2;
        int beat[3] = {2, 0, 1};
        int score[3][3]{};
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                if (a == b) score[a][b] = 0;
                else if (beat[a] == b) score[a][b] = 1;
                else score[a][b] = -1;
            }
        }
        int offset = n;
        std::vector<std::vector<int>> dp(3, std::vector<int>(2 * n + 1, 0));
        int b0 = mp[(unsigned char)s[0]];
        for (int a = 0; a < 3; a++) dp[a][score[a][b0] + offset] = 1;
        for (int i = 1; i < n; i++) {
            std::vector<std::vector<int>> ndp(3, std::vector<int>(2 * n + 1, 0));
            int b = mp[(unsigned char)s[i]];
            for (int last = 0; last < 3; last++) {
                for (int d = 0; d <= 2 * n; d++) {
                    if (dp[last][d] == 0) continue;
                    for (int a = 0; a < 3; a++) {
                        if (a == last) continue;
                        int nd = d + score[a][b];
                        if (nd < 0 || nd > 2 * n) continue;
                        ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod;
                    }
                }
            }
            dp = ndp;
        }
        int ans = 0;
        for (int a = 0; a < 3; a++) {
            for (int d = offset + 1; d <= 2 * n; d++) ans = (ans + dp[a][d]) % mod;
        }
        return ans;
    }
};


// ========== 3321_find_x_sum_of_all_k_long_subarrays_ii ==========
// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<long long> findXSum(std::vector<int>& nums, int k, int x) {
        int n = (int)nums.size();
        std::vector<long long> ans(n - k + 1);
        for (int i = 0; i <= n - k; i++) {
            std::unordered_map<int, int> freq;
            for (int j = i; j < i + k; j++) freq[nums[j]]++;
            struct P { int v, f; };
            std::vector<P> arr;
            for (auto& p : freq) arr.push_back({p.first, p.second});
            for (int a = 0; a < (int)arr.size(); a++) {
                for (int b = a + 1; b < (int)arr.size(); b++) {
                    if (arr[b].f > arr[a].f || (arr[b].f == arr[a].f && arr[b].v > arr[a].v))
                        std::swap(arr[a], arr[b]);
                }
            }
            int lim = std::min(x, (int)arr.size());
            std::unordered_map<int, char> keep;
            for (int t = 0; t < lim; t++) keep[arr[t].v] = 1;
            long long sum = 0;
            for (int j = i; j < i + k; j++) if (keep.count(nums[j])) sum += nums[j];
            ans[i] = sum;
        }
        return ans;
    }
};


// ========== 3323_minimize_connected_groups_by_inserting_interval ==========
// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minConnectedGroups(std::vector<std::vector<int>>& intervals, int k) {
        std::sort(intervals.begin(), intervals.end());
        std::vector<std::vector<int>> merged;
        for (auto& it : intervals) {
            if (merged.empty() || it[0] > merged.back()[1]) merged.push_back({it[0], it[1]});
            else if (it[1] > merged.back()[1]) merged.back()[1] = it[1];
        }
        int m = (int)merged.size();
        int ans = m;
        for (int i = 0; i < m; i++) {
            int end = merged[i][1] + k;
            int j = i;
            while (j < m && merged[j][0] <= end) j++;
            int groups = i + 1 + (m - j);
            if (groups < ans) ans = groups;
        }
        return ans;
    }
};


// ========== 3324_find_the_sequence_of_strings_appeared_on_the_screen ==========
// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> stringSequence(std::string target) {
        std::vector<std::string> ans;
        std::string cur;
        for (char ch : target) {
            cur.push_back('a');
            ans.push_back(cur);
            while (cur.back() != ch) {
                cur.back()++;
                ans.push_back(cur);
            }
        }
        return ans;
    }
};


// ========== 3325_count_substrings_with_k_frequency_characters_i ==========
// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

#include <array>
#include <string>

class Solution {
public:
    int numberOfSubstrings(std::string s, int k) {
        int n = (int)s.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::array<int, 26> freq{};
            for (int j = i; j < n; j++) {
                freq[s[j] - 'a']++;
                bool ok = false;
                for (int f : freq) if (f >= k) { ok = true; break; }
                if (ok) { ans += n - j; break; }
            }
        }
        return ans;
    }
};


// ========== 3326_minimum_division_operations_to_make_array_non_decreasing ==========
// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

#include <vector>

class Solution {
    int smallestProperDivisor(int x) {
        for (int d = 2; d * d <= x; d++) if (x % d == 0) return d;
        return x;
    }

public:
    int minOperations(std::vector<int>& nums) {
        int ops = 0;
        for (int i = (int)nums.size() - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) continue;
            while (nums[i] > nums[i + 1]) {
                int d = smallestProperDivisor(nums[i]);
                if (d == nums[i]) return -1;
                nums[i] /= d;
                ops++;
                if (nums[i] > nums[i + 1] && smallestProperDivisor(nums[i]) == nums[i]) return -1;
            }
        }
        return ops;
    }
};


// ========== 3327_check_if_dfs_strings_are_palindromes ==========
// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

#include <functional>
#include <string>
#include <vector>

class Solution {
    bool isPal(const std::string& s) {
        for (int i = 0, j = (int)s.size() - 1; i < j; i++, j--) {
            if (s[i] != s[j]) return false;
        }
        return true;
    }

public:
    std::vector<bool> findAnswer(std::vector<int>& parent, std::string s) {
        int n = (int)parent.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[parent[i]].push_back(i);
        std::vector<bool> ans(n);
        std::function<std::string(int)> dfsStr = [&](int u) -> std::string {
            std::string out;
            for (int v : g[u]) out += dfsStr(v);
            out.push_back(s[u]);
            ans[u] = isPal(out);
            return out;
        };
        dfsStr(0);
        return ans;
    }
};


// ========== 3329_count_substrings_with_k_frequency_characters_ii ==========
// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

#include <array>
#include <string>

class Solution {
public:
    long long numberOfSubstrings(std::string s, int k) {
        int n = (int)s.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            std::array<int, 26> freq{};
            for (int j = i; j < n; j++) {
                freq[s[j] - 'a']++;
                bool ok = false;
                for (int f : freq) if (f >= k) { ok = true; break; }
                if (ok) { ans += n - j; break; }
            }
        }
        return ans;
    }
};


// ========== 3330_find_the_original_typed_string_i ==========
// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

#include <string>

class Solution {
public:
    int possibleStringCount(std::string word) {
        int ans = 1;
        for (int i = 1; i < (int)word.size(); i++) {
            if (word[i] == word[i - 1]) ans++;
        }
        return ans;
    }
};


// ========== 3331_find_subtree_sizes_after_changes ==========
// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> findSubtreeSizes(std::vector<int>& parent, std::string s) {
        int n = (int)parent.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[parent[i]].push_back(i);
        std::vector<int> newParent = parent;
        std::vector<int> last(26, -1);
        std::function<void(int)> dfs1 = [&](int u) {
            int c = s[u] - 'a';
            int prev = last[c];
            if (prev != -1) newParent[u] = prev;
            last[c] = u;
            for (int v : g[u]) dfs1(v);
            last[c] = prev;
        };
        dfs1(0);
        std::vector<std::vector<int>> ng(n);
        for (int i = 1; i < n; i++) ng[newParent[i]].push_back(i);
        std::vector<int> ans(n);
        std::function<int(int)> dfs2 = [&](int u) {
            int sz = 1;
            for (int v : ng[u]) sz += dfs2(v);
            return ans[u] = sz;
        };
        dfs2(0);
        return ans;
    }
};


// ========== 3332_maximum_points_tourist_can_earn ==========
// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxScore(int n, int k, std::vector<std::vector<int>>& stayScore, std::vector<std::vector<int>>& travelScore) {
        std::vector<int> dp(n, 0);
        for (int day = 0; day < k; day++) {
            std::vector<int> ndp(n, -(1 << 30));
            for (int dest = 0; dest < n; dest++) {
                int best = -(1 << 30);
                for (int src = 0; src < n; src++) {
                    int val = dp[src];
                    if (src == dest) val += stayScore[day][dest];
                    else val += travelScore[src][dest];
                    if (val > best) best = val;
                }
                ndp[dest] = best;
            }
            dp = ndp;
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};


// ========== 3333_find_the_original_typed_string_ii ==========
// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

#include <string>
#include <vector>

class Solution {
public:
    int possibleStringCount(std::string word, int k) {
        const int mod = 1000000007;
        std::vector<int> groups;
        for (int i = 0; i < (int)word.size(); ) {
            int j = i;
            while (j < (int)word.size() && word[j] == word[i]) j++;
            groups.push_back(j - i);
            i = j;
        }
        int total = 1;
        for (int g : groups) total = (int)((long long)total * g % mod);
        if (k <= (int)groups.size()) return total;
        int need = k - 1;
        std::vector<int> dp(need, 0);
        dp[0] = 1;
        for (int g : groups) {
            std::vector<int> ndp(need, 0);
            std::vector<int> pref(need + 1, 0);
            for (int i = 0; i < need; i++) pref[i + 1] = (pref[i] + dp[i]) % mod;
            for (int s = 0; s < need; s++) {
                int lo = s - g;
                if (lo < 0) lo = 0;
                int hi = s - 1;
                if (hi >= 0) ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod;
            }
            dp = ndp;
        }
        int bad = 0;
        for (int v : dp) bad = (bad + v) % mod;
        return (total - bad + mod) % mod;
    }
};


// ========== 3334_find_the_maximum_factor_score_of_array ==========
// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

#include <cstdint>
#include <vector>

class Solution {
    int gcd(int a, int b) {
        while (b) { int t = a % b; a = b; b = t; }
        return a;
    }
    int lcm(int a, int b) { return a / gcd(a, b) * b; }

public:
    long long maxScore(std::vector<int>& nums) {
        int n = (int)nums.size();
        int gcdAll = nums[0], lcmAll = nums[0];
        for (int i = 1; i < n; i++) {
            gcdAll = gcd(gcdAll, nums[i]);
            lcmAll = lcm(lcmAll, nums[i]);
        }
        long long ans = (long long)gcdAll * lcmAll;
        for (int skip = 0; skip < n; skip++) {
            int g = 0, l = 1;
            bool first = true;
            for (int i = 0; i < n; i++) {
                if (i == skip) continue;
                if (first) { g = l = nums[i]; first = false; }
                else { g = gcd(g, nums[i]); l = lcm(l, nums[i]); }
            }
            if (first) continue;
            long long v = (long long)g * l;
            if (v > ans) ans = v;
        }
        return ans;
    }
};


// ========== 3335_total_characters_in_string_after_transformations_i ==========
// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

#include <array>
#include <string>

class Solution {
public:
    int lengthAfterTransformations(std::string s, int t) {
        const int mod = 1000000007;
        std::array<int, 26> cnt{};
        for (char c : s) cnt[c - 'a']++;
        for (int step = 0; step < t; step++) {
            std::array<int, 26> ncnt{};
            for (int i = 0; i < 25; i++) ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod;
            ncnt[0] = (ncnt[0] + cnt[25]) % mod;
            ncnt[1] = (ncnt[1] + cnt[25]) % mod;
            cnt = ncnt;
        }
        int ans = 0;
        for (int v : cnt) ans = (ans + v) % mod;
        return ans;
    }
};


// ========== 3336_find_the_number_of_subsequences_with_equal_gcd ==========
// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

#include <algorithm>
#include <vector>

class Solution {
    int gcd(int a, int b) {
        if (a == 0) return b;
        while (b) { int t = a % b; a = b; b = t; }
        return a;
    }

public:
    int subsequencePairCount(std::vector<int>& nums) {
        const int mod = 1000000007;
        int maxV = *std::max_element(nums.begin(), nums.end());
        std::vector<std::vector<int>> dp(maxV + 1, std::vector<int>(maxV + 1, 0));
        dp[0][0] = 1;
        for (int x : nums) {
            std::vector<std::vector<int>> ndp = dp;
            for (int a = 0; a <= maxV; a++) {
                for (int b = 0; b <= maxV; b++) {
                    if (dp[a][b] == 0) continue;
                    int na = a == 0 ? x : gcd(a, x);
                    int nb = b == 0 ? x : gcd(b, x);
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod;
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod;
                }
            }
            dp = ndp;
        }
        int ans = 0;
        for (int g = 1; g <= maxV; g++) ans = (ans + dp[g][g]) % mod;
        return ans;
    }
};


// ========== 3337_total_characters_in_string_after_transformations_ii ==========
// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

#include <string>
#include <vector>

class Solution {
    using Mat = std::vector<std::vector<int>>;

    Mat matMul(const Mat& a, const Mat& b, int mod) {
        int n = (int)a.size();
        Mat c(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (a[i][k] == 0) continue;
                for (int j = 0; j < n; j++) {
                    c[i][j] = (c[i][j] + (int)((long long)a[i][k] * b[k][j] % mod)) % mod;
                }
            }
        }
        return c;
    }

    Mat matPow(Mat a, int e, int mod) {
        int n = (int)a.size();
        Mat r(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; i++) r[i][i] = 1;
        while (e > 0) {
            if (e & 1) r = matMul(r, a, mod);
            a = matMul(a, a, mod);
            e >>= 1;
        }
        return r;
    }

public:
    int lengthAfterTransformations(std::string s, int t, std::vector<int>& nums) {
        const int mod = 1000000007;
        Mat mat(26, std::vector<int>(26, 0));
        for (int i = 0; i < 26; i++) {
            for (int j = 1; j <= nums[i]; j++) mat[i][(i + j) % 26] = 1;
        }
        mat = matPow(mat, t, mod);
        std::vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                ans = (ans + (int)((long long)cnt[i] * mat[i][j] % mod)) % mod;
            }
        }
        return ans;
    }
};


// ========== 3339_find_the_number_of_k_even_arrays ==========
// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

#include <array>
#include <vector>

class Solution {
public:
    int countOfArrays(int n, int m, int k) {
        const int mod = 1000000007;
        int even = m / 2, odd = m - even;
        std::vector<std::vector<std::array<int, 2>>> dp(n + 1, std::vector<std::array<int, 2>>(k + 1));
        for (auto& row : dp) for (auto& a : row) a = {0, 0};
        dp[1][0][0] = odd;
        dp[1][0][1] = even;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i + 1][j][0] = (dp[i + 1][j][0] + (int)(((long long)dp[i][j][0] + dp[i][j][1]) % mod * odd % mod)) % mod;
                dp[i + 1][j][1] = (dp[i + 1][j][1] + (int)((long long)dp[i][j][0] * even % mod)) % mod;
                if (j < k) {
                    dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + (int)((long long)dp[i][j][1] * even % mod)) % mod;
                }
            }
        }
        return (dp[n][k][0] + dp[n][k][1]) % mod;
    }
};


// ========== 3340_check_balanced_string ==========
// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

#include <string>

class Solution {
public:
    bool isBalanced(std::string num) {
        int even = 0, odd = 0;
        for (int i = 0; i < (int)num.size(); i++) {
            if (i % 2 == 0) even += num[i] - '0';
            else odd += num[i] - '0';
        }
        return even == odd;
    }
};


// ========== 3341_find_minimum_time_to_reach_last_room_i ==========
// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

#include <array>
#include <queue>
#include <vector>

class Solution {
public:
    int minTimeToReach(std::vector<std::vector<int>>& moveTime) {
        int m = (int)moveTime.size(), n = (int)moveTime[0].size();
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, 1 << 30));
        using Node = std::array<int, 3>; // t, r, c
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> h;
        h.push({0, 0, 0});
        dist[0][0] = 0;
        const int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!h.empty()) {
            auto cur = h.top(); h.pop();
            int t = cur[0], r = cur[1], c = cur[2];
            if (t != dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return t;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int start = t;
                if (moveTime[nr][nc] > start) start = moveTime[nr][nc];
                int nt = start + 1;
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt;
                    h.push({nt, nr, nc});
                }
            }
        }
        return -1;
    }
};


// ========== 3342_find_minimum_time_to_reach_last_room_ii ==========
// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

#include <queue>
#include <vector>

class Solution {
public:
    int minTimeToReach(std::vector<std::vector<int>>& moveTime) {
        int m = (int)moveTime.size(), n = (int)moveTime[0].size();
        const int INF = 1 << 30;
        std::vector<std::vector<std::vector<int>>> dist(m, std::vector<std::vector<int>>(n, std::vector<int>(2, INF)));
        using Node = std::tuple<int, int, int, int>; // t, r, c, parity
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> pq;
        dist[0][0][0] = 0;
        pq.emplace(0, 0, 0, 0);
        int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!pq.empty()) {
            auto [t, r, c, parity] = pq.top();
            pq.pop();
            if (t != dist[r][c][parity]) continue;
            if (r == m - 1 && c == n - 1) return t;
            int cost = parity == 1 ? 2 : 1;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int start = t;
                if (moveTime[nr][nc] > start) start = moveTime[nr][nc];
                int nt = start + cost;
                int np = 1 - parity;
                if (nt < dist[nr][nc][np]) {
                    dist[nr][nc][np] = nt;
                    pq.emplace(nt, nr, nc, np);
                }
            }
        }
        return -1;
    }
};


// ========== 3343_count_number_of_balanced_permutations ==========
// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

#include <map>
#include <string>
#include <utility>
#include <vector>

class Solution {
    static int modPow(long long a, long long e, int mod) {
        long long r = 1;
        a %= mod;
        while (e > 0) {
            if (e & 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return (int)r;
    }

public:
    int countBalancedPermutations(std::string num) {
        const int mod = 1000000007;
        int cnt[10] = {};
        int sum = 0;
        for (char c : num) {
            cnt[c - '0']++;
            sum += c - '0';
        }
        if (sum % 2 == 1) return 0;
        int n = (int)num.size();
        int halfN = n / 2, halfS = sum / 2;
        std::vector<int> fact(n + 1), invF(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = (int)((long long)fact[i - 1] * i % mod);
        invF[n] = modPow(fact[n], mod - 2, mod);
        for (int i = n; i > 0; i--) invF[i - 1] = (int)((long long)invF[i] * i % mod);

        std::map<std::pair<int, int>, int> dp;
        dp[{0, 0}] = 1;
        for (int d = 0; d <= 9; d++) {
            std::map<std::pair<int, int>, int> ndp;
            for (auto& [st, ways] : dp) {
                int used = st.first, s = st.second;
                for (int take = 0; take <= cnt[d]; take++) {
                    int nu = used + take, ns = s + take * d;
                    if (nu > halfN || ns > halfS) continue;
                    int w = (int)((long long)ways * invF[take] % mod * invF[cnt[d] - take] % mod);
                    ndp[{nu, ns}] = (ndp[{nu, ns}] + w) % mod;
                }
            }
            dp.swap(ndp);
        }
        int ans = dp[{halfN, halfS}];
        ans = (int)((long long)ans * fact[halfN] % mod * fact[n - halfN] % mod);
        for (int d = 0; d <= 9; d++) ans = (int)((long long)ans * fact[cnt[d]] % mod);
        return ans;
    }
};


// ========== 3344_maximum_sized_array ==========
// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

#include <cstdint>

class Solution {
public:
    int maxSizedArray(long long s) {
        auto ok = [&](long long n) -> bool {
            long long sum = 0;
            for (long long i = 0; i < n; i++) {
                for (long long j = 0; j < n; j++) {
                    long long ij = i | j;
                    sum += ij * (n - 1) * n / 2;
                    if (sum > s) return false;
                }
            }
            return sum <= s;
        };
        long long lo = 1, hi = 2000;
        while (lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return (int)lo;
    }
};


// ========== 3345_smallest_divisible_digit_product_i ==========
// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution {
public:
    int smallestNumber(int n, int t) {
        for (int x = n;; x++) {
            int p = 1, y = x;
            while (y > 0) {
                p *= y % 10;
                y /= 10;
            }
            if (p % t == 0) return x;
        }
    }
};


// ========== 3346_maximum_frequency_of_an_element_after_performing_operations_i ==========
// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k, int numOperations) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        int ans = 1;
        for (auto& [t, f] : freq) {
            int lo = (int)(std::lower_bound(nums.begin(), nums.end(), t - k) - nums.begin());
            int hi = (int)(std::upper_bound(nums.begin(), nums.end(), t + k) - nums.begin());
            int can = hi - lo;
            int use = can;
            if (use > f + numOperations) use = f + numOperations;
            if (use > ans) ans = use;
        }
        int l = 0;
        for (int r = 0; r < n; r++) {
            while (nums[r] - nums[l] > 2 * k) l++;
            int window = r - l + 1;
            if (window > numOperations) window = numOperations;
            if (window > ans) ans = window;
        }
        return ans;
    }
};


// ========== 3347_maximum_frequency_of_an_element_after_performing_operations_ii ==========
// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k, int numOperations) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        int ans = 1;
        std::vector<int> candidates;
        std::unordered_set<int> seen;
        for (int x : nums) {
            for (int t : {x - k, x, x + k}) {
                if (!seen.count(t)) {
                    seen.insert(t);
                    candidates.push_back(t);
                }
            }
        }
        for (int t : candidates) {
            int lo = (int)(std::lower_bound(nums.begin(), nums.end(), t - k) - nums.begin());
            int hi = (int)(std::upper_bound(nums.begin(), nums.end(), t + k) - nums.begin());
            int can = hi - lo;
            int f = freq.count(t) ? freq[t] : 0;
            int use = can;
            if (use > f + numOperations) use = f + numOperations;
            if (use > ans) ans = use;
        }
        return ans;
    }
};


// ========== 3348_smallest_divisible_digit_product_ii ==========
// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

#include <cstdint>
#include <string>
#include <vector>

class Solution {
    bool dfs(std::vector<char>& res, int i, bool tight, bool sameLen, const std::string& num, long long t) {
        if (i == (int)res.size()) {
            long long prod = 1;
            for (char c : res) {
                prod *= (c - '0');
                if (prod == 0) break;
            }
            return prod % t == 0 && prod > 0;
        }
        char start = (i == 0) ? '1' : '0';
        if (tight && sameLen && i < (int)num.size()) start = num[i];
        for (char c = start; c <= '9'; c++) {
            res[i] = c;
            bool nt = tight && sameLen && i < (int)num.size() && c == num[i];
            if (dfs(res, i + 1, nt, sameLen, num, t)) return true;
        }
        return false;
    }

public:
    std::string smallestNumber(std::string num, long long t) {
        long long tt = t;
        for (int d = 9; d >= 2; d--) {
            while (tt % d == 0) tt /= d;
        }
        if (tt > 1) return "-1";
        for (int extra = 0; extra <= 60; extra++) {
            int L = (int)num.size() + extra;
            std::vector<char> res(L);
            if (dfs(res, 0, true, extra == 0, num, t)) return std::string(res.begin(), res.end());
        }
        return "-1";
    }
};


// ========== 3349_adjacent_increasing_subarrays_detection_i ==========
// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

#include <vector>

class Solution {
public:
    bool hasIncreasingSubarrays(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        auto inc = [&](int start) {
            for (int i = start; i + 1 < start + k; i++) {
                if (nums[i] >= nums[i + 1]) return false;
            }
            return true;
        };
        for (int i = 0; i + 2 * k <= n; i++) {
            if (inc(i) && inc(i + k)) return true;
        }
        return false;
    }
};


// ========== 3350_adjacent_increasing_subarrays_detection_ii ==========
// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

#include <vector>

class Solution {
public:
    int maxIncreasingSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> up(n);
        up[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            up[i] = (nums[i] < nums[i + 1]) ? up[i + 1] + 1 : 1;
        }
        int lo = 1, hi = n / 2;
        auto ok = [&](int k) {
            for (int i = 0; i + 2 * k <= n; i++) {
                if (up[i] >= k && up[i + k] >= k) return true;
            }
            return false;
        };
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};


// ========== 3351_sum_of_good_subsequences ==========
// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int sumOfGoodSubsequences(std::vector<int>& nums) {
        const int mod = 1000000007;
        std::unordered_map<int, int> cnt, sum;
        int ans = 0;
        for (int x : nums) {
            int c = 1;
            int s = x;
            if (cnt.count(x - 1) && cnt[x - 1] > 0) {
                c = (c + cnt[x - 1]) % mod;
                s = (int)(((long long)s + sum[x - 1] + (long long)cnt[x - 1] * x % mod) % mod);
            }
            if (cnt.count(x + 1) && cnt[x + 1] > 0) {
                c = (c + cnt[x + 1]) % mod;
                s = (int)(((long long)s + sum[x + 1] + (long long)cnt[x + 1] * x % mod) % mod);
            }
            cnt[x] = (cnt[x] + c) % mod;
            sum[x] = (sum[x] + s) % mod;
            ans = (ans + s) % mod;
        }
        return ans;
    }
};


// ========== 3352_count_k_reducible_numbers_less_than_n ==========
// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

#include <map>
#include <string>
#include <tuple>
#include <vector>

class Solution {
    static int bitsPop(int x) {
        int c = 0;
        while (x > 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }

public:
    int countKReducibleNumbers(std::string s, int k) {
        const int mod = 1000000007;
        std::vector<int> red(801);
        red[1] = 0;
        for (int i = 2; i <= 800; i++) red[i] = 1 + red[bitsPop(i)];
        int n = (int)s.size();
        std::map<std::tuple<int, int, int>, int> memo;
        auto dfs = [&](auto&& self, int pos, bool tight, int ones) -> int {
            if (pos == n) {
                if (ones == 0) return 0;
                return red[ones] <= k - 1 ? 1 : 0;
            }
            auto key = std::make_tuple(pos, tight ? 1 : 0, ones);
            if (memo.count(key)) return memo[key];
            int up = tight ? (s[pos] - '0') : 1;
            int ans = 0;
            for (int d = 0; d <= up; d++) {
                bool nt = tight && d == up;
                ans = (ans + self(self, pos + 1, nt, ones + d)) % mod;
            }
            return memo[key] = ans;
        };
        return dfs(dfs, 0, true, 0);
    }
};


// ========== 3353_minimum_total_operations ==========
// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

#include <vector>

class Solution {
public:
    int minimumOperations(std::vector<int>& nums) {
        int ops = 0;
        for (int i = (int)nums.size() - 2; i >= 0; i--) {
            if (nums[i] != nums[i + 1]) ops++;
        }
        return ops;
    }
};


// ========== 3354_make_array_elements_equal_to_zero ==========
// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

#include <vector>

class Solution {
public:
    int countValidSelections(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) continue;
            for (int dir : {-1, 1}) {
                std::vector<int> a = nums;
                int cur = i, d = dir;
                while (cur >= 0 && cur < n) {
                    if (a[cur] == 0) cur += d;
                    else {
                        a[cur]--;
                        d = -d;
                        cur += d;
                    }
                }
                bool ok = true;
                for (int v : a) if (v != 0) { ok = false; break; }
                if (ok) ans++;
            }
        }
        return ans;
    }
};


// ========== 3355_zero_array_transformation_i ==========
// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

#include <vector>

class Solution {
public:
    bool isZeroArray(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> diff(n + 1);
        for (auto& q : queries) {
            diff[q[0]]++;
            diff[q[1] + 1]--;
        }
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            if (cur < nums[i]) return false;
        }
        return true;
    }
};


// ========== 3356_zero_array_transformation_ii ==========
// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

#include <vector>

class Solution {
public:
    int minZeroArray(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        auto ok = [&](int k) {
            std::vector<long long> diff(n + 1);
            for (int i = 0; i < k; i++) {
                auto& q = queries[i];
                diff[q[0]] += q[2];
                diff[q[1] + 1] -= q[2];
            }
            long long cur = 0;
            for (int i = 0; i < n; i++) {
                cur += diff[i];
                if (cur < nums[i]) return false;
            }
            return true;
        };
        if (ok(0)) return 0;
        int lo = 1, hi = (int)queries.size() + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid <= (int)queries.size() && ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        if (lo > (int)queries.size()) return -1;
        return lo;
    }
};


// ========== 3357_minimize_the_maximum_adjacent_element_difference ==========
// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int minDifference(std::vector<int>& nums) {
        int n = (int)nums.size();
        auto ok = [&](int d) {
            int prev = -1;
            for (int i = 0; i < n; i++) {
                if (nums[i] != -1) {
                    if (prev != -1 && std::abs(nums[i] - prev) > d) return false;
                    prev = nums[i];
                    continue;
                }
                int j = i;
                while (j < n && nums[j] == -1) j++;
                int left = prev;
                int right = (j < n) ? nums[j] : -1;
                int gap = j - i;
                if (left == -1 && right == -1) return true;
                if (left == -1 || right == -1) {
                    prev = -1;
                    i = j - 1;
                    continue;
                }
                if (std::abs(left - right) > d * (gap + 1)) return false;
                prev = -1;
                i = j - 1;
            }
            return true;
        };
        int lo = 0, hi = 1000000000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};


// ========== 3359_find_sorted_submatrices_with_maximum_element_at_most_k ==========
// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long countSortedMatrices(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        long long ans = 0;
        for (int r1 = 0; r1 < m; r1++) {
            for (int r2 = r1; r2 < m; r2++) {
                for (int c1 = 0; c1 < n; c1++) {
                    for (int c2 = c1; c2 < n; c2++) {
                        bool ok = true;
                        for (int i = r1; i <= r2 && ok; i++) {
                            for (int j = c1; j <= c2; j++) {
                                if (grid[i][j] > k) { ok = false; break; }
                                if (j > c1 && grid[i][j] < grid[i][j - 1]) { ok = false; break; }
                                if (i > r1 && grid[i][j] < grid[i - 1][j]) { ok = false; break; }
                            }
                        }
                        if (ok) ans++;
                    }
                }
            }
        }
        return ans;
    }
};


// ========== 3360_stone_removal_game ==========
// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

class Solution {
public:
    bool canAliceWin(int n) {
        int take = 10;
        bool alice = true;
        while (n >= take && take > 0) {
            n -= take;
            take--;
            alice = !alice;
        }
        return !alice;
    }
};


// ========== 3361_shift_distance_between_two_strings ==========
// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

#include <cstdint>
#include <string>
#include <vector>

class Solution {
public:
    long long shiftDistance(std::string s, std::string t, std::vector<int>& nextCost, std::vector<int>& previousCost) {
        long long ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            int a = s[i] - 'a', b = t[i] - 'a';
            if (a == b) continue;
            long long fwd = 0;
            for (int x = a; x != b; x = (x + 1) % 26) fwd += nextCost[x];
            long long bwd = 0;
            for (int x = a; x != b; x = (x + 25) % 26) bwd += previousCost[x];
            ans += fwd < bwd ? fwd : bwd;
        }
        return ans;
    }
};


// ========== 3362_zero_array_transformation_iii ==========
// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    int maxRemoval(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        std::sort(queries.begin(), queries.end(), [](auto& a, auto& b) { return a[0] < b[0]; });
        std::priority_queue<int> h;
        int n = (int)nums.size();
        std::vector<int> diff(n + 1);
        int j = 0, used = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            while (j < (int)queries.size() && queries[j][0] == i) {
                h.push(queries[j][1]);
                j++;
            }
            while (cur < nums[i]) {
                if (h.empty() || h.top() < i) return -1;
                int r = h.top();
                h.pop();
                cur++;
                diff[r + 1]--;
                used++;
            }
        }
        return (int)queries.size() - used;
    }
};


// ========== 3363_find_the_maximum_number_of_fruits_collected ==========
// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

#include <vector>

class Solution {
public:
    int maxCollectedFruits(std::vector<std::vector<int>>& fruits) {
        int n = (int)fruits.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += fruits[i][i];
            fruits[i][i] = 0;
        }
        const int neg = -(1 << 30);
        std::vector<std::vector<int>> dp2(n, std::vector<int>(n, neg));
        std::vector<std::vector<int>> dp3(n, std::vector<int>(n, neg));
        dp2[0][n - 1] = fruits[0][n - 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp2[i][j] == neg) continue;
                for (int dj : {-1, 0, 1}) {
                    int ni = i + 1, nj = j + dj;
                    if (ni < n && nj >= 0 && nj < n && nj > ni) {
                        int v = dp2[i][j] + fruits[ni][nj];
                        if (v > dp2[ni][nj]) dp2[ni][nj] = v;
                    }
                }
            }
        }
        dp3[n - 1][0] = fruits[n - 1][0];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                if (dp3[i][j] == neg) continue;
                for (int di : {-1, 0, 1}) {
                    int ni = i + di, nj = j + 1;
                    if (ni >= 0 && ni < n && nj < n && ni > nj) {
                        int v = dp3[i][j] + fruits[ni][nj];
                        if (v > dp3[ni][nj]) dp3[ni][nj] = v;
                    }
                }
            }
        }
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1];
        return ans;
    }
};


// ========== 3364_minimum_positive_sum_subarray ==========
// LeetCode 3364 - Minimum Positive Sum Subarray 
// https://leetcode.com/problems/minimum-positive-sum-subarray/

#include <climits>
#include <vector>

class Solution {
public:
    int minimumSumSubarray(std::vector<int>& nums, int l, int r) {
        int n = (int)nums.size();
        std::vector<int> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        int ans = INT_MAX;
        bool found = false;
        for (int i = 0; i < n; i++) {
            for (int length = l; length <= r && i + length <= n; length++) {
                int s = pref[i + length] - pref[i];
                if (s > 0 && s < ans) {
                    ans = s;
                    found = true;
                }
            }
        }
        return found ? ans : -1;
    }
};


// ========== 3365_rearrange_k_substrings_to_form_target_string ==========
// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

#include <string>
#include <unordered_map>

class Solution {
public:
    bool isPossibleToRearrange(std::string s, std::string t, int k) {
        int n = (int)s.size();
        int sz = n / k;
        std::unordered_map<std::string, int> cnt;
        for (int i = 0; i < n; i += sz) {
            cnt[s.substr(i, sz)]++;
            cnt[t.substr(i, sz)]--;
        }
        for (auto& [_, v] : cnt) if (v != 0) return false;
        return true;
    }
};


// ========== 3366_minimum_array_sum ==========
// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

#include <climits>
#include <vector>

class Solution {
public:
    int minArraySum(std::vector<int>& nums, int k, int op1, int op2) {
        const long long inf = (long long)1e18;
        std::vector<std::vector<long long>> dp(op1 + 1, std::vector<long long>(op2 + 1, inf));
        dp[0][0] = 0;
        for (int x : nums) {
            std::vector<std::vector<long long>> ndp(op1 + 1, std::vector<long long>(op2 + 1, inf));
            for (int a = 0; a <= op1; a++) {
                for (int b = 0; b <= op2; b++) {
                    if (dp[a][b] == inf) continue;
                    struct Cand { int na, nb, v; };
                    std::vector<Cand> cand{{a, b, x}};
                    if (a < op1) cand.push_back({a + 1, b, (x + 1) / 2});
                    if (b < op2 && x >= k) cand.push_back({a, b + 1, x - k});
                    if (a < op1 && b < op2) {
                        int v1 = (x + 1) / 2;
                        if (v1 >= k) cand.push_back({a + 1, b + 1, v1 - k});
                        if (x >= k) cand.push_back({a + 1, b + 1, (x - k + 1) / 2});
                    }
                    for (auto& c : cand) {
                        if (dp[a][b] + c.v < ndp[c.na][c.nb]) ndp[c.na][c.nb] = dp[a][b] + c.v;
                    }
                }
            }
            dp.swap(ndp);
        }
        long long ans = inf;
        for (int a = 0; a <= op1; a++)
            for (int b = 0; b <= op2; b++)
                if (dp[a][b] < ans) ans = dp[a][b];
        return (int)ans;
    }
};


// ========== 3367_maximize_sum_of_weights_after_edge_removals ==========
// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

#include <algorithm>
#include <cstdint>
#include <functional>
#include <utility>
#include <vector>

class Solution {
public:
    long long maximizeSumOfWeights(std::vector<std::vector<int>>& edges, int k) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        std::function<std::pair<long long, long long>(int, int)> dfs = [&](int u, int p) -> std::pair<long long, long long> {
            long long base = 0;
            std::vector<long long> gains;
            for (auto [to, w] : g[u]) {
                if (to == p) continue;
                auto [keep, drop] = dfs(to, u);
                base += drop;
                long long gain = keep + w - drop;
                if (gain > 0) gains.push_back(gain);
            }
            std::sort(gains.begin(), gains.end(), std::greater<long long>());
            long long with = base, without = base;
            for (int i = 0; i < (int)gains.size() && i < k - 1; i++) with += gains[i];
            for (int i = 0; i < (int)gains.size() && i < k; i++) without += gains[i];
            return {with, without};
        };
        return dfs(0, -1).second;
    }
};


// ========== 3369_design_an_array_statistics_tracker ==========
// LeetCode 3369 - Design an Array Statistics Tracker 
// https://leetcode.com/problems/design-an-array-statistics-tracker/

#include <algorithm>
#include <climits>
#include <cstdint>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class StatisticsTracker {
    std::vector<int> arr;
    long long sum = 0;
    std::unordered_map<int, int> freq;
    int modeFreq = 0;
    std::unordered_set<int> modes;

public:
    StatisticsTracker() {}

    void addNumber(int num) {
        arr.push_back(num);
        sum += num;
        int f = ++freq[num];
        if (f > modeFreq) {
            modeFreq = f;
            modes = {num};
        } else if (f == modeFreq) {
            modes.insert(num);
        }
    }

    void removeFirst() {
        if (arr.empty()) return;
        int num = arr[0];
        arr.erase(arr.begin());
        sum -= num;
        if (--freq[num] == 0) freq.erase(num);
        modeFreq = 0;
        modes.clear();
        for (auto& [v, f] : freq) {
            if (f > modeFreq) {
                modeFreq = f;
                modes = {v};
            } else if (f == modeFreq) {
                modes.insert(v);
            }
        }
    }

    int getMean() {
        if (arr.empty()) return 0;
        return (int)(sum / (long long)arr.size());
    }

    int getMedian() {
        int n = (int)arr.size();
        std::vector<int> tmp = arr;
        std::sort(tmp.begin(), tmp.end());
        if (n % 2 == 1) return tmp[n / 2];
        return tmp[n / 2 - 1];
    }

    int getMode() {
        long long best = LLONG_MAX;
        for (int v : modes) if (v < best) best = v;
        if (best == LLONG_MAX) return 0;
        return (int)best;
    }
};


// ========== 3370_smallest_number_with_all_set_bits ==========
// LeetCode 3370 - Smallest Number With All Set Bits
// https://leetcode.com/problems/smallest-number-with-all-set-bits/

class Solution {
public:
    int smallestNumber(int n) {
        int x = 1;
        while (x < n) x = x * 2 + 1;
        return x;
    }
};


// ========== 3371_identify_the_largest_outlier_in_an_array ==========
// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int getLargestOutlier(std::vector<int>& nums) {
        int sum = 0;
        std::unordered_map<int, int> freq;
        for (int x : nums) {
            sum += x;
            freq[x]++;
        }
        int ans = INT_MIN;
        for (int x : nums) {
            freq[x]--;
            int rem = sum - x;
            if (rem % 2 == 0) {
                int cand = rem / 2;
                if (freq[cand] > 0 && x > ans) ans = x;
            }
            freq[x]++;
        }
        return ans;
    }
};


// ========== 3372_maximize_the_number_of_target_nodes_after_connecting_trees_i ==========
// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

#include <queue>
#include <utility>
#include <vector>

class Solution {
    std::vector<std::vector<int>> buildTree(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        return g;
    }

    int countWithin(std::vector<std::vector<int>>& g, int start, int k) {
        if (k < 0) return 0;
        int n = (int)g.size();
        std::vector<char> vis(n);
        std::queue<std::pair<int, int>> q;
        q.push({start, 0});
        vis[start] = 1;
        int cnt = 0;
        while (!q.empty()) {
            auto [u, d] = q.front();
            q.pop();
            cnt++;
            if (d == k) continue;
            for (int v : g[u]) {
                if (!vis[v]) {
                    vis[v] = 1;
                    q.push({v, d + 1});
                }
            }
        }
        return cnt;
    }

public:
    std::vector<int> maxTargetNodes(std::vector<std::vector<int>>& edges1, std::vector<std::vector<int>>& edges2, int k) {
        int n = (int)edges1.size() + 1;
        int m = (int)edges2.size() + 1;
        auto g1 = buildTree(n, edges1);
        auto g2 = buildTree(m, edges2);
        std::vector<int> cnt1(n);
        for (int i = 0; i < n; i++) cnt1[i] = countWithin(g1, i, k);
        int best2 = 0;
        if (k > 0) {
            for (int i = 0; i < m; i++) {
                int c = countWithin(g2, i, k - 1);
                if (c > best2) best2 = c;
            }
        }
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = cnt1[i] + best2;
        return ans;
    }
};


// ========== 3373_maximize_the_number_of_target_nodes_after_connecting_trees_ii ==========
// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

#include <array>
#include <queue>
#include <vector>

class Solution {
    std::vector<std::vector<int>> buildTree(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        return g;
    }

    std::array<int, 2> bipartiteCount(std::vector<std::vector<int>>& g, std::vector<int>& color) {
        int n = (int)g.size();
        std::fill(color.begin(), color.end(), -1);
        std::queue<int> q;
        q.push(0);
        color[0] = 0;
        std::array<int, 2> cnt{{1, 0}};
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : g[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    cnt[color[v]]++;
                    q.push(v);
                }
            }
        }
        (void)n;
        return cnt;
    }

public:
    std::vector<int> maxTargetNodes(std::vector<std::vector<int>>& edges1, std::vector<std::vector<int>>& edges2) {
        int n = (int)edges1.size() + 1;
        int m = (int)edges2.size() + 1;
        auto g1 = buildTree(n, edges1);
        auto g2 = buildTree(m, edges2);
        std::vector<int> color1(n), color2(m);
        auto c1 = bipartiteCount(g1, color1);
        auto c2 = bipartiteCount(g2, color2);
        int best2 = std::max(c2[0], c2[1]);
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = c1[color1[i]] + best2;
        return ans;
    }
};


// ========== 3375_minimum_operations_to_make_array_values_equal_to_k ==========
// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        std::unordered_set<int> seen;
        for (int x : nums) {
            if (x < k) return -1;
            if (x > k) seen.insert(x);
        }
        return (int)seen.size();
    }
};


// ========== 3376_minimum_time_to_break_locks_i ==========
// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

#include <vector>

class Solution {
    static int bitsOnes(int x) {
        int c = 0;
        while (x > 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }

public:
    int findMinimumTime(std::vector<int>& strength, int k) {
        int n = (int)strength.size();
        const int inf = 1000000000;
        int N = 1 << n;
        std::vector<int> dp(N, inf);
        dp[0] = 0;
        for (int mask = 0; mask < N; mask++) {
            if (dp[mask] == inf) continue;
            int opened = bitsOnes(mask);
            int x = 1 + opened * k;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                int t = (strength[i] + x - 1) / x;
                int nmask = mask | (1 << i);
                if (dp[mask] + t < dp[nmask]) dp[nmask] = dp[mask] + t;
            }
        }
        return dp[N - 1];
    }
};


// ========== 3377_digit_operations_to_make_two_integers_equal ==========
// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

#include <queue>
#include <string>
#include <utility>
#include <vector>

class Solution {
    std::vector<bool> sieve(int n) {
        std::vector<bool> isP(n, false);
        for (int i = 2; i < n; i++) isP[i] = true;
        for (int i = 2; i * i < n; i++) {
            if (isP[i]) {
                for (int j = i * i; j < n; j += i) isP[j] = false;
            }
        }
        return isP;
    }

public:
    int minOperations(int n, int m) {
        auto isPrime = sieve(100000);
        if (isPrime[n]) return -1;
        std::vector<int> dist(100000, -1);
        using Item = std::pair<int, int>;
        std::priority_queue<Item, std::vector<Item>, std::greater<Item>> pq;
        pq.push({n, n});
        dist[n] = n;
        while (!pq.empty()) {
            auto [cost, val] = pq.top();
            pq.pop();
            if (cost != dist[val]) continue;
            if (val == m) return cost;
            std::string s = std::to_string(val);
            for (int i = 0; i < (int)s.size(); i++) {
                char orig = s[i];
                for (int d : {-1, 1}) {
                    int nd = (orig - '0') + d;
                    if (nd < 0 || nd > 9) continue;
                    if (i == 0 && nd == 0 && (int)s.size() > 1) continue;
                    s[i] = char('0' + nd);
                    int nv = std::stoi(s);
                    s[i] = orig;
                    if (isPrime[nv]) continue;
                    int nc = cost + nv;
                    if (dist[nv] == -1 || nc < dist[nv]) {
                        dist[nv] = nc;
                        pq.push({nc, nv});
                    }
                }
            }
        }
        return -1;
    }
};


// ========== 3378_count_connected_components_in_lcm_graph ==========
// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

#include <numeric>
#include <unordered_map>
#include <unordered_set>
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
    int countComponents(std::vector<int>& nums, int threshold) {
        int n = (int)nums.size();
        std::vector<int> parent(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            if (parent[x] != x) parent[x] = self(self, parent[x]);
            return parent[x];
        };
        auto unite = [&](int a, int b) {
            int ra = find(find, a), rb = find(find, b);
            if (ra != rb) parent[ra] = rb;
        };
        std::unordered_map<int, int> idx;
        for (int i = 0; i < n; i++) idx[nums[i]] = i;
        for (int d = 1; d <= threshold; d++) {
            int first = -1;
            for (int m = d; m <= threshold; m += d) {
                auto it = idx.find(m);
                if (it != idx.end()) {
                    int i = it->second;
                    if (first == -1) first = i;
                    else if ((long long)nums[first] * nums[i] / gcd(nums[first], nums[i]) <= threshold)
                        unite(first, i);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = nums[i], b = nums[j];
                int g = gcd(a, b);
                if ((long long)a / g * b <= threshold) unite(i, j);
            }
        }
        std::unordered_set<int> comp;
        for (int i = 0; i < n; i++) comp.insert(find(find, i));
        return (int)comp.size();
    }
};


// ========== 3379_transformed_array ==========
// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

#include <vector>

class Solution {
public:
    std::vector<int> constructTransformedArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            int j = ((i + nums[i]) % n + n) % n;
            ans[i] = nums[j];
        }
        return ans;
    }
};


// ========== 3380_maximum_area_rectangle_with_point_constraints_i ==========
// LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    int maxRectangleArea(std::vector<std::vector<int>>& points) {
        std::set<std::pair<int, int>> set;
        for (auto& p : points) set.insert({p[0], p[1]});
        int ans = -1;
        int n = (int)points.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue;
                if (!set.count({x1, y2}) || !set.count({x2, y1})) continue;
                int minX = std::min(x1, x2), maxX = std::max(x1, x2);
                int minY = std::min(y1, y2), maxY = std::max(y1, y2);
                bool ok = true;
                for (auto& p : points) {
                    int x = p[0], y = p[1];
                    if (x > minX && x < maxX && y > minY && y < maxY) { ok = false; break; }
                    bool onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                                    ((y == minY || y == maxY) && x >= minX && x <= maxX);
                    if (onBorder) {
                        bool isCorner = (x == minX || x == maxX) && (y == minY || y == maxY);
                        if (!isCorner) { ok = false; break; }
                    }
                }
                if (ok) {
                    int area = (maxX - minX) * (maxY - minY);
                    if (area > ans) ans = area;
                }
            }
        }
        return ans;
    }
};


// ========== 3381_maximum_subarray_sum_with_length_divisible_by_k ==========
// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxSubarraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        const long long INF = 1LL << 62;
        std::vector<long long> best(k, INF);
        best[0] = 0;
        long long ans = -(1LL << 62);
        for (int i = 1; i <= n; i++) {
            int r = i % k;
            if (best[r] != INF) {
                long long cand = pref[i] - best[r];
                if (cand > ans) ans = cand;
            }
            if (pref[i] < best[r]) best[r] = pref[i];
        }
        return ans;
    }
};


// ========== 3382_maximum_area_rectangle_with_point_constraints_ii ==========
// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

#include <cstdint>
#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    long long maxRectangleArea(std::vector<int>& xCoord, std::vector<int>& yCoord) {
        int n = (int)xCoord.size();
        std::vector<std::vector<int>> points(n);
        for (int i = 0; i < n; i++) points[i] = {xCoord[i], yCoord[i]};
        std::set<std::pair<int, int>> set;
        for (auto& p : points) set.insert({p[0], p[1]});
        long long ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue;
                if (!set.count({x1, y2}) || !set.count({x2, y1})) continue;
                int minX = std::min(x1, x2), maxX = std::max(x1, x2);
                int minY = std::min(y1, y2), maxY = std::max(y1, y2);
                bool ok = true;
                for (auto& p : points) {
                    int x = p[0], y = p[1];
                    if (x > minX && x < maxX && y > minY && y < maxY) { ok = false; break; }
                    bool onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                                    ((y == minY || y == maxY) && x >= minX && x <= maxX);
                    if (onBorder) {
                        bool isCorner = (x == minX || x == maxX) && (y == minY || y == maxY);
                        if (!isCorner) { ok = false; break; }
                    }
                }
                if (ok) {
                    long long area = (long long)(maxX - minX) * (maxY - minY);
                    if (area > ans) ans = area;
                }
            }
        }
        return ans;
    }
};


// ========== 3383_minimum_runes_to_add_to_cast_spell ==========
// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

#include <functional>
#include <vector>

class Solution {
public:
    int minRunesToAdd(int n, std::vector<int>& crystals, std::vector<int>& flowFrom, std::vector<int>& flowTo) {
        std::vector<std::vector<int>> g(n), rg(n);
        for (int i = 0; i < (int)flowFrom.size(); i++) {
            int a = flowFrom[i], b = flowTo[i];
            g[a].push_back(b);
            rg[b].push_back(a);
        }
        std::vector<char> vis(n);
        std::vector<int> order;
        std::function<void(int)> dfs1 = [&](int u) {
            vis[u] = 1;
            for (int v : g[u]) if (!vis[v]) dfs1(v);
            order.push_back(u);
        };
        for (int i = 0; i < n; i++) if (!vis[i]) dfs1(i);
        std::vector<int> comp(n, -1);
        int cid = 0;
        std::function<void(int)> dfs2 = [&](int u) {
            comp[u] = cid;
            for (int v : rg[u]) if (comp[v] == -1) dfs2(v);
        };
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            if (comp[u] == -1) {
                dfs2(u);
                cid++;
            }
        }
        std::vector<char> hasCrystal(cid);
        for (int c : crystals) hasCrystal[comp[c]] = 1;
        std::vector<int> indeg(cid);
        for (int u = 0; u < n; u++) {
            for (int v : g[u]) {
                if (comp[u] != comp[v]) indeg[comp[v]]++;
            }
        }
        int ans = 0;
        for (int i = 0; i < cid; i++) {
            if (indeg[i] == 0 && !hasCrystal[i]) ans++;
        }
        return ans;
    }
};


// ========== 3385_minimum_time_to_break_locks_ii ==========
// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

#include <cstdint>
#include <vector>

class Solution {
    static int bitsOnes(int x) {
        int c = 0;
        while (x > 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }

public:
    int findMinimumTime(std::vector<int>& strength) {
        int n = (int)strength.size();
        int N = 1 << n;
        const long long inf = (long long)1e18;
        std::vector<long long> dp(N, inf);
        dp[0] = 0;
        int k = 1;
        for (int mask = 0; mask < N; mask++) {
            if (dp[mask] == inf) continue;
            int opened = bitsOnes(mask);
            int x = 1 + opened * k;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                int t = (strength[i] + x - 1) / x;
                int nmask = mask | (1 << i);
                if (dp[mask] + t < dp[nmask]) dp[nmask] = dp[mask] + t;
            }
        }
        return (int)dp[N - 1];
    }
};


// ========== 3386_button_with_longest_push_time ==========
// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

#include <vector>

class Solution {
public:
    int buttonWithLongestTime(std::vector<std::vector<int>>& events) {
        int bestT = events[0][1], bestI = events[0][0];
        for (int i = 1; i < (int)events.size(); i++) {
            int t = events[i][1] - events[i - 1][1];
            if (t > bestT || (t == bestT && events[i][0] < bestI)) {
                bestT = t;
                bestI = events[i][0];
            }
        }
        return bestI;
    }
};


// ========== 3387_maximize_amount_after_two_days_of_conversions ==========
// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
    using Graph = std::unordered_map<std::string, std::unordered_map<std::string, double>>;

    Graph buildRateGraph(std::vector<std::vector<std::string>>& pairs, std::vector<double>& rates) {
        Graph g;
        for (int i = 0; i < (int)pairs.size(); i++) {
            auto& a = pairs[i][0];
            auto& b = pairs[i][1];
            g[a][b] = rates[i];
            g[b][a] = 1.0 / rates[i];
        }
        return g;
    }

    std::unordered_map<std::string, double> bellman(const std::string& start,
        std::vector<std::vector<std::string>>& pairs, std::vector<double>& rates) {
        Graph g = buildRateGraph(pairs, rates);
        std::unordered_map<std::string, double> dist;
        dist[start] = 1.0;
        for (int it = 0; it < 100; it++) {
            bool updated = false;
            for (auto& [from, edges] : g) {
                if (!dist.count(from) || dist[from] == 0) continue;
                for (auto& [to, rate] : edges) {
                    double nv = dist[from] * rate;
                    if (!dist.count(to) || nv > dist[to]) {
                        dist[to] = nv;
                        updated = true;
                    }
                }
            }
            if (!updated) break;
        }
        return dist;
    }

public:
    double maxAmount(std::string initialCurrency, std::vector<std::vector<std::string>>& pairs1,
                     std::vector<double>& rates1, std::vector<std::vector<std::string>>& pairs2,
                     std::vector<double>& rates2) {
        auto amt1 = bellman(initialCurrency, pairs1, rates1);
        double ans = 1.0;
        Graph g2 = buildRateGraph(pairs2, rates2);
        for (auto& [c, a] : amt1) {
            if (a <= 0) continue;
            std::unordered_map<std::string, double> dist;
            dist[c] = a;
            bool updated = true;
            for (int it = 0; it < 100 && updated; it++) {
                updated = false;
                for (auto& [from, edges] : g2) {
                    if (!dist.count(from) || dist[from] == 0) continue;
                    for (auto& [to, rate] : edges) {
                        double nv = dist[from] * rate;
                        if (!dist.count(to) || nv > dist[to]) {
                            dist[to] = nv;
                            updated = true;
                        }
                    }
                }
            }
            if (dist.count(initialCurrency) && dist[initialCurrency] > ans)
                ans = dist[initialCurrency];
        }
        return ans;
    }
};


// ========== 3388_count_beautiful_splits_in_an_array ==========
// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

#include <vector>

class Solution {
    bool equal(const std::vector<int>& a, int as, int ae, const std::vector<int>& b, int bs, int be) {
        if (ae - as != be - bs) return false;
        for (int i = 0; i < ae - as; i++) if (a[as + i] != b[bs + i]) return false;
        return true;
    }

public:
    int beautifulSplits(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = 0;
        for (int i = 1; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                bool ok = false;
                if (i <= j - i && equal(nums, 0, i, nums, i, i + i)) ok = true;
                if (!ok && j - i <= n - j && equal(nums, i, j, nums, j, j + (j - i))) ok = true;
                if (ok) ans++;
            }
        }
        return ans;
    }
};


// ========== 3389_minimum_operations_to_make_character_frequencies_equal ==========
// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

#include <algorithm>
#include <string>

class Solution {
public:
    int makeStringGood(std::string s) {
        int freq[26] = {};
        for (char c : s) freq[c - 'a']++;
        int ans = (int)s.size();
        for (int t = 1; t <= (int)s.size(); t++) {
            int pool = 0;
            for (int i = 0; i < 26; i++) if (freq[i] > t) pool += freq[i] - t;
            int deficit = 0;
            for (int i = 0; i < 26; i++) if (freq[i] < t) deficit += t - freq[i];
            int ops = (pool >= deficit) ? pool : deficit;
            if (ops < ans) ans = ops;
        }
        if ((int)s.size() < ans) ans = (int)s.size();
        return ans;
    }
};


// ========== 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking ==========
// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

#include <vector>

class Matrix3D {
    std::vector<std::vector<std::vector<int>>> m;
    std::vector<int> ones;
    int n;

public:
    Matrix3D(int n_) : m(n_, std::vector<std::vector<int>>(n_, std::vector<int>(n_, 0))), ones(n_, 0), n(n_) {}

    void setCell(int x, int y, int z) {
        if (m[x][y][z] == 0) {
            m[x][y][z] = 1;
            ones[x]++;
        }
    }

    void unsetCell(int x, int y, int z) {
        if (m[x][y][z] == 1) {
            m[x][y][z] = 0;
            ones[x]--;
        }
    }

    int largestMatrix() {
        int best = -1, idx = 0;
        for (int i = 0; i < n; i++) {
            if (ones[i] >= best) {
                best = ones[i];
                idx = i;
            }
        }
        return idx;
    }
};


// ========== 3392_count_subarrays_of_length_three_with_a_condition ==========
// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

#include <vector>

class Solution {
public:
    int countSubarrays(std::vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i + 2 < (int)nums.size(); i++) {
            if (nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1]) ans++;
        }
        return ans;
    }
};
