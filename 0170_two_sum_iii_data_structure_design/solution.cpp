// LeetCode 0170 - Two Sum III - Data structure design
#include <unordered_map>
using namespace std;
class TwoSum {
    unordered_map<int, int> counts;
public:
    void add(int number) { ++counts[number]; }
    bool find(int value) {
        for (const auto& [number, count] : counts) {
            int complement = value - number;
            if (complement == number ? count >= 2 : counts.count(complement)) return true;
        }
        return false;
    }
};