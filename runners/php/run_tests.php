<?php
declare(strict_types=1);

class MockRobot {
    /** @var array<int, array<int, int>> */
    public array $room;
    public int $row;
    public int $col;
    public int $direction = 0;
    /** @var array<string, bool> */
    public array $cleaned = [];
    /** @var array<int, array{0: int, 1: int}> */
    private array $directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];

    /**
     * @param array<int, array<int, int>> $room
     */
    public function __construct(array $room, int $row, int $col) {
        $this->room = $room;
        $this->row = $row;
        $this->col = $col;
    }

    public function move(): bool {
        [$dr, $dc] = $this->directions[$this->direction];
        $nextRow = $this->row + $dr;
        $nextCol = $this->col + $dc;
        if ($nextRow >= 0 && $nextRow < count($this->room) && $nextCol >= 0 && $nextCol < count($this->room[0]) && $this->room[$nextRow][$nextCol] === 1) {
            $this->row = $nextRow;
            $this->col = $nextCol;
            return true;
        }
        return false;
    }

    public function turnLeft(): void {
        $this->direction = ($this->direction + 3) % 4;
    }

    public function turnRight(): void {
        $this->direction = ($this->direction + 1) % 4;
    }

    public function clean(): void {
        $this->cleaned["{$this->row},{$this->col}"] = true;
    }
}

function robotCleanedAll(MockRobot $robot): bool {
    foreach ($robot->room as $r => $row) {
        foreach ($row as $c => $cell) {
            if ($cell === 1 && !isset($robot->cleaned["{$r},{$c}"])) {
                return false;
            }
        }
    }
    return true;
}

function listToListNode(?array $values): ?object {
    if ($values === null || count($values) === 0) {
        return null;
    }
    $head = (object)['val' => $values[0], 'next' => null];
    $current = $head;
    for ($i = 1; $i < count($values); $i++) {
        $current->next = (object)['val' => $values[$i], 'next' => null];
        $current = $current->next;
    }
    return $head;
}

function listNodeToList(?object $node): array {
    $result = [];
    while ($node !== null) {
        $result[] = $node->val;
        $node = $node->next;
    }
    return $result;
}

function listToTree(?array $values): ?object {
    if ($values === null || count($values) === 0) {
        return null;
    }
    $root = (object)['val' => $values[0], 'left' => null, 'right' => null];
    $queue = [$root];
    $index = 1;
    while (count($queue) > 0 && $index < count($values)) {
        $node = array_shift($queue);
        if ($index < count($values)) {
            if ($values[$index] !== null) {
                $node->left = (object)['val' => $values[$index], 'left' => null, 'right' => null];
                $queue[] = $node->left;
            }
            $index++;
        }
        if ($index < count($values)) {
            if ($values[$index] !== null) {
                $node->right = (object)['val' => $values[$index], 'left' => null, 'right' => null];
                $queue[] = $node->right;
            }
            $index++;
        }
    }
    return $root;
}

function listToParentTree(?array $values): ?object {
    if ($values === null || count($values) === 0) {
        return null;
    }
    $root = (object)['val' => $values[0], 'left' => null, 'right' => null, 'parent' => null];
    $queue = [$root];
    $index = 1;
    while (count($queue) > 0 && $index < count($values)) {
        $node = array_shift($queue);
        if ($index < count($values)) {
            if ($values[$index] !== null) {
                $node->left = (object)['val' => $values[$index], 'left' => null, 'right' => null, 'parent' => $node];
                $queue[] = $node->left;
            }
            $index++;
        }
        if ($index < count($values)) {
            if ($values[$index] !== null) {
                $node->right = (object)['val' => $values[$index], 'left' => null, 'right' => null, 'parent' => $node];
                $queue[] = $node->right;
            }
            $index++;
        }
    }
    return $root;
}

function findParentNode(?object $root, int $val): ?object {
    if ($root === null) {
        return null;
    }
    if ($root->val === $val) {
        return $root;
    }
    $left = findParentNode($root->left, $val);
    if ($left !== null) {
        return $left;
    }
    return findParentNode($root->right, $val);
}

function treeToList(?object $root): array {
    if ($root === null) {
        return [];
    }
    $result = [];
    $queue = [$root];
    while (count($queue) > 0) {
        $node = array_shift($queue);
        if ($node === null) {
            $result[] = null;
            continue;
        }
        $result[] = $node->val;
        $queue[] = $node->left;
        $queue[] = $node->right;
    }
    while (count($result) > 0 && $result[count($result) - 1] === null) {
        array_pop($result);
    }
    return $result;
}

function listToNary(?array $values): ?object {
    if ($values === null || count($values) === 0) {
        return null;
    }
    $root = (object)['val' => $values[0], 'children' => []];
    $parents = [$root];
    $index = 1;
    if ($index < count($values) && $values[$index] === null) {
        $index++;
    }
    while (count($parents) > 0) {
        $nextParents = [];
        $parentIndex = 0;
        while ($index < count($values) && $values[$index] === null) {
            $index++;
        }
        while ($parentIndex < count($parents) && $index < count($values)) {
            $parent = $parents[$parentIndex];
            $segment = [];
            while ($index < count($values) && $values[$index] !== null) {
                $segment[] = $values[$index];
                $index++;
            }
            foreach ($segment as $value) {
                $child = (object)['val' => $value, 'children' => []];
                $parent->children[] = $child;
                $nextParents[] = $child;
            }
            $parentIndex++;
            if ($index < count($values) && $values[$index] === null) {
                $index++;
                if ($index < count($values) && $values[$index] === null) {
                    $index++;
                    $parentIndex = count($parents);
                    break;
                }
            }
        }
        $parents = $nextParents;
    }
    return $root;
}

function naryToList(?object $root): array {
    if ($root === null) {
        return [];
    }
    $result = [$root->val];
    $parents = [$root];
    while (count($parents) > 0) {
        $nextParents = [];
        $segments = [];
        foreach ($parents as $parent) {
            $segment = [];
            foreach ($parent->children as $child) {
                $segment[] = $child->val;
            }
            $segments[] = $segment;
            foreach ($parent->children as $child) {
                $nextParents[] = $child;
            }
        }
        if (count($nextParents) === 0) {
            break;
        }
        $padding = 0;
        foreach ($segments as $segment) {
            if (count($segment) === 0) {
                $padding++;
            } else {
                break;
            }
        }
        for ($i = 0; $i < $padding; $i++) {
            $result[] = null;
        }
        foreach ($segments as $segmentIndex => $segment) {
            if ($segmentIndex < $padding) {
                continue;
            }
            if (count($segment) > 0) {
                foreach ($segment as $value) {
                    $result[] = $value;
                }
            }
            if ($segmentIndex < count($segments) - 1) {
                $result[] = null;
            }
        }
        $parents = $nextParents;
    }
    return $result;
}

function naryTreesEqual(?object $left, ?object $right): bool {
    if ($left === null && $right === null) {
        return true;
    }
    if ($left === null || $right === null) {
        return false;
    }
    if ($left->val !== $right->val || count($left->children) !== count($right->children)) {
        return false;
    }
    foreach ($left->children as $index => $child) {
        if (!naryTreesEqual($child, $right->children[$index])) {
            return false;
        }
    }
    return true;
}

function quadTreeToList(?object $root): array {
    if ($root === null) {
        return [];
    }
    $result = [];
    $queue = [$root];
    while (count($queue) > 0) {
        $node = array_shift($queue);
        if ($node === null) {
            $result[] = null;
            continue;
        }
        $result[] = [(int)$node->isLeaf, (int)$node->val];
        if ($node->isLeaf) {
            array_push($queue, null, null, null, null);
        } else {
            $queue[] = $node->topLeft;
            $queue[] = $node->topRight;
            $queue[] = $node->bottomLeft;
            $queue[] = $node->bottomRight;
        }
    }
    while (count($result) > 0 && $result[count($result) - 1] === null) {
        array_pop($result);
    }
    return $result;
}

function splitMultilevelRows(array $values): array {
    $rows = [];
    $index = 0;
    $length = count($values);
    while ($index < $length) {
        $row = [];
        while ($index < $length && $values[$index] !== null) {
            $row[] = $index;
            $index++;
        }
        if (count($row) > 0) {
            $rows[] = $row;
        }
        if ($index < $length && $values[$index] === null) {
            $index++;
        }
        while ($index < $length && $values[$index] === null) {
            $index++;
        }
    }
    return $rows;
}

function listToMultilevel(array $values): ?object {
    if (count($values) === 0) {
        return null;
    }
    $nodes = [];
    foreach ($values as $nodeIndex => $value) {
        if ($value !== null) {
            $nodes[$nodeIndex] = (object)['val' => $value, 'prev' => null, 'next' => null, 'child' => null];
        }
    }
    $rows = splitMultilevelRows($values);
    foreach ($rows as $row) {
        foreach ($row as $position => $nodeIndex) {
            $node = $nodes[$nodeIndex];
            if ($position > 0) {
                $previousIndex = $row[$position - 1];
                $node->prev = $nodes[$previousIndex];
                $nodes[$previousIndex]->next = $node;
            }
        }
    }
    for ($rowIndex = 0; $rowIndex < count($rows) - 1; $rowIndex++) {
        $parentRow = $rows[$rowIndex];
        $childRow = $rows[$rowIndex + 1];
        $padding = $childRow[0] - $parentRow[count($parentRow) - 1] - 2;
        if ($padding < 0) {
            $padding = 0;
        }
        if ($padding < count($parentRow)) {
            $nodes[$parentRow[$padding]]->child = $nodes[$childRow[0]];
        }
    }
    return $nodes[$rows[0][0]];
}

function multilevelToList(?object $head): array {
    $result = [];
    $current = $head;
    while ($current !== null) {
        $result[] = $current->val;
        $current = $current->next;
    }
    return $result;
}

function doublyTreeNodeToList(?object $head): array {
    if ($head === null) {
        return [];
    }
    $result = [];
    $node = $head;
    $start = $head;
    while (true) {
        $result[] = $node->val;
        if ($node->right === null || $node->right === $start) {
            break;
        }
        $node = $node->right;
    }
    return $result;
}

function convertArg(mixed $value, ?string $typeName): mixed {
    if ($typeName === 'listnode') {
        return listToListNode($value);
    }
    if ($typeName === 'treenode') {
        return listToTree($value);
    }
    if ($typeName === 'narynode') {
        return listToNary($value);
    }
    if ($typeName === 'multilevelnode') {
        return listToMultilevel($value);
    }
    return $value;
}

function convertResult(mixed $value, ?string $typeName): mixed {
    if ($typeName === 'listnode') {
        return listNodeToList($value);
    }
    if ($typeName === 'treenode') {
        return treeToList($value);
    }
    if ($typeName === 'narynode') {
        return naryToList($value);
    }
    if ($typeName === 'quadnode') {
        return quadTreeToList($value);
    }
    if ($typeName === 'multilevelnode') {
        return multilevelToList($value);
    }
    if ($typeName === 'doublytreenode') {
        return doublyTreeNodeToList($value);
    }
    return $value;
}

function isInplaceExpected($expected): bool {
    return is_string($expected) && (str_contains($expected, ', nums = [') || str_contains($expected, ', chars = ['));
}

function parseInplaceExpected(string $expected): ?array {
    if (!preg_match('/^(\d+),\s*(nums|chars)\s*=\s*\[(.*)\]$/', trim($expected), $match)) {
        return null;
    }
    $count = (int)$match[1];
    $field = $match[2];
    $raw = $match[3];
    if ($field === 'chars') {
        preg_match_all('/"([^"]*)"|\'([^\']*)\'/', $raw, $tokens, PREG_SET_ORDER);
        $prefix = array_map(fn($token) => $token[1] !== '' ? $token[1] : $token[2], $tokens);
        return [$count, $prefix];
    }
    $prefix = [];
    foreach (explode(',', $raw) as $token) {
        $token = trim($token);
        if ($token === '' || $token === '_') {
            continue;
        }
        $prefix[] = (int)$token;
    }
    return [$count, $prefix];
}

function deepEqualDesign($actual, $expected): bool {
    if (is_array($actual) && is_array($expected)) {
        if (count($actual) !== count($expected)) {
            return false;
        }
        foreach ($actual as $index => $value) {
            if (!deepEqualDesign($value, $expected[$index])) {
                return false;
            }
        }
        return true;
    }
    if (is_float($actual) || is_float($expected) || is_int($actual) || is_int($expected)) {
        return abs((float)$actual - (float)$expected) < 1e-5;
    }
    return $actual == $expected;
}

function runDesignCases(array $casesDoc): array {
    $passed = 0;
    foreach ($casesDoc['cases'] as $index => $case) {
        $operations = $case['operations'];
        $arguments = $case['arguments'];
        $expected = $case['expected'];
        $instance = null;
        $ok = true;

        if (isset($case['randomUniformSequence'])) {
            $sequence = $case['randomUniformSequence'];
            $position = 0;
            set_uniform(function () use (&$sequence, &$position) {
                $value = $sequence[$position];
                $position++;
                return $value;
            });
        }

        foreach ($operations as $opIndex => $operation) {
            $callArgs = $arguments[$opIndex] ?? [];
            if ($opIndex === 0) {
                $instance = empty($callArgs) ? new $operation() : new $operation(...$callArgs);
                $result = null;
            } else {
                $result = empty($callArgs) ? $instance->$operation() : $instance->$operation(...$callArgs);
            }

            if (!deepEqualDesign($result, $expected[$opIndex])) {
                $ok = false;
                echo '  FAIL case ' . ($index + 1) . ' step ' . ($opIndex + 1) . ': expected '
                    . json_encode($expected[$opIndex]) . ', got ' . json_encode($result) . "\n";
                break;
            }
        }

        if ($ok) {
            $passed++;
            echo '  PASS case ' . ($index + 1) . "\n";
        }
    }

    return [$passed, count($casesDoc['cases'])];
}

$problemDir = realpath($argv[1]);
$config = json_decode(file_get_contents($problemDir . '/tests/config.json'), true);
$casesDoc = json_decode(file_get_contents($problemDir . '/tests/cases.json'), true);
$cases = $casesDoc['cases'] ?? [];

if (count($cases) === 0) {
    echo 'PHP tests: ' . basename($problemDir) . "\n";
    echo "  no test cases defined in tests/cases.json\n";
    exit(4);
}

$kind = $config['kind'] ?? ($cases[0]['kind'] ?? 'standard');
if (in_array($kind, ['sql', 'shell'], true)) {
    echo 'PHP tests: ' . basename($problemDir) . "\n";
    if (($config['runnable'] ?? null) === false) {
        echo "  SKIP kind={$kind} (runner not implemented)\n";
        exit(0);
    }
    echo "  kind={$kind} requires a runner but none is configured\n";
    exit(2);
}
if ($kind === 'design') {
    if (!file_exists($problemDir . '/solution.php')) {
        echo 'PHP tests: ' . basename($problemDir) . "\n";
        echo "  missing solution file for php\n";
        exit(2);
    }

    require $problemDir . '/solution.php';
    $designClass = $config['class'] ?? $cases[0]['operations'][0];
    echo 'PHP design tests: ' . basename($problemDir) . " :: {$designClass}\n";
    [$passed, $total] = runDesignCases($casesDoc);
    echo "Result: {$passed}/{$total} passed\n";
    exit($passed === $total ? 0 : 1);
}

if (!file_exists($problemDir . '/solution.php')) {
    echo 'PHP tests: ' . basename($problemDir) . "\n";
    echo "  missing solution file for php\n";
    exit(2);
}

require $problemDir . '/solution.php';

$className = $config['class'] ?? 'Solution';
$method = $config['method'];
$argTypes = $config['types'] ?? [];
$paramOrder = $config['paramOrder'] ?? [];

echo 'PHP tests: ' . basename($problemDir) . " :: {$method}()\n";

$passed = 0;
foreach ($casesDoc['cases'] as $index => $case) {
    $args = $case['args'] ?? [];
    $expected = $case['expected'];
    $actual = null;
    $converted = null;
    $naryTreeCompare = false;
    $keys = count($paramOrder) > 0 ? $paramOrder : array_keys($args);

    if (($config['class'] ?? null) === 'Codec' && (isset($args['url']) || isset($args['longUrl']))) {
        $codec = new Codec();
        $longUrl = $args['url'] ?? $args['longUrl'];
        $actual = $codec->decode($codec->encode($longUrl));
    } elseif (isset($args['root']) && $method === 'encodeNaryTree' && ($argTypes['root'] ?? null) === 'narynode') {
        $solution = new Solution();
        $root = listToNary($args['root']);
        $binary = $solution->encodeNaryTree($root);
        $actual = $solution->decodeBinaryTree($binary);
        $expected = $root;
        $naryTreeCompare = true;
    } elseif (isset($args['root']) && $className === 'Codec' && ($argTypes['root'] ?? null) === 'narynode') {
        $codec = new Codec();
        $root = listToNary($args['root']);
        $actual = $codec->decode($codec->encode($root));
        $expected = $root;
        $naryTreeCompare = true;
    } elseif (isset($args['root']) && $className === 'Codec' && !isset($args['p']) && !isset($args['q'])) {
        $codec = new Codec();
        $root = listToTree($args['root']);
        $actual = treeToList($codec->deserialize($codec->serialize($root)));
    } elseif (isset($args['root']) && $method === 'treeToDoublyList') {
        $solution = new Solution();
        $actual = doublyTreeNodeToList($solution->treeToDoublyList(listToTree($args['root'])));
    } elseif (isset($args['grid']) && $method === 'construct') {
        $solution = new Solution();
        $actual = quadTreeToList($solution->construct($args['grid']));
    } elseif (isset($args['root']) && $method === 'levelOrder' && ($argTypes['root'] ?? null) === 'narynode') {
        $solution = new Solution();
        $actual = $solution->levelOrder(listToNary($args['root']));
    } elseif (isset($args['root']) && isset($args['p']) && $method === 'inorderSuccessor') {
        $solution = new $className();
        $root = listToTree($args['root']);
        $pNode = findParentNode($root, $args['p']);
        $result = $solution->$method($root, $pNode);
        $actual = $result !== null ? $result->val : null;
    } elseif (isset($args['tree']) && isset($args['node']) && $method === 'inorderSuccessor') {
        $solution = new $className();
        $root = listToParentTree($args['tree']);
        $target = findParentNode($root, $args['node']);
        $result = $solution->$method($target);
        $actual = $result !== null ? $result->val : null;
    } elseif (isset($args['head']) && $method === 'flatten' && ($argTypes['head'] ?? null) === 'multilevelnode') {
        $solution = new Solution();
        $actual = multilevelToList($solution->flatten(listToMultilevel($args['head'])));
    } elseif (isset($args['room']) && $method === 'cleanRoom') {
        $robot = new MockRobot($args['room'], $args['row'], $args['col']);
        $solution = new Solution();
        $solution->cleanRoom($robot);
        $actual = robotCleanedAll($robot) ? 'Robot cleaned all rooms.' : 'Robot missed rooms.';
    } elseif ($method === 'rand10' && isset($args['n'])) {
        $GLOBALS['__rand7_sequence__'] = $case['rand7Sequence'] ?? [];
        $solution = new Solution();
        $actual = [];
        for ($call = 0; $call < $args['n']; $call++) {
            $actual[] = $solution->rand10();
        }
    } else {
        $instance = new $className();
        $converted = [];
        foreach ($keys as $key) {
            $converted[] = convertArg($args[$key], $argTypes[$key] ?? null);
        }
        if (in_array('chars', $keys, true) && isInplaceExpected($expected)) {
            $converted[array_search('chars', $keys, true)] = array_values($args['chars']);
        }
        if (($argTypes['return'] ?? null) === 'void') {
            $instance->$method(...$converted);
            if (in_array('root', $keys, true)) {
                $actual = treeToList($converted[array_search('root', $keys, true)]);
            }
        } else {
            $actual = $instance->$method(...$converted);
            if (!isInplaceExpected($expected)) {
                $actual = convertResult($actual, $argTypes['return'] ?? null);
            }
        }
    }

    if ($naryTreeCompare) {
        $ok = naryTreesEqual($actual, $expected);
    } elseif (isInplaceExpected($expected)) {
        $parsed = parseInplaceExpected($expected);
        if ($parsed === null) {
            $ok = false;
        } else {
            [$expectedCount, $expectedPrefix] = $parsed;
            $fieldIndex = array_search('nums', $keys, true);
            if ($fieldIndex === false) {
                $fieldIndex = array_search('chars', $keys, true);
            }
            $mutated = ($fieldIndex !== false && $converted !== null) ? $converted[$fieldIndex] : null;
            $ok = $actual === $expectedCount
                && $mutated !== null
                && array_slice($mutated, 0, $expectedCount) === $expectedPrefix;
        }
    } else {
        $ok = deepEqualDesign($actual, $expected);
    }
    if ($ok) {
        $passed++;
        echo '  PASS case ' . ($index + 1) . "\n";
    } else {
        echo '  FAIL case ' . ($index + 1) . ': expected ' . json_encode($expected) . ', got ' . json_encode($actual) . "\n";
    }
}

echo "Result: {$passed}/" . count($casesDoc['cases']) . " passed\n";
exit($passed === count($casesDoc['cases']) ? 0 : 1);
