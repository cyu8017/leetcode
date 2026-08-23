// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

#include <cmath>
#include <string>

class Solution {
public:
    bool isRationalEqual(std::string s, std::string t) {
        auto parse = [](const std::string& x) -> long double {
            if (x.find('(') == std::string::npos) {
                return x.empty() ? 0.0L : std::stold(x);
            }
            auto lp = x.find('(');
            std::string nonRep = x.substr(0, lp);
            std::string rep = x.substr(lp + 1, x.size() - lp - 2);
            if (nonRep.find('.') == std::string::npos) nonRep += '.';
            auto dot = nonRep.find('.');
            std::string integer = nonRep.substr(0, dot);
            std::string frac = nonRep.substr(dot + 1);
            long double base = integer.empty() ? 0.0L : std::stold(integer);
            if (!frac.empty()) {
                long double denom = 1;
                for (size_t i = 0; i < frac.size(); i++) denom *= 10;
                base += std::stold(frac) / denom;
            }
            if (!rep.empty()) {
                long double repVal = std::stold(rep);
                long double cycle = 1;
                for (size_t i = 0; i < rep.size(); i++) cycle *= 10;
                long double denom = (cycle - 1);
                for (size_t i = 0; i < frac.size(); i++) denom *= 10;
                base += repVal / denom;
            }
            return base;
        };
        return std::abs(parse(s) - parse(t)) < 1e-12L;
    }
};
