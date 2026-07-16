// LeetCode 0133 - Clone Graph
#include <unordered_map>
#include <vector>
using namespace std;
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() : val(0) {}
    Node(int value) : val(value) {}
};
class Solution {
    unordered_map<Node*, Node*> copies;
    Node* dfs(Node* node) {
        if (copies.count(node)) return copies[node];
        Node* copy = new Node(node->val);
        copies[node] = copy;
        for (Node* neighbor : node->neighbors) copy->neighbors.push_back(dfs(neighbor));
        return copy;
    }
public:
    Node* cloneGraph(Node* node) { return node ? dfs(node) : nullptr; }
};