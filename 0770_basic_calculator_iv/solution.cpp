// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

#include <algorithm>
#include <cctype>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
    using Poly = std::map<std::vector<std::string>, int>;

public:
    std::vector<std::string> basicCalculatorIV(std::string expression, std::vector<std::string>& evalvars,
                                               std::vector<int>& evalints) {
        values_.clear();
        for (size_t i = 0; i < evalvars.size(); ++i) {
            values_[evalvars[i]] = evalints[i];
        }
        tokens_.clear();
        std::string cur;
        for (char ch : expression) {
            if (ch == '(' || ch == ')') {
                if (!cur.empty()) {
                    tokens_.push_back(cur);
                    cur.clear();
                }
                tokens_.push_back(std::string(1, ch));
            } else if (std::isspace(static_cast<unsigned char>(ch))) {
                if (!cur.empty()) {
                    tokens_.push_back(cur);
                    cur.clear();
                }
            } else {
                cur.push_back(ch);
            }
        }
        if (!cur.empty()) {
            tokens_.push_back(cur);
        }
        pos_ = 0;
        Poly poly = parseExpr();
        std::vector<std::pair<std::vector<std::string>, int>> keys(poly.begin(), poly.end());
        std::sort(keys.begin(), keys.end(), [](const auto& a, const auto& b) {
            if (a.first.size() != b.first.size()) {
                return a.first.size() > b.first.size();
            }
            return a.first < b.first;
        });
        std::vector<std::string> answer;
        for (const auto& [key, coef] : keys) {
            if (coef == 0) {
                continue;
            }
            if (key.empty()) {
                answer.push_back(std::to_string(coef));
            } else {
                std::string term = std::to_string(coef);
                for (const std::string& var : key) {
                    term += "*" + var;
                }
                answer.push_back(term);
            }
        }
        return answer;
    }

private:
    std::unordered_map<std::string, int> values_;
    std::vector<std::string> tokens_;
    int pos_ = 0;

    Poly parseExpr() {
        Poly poly = parseTerm();
        while (pos_ < static_cast<int>(tokens_.size()) &&
               (tokens_[pos_] == "+" || tokens_[pos_] == "-")) {
            std::string op = tokens_[pos_++];
            Poly right = parseTerm();
            poly = add(poly, op == "+" ? right : negate(right));
        }
        return poly;
    }

    Poly parseTerm() {
        Poly poly = parseFactor();
        while (pos_ < static_cast<int>(tokens_.size()) && tokens_[pos_] == "*") {
            ++pos_;
            poly = mul(poly, parseFactor());
        }
        return poly;
    }

    Poly parseFactor() {
        if (tokens_[pos_] == "(") {
            ++pos_;
            Poly poly = parseExpr();
            ++pos_;
            return poly;
        }
        return atom(tokens_[pos_++]);
    }

    Poly atom(const std::string& token) {
        Poly poly;
        if (std::isalpha(static_cast<unsigned char>(token[0]))) {
            auto it = values_.find(token);
            if (it != values_.end()) {
                poly[{}] = it->second;
            } else {
                poly[{token}] = 1;
            }
        } else {
            poly[{}] = std::stoi(token);
        }
        return clean(poly);
    }

    Poly add(const Poly& left, const Poly& right) {
        Poly result = left;
        for (const auto& [key, coef] : right) {
            result[key] += coef;
        }
        return clean(result);
    }

    Poly negate(const Poly& poly) {
        Poly result;
        for (const auto& [key, coef] : poly) {
            result[key] = -coef;
        }
        return result;
    }

    Poly mul(const Poly& left, const Poly& right) {
        Poly result;
        for (const auto& [lk, lv] : left) {
            for (const auto& [rk, rv] : right) {
                std::vector<std::string> key = lk;
                key.insert(key.end(), rk.begin(), rk.end());
                std::sort(key.begin(), key.end());
                result[key] += lv * rv;
            }
        }
        return clean(result);
    }

    Poly clean(Poly poly) {
        for (auto it = poly.begin(); it != poly.end();) {
            if (it->second == 0) {
                it = poly.erase(it);
            } else {
                ++it;
            }
        }
        return poly;
    }
};
