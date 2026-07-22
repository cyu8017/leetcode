// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class ThroneInheritance {
    std::string king_;
    std::unordered_map<std::string, std::vector<std::string>> children_;
    std::unordered_set<std::string> dead_;

    void visit(const std::string& name, std::vector<std::string>& order) {
        if (!dead_.count(name)) {
            order.push_back(name);
        }
        for (const auto& child : children_[name]) {
            visit(child, order);
        }
    }

public:
    ThroneInheritance(std::string kingName) : king_(std::move(kingName)) {}

    void birth(std::string parentName, std::string childName) {
        children_[parentName].push_back(std::move(childName));
    }

    void death(std::string name) { dead_.insert(std::move(name)); }

    std::vector<std::string> getInheritanceOrder() {
        std::vector<std::string> order;
        visit(king_, order);
        return order;
    }
};
