"""Port JavaScript implementations for LeetCode problems 1463 through 1499."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SOLUTIONS = {
    "1463_cherry_pickup_ii": r"""var cherryPickup = function(grid) {
    const rows = grid.length, cols = grid[0].length;
    let dp = new Map([[`0,${cols - 1}`, grid[0][0] + (cols > 1 ? grid[0][cols - 1] : 0)]]);
    for (let r = 1; r < rows; r++) {
        const next = new Map();
        for (const [key, score] of dp) {
            const [a, b] = key.split(',').map(Number);
            for (let na = a - 1; na <= a + 1; na++) for (let nb = b - 1; nb <= b + 1; nb++) {
                if (na < 0 || nb < 0 || na >= cols || nb >= cols) continue;
                const state = `${na},${nb}`;
                const value = score + grid[r][na] + (na === nb ? 0 : grid[r][nb]);
                next.set(state, Math.max(next.get(state) ?? -Infinity, value));
            }
        }
        dp = next;
    }
    return Math.max(...dp.values());
};""",
    "1464_maximum_product_of_two_elements_in_an_array": r"""var maxProduct = function(nums) {
    let first = 0, second = 0;
    for (const value of nums) {
        if (value >= first) [first, second] = [value, first];
        else if (value > second) second = value;
    }
    return (first - 1) * (second - 1);
};""",
    "1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts": r"""var maxArea = function(h, w, horizontalCuts, verticalCuts) {
    const largestGap = (cuts, end) => {
        cuts.sort((a, b) => a - b);
        let best = cuts[0], previous = 0;
        for (const cut of cuts) {
            best = Math.max(best, cut - previous);
            previous = cut;
        }
        return Math.max(best, end - previous);
    };
    const mod = 1000000007n;
    return Number((BigInt(largestGap(horizontalCuts, h)) * BigInt(largestGap(verticalCuts, w))) % mod);
};""",
    "1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero": r"""var minReorder = function(n, connections) {
    const graph = Array.from({ length: n }, () => []);
    for (const [from, to] of connections) {
        graph[from].push([to, 1]);
        graph[to].push([from, 0]);
    }
    let changes = 0;
    const seen = new Set([0]), stack = [0];
    while (stack.length) {
        const node = stack.pop();
        for (const [next, cost] of graph[node]) if (!seen.has(next)) {
            seen.add(next);
            changes += cost;
            stack.push(next);
        }
    }
    return changes;
};""",
    "1467_probability_of_a_two_boxes_having_the_same_number_of_distinct_balls": r"""var getProbability = function(balls) {
    const half = balls.reduce((sum, value) => sum + value, 0) / 2;
    const choose = (n, k) => {
        k = Math.min(k, n - k);
        let result = 1;
        for (let i = 1; i <= k; i++) result = result * (n - k + i) / i;
        return result;
    };
    let good = 0, total = 0;
    const dfs = (index, leftCount, distinctDifference, ways) => {
        if (index === balls.length) {
            if (leftCount === half) {
                total += ways;
                if (distinctDifference === 0) good += ways;
            }
            return;
        }
        for (let left = 0; left <= balls[index] && leftCount + left <= half; left++) {
            dfs(index + 1, leftCount + left,
                distinctDifference + (left > 0 ? 1 : 0) - (left < balls[index] ? 1 : 0),
                ways * choose(balls[index], left));
        }
    };
    dfs(0, 0, 0, 1);
    return good / total;
};""",
    "1469_find_all_the_lonely_nodes": r"""var getLonelyNodes = function(root) {
    if (!root) return [];
    const result = [], stack = [root];
    while (stack.length) {
        const node = stack.pop();
        if (node.left) {
            if (!node.right) result.push(node.left.val);
            stack.push(node.left);
        }
        if (node.right) {
            if (!node.left) result.push(node.right.val);
            stack.push(node.right);
        }
    }
    return result;
};""",
    "1470_shuffle_the_array": r"""var shuffle = function(nums, n) {
    const result = [];
    for (let i = 0; i < n; i++) result.push(nums[i], nums[i + n]);
    return result;
};""",
    "1471_the_k_strongest_values_in_an_array": r"""var getStrongest = function(arr, k) {
    arr.sort((a, b) => a - b);
    const median = arr[Math.floor((arr.length - 1) / 2)];
    arr.sort((a, b) => Math.abs(b - median) - Math.abs(a - median) || b - a);
    return arr.slice(0, k);
};""",
    "1472_design_browser_history": r"""var BrowserHistory = function(homepage) {
    this.history = [homepage];
    this.index = 0;
};

BrowserHistory.prototype.visit = function(url) {
    this.history.length = this.index + 1;
    this.history.push(url);
    this.index++;
};

BrowserHistory.prototype.back = function(steps) {
    this.index = Math.max(0, this.index - steps);
    return this.history[this.index];
};

BrowserHistory.prototype.forward = function(steps) {
    this.index = Math.min(this.history.length - 1, this.index + steps);
    return this.history[this.index];
};""",
    "1473_paint_house_iii": r"""var minCost = function(houses, cost, m, n, target) {
    const inf = Infinity;
    let dp = Array.from({ length: n + 1 }, () => Array(target + 1).fill(inf));
    dp[0][0] = 0;
    for (let i = 0; i < m; i++) {
        const next = Array.from({ length: n + 1 }, () => Array(target + 1).fill(inf));
        for (let previous = 0; previous <= n; previous++) for (let groups = 0; groups <= target; groups++) {
            if (dp[previous][groups] === inf) continue;
            const colors = houses[i] ? [houses[i]] : Array.from({ length: n }, (_, c) => c + 1);
            for (const color of colors) {
                const newGroups = groups + (color !== previous ? 1 : 0);
                if (newGroups <= target) {
                    next[color][newGroups] = Math.min(next[color][newGroups],
                        dp[previous][groups] + (houses[i] ? 0 : cost[i][color - 1]));
                }
            }
        }
        dp = next;
    }
    const answer = Math.min(...dp.map(row => row[target]));
    return answer === inf ? -1 : answer;
};""",
    "1474_delete_n_nodes_after_m_nodes_of_a_linked_list": r"""var deleteNodes = function(head, m, n) {
    let current = head;
    while (current) {
        for (let kept = 1; kept < m && current; kept++) current = current.next;
        if (!current) break;
        let removed = current.next;
        for (let count = 0; count < n && removed; count++) removed = removed.next;
        current.next = removed;
        current = removed;
    }
    return head;
};""",
    "1475_final_prices_with_a_special_discount_in_a_shop": r"""var finalPrices = function(prices) {
    const stack = [];
    for (let i = 0; i < prices.length; i++) {
        while (stack.length && prices[stack[stack.length - 1]] >= prices[i]) {
            prices[stack.pop()] -= prices[i];
        }
        stack.push(i);
    }
    return prices;
};""",
    "1476_subrectangle_queries": r"""var SubrectangleQueries = function(rectangle) {
    this.rectangle = rectangle;
};

SubrectangleQueries.prototype.updateSubrectangle = function(row1, col1, row2, col2, newValue) {
    for (let row = row1; row <= row2; row++) {
        for (let col = col1; col <= col2; col++) this.rectangle[row][col] = newValue;
    }
};

SubrectangleQueries.prototype.getValue = function(row, col) {
    return this.rectangle[row][col];
};""",
    "1477_find_two_non_overlapping_sub_arrays_each_with_target_sum": r"""var minSumOfLengths = function(arr, target) {
    const inf = Infinity, shortest = Array(arr.length).fill(inf);
    let left = 0, sum = 0, best = inf, answer = inf;
    for (let right = 0; right < arr.length; right++) {
        sum += arr[right];
        while (sum > target) sum -= arr[left++];
        if (sum === target) {
            const length = right - left + 1;
            if (left > 0) answer = Math.min(answer, length + shortest[left - 1]);
            best = Math.min(best, length);
        }
        shortest[right] = best;
    }
    return answer === inf ? -1 : answer;
};""",
    "1478_allocate_mailboxes": r"""var minDistance = function(houses, k) {
    houses.sort((a, b) => a - b);
    const n = houses.length, cost = Array.from({ length: n }, () => Array(n).fill(0));
    for (let start = 0; start < n; start++) for (let end = start; end < n; end++) {
        const median = houses[Math.floor((start + end) / 2)];
        for (let i = start; i <= end; i++) cost[start][end] += Math.abs(houses[i] - median);
    }
    let dp = Array(n + 1).fill(Infinity);
    dp[0] = 0;
    for (let mailbox = 0; mailbox < k; mailbox++) {
        const next = Array(n + 1).fill(Infinity);
        next[0] = 0;
        for (let end = 1; end <= n; end++) {
            for (let start = 0; start < end; start++) {
                next[end] = Math.min(next[end], dp[start] + cost[start][end - 1]);
            }
        }
        dp = next;
    }
    return dp[n];
};""",
    "1480_running_sum_of_1d_array": r"""var runningSum = function(nums) {
    for (let i = 1; i < nums.length; i++) nums[i] += nums[i - 1];
    return nums;
};""",
    "1481_least_number_of_unique_integers_after_k_removals": r"""var findLeastNumOfUniqueInts = function(arr, k) {
    const frequencies = new Map();
    for (const value of arr) frequencies.set(value, (frequencies.get(value) || 0) + 1);
    const counts = [...frequencies.values()].sort((a, b) => a - b);
    let remaining = counts.length;
    for (const count of counts) {
        if (k < count) break;
        k -= count;
        remaining--;
    }
    return remaining;
};""",
    "1482_minimum_number_of_days_to_make_m_bouquets": r"""var minDays = function(bloomDay, m, k) {
    if (m * k > bloomDay.length) return -1;
    const canMake = day => {
        let bouquets = 0, flowers = 0;
        for (const bloom of bloomDay) {
            flowers = bloom <= day ? flowers + 1 : 0;
            if (flowers === k) {
                bouquets++;
                flowers = 0;
            }
        }
        return bouquets >= m;
    };
    let low = Math.min(...bloomDay), high = Math.max(...bloomDay);
    while (low < high) {
        const middle = Math.floor((low + high) / 2);
        if (canMake(middle)) high = middle;
        else low = middle + 1;
    }
    return low;
};""",
    "1483_kth_ancestor_of_a_tree_node": r"""var TreeAncestor = function(n, parent) {
    this.up = [parent.slice()];
    const width = Math.max(1, Math.ceil(Math.log2(Math.max(2, n))) + 1);
    for (let bit = 1; bit < width; bit++) {
        const previous = this.up[bit - 1];
        this.up.push(previous.map(node => node === -1 ? -1 : previous[node]));
    }
};

TreeAncestor.prototype.getKthAncestor = function(node, k) {
    let bit = 0;
    while (k && node !== -1) {
        if (k & 1) {
            if (bit === this.up.length) return -1;
            node = this.up[bit][node];
        }
        k >>= 1;
        bit++;
    }
    return node;
};""",
    "1485_clone_binary_tree_with_random_pointer": r"""var copyRandomBinaryTree = function(root) {
    const copies = new Map();
    const clone = node => {
        if (!node) return null;
        if (!copies.has(node)) {
            const copy = new Node(node.val);
            copies.set(node, copy);
            copy.left = clone(node.left);
            copy.right = clone(node.right);
            copy.random = clone(node.random);
        }
        return copies.get(node);
    };
    return clone(root);
};""",
    "1486_xor_operation_in_an_array": r"""var xorOperation = function(n, start) {
    let value = 0;
    for (let i = 0; i < n; i++) value ^= start + 2 * i;
    return value;
};""",
    "1487_making_file_names_unique": r"""var getFolderNames = function(names) {
    const used = new Map(), result = [];
    for (const name of names) {
        if (!used.has(name)) {
            used.set(name, 1);
            result.push(name);
            continue;
        }
        let suffix = used.get(name);
        while (used.has(`${name}(${suffix})`)) suffix++;
        const unique = `${name}(${suffix})`;
        used.set(name, suffix + 1);
        used.set(unique, 1);
        result.push(unique);
    }
    return result;
};""",
    "1488_avoid_flood_in_the_city": r"""var avoidFlood = function(rains) {
    const answer = Array(rains.length).fill(-1), full = new Map(), dryDays = [], parent = [];
    const find = index => {
        if (index === parent.length) return index;
        if (parent[index] === index) return index;
        parent[index] = find(parent[index]);
        return parent[index];
    };
    const lowerBound = value => {
        let low = 0, high = dryDays.length;
        while (low < high) {
            const middle = Math.floor((low + high) / 2);
            if (dryDays[middle] <= value) low = middle + 1;
            else high = middle;
        }
        return low;
    };
    for (let day = 0; day < rains.length; day++) {
        const lake = rains[day];
        if (lake === 0) {
            answer[day] = 1;
            parent[dryDays.length] = dryDays.length;
            dryDays.push(day);
        } else {
            if (full.has(lake)) {
                const position = find(lowerBound(full.get(lake)));
                if (position === dryDays.length) return [];
                answer[dryDays[position]] = lake;
                parent[position] = find(position + 1);
            }
            full.set(lake, day);
        }
    }
    return answer;
};""",
    "1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree": r"""var findCriticalAndPseudoCriticalEdges = function(n, edges) {
    const sorted = edges.map((edge, index) => [...edge, index]).sort((a, b) => a[2] - b[2]);
    const mst = (skip = -1, force = -1) => {
        const parent = Array.from({ length: n }, (_, i) => i);
        const find = node => parent[node] === node ? node : parent[node] = find(parent[node]);
        let total = 0, used = 0;
        const join = edge => {
            const [from, to, weight] = sorted[edge], a = find(from), b = find(to);
            if (a === b) return;
            parent[a] = b;
            total += weight;
            used++;
        };
        if (force !== -1) join(force);
        for (let i = 0; i < sorted.length; i++) if (i !== skip && i !== force) join(i);
        return used === n - 1 ? total : Infinity;
    };
    const baseline = mst(), critical = [], pseudo = [];
    for (let i = 0; i < sorted.length; i++) {
        if (mst(i) > baseline) critical.push(sorted[i][3]);
        else if (mst(-1, i) === baseline) pseudo.push(sorted[i][3]);
    }
    return [critical.sort((a, b) => a - b), pseudo.sort((a, b) => a - b)];
};""",
    "1490_clone_n_ary_tree": r"""var cloneTree = function(root) {
    if (!root) return null;
    return new Node(root.val, root.children.map(cloneTree));
};""",
    "1491_average_salary_excluding_the_minimum_and_maximum_salary": r"""var average = function(salary) {
    let total = 0, minimum = Infinity, maximum = -Infinity;
    for (const value of salary) {
        total += value;
        minimum = Math.min(minimum, value);
        maximum = Math.max(maximum, value);
    }
    return (total - minimum - maximum) / (salary.length - 2);
};""",
    "1492_the_kth_factor_of_n": r"""var kthFactor = function(n, k) {
    for (let factor = 1; factor <= n; factor++) {
        if (n % factor === 0 && --k === 0) return factor;
    }
    return -1;
};""",
    "1493_longest_subarray_of_1s_after_deleting_one_element": r"""var longestSubarray = function(nums) {
    let left = 0, zeros = 0, best = 0;
    for (let right = 0; right < nums.length; right++) {
        if (nums[right] === 0) zeros++;
        while (zeros > 1) if (nums[left++] === 0) zeros--;
        best = Math.max(best, right - left);
    }
    return best;
};""",
    "1494_parallel_courses_ii": r"""var minNumberOfSemesters = function(n, relations, k) {
    const prereq = Array(n).fill(0), full = (1 << n) - 1, dp = Array(1 << n).fill(Infinity);
    for (const [before, after] of relations) prereq[after - 1] |= 1 << (before - 1);
    dp[0] = 0;
    const bitCount = value => {
        let count = 0;
        while (value) {
            value &= value - 1;
            count++;
        }
        return count;
    };
    for (let mask = 0; mask <= full; mask++) {
        if (dp[mask] === Infinity) continue;
        let available = 0;
        for (let course = 0; course < n; course++) {
            if (!(mask & (1 << course)) && (prereq[course] & mask) === prereq[course]) available |= 1 << course;
        }
        if (bitCount(available) <= k) dp[mask | available] = Math.min(dp[mask | available], dp[mask] + 1);
        else for (let subset = available; subset; subset = (subset - 1) & available) {
            if (bitCount(subset) === k) dp[mask | subset] = Math.min(dp[mask | subset], dp[mask] + 1);
        }
    }
    return dp[full];
};""",
    "1496_path_crossing": r"""var isPathCrossing = function(path) {
    let x = 0, y = 0;
    const visited = new Set(['0,0']);
    const moves = { N: [0, 1], S: [0, -1], E: [1, 0], W: [-1, 0] };
    for (const direction of path) {
        x += moves[direction][0];
        y += moves[direction][1];
        const location = `${x},${y}`;
        if (visited.has(location)) return true;
        visited.add(location);
    }
    return false;
};""",
    "1497_check_if_array_pairs_are_divisible_by_k": r"""var canArrange = function(arr, k) {
    const count = Array(k).fill(0);
    for (const value of arr) count[((value % k) + k) % k]++;
    if (count[0] % 2) return false;
    for (let remainder = 1; remainder < k; remainder++) {
        if (count[remainder] !== count[k - remainder]) return false;
    }
    return true;
};""",
    "1498_number_of_subsequences_that_satisfy_the_given_sum_condition": r"""var numSubseq = function(nums, target) {
    const mod = 1000000007;
    nums.sort((a, b) => a - b);
    const powers = [1];
    for (let i = 1; i < nums.length; i++) powers.push((powers[i - 1] * 2) % mod);
    let left = 0, right = nums.length - 1, answer = 0;
    while (left <= right) {
        if (nums[left] + nums[right] <= target) answer = (answer + powers[right - left++]) % mod;
        else right--;
    }
    return answer;
};""",
    "1499_max_value_of_equation": r"""var findMaxValueOfEquation = function(points, k) {
    const deque = [];
    let head = 0, answer = -Infinity;
    for (const [x, y] of points) {
        while (head < deque.length && x - deque[head][0] > k) head++;
        if (head < deque.length) answer = Math.max(answer, x + y + deque[head][1]);
        const value = y - x;
        while (deque.length > head && deque[deque.length - 1][1] <= value) deque.pop();
        deque.push([x, value]);
    }
    return answer;
};""",
}


def main() -> int:
    written, failures = 0, []
    for folder, implementation in SOLUTIONS.items():
        destination = ROOT / folder / "solution.js"
        try:
            destination.write_text(implementation + "\n", encoding="utf-8")
            written += 1
        except OSError as error:
            failures.append(f"{folder}: {error}")
    print(f"Written: {written}")
    if failures:
        print("Failures:")
        print("\n".join(failures))
        return 1
    print("Failures: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
