// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

func minMutation(startGene string, endGene string, bank []string) int {
	if startGene == endGene {
		return 0
	}

	valid := make(map[string]struct{}, len(bank))
	for _, gene := range bank {
		valid[gene] = struct{}{}
	}
	if _, ok := valid[endGene]; !ok {
		return -1
	}

	genes := []byte("ACGT")
	type state struct {
		gene  string
		steps int
	}
	queue := []state{{startGene, 0}}
	visited := map[string]struct{}{startGene: {}}

	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]
		if current.gene == endGene {
			return current.steps
		}

		chars := []byte(current.gene)
		for index := range chars {
			original := chars[index]
			for _, letter := range genes {
				if letter == original {
					continue
				}
				chars[index] = letter
				candidate := string(chars)
				if _, ok := valid[candidate]; ok {
					if _, seen := visited[candidate]; !seen {
						visited[candidate] = struct{}{}
						queue = append(queue, state{candidate, current.steps + 1})
					}
				}
				chars[index] = original
			}
		}
	}

	return -1
}
