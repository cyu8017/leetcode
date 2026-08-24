

########## 3437_permutations_iii ##########
// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> permute(int n) {
        std::vector<std::vector<int>> ans;
        std::vector<char> used(n + 1);
        std::vector<int> cur;
        std::function<void()> dfs = [&]() {
            if ((int)cur.size() == n) {
                ans.push_back(cur);
                return;
            }
            for (int i = 1; i <= n; i++) {
                if (used[i]) continue;
                if (!cur.empty() && (cur.back() % 2 == i % 2)) continue;
                used[i] = 1;
                cur.push_back(i);
                dfs();
                cur.pop_back();
                used[i] = 0;
            }
        };
        dfs();
        return ans;
    }
};


########## 3438_find_valid_pair_of_adjacent_digits_in_string ##########
// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

#include <string>

class Solution {
public:
    std::string findValidPair(std::string s) {
        int freq[10] = {};
        for (char c : s) freq[c - '0']++;
        for (int i = 0; i + 1 < (int)s.size(); i++) {
            int a = s[i] - '0', b = s[i + 1] - '0';
            if (a != b && freq[a] == a && freq[b] == b) return s.substr(i, 2);
        }
        return "";
    }
};


########## 3439_reschedule_meetings_for_maximum_free_time_i ##########
// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

#include <vector>

class Solution {
public:
    int maxFreeTime(int eventTime, int k, std::vector<int>& startTime, std::vector<int>& endTime) {
        int n = (int)startTime.size();
        std::vector<int> gaps(n + 1);
        gaps[0] = startTime[0];
        for (int i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
        gaps[n] = eventTime - endTime[n - 1];
        int window = k + 1;
        int sum = 0;
        for (int i = 0; i < window && i < (int)gaps.size(); i++) sum += gaps[i];
        int ans = sum;
        for (int i = window; i < (int)gaps.size(); i++) {
            sum += gaps[i] - gaps[i - window];
            if (sum > ans) ans = sum;
        }
        return ans;
    }
};


########## 3440_reschedule_meetings_for_maximum_free_time_ii ##########
// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

#include <vector>

class Solution {
public:
    int maxFreeTime(int eventTime, std::vector<int>& startTime, std::vector<int>& endTime) {
        int n = (int)startTime.size();
        std::vector<int> gaps(n + 1);
        gaps[0] = startTime[0];
        for (int i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
        gaps[n] = eventTime - endTime[n - 1];
        int ans = 0;
        for (int g : gaps) if (g > ans) ans = g;
        std::vector<int> leftMax(n + 1), rightMax(n + 1);
        for (int i = 0; i <= n; i++) {
            leftMax[i] = gaps[i];
            if (i > 0 && leftMax[i - 1] > leftMax[i]) leftMax[i] = leftMax[i - 1];
        }
        for (int i = n; i >= 0; i--) {
            rightMax[i] = gaps[i];
            if (i < n && rightMax[i + 1] > rightMax[i]) rightMax[i] = rightMax[i + 1];
        }
        for (int i = 0; i < n; i++) {
            int dur = endTime[i] - startTime[i];
            int merged = gaps[i] + gaps[i + 1];
            int bestOther = 0;
            if (i > 0 && leftMax[i - 1] > bestOther) bestOther = leftMax[i - 1];
            if (i + 2 <= n && rightMax[i + 2] > bestOther) bestOther = rightMax[i + 2];
            int cand = merged;
            if (bestOther >= dur) cand = merged + dur;
            if (cand > ans) ans = cand;
        }
        return ans;
    }
};


########## 3441_minimum_cost_good_caption ##########
// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

#include <string>
#include <vector>

class Solution {
public:
    std::string minCostGoodCaption(std::string caption) {
        int n = (int)caption.size();
        if (n < 3) return "";
        std::vector<char> ans(caption.begin(), caption.end());
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && ans[j] == ans[i]) j++;
            if (j - i >= 3) { i = j; continue; }
            int need = 3 - (j - i);
            if (j + need <= n) {
                for (int t = 0; t < need; t++) ans[j + t] = ans[i];
                i = j + need;
            } else {
                char ch = 'a';
                if (i > 0) ch = ans[i - 1];
                else if (j < n) ch = caption[j];
                for (int t = i; t < n; t++) ans[t] = ch;
                break;
            }
        }
        i = 0;
        while (i < n) {
            int j = i;
            while (j < n && ans[j] == ans[i]) j++;
            if (j - i < 3) return "";
            i = j;
        }
        return std::string(ans.begin(), ans.end());
    }
};


########## 3442_maximum_difference_between_even_and_odd_frequency_i ##########
// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

#include <string>

class Solution {
public:
    int maxDifference(std::string s) {
        int freq[26] = {};
        for (char c : s) freq[c - 'a']++;
        int maxOdd = 0, minEven = 1000000000;
        for (int f : freq) {
            if (f == 0) continue;
            if (f % 2 == 1) {
                if (f > maxOdd) maxOdd = f;
            } else if (f < minEven) minEven = f;
        }
        return maxOdd - minEven;
    }
};


########## 3443_maximum_manhattan_distance_after_k_changes ##########
// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

#include <cstdlib>
#include <string>

class Solution {
public:
    int maxDistance(std::string s, int k) {
        int ans = 0;
        int lat = 0, lon = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            char c = s[i];
            if (c == 'N') lat++;
            else if (c == 'S') lat--;
            else if (c == 'E') lon++;
            else lon--;
            int md = std::abs(lat) + std::abs(lon);
            int steps = i + 1;
            int cur = md + 2 * k;
            if (cur > steps) cur = steps;
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};


########## 3444_minimum_increments_for_target_multiples_in_an_array ##########
// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

#include <cstdint>
#include <vector>

class Solution {
    static int gcd(int a, int b) {
        while (b) { int t = a % b; a = b; b = t; }
        return a;
    }
    static int lcm(int a, int b) { return a / gcd(a, b) * b; }

public:
    int minimumIncrements(std::vector<int>& nums, std::vector<int>& target) {
        int m = (int)target.size();
        int N = 1 << m;
        const long long inf = (long long)1e18;
        std::vector<long long> dp(N, inf);
        dp[0] = 0;
        for (int x : nums) {
            std::vector<long long> ndp = dp;
            for (int mask = 0; mask < N; mask++) {
                for (int sub = 1; sub < N; sub++) {
                    int L = 1;
                    bool ok = true;
                    for (int i = 0; i < m; i++) {
                        if (sub & (1 << i)) {
                            L = lcm(L, target[i]);
                            if (L > 1000000000) { ok = false; break; }
                        }
                    }
                    if (!ok) continue;
                    int cost = (L - x % L) % L;
                    int nmask = mask | sub;
                    if (dp[mask] + cost < ndp[nmask]) ndp[nmask] = dp[mask] + cost;
                }
            }
            dp.swap(ndp);
        }
        return (int)dp[N - 1];
    }
};


########## 3445_maximum_difference_between_even_and_odd_frequency_ii ##########
// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

#include <string>
#include <vector>

class Solution {
public:
    int maxDifference(std::string s, int k) {
        int n = (int)s.size();
        int ans = -1000000000;
        for (int a = 0; a < 5; a++) {
            for (int b = 0; b < 5; b++) {
                if (a == b) continue;
                std::vector<int> prefA(n + 1), prefB(n + 1);
                for (int i = 0; i < n; i++) {
                    prefA[i + 1] = prefA[i];
                    prefB[i + 1] = prefB[i];
                    if (s[i] - '0' == a) prefA[i + 1]++;
                    if (s[i] - '0' == b) prefB[i + 1]++;
                }
                for (int i = 0; i < n; i++) {
                    for (int j = i + k - 1; j < n; j++) {
                        int fa = prefA[j + 1] - prefA[i];
                        int fb = prefB[j + 1] - prefB[i];
                        if (fa % 2 == 1 && fb % 2 == 0 && fb > 0) {
                            if (fa - fb > ans) ans = fa - fb;
                        }
                    }
                }
            }
        }
        return ans;
    }
};


########## 3446_sort_matrix_by_diagonals ##########
// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> sortMatrix(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        std::unordered_map<int, std::vector<int>> diags;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) diags[i - j].push_back(grid[i][j]);
        }
        for (auto& [k, arr] : diags) {
            if (k >= 0) std::sort(arr.begin(), arr.end(), std::greater<int>());
            else std::sort(arr.begin(), arr.end());
        }
        std::unordered_map<int, int> idx;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int k = i - j;
                grid[i][j] = diags[k][idx[k]++];
            }
        }
        return grid;
    }
};


########## 3447_assign_elements_to_groups_with_constraints ##########
// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

#include <vector>

class Solution {
public:
    std::vector<int> assignElements(std::vector<int>& groups, std::vector<int>& elements) {
        const int maxV = 100001;
        std::vector<int> first(maxV, -1);
        for (int i = 0; i < (int)elements.size(); i++) {
            int e = elements[i];
            if (e < maxV && first[e] == -1) first[e] = i;
        }
        std::vector<int> ans(groups.size());
        for (int gi = 0; gi < (int)groups.size(); gi++) {
            int g = groups[gi];
            int best = -1;
            for (int d = 1; d * d <= g; d++) {
                if (g % d == 0) {
                    if (first[d] != -1 && (best == -1 || first[d] < best)) best = first[d];
                    int other = g / d;
                    if (first[other] != -1 && (best == -1 || first[other] < best)) best = first[other];
                }
            }
            ans[gi] = best;
        }
        return ans;
    }
};


########## 3448_count_substrings_divisible_by_last_digit ##########
// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

#include <cstdint>
#include <string>

class Solution {
public:
    long long countSubstrings(std::string s) {
        long long ans = 0;
        int n = (int)s.size();
        for (int r = 0; r < n; r++) {
            int last = s[r] - '0';
            if (last == 0) continue;
            int mod = 0;
            int p = 1 % last;
            for (int l = r; l >= 0; l--) {
                mod = (mod + (s[l] - '0') * p) % last;
                p = (p * 10) % last;
                if (mod == 0) ans++;
            }
        }
        return ans;
    }
};


########## 3449_maximize_the_minimum_game_score ##########
// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& points, int m) {
        auto ok = [&](long long mid) {
            long long need = 0;
            long long extra = 0;
            for (int p : points) {
                long long req = (mid + p - 1) / p;
                if (req > extra) {
                    long long visits = req - extra;
                    need += 2 * visits - 1;
                    extra = visits - 1;
                } else {
                    need += 1;
                    extra = 0;
                }
                if (need > m) return false;
            }
            return need <= m;
        };
        long long lo = 0, hi = (long long)1e18;
        while (lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};


########## 3450_maximum_students_on_a_single_bench ##########
// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxStudentsOnBench(std::vector<std::vector<int>>& students) {
        std::unordered_map<int, std::unordered_set<int>> bench;
        for (auto& s : students) {
            int sid = s[0], b = s[1];
            bench[b].insert(sid);
        }
        int ans = 0;
        for (auto& [_, set] : bench) {
            if ((int)set.size() > ans) ans = (int)set.size();
        }
        return ans;
    }
};


########## 3452_sum_of_good_numbers ##########
// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

#include <vector>

class Solution {
public:
    int sumOfGoodNumbers(std::vector<int>& nums, int k) {
        int ans = 0;
        int n = (int)nums.size();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            bool good = true;
            if (i - k >= 0 && x <= nums[i - k]) good = false;
            if (i + k < n && x <= nums[i + k]) good = false;
            if (good) ans += x;
        }
        return ans;
    }
};


########## 3453_separate_squares_i ##########
// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

#include <vector>

class Solution {
public:
    double separateSquares(std::vector<std::vector<int>>& squares) {
        auto okArea = [&](double y) {
            double below = 0;
            for (auto& sq : squares) {
                double yi = sq[1], l = sq[2];
                double top = yi + l;
                if (y <= yi) continue;
                if (y >= top) below += l * l;
                else below += l * (y - yi);
            }
            return below;
        };
        double total = 0;
        for (auto& sq : squares) {
            double l = sq[2];
            total += l * l;
        }
        double lo = 0.0, hi = 2e9;
        for (int it = 0; it < 60; it++) {
            double mid = (lo + hi) / 2;
            if (okArea(mid) * 2 < total) lo = mid;
            else hi = mid;
        }
        return hi;
    }
};


########## 3454_separate_squares_ii ##########
// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

#include <vector>

class Solution {
public:
    double separateSquares(std::vector<std::vector<int>>& squares) {
        double total = 0;
        for (auto& sq : squares) {
            double l = sq[2];
            total += l * l;
        }
        auto areaBelow = [&](double y) {
            double below = 0;
            for (auto& sq : squares) {
                double yi = sq[1], l = sq[2];
                double top = yi + l;
                if (y <= yi) continue;
                else if (y >= top) below += l * l;
                else below += l * (y - yi);
            }
            return below;
        };
        double lo = 0.0, hi = 2e9;
        for (int it = 0; it < 60; it++) {
            double mid = (lo + hi) / 2;
            if (areaBelow(mid) * 2 < total) lo = mid;
            else hi = mid;
        }
        return hi;
    }
};


########## 3455_shortest_matching_substring ##########
// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int shortestMatchingSubstring(std::string s, std::string p) {
        std::vector<std::string> parts;
        std::string cur;
        for (char c : p) {
            if (c == '*') {
                parts.push_back(cur);
                cur.clear();
            } else cur.push_back(c);
        }
        parts.push_back(cur);
        while ((int)parts.size() < 3) parts.push_back("");
        std::string a = parts[0], b = parts[1], c = parts[2];
        int n = (int)s.size();
        auto findAll = [&](const std::string& sub) {
            std::vector<int> res;
            if (sub.empty()) {
                res.resize(n + 1);
                for (int i = 0; i <= n; i++) res[i] = i;
                return res;
            }
            for (int i = 0; i + (int)sub.size() <= n; i++) {
                if (s.compare(i, sub.size(), sub) == 0) res.push_back(i);
            }
            return res;
        };
        auto sortSearch = [](const std::vector<int>& arr, int x) {
            return (int)(std::lower_bound(arr.begin(), arr.end(), x) - arr.begin());
        };
        auto posA = findAll(a), posB = findAll(b), posC = findAll(c);
        int ans = n + 1;
        for (int ia : posA) {
            int endA = ia + (int)a.size();
            int bi = sortSearch(posB, endA);
            for (; bi < (int)posB.size(); bi++) {
                int endB = posB[bi] + (int)b.size();
                int ci = sortSearch(posC, endB);
                if (ci < (int)posC.size()) {
                    int length = posC[ci] + (int)c.size() - ia;
                    if (length < ans) ans = length;
                }
                if (b.empty()) break;
                break;
            }
        }
        return ans == n + 1 ? -1 : ans;
    }
};


########## 3456_find_special_substring_of_length_k ##########
// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

#include <string>

class Solution {
public:
    bool hasSpecialSubstring(std::string s, int k) {
        int n = (int)s.size();
        for (int i = 0; i + k <= n; i++) {
            bool ok = true;
            for (int j = i + 1; j < i + k; j++) {
                if (s[j] != s[i]) { ok = false; break; }
            }
            if (!ok) continue;
            if (i > 0 && s[i - 1] == s[i]) continue;
            if (i + k < n && s[i + k] == s[i]) continue;
            return true;
        }
        return false;
    }
};


########## 3457_eat_pizzas ##########
// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxWeight(std::vector<int>& pizzas) {
        std::sort(pizzas.begin(), pizzas.end());
        int n = (int)pizzas.size();
        int days = n / 4;
        long long ans = 0;
        int oddDays = (days + 1) / 2;
        int evenDays = days / 2;
        int idx = n - 1;
        for (int i = 0; i < oddDays; i++) {
            ans += pizzas[idx];
            idx--;
        }
        for (int i = 0; i < evenDays; i++) {
            idx--;
            ans += pizzas[idx];
            idx--;
        }
        return ans;
    }
};
