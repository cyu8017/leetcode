#include <string>
#include <vector>

class Solution {
public:
    std::string largestNumber(std::vector<int>& cost, int target) {
        std::vector<std::string> dp(target + 1, "#");
        dp[0] = "";
        for (int total = 1; total <= target; ++total) {
            std::string best = "#";
            for (int digit = 1; digit <= 9; ++digit) {
                int price = cost[digit - 1];
                if (total >= price && dp[total - price] != "#") {
                    std::string candidate = std::to_string(digit) + dp[total - price];
                    if (best == "#" || candidate.size() > best.size() ||
                        (candidate.size() == best.size() && candidate > best))
                        best = candidate;
                }
            }
            dp[total] = best;
        }
        return dp[target] == "#" ? "0" : dp[target];
    }
};
