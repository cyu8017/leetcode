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
