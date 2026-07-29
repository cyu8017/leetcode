// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

#include <cctype>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int evaluate(std::string expression) {
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
        std::vector<std::unordered_map<std::string, int>> env;
        return parse(env);
    }

private:
    std::vector<std::string> tokens_;
    int pos_ = 0;

    int parse(std::vector<std::unordered_map<std::string, int>>& env) {
        const std::string& token = tokens_[pos_];
        if (token != "(") {
            ++pos_;
            if (std::isdigit(static_cast<unsigned char>(token[0])) ||
                (token[0] == '-' && token.size() > 1)) {
                return std::stoi(token);
            }
            for (int i = static_cast<int>(env.size()) - 1; i >= 0; --i) {
                auto it = env[i].find(token);
                if (it != env[i].end()) {
                    return it->second;
                }
            }
            return 0;
        }

        ++pos_;
        std::string op = tokens_[pos_++];
        if (op == "let") {
            env.push_back({});
            while (tokens_[pos_] != ")") {
                if (tokens_[pos_] == "(" || tokens_[pos_ + 1] == ")") {
                    int value = parse(env);
                    ++pos_;
                    env.pop_back();
                    return value;
                }
                std::string var = tokens_[pos_++];
                env.back()[var] = parse(env);
            }
        }
        if (op == "add") {
            int left = parse(env);
            int right = parse(env);
            ++pos_;
            return left + right;
        }
        if (op == "mult") {
            int left = parse(env);
            int right = parse(env);
            ++pos_;
            return left * right;
        }
        return 0;
    }
};
