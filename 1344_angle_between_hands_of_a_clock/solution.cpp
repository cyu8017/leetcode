#include <algorithm>
#include <cmath>

class Solution {
public:
    double angleClock(int hour, int minutes) {
        double difference = std::abs((hour % 12) * 30.0 + minutes * 0.5 - minutes * 6.0);
        return std::min(difference, 360.0 - difference);
    }
};
