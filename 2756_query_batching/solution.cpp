// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/
// JS QueryBatcher design stand-in.

#include <functional>
#include <vector>

class QueryBatcher {
public:
    QueryBatcher(std::function<std::vector<int>(std::vector<int>)> queryMultiple, int t)
        : queryMultiple(std::move(queryMultiple)), t(t) {}

    void addQuery(int query, std::function<void(int)> resolve) {
        pending.push_back(query);
        resolvers.push_back(std::move(resolve));
    }

private:
    std::function<std::vector<int>(std::vector<int>)> queryMultiple;
    int t;
    std::vector<int> pending;
    std::vector<std::function<void(int)>> resolvers;
};
