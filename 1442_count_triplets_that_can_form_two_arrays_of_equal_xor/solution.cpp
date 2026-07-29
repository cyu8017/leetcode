#include <vector>

class Solution {
public:
    int countTriplets(std::vector<int>& arr) {
        int answer = 0;
        for (int i = 0; i < (int)arr.size(); ++i) {
            int value = 0;
            for (int k = i; k < (int)arr.size(); ++k) {
                value ^= arr[k];
                if (value == 0) answer += k - i;
            }
        }
        return answer;
    }
};
