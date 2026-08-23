// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

#include <queue>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minMutation(std::string startGene, std::string endGene, std::vector<std::string>& bank) {
        if (startGene == endGene) {
            return 0;
        }

        std::unordered_set<std::string> valid(bank.begin(), bank.end());
        if (!valid.count(endGene)) {
            return -1;
        }

        const std::string genes = "ACGT";
        std::queue<std::pair<std::string, int>> queue;
        std::unordered_set<std::string> visited;
        queue.push({startGene, 0});
        visited.insert(startGene);

        while (!queue.empty()) {
            auto [gene, steps] = queue.front();
            queue.pop();
            if (gene == endGene) {
                return steps;
            }

            for (size_t index = 0; index < gene.size(); ++index) {
                char original = gene[index];
                for (char letter : genes) {
                    if (letter == original) {
                        continue;
                    }
                    std::string candidate = gene;
                    candidate[index] = letter;
                    if (valid.count(candidate) && !visited.count(candidate)) {
                        visited.insert(candidate);
                        queue.push({candidate, steps + 1});
                    }
                }
            }
        }

        return -1;
    }
};
