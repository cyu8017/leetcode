// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

#include <cctype>
#include <map>
#include <stack>
#include <string>

class Solution {
public:
    std::string countOfAtoms(std::string formula) {
        std::stack<std::map<std::string, int>> st;
        st.push({});
        int i = 0;
        int n = static_cast<int>(formula.size());
        while (i < n) {
            if (formula[i] == '(') {
                st.push({});
                ++i;
            } else if (formula[i] == ')') {
                ++i;
                int start = i;
                while (i < n && std::isdigit(static_cast<unsigned char>(formula[i]))) {
                    ++i;
                }
                int mult = start < i ? std::stoi(formula.substr(start, i - start)) : 1;
                auto top = st.top();
                st.pop();
                for (auto& [atom, count] : top) {
                    st.top()[atom] += count * mult;
                }
            } else {
                int start = i++;
                while (i < n && std::islower(static_cast<unsigned char>(formula[i]))) {
                    ++i;
                }
                std::string atom = formula.substr(start, i - start);
                start = i;
                while (i < n && std::isdigit(static_cast<unsigned char>(formula[i]))) {
                    ++i;
                }
                int count = start < i ? std::stoi(formula.substr(start, i - start)) : 1;
                st.top()[atom] += count;
            }
        }
        std::string result;
        for (auto& [atom, count] : st.top()) {
            result += atom;
            if (count > 1) {
                result += std::to_string(count);
            }
        }
        return result;
    }
};
