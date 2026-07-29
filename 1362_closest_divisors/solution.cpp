#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<int> closestDivisors(int num) {
        std::vector<int> best;
        for (int x : {num + 1, num + 2}) {
            for (int a = (int)std::sqrt(x); a >= 1; --a) {
                if (x % a == 0) {
                    std::vector<int> pair{a, x / a};
                    if (best.empty() || pair[1] - pair[0] < best[1] - best[0]) best = pair;
                    break;
                }
            }
        }
        return best;
    }
};
