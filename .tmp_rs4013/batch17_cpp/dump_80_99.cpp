

########## 3480_maximize_subarrays_after_removing_one_conflicting_pair ##########
// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxSubarrays(int n, std::vector<std::vector<int>>& conflictingPairs) {
        int m = (int)conflictingPairs.size();
        long long best = 0;
        for (int skip = 0; skip < m; skip++) {
            std::vector<std::pair<int, int>> banned;
            for (int i = 0; i < m; i++) {
                if (i == skip) continue;
                int a = conflictingPairs[i][0], b = conflictingPairs[i][1];
                if (a > b) std::swap(a, b);
                banned.push_back({a, b});
            }
            std::vector<int> rightLimit(n + 2, n + 1);
            for (auto& b : banned) {
                if (b.second < rightLimit[b.first]) rightLimit[b.first] = b.second;
            }
            int minRight = n + 1;
            long long cnt = 0;
            for (int l = n; l >= 1; l--) {
                if (rightLimit[l] < minRight) minRight = rightLimit[l];
                cnt += minRight - l;
            }
            if (cnt > best) best = cnt;
        }
        return best;
    }
};


########## 3481_apply_substitutions ##########
// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

#include <string>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::string applySubstitutions(std::vector<std::vector<std::string>>& replacements, std::string text) {
        std::unordered_map<std::string, std::string> mp;
        for (auto& r : replacements) mp[r[0]] = r[1];
        auto resolve = [&](auto&& self, const std::string& s) -> std::string {
            std::string out;
            for (int i = 0; i < (int)s.size();) {
                if (s[i] == '%') {
                    int j = i + 1;
                    while (j < (int)s.size() && s[j] != '%') j++;
                    std::string key = s.substr(i + 1, j - i - 1);
                    out += self(self, mp[key]);
                    i = j + 1;
                } else {
                    out.push_back(s[i]);
                    i++;
                }
            }
            return out;
        };
        return resolve(resolve, text);
    }
};


########## 3483_unique_3_digit_even_numbers ##########
// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

#include <vector>
#include <unordered_set>

class Solution {
public:
    int totalNumbers(std::vector<int>& digits) {
        std::unordered_set<int> seen;
        int n = (int)digits.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) continue;
                    if (digits[i] == 0) continue;
                    if (digits[k] % 2 != 0) continue;
                    seen.insert(digits[i] * 100 + digits[j] * 10 + digits[k]);
                }
            }
        }
        return (int)seen.size();
    }
};


########## 3484_design_spreadsheet ##########
// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

#include <string>
#include <unordered_map>

class Spreadsheet {
    std::unordered_map<std::string, int> cells;
public:
    Spreadsheet(int rows) {}

    void setCell(std::string cell, int value) { cells[cell] = value; }

    void resetCell(std::string cell) { cells.erase(cell); }

    int getValue(std::string formula) {
        if (!formula.empty() && formula[0] == '=') formula = formula.substr(1);
        int sum = 0;
        size_t start = 0;
        while (start < formula.size()) {
            size_t plus = formula.find('+', start);
            std::string p = formula.substr(start, plus == std::string::npos ? std::string::npos : plus - start);
            bool isNum = !p.empty() && (isdigit(p[0]) || (p[0] == '-' && p.size() > 1));
            if (isNum) {
                for (size_t i = 1; i < p.size(); i++) if (!isdigit(p[i])) { isNum = false; break; }
            }
            if (isNum) sum += std::stoi(p);
            else sum += cells[p];
            if (plus == std::string::npos) break;
            start = plus + 1;
        }
        return sum;
    }
};


########## 3485_longest_common_prefix_of_k_strings_after_removal ##########
// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
    int lcpOf(const std::vector<std::string>& a) {
        if (a.empty()) return 0;
        std::string pref = a[0];
        for (size_t t = 1; t < a.size(); t++) {
            const std::string& s = a[t];
            size_t i = 0;
            while (i < pref.size() && i < s.size() && pref[i] == s[i]) i++;
            pref.resize(i);
            if (pref.empty()) return 0;
        }
        return (int)pref.size();
    }
public:
    std::vector<int> longestCommonPrefix(std::vector<std::string>& words, int k) {
        int n = (int)words.size();
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            std::vector<std::string> rest;
            for (int j = 0; j < n; j++) if (j != i) rest.push_back(words[j]);
            if ((int)rest.size() < k) { ans[i] = 0; continue; }
            std::sort(rest.begin(), rest.end());
            int best = 0;
            for (int j = 0; j + k - 1 < (int)rest.size(); j++) {
                std::vector<std::string> window(rest.begin() + j, rest.begin() + j + k);
                best = std::max(best, lcpOf(window));
            }
            ans[i] = best;
        }
        return ans;
    }
};


########## 3486_longest_special_path_ii ##########
// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

#include <vector>
#include <unordered_map>

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
        auto dfs = [&](auto&& self, int u, int p, int dist, std::vector<int>& pathVals, std::vector<int>& pathDist) -> void {
            pathVals.push_back(nums[u]);
            pathDist.push_back(dist);
            std::unordered_map<int, int> freq;
            int dups = 0, left = 0;
            for (int right = 0; right < (int)pathVals.size(); right++) {
                if (++freq[pathVals[right]] == 2) dups++;
                while (dups > 1) {
                    if (freq[pathVals[left]] == 2) dups--;
                    freq[pathVals[left]]--;
                    left++;
                }
            }
            int length = dist - pathDist[left];
            int nodes = (int)pathVals.size() - left;
            if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
                bestLen = length;
                bestNodes = nodes;
            }
            for (auto& [to, w] : g[u]) {
                if (to == p) continue;
                self(self, to, u, dist + w, pathVals, pathDist);
            }
            pathVals.pop_back();
            pathDist.pop_back();
        };
        std::vector<int> pathVals, pathDist;
        dfs(dfs, 0, -1, 0, pathVals, pathDist);
        return {bestLen, bestNodes};
    }
};


########## 3487_maximum_unique_subarray_sum_after_deletion ##########
// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

#include <vector>
#include <unordered_set>

class Solution {
public:
    int maxSum(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        int sum = 0;
        bool hasPos = false;
        int maxNeg = (int)(-1e9);
        for (int x : nums) {
            if (x < 0) {
                if (x > maxNeg) maxNeg = x;
                continue;
            }
            hasPos = true;
            if (!seen.count(x)) {
                seen.insert(x);
                sum += x;
            }
        }
        return hasPos ? sum : maxNeg;
    }
};


########## 3488_closest_equal_element_queries ##########
// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> solveQueries(std::vector<int>& nums, std::vector<int>& queries) {
        int n = (int)nums.size();
        std::unordered_map<int, std::vector<int>> pos;
        for (int i = 0; i < n; i++) pos[nums[i]].push_back(i);
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int idx = queries[qi];
            int x = nums[idx];
            auto& arr = pos[x];
            if ((int)arr.size() == 1) { ans[qi] = -1; continue; }
            int best = n;
            for (int p : arr) {
                if (p == idx) continue;
                int d = abs(p - idx);
                d = std::min(d, n - d);
                if (d < best) best = d;
            }
            ans[qi] = best;
        }
        return ans;
    }
};


########## 3489_zero_array_transformation_iv ##########
// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

#include <vector>

class Solution {
    bool canSubsetSum(const std::vector<int>& vals, int target) {
        if (target == 0) return true;
        std::vector<char> dp(target + 1, 0);
        dp[0] = 1;
        for (int v : vals) {
            for (int s = target; s >= v; s--) if (dp[s - v]) dp[s] = 1;
        }
        return dp[target];
    }
public:
    int minZeroArray(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        auto ok = [&](int k) {
            for (int i = 0; i < n; i++) {
                if (nums[i] == 0) continue;
                std::vector<int> vals;
                for (int q = 0; q < k; q++) {
                    int l = queries[q][0], r = queries[q][1], v = queries[q][2];
                    if (l <= i && i <= r) vals.push_back(v);
                }
                if (!canSubsetSum(vals, nums[i])) return false;
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
        return lo > (int)queries.size() ? -1 : lo;
    }
};


########## 3490_count_beautiful_numbers ##########
// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

#include <string>
#include <functional>

class Solution {
    std::string itoa3490(int x) {
        if (x == 0) return "0";
        std::string b;
        while (x > 0) {
            b.insert(b.begin(), char('0' + x % 10));
            x /= 10;
        }
        return b;
    }
    int countBeautiful(int n) {
        if (n <= 0) return 0;
        std::string s = itoa3490(n);
        std::function<int(int, bool, int, int, bool)> dfs = [&](int pos, bool tight, int sum, int prod, bool started) -> int {
            if (pos == (int)s.size()) {
                if (!started) return 0;
                return (sum > 0 && prod % sum == 0) ? 1 : 0;
            }
            int up = tight ? (s[pos] - '0') : 9;
            int ans = 0;
            for (int d = 0; d <= up; d++) {
                bool nt = tight && d == up;
                if (!started && d == 0) ans += dfs(pos + 1, nt, 0, 1, false);
                else {
                    int ns = sum + d;
                    int np = !started ? d : prod * d;
                    ans += dfs(pos + 1, nt, ns, np, true);
                }
            }
            return ans;
        };
        return dfs(0, true, 0, 1, false);
    }
public:
    int beautifulNumbers(int l, int r) {
        return countBeautiful(r) - countBeautiful(l - 1);
    }
};


########## 3491_phone_number_prefix ##########
// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    bool phonePrefix(std::vector<std::string>& numbers) {
        std::sort(numbers.begin(), numbers.end());
        for (int i = 0; i + 1 < (int)numbers.size(); i++) {
            if (numbers[i].size() <= numbers[i + 1].size() &&
                numbers[i + 1].compare(0, numbers[i].size(), numbers[i]) == 0)
                return false;
        }
        return true;
    }
};


########## 3492_maximum_containers_on_a_ship ##########
// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        int cap = n * n;
        int byW = maxWeight / w;
        return cap < byW ? cap : byW;
    }
};


########## 3493_properties_graph ##########
// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

#include <vector>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    int numberOfComponents(std::vector<std::vector<int>>& properties, int k) {
        int n = (int)properties.size();
        std::vector<std::unordered_set<int>> sets(n);
        for (int i = 0; i < n; i++)
            for (int v : properties[i]) sets[i].insert(v);
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
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int cnt = 0;
                for (int v : sets[i]) if (sets[j].count(v)) cnt++;
                if (cnt >= k) unite(i, j);
            }
        }
        std::unordered_set<int> comp;
        for (int i = 0; i < n; i++) comp.insert(find(find, i));
        return (int)comp.size();
    }
};


########## 3494_find_the_minimum_amount_of_time_to_brew_potions ##########
// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long minTime(std::vector<int>& skill, std::vector<int>& mana) {
        int n = (int)skill.size(), m = (int)mana.size();
        std::vector<long long> done(n);
        for (int j = 0; j < m; j++) {
            long long t = 0;
            for (int i = 0; i < n; i++) {
                if (done[i] > t) t = done[i];
                t += 1LL * skill[i] * mana[j];
                done[i] = t;
            }
            for (int i = n - 2; i >= 0; i--)
                done[i] = done[i + 1] - 1LL * skill[i + 1] * mana[j];
        }
        return done[n - 1];
    }
};


########## 3495_minimum_operations_to_make_array_elements_zero ##########
// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

#include <vector>

class Solution {
    int opsToZero(int x) {
        int ops = 0;
        while (x > 0) { x /= 4; ops++; }
        return ops;
    }
public:
    long long minOperations(std::vector<std::vector<int>>& queries) {
        long long ans = 0;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            long long sum = 0;
            for (int x = l; x <= r; x++) sum += opsToZero(x);
            ans += (sum + 1) / 2;
        }
        return ans;
    }
};


########## 3496_maximize_score_after_pair_deletions ##########
// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximizeScore(std::vector<int>& nums) {
        int n = (int)nums.size();
        int total = 0;
        for (int x : nums) total += x;
        if (n % 2 == 1) {
            int mn = nums[0];
            for (int x : nums) if (x < mn) mn = x;
            return total - mn;
        }
        int mn = nums[0] + nums[1];
        for (int i = 0; i + 1 < n; i++) mn = std::min(mn, nums[i] + nums[i + 1]);
        return total - mn;
    }
};


########## 3498_reverse_degree_of_a_string ##########
// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

#include <string>

class Solution {
public:
    int reverseDegree(std::string s) {
        int ans = 0;
        for (int i = 0; i < (int)s.size(); i++)
            ans += (26 - (s[i] - 'a')) * (i + 1);
        return ans;
    }
};


########## 3499_maximize_active_section_with_trade_i ##########
// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

#include <string>
#include <vector>

class Solution {
public:
    int maxActiveSectionsAfterTrade(std::string s) {
        int ones = 0;
        for (char c : s) if (c == '1') ones++;
        std::vector<std::pair<int, int>> zeros;
        int n = (int)s.size();
        for (int i = 0; i < n;) {
            if (s[i] != '0') { i++; continue; }
            int j = i;
            while (j < n && s[j] == '0') j++;
            zeros.push_back({i, j - 1});
            i = j;
        }
        int best = 0;
        for (int i = 0; i + 1 < (int)zeros.size(); i++) {
            int gain = (zeros[i].second - zeros[i].first + 1) + (zeros[i + 1].second - zeros[i + 1].first + 1);
            if (gain > best) best = gain;
        }
        return ones + best;
    }
};


########## 3500_minimum_cost_to_divide_array_into_subarrays ##########
// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long minimumCost(std::vector<int>& nums, std::vector<int>& cost, int k) {
        int n = (int)nums.size();
        std::vector<long long> pn(n + 1), pc(n + 1);
        for (int i = 0; i < n; i++) {
            pn[i + 1] = pn[i] + nums[i];
            pc[i + 1] = pc[i] + cost[i];
        }
        const long long inf = 1LL << 62;
        std::vector<long long> dp(n + 1, 0);
        for (int i = 0; i < n; i++) dp[i] = inf;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                long long cand = pn[j + 1] * (pc[j + 1] - pc[i]) + 1LL * k * (pc[n] - pc[i]) + dp[j + 1];
                if (cand < dp[i]) dp[i] = cand;
            }
        }
        return dp[0];
    }
};


########## 3501_maximize_active_section_with_trade_ii ##########
// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> maxActiveSectionsAfterTrade(std::string s, std::vector<std::vector<int>>& queries) {
        int ones = 0;
        for (char c : s) if (c == '1') ones++;
        std::vector<int> ans(queries.size(), ones);
        return ans;
    }
};
