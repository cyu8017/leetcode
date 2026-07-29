#!/usr/bin/env ruby
# frozen_string_literal: true

require "json"

ListNode = Struct.new(:val, :next)

def list_to_listnode(values)
  return nil if values.nil? || values.empty?

  head = ListNode.new(values[0], nil)
  current = head
  values[1..].each do |value|
    current.next = ListNode.new(value, nil)
    current = current.next
  end
  head
end

def listnode_to_list(node)
  result = []
  while node
    result << node.val
    node = node.next
  end
  result
end

def list_to_tree(values)
  return nil if values.nil? || values.empty?

  root = Struct.new(:val, :left, :right).new(values[0], nil, nil)
  queue = [root]
  index = 1
  while !queue.empty? && index < values.length
    node = queue.shift
    if index < values.length
      unless values[index].nil?
        node.left = Struct.new(:val, :left, :right).new(values[index], nil, nil)
        queue << node.left
      end
      index += 1
    end
    if index < values.length
      unless values[index].nil?
        node.right = Struct.new(:val, :left, :right).new(values[index], nil, nil)
        queue << node.right
      end
      index += 1
    end
  end
  root
end

def list_to_parent_tree(values)
  return nil if values.nil? || values.empty?

  root = Struct.new(:val, :left, :right, :parent).new(values[0], nil, nil, nil)
  queue = [root]
  index = 1
  while !queue.empty? && index < values.length
    node = queue.shift
    if index < values.length
      unless values[index].nil?
        node.left = Struct.new(:val, :left, :right, :parent).new(values[index], nil, nil, node)
        queue << node.left
      end
      index += 1
    end
    if index < values.length
      unless values[index].nil?
        node.right = Struct.new(:val, :left, :right, :parent).new(values[index], nil, nil, node)
        queue << node.right
      end
      index += 1
    end
  end
  root
end

def find_parent_node(root, val)
  return nil if root.nil?
  return root if root.val == val

  left = find_parent_node(root.left, val)
  return left if left

  find_parent_node(root.right, val)
end

def tree_to_list(root)
  return [] if root.nil?

  result = []
  queue = [root]
  while !queue.empty?
    node = queue.shift
    if node.nil?
      result << nil
      next
    end
    result << node.val
    queue << node.left
    queue << node.right
  end
  result.pop while !result.empty? && result.last.nil?
  result
end

def list_to_nary(values)
  return nil if values.nil? || values.empty?

  root = Struct.new(:val, :children).new(values[0], [])
  parents = [root]
  index = 1
  index += 1 if index < values.length && values[index].nil?

  while !parents.empty?
    next_parents = []
    parent_index = 0
    index += 1 while index < values.length && values[index].nil?
    while parent_index < parents.length && index < values.length
      parent = parents[parent_index]
      segment = []
      while index < values.length && !values[index].nil?
        segment << values[index]
        index += 1
      end
      segment.each do |value|
        child = Struct.new(:val, :children).new(value, [])
        parent.children << child
        next_parents << child
      end
      parent_index += 1
      if index < values.length && values[index].nil?
        index += 1
        if index < values.length && values[index].nil?
          index += 1
          parent_index = parents.length
          break
        end
      end
    end
    parents = next_parents
  end
  root
end

def nary_to_list(root)
  return [] if root.nil?

  result = [root.val]
  parents = [root]
  while !parents.empty?
    next_parents = []
    segments = parents.map { |parent| parent.children.map(&:val) }
    parents.each { |parent| next_parents.concat(parent.children) }
    break if next_parents.empty?

    padding = 0
    segments.each do |segment|
      if segment.empty?
        padding += 1
      else
        break
      end
    end
    padding.times { result << nil }
    segments.each_with_index do |segment, segment_index|
      next if segment_index < padding

      result.concat(segment) unless segment.empty?
      result << nil if segment_index < segments.length - 1
    end
    parents = next_parents
  end
  result
end

def nary_trees_equal(left, right)
  return true if left.nil? && right.nil?
  return false if left.nil? || right.nil?
  return false unless left.val == right.val && left.children.length == right.children.length

  left.children.each_with_index.all? { |child, index| nary_trees_equal(child, right.children[index]) }
end

def quad_tree_to_list(root)
  return [] if root.nil?

  result = []
  queue = [root]
  while !queue.empty?
    node = queue.shift
    if node.nil?
      result << nil
      next
    end
    result << [node.isLeaf ? 1 : 0, node.val ? 1 : 0]
    if node.isLeaf
      queue.concat([nil, nil, nil, nil])
    else
      queue << node.topLeft
      queue << node.topRight
      queue << node.bottomLeft
      queue << node.bottomRight
    end
  end
  result.pop while !result.empty? && result.last.nil?
  result
end

def split_multilevel_rows(values)
  rows = []
  index = 0
  while index < values.length
    row = []
    while index < values.length && !values[index].nil?
      row << index
      index += 1
    end
    rows << row unless row.empty?
    index += 1 if index < values.length && values[index].nil?
    while index < values.length && values[index].nil?
      index += 1
    end
  end
  rows
end

def list_to_multilevel(values)
  return nil if values.nil? || values.empty?

  nodes = {}
  values.each_with_index do |value, node_index|
    nodes[node_index] = Struct.new(:val, :prev, :next, :child).new(value, nil, nil, nil) unless value.nil?
  end
  rows = split_multilevel_rows(values)
  rows.each do |row|
    row.each_with_index do |node_index, position|
      node = nodes[node_index]
      next unless position.positive?

      previous_index = row[position - 1]
      node.prev = nodes[previous_index]
      nodes[previous_index].next = node
    end
  end
  (0...(rows.length - 1)).each do |row_index|
    parent_row = rows[row_index]
    child_row = rows[row_index + 1]
    padding = child_row[0] - parent_row[-1] - 2
    padding = 0 if padding.negative?
    nodes[parent_row[padding]].child = nodes[child_row[0]] if padding < parent_row.length
  end
  nodes[rows[0][0]]
end

def multilevel_to_list(head)
  result = []
  current = head
  while current
    result << current.val
    current = current.next
  end
  result
end

def doubly_tree_node_to_list(head)
  return [] if head.nil?

  result = []
  node = head
  start = head
  loop do
    result << node.val
    break if node.right.nil? || node.right.equal?(start)

    node = node.right
  end
  result
end

def convert_arg(value, type_name)
  return list_to_listnode(value) if type_name == "listnode"
  return value.map { |item| item.nil? || item.empty? ? nil : list_to_listnode(item) } if type_name == "listnode[]"
  return list_to_tree(value) if type_name == "treenode"
  return list_to_nary(value) if type_name == "narynode"
  return list_to_multilevel(value) if type_name == "multilevelnode"

  value
end

class MockMountainArray
  def initialize(values)
    @values = values
  end

  def get(index)
    @values[index]
  end

  def length
    @values.length
  end
end

def convert_result(value, type_name)
  return listnode_to_list(value) if type_name == "listnode"
  return tree_to_list(value) if type_name == "treenode"
  return nary_to_list(value) if type_name == "narynode"
  return quad_tree_to_list(value) if type_name == "quadnode"
  return multilevel_to_list(value) if type_name == "multilevelnode"
  return doubly_tree_node_to_list(value) if type_name == "doublytreenode"

  value
end

def deep_equal(actual, expected)
  if actual.is_a?(Array) && expected.is_a?(Array)
    return false if actual.length != expected.length

    actual.each_with_index.all? { |value, index| deep_equal(value, expected[index]) }
  elsif actual.is_a?(Float) || expected.is_a?(Float)
    (actual.to_f - expected.to_f).abs < 1e-5
  else
    actual == expected
  end
end

def run_design_cases(cases_doc)
  passed = 0
  cases_doc["cases"].each_with_index do |test_case, index|
    operations = test_case["operations"]
    arguments = test_case["arguments"]
    expected = test_case["expected"]
    instance = nil
    actual_outputs = []
    ok = true

    if test_case["randomUniformSequence"]
      iterator = test_case["randomUniformSequence"].each
      set_uniform(->(_a, _b) { iterator.next })
    end

    operations.each_with_index do |operation, op_index|
      call_args = arguments[op_index] || []
      if op_index.zero?
        klass = Object.const_get(operation)
        instance = call_args.empty? ? klass.new : klass.new(*call_args)
        result = nil
      else
        method_sym = if instance.respond_to?(operation)
                       operation
                     else
                       camel_to_snake(operation)
                     end
        result = call_args.empty? ? instance.public_send(method_sym) : instance.public_send(method_sym, *call_args)
      end
      actual_outputs << result
      unless deep_equal(result, expected[op_index])
        ok = false
        step = op_index
        puts "  FAIL case #{index + 1} step #{step + 1}: expected #{expected[step].inspect}, got #{result.inspect}"
        break
      end
    end

    if ok
      passed += 1
      puts "  PASS case #{index + 1}"
    end
  end
  [passed, cases_doc["cases"].length]
end

def inplace_expected?(expected)
  expected.is_a?(String) && (expected.include?(", nums = [") || expected.include?(", chars = ["))
end

def parse_inplace_expected(expected)
  match = expected.strip.match(/\A(\d+),\s*(nums|chars)\s*=\s*\[(.*)\]\z/)
  return nil unless match

  count = match[1].to_i
  field = match[2]
  raw = match[3]
  if field == "chars"
    prefix = raw.scan(/"([^"]*)"|'([^']*)'/).map { |left, right| left || right }
    [count, prefix]
  else
    prefix = raw.split(",").map(&:strip).reject { |token| token.empty? || token == "_" }.map(&:to_i)
    [count, prefix]
  end
end

def camel_to_snake(name)
  name
    .gsub(/([A-Z\d]+)([A-Z][a-z])/, '\1_\2')
    .gsub(/([a-z\d])([A-Z])/, '\1_\2')
    .downcase
    .sub(/^_/, "")
end

def resolve_callable(config)
  method_name = config["method"]
  snake_method = camel_to_snake(method_name)
  class_name = config["class"] || "Solution"

  if Object.const_defined?(class_name)
    klass = Object.const_get(class_name)
    return ->(*values) { klass.new.public_send(method_name, *values) }
  end
  return ->(*values) { __send__(snake_method.to_sym, *values) } if respond_to?(snake_method.to_sym, true)

  raise "Method #{method_name} not found in solution.rb"
end

problem_dir = File.expand_path(ARGV[0])
config = JSON.parse(File.read(File.join(problem_dir, "tests", "config.json")))
cases_doc = JSON.parse(File.read(File.join(problem_dir, "tests", "cases.json")))

cases = cases_doc["cases"] || []
if cases.empty?
  puts "Ruby tests: #{File.basename(problem_dir)}"
  puts "  no test cases defined in tests/cases.json"
  exit 4
end

kind = config["kind"] || cases[0]["kind"] || "standard"
if %w[sql shell].include?(kind)
  if config["runnable"] == false
    puts "Ruby tests: #{File.basename(problem_dir)}"
    puts "  SKIP kind=#{kind} (runner not implemented)"
    exit 0
  end
  puts "Ruby tests: #{File.basename(problem_dir)}"
  puts "  kind=#{kind} requires a runner but none is configured"
  exit 2
end
if kind == "design"
  unless File.exist?(File.join(problem_dir, "solution.rb"))
    puts "Ruby tests: #{File.basename(problem_dir)}"
    puts "  missing solution file for ruby"
    exit 2
  end

  load File.join(problem_dir, "solution.rb")
  design_class = config["class"] || cases[0]["operations"][0]
  puts "Ruby design tests: #{File.basename(problem_dir)} :: #{design_class}"
  passed, total = run_design_cases(cases_doc)
  puts "Result: #{passed}/#{total} passed"
  exit(passed == total ? 0 : 1)
end

unless File.exist?(File.join(problem_dir, "solution.rb"))
  puts "Ruby tests: #{File.basename(problem_dir)}"
  puts "  missing solution file for ruby"
  exit 2
end

load File.join(problem_dir, "solution.rb")

method_name = config["method"]
arg_types = config["types"] || {}
param_order = config["paramOrder"] || []
callable = resolve_callable(config)

puts "Ruby tests: #{File.basename(problem_dir)} :: #{method_name}()"

passed = 0
cases_doc["cases"].each_with_index do |test_case, index|
  args = test_case["args"] || {}
  keys = param_order.empty? ? args.keys : param_order
  expected = test_case["expected"]
  actual = nil
  values = nil
  nary_tree_compare = false

  if config["class"] == "Codec" && (args.key?("url") || args.key?("longUrl"))
    codec = Codec.new
    long_url = args["url"] || args["longUrl"]
    actual = codec.decode(codec.encode(long_url))
  elsif args.key?("root") && method_name == "encodeNaryTree" && arg_types["root"] == "narynode"
    solution = Solution.new
    root = list_to_nary(args["root"])
    binary = solution.encodeNaryTree(root)
    actual = solution.decodeBinaryTree(binary)
    expected = root
    nary_tree_compare = true
  elsif args.key?("root") && config["class"] == "Codec" && arg_types["root"] == "narynode"
    codec = Codec.new
    root = list_to_nary(args["root"])
    actual = codec.decode(codec.encode(root))
    expected = root
    nary_tree_compare = true
  elsif args.key?("root") && config["class"] == "Codec" && !args.key?("p") && !args.key?("q")
    codec = Codec.new
    root = list_to_tree(args["root"])
    actual = tree_to_list(codec.deserialize(codec.serialize(root)))
  elsif args.key?("root") && method_name == "treeToDoublyList"
    actual = doubly_tree_node_to_list(callable.call(list_to_tree(args["root"])))
  elsif args.key?("grid") && method_name == "construct"
    actual = quad_tree_to_list(callable.call(args["grid"]))
  elsif args.key?("root") && method_name == "levelOrder" && arg_types["root"] == "narynode"
    actual = callable.call(list_to_nary(args["root"]))
  elsif method_name == "expTree" && (config["class"] || "") == "TreeBuilder"
    builder = TreeBuilder.new
    node = if builder.respond_to?(:expTree)
             builder.expTree(args["postfix"])
           else
             builder.exp_tree(args["postfix"])
           end
    actual = node.respond_to?(:evaluate) ? node.evaluate : node
  elsif args.key?("root") && args.key?("p") && args.key?("q") && method_name == "lowestCommonAncestor"
    root = list_to_tree(args["root"])
    p_node = find_parent_node(root, args["p"])
    q_node = find_parent_node(root, args["q"])
    result = callable.call(root, p_node, q_node)
    actual = result ? result.val : nil
  elsif args.key?("root") && args.key?("nodes") && method_name == "lowestCommonAncestor"
    root = list_to_tree(args["root"])
    node_list = args["nodes"].map { |value| find_parent_node(root, value) }
    result = callable.call(root, node_list)
    actual = result ? result.val : nil
  elsif args.key?("root") && args.key?("fromNode") && args.key?("toNode") && method_name == "correctBinaryTree"
    root = list_to_tree(args["root"])
    from_node = find_parent_node(root, args["fromNode"])
    to_node = find_parent_node(root, args["toNode"])
    from_node.right = to_node
    actual = tree_to_list(callable.call(root))
  elsif args.key?("root") && args.key?("leaf") && method_name == "flipBinaryTree"
    root = list_to_parent_tree(args["root"])
    leaf = find_parent_node(root, args["leaf"])
    actual = tree_to_list(callable.call(root, leaf))
  elsif args.key?("root") && args.key?("p") && method_name == "inorderSuccessor"
    root = list_to_tree(args["root"])
    p_node = find_parent_node(root, args["p"])
    result = callable.call(root, p_node)
    actual = result ? result.val : nil
  elsif args.key?("tree") && args.key?("node") && method_name == "inorderSuccessor"
    root = list_to_parent_tree(args["tree"])
    target = find_parent_node(root, args["node"])
    result = callable.call(target)
    actual = result ? result.val : nil
    elsif args.key?("head") && method_name == "flatten" && arg_types["head"] == "multilevelnode"
    actual = multilevel_to_list(callable.call(list_to_multilevel(args["head"])))
  elsif args.key?("room") && method_name == "cleanRoom"
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    robot = Struct.new(:room, :row, :col, :direction, :cleaned).new(
      args["room"],
      args["row"],
      args["col"],
      0,
      {}
    )
    robot.define_singleton_method(:move) do
      dr, dc = directions[direction]
      nr = row + dr
      nc = col + dc
      if nr >= 0 && nr < room.length && nc >= 0 && nc < room[0].length && room[nr][nc] == 1
        self.row = nr
        self.col = nc
        true
      else
        false
      end
    end
    robot.define_singleton_method(:turnLeft) { self.direction = (direction + 3) % 4 }
    robot.define_singleton_method(:turnRight) { self.direction = (direction + 1) % 4 }
    robot.define_singleton_method(:clean) { cleaned["#{row},#{col}"] = true }
    Solution.new.cleanRoom(robot)
    all_cleaned = true
    args["room"].each_with_index do |row_cells, r|
      row_cells.each_with_index do |cell, c|
        if cell == 1 && !robot.cleaned["#{r},#{c}"]
          all_cleaned = false
        end
      end
    end
    actual = all_cleaned ? "Robot cleaned all rooms." : "Robot missed rooms."
  elsif method_name == "rand10" && args.key?("n")
    sequence = (test_case["rand7Sequence"] || []).each
    Object.send(:define_method, :rand7) { sequence.next }
    actual = Array.new(args["n"]) { Solution.new.rand10 }
  else
    values = keys.map { |key| convert_arg(args[key], arg_types[key]) }
    if keys.include?("chars") && inplace_expected?(expected)
      values[keys.index("chars")] = args["chars"].dup
    end
    if keys.include?("nums") && (inplace_expected?(expected) || arg_types["return"] == "void")
      values[keys.index("nums")] = args["nums"].dup
    end
    if keys.include?("arr") && arg_types["return"] == "void" && args["arr"].is_a?(Array)
      values[keys.index("arr")] = args["arr"].dup
    end
    if keys.include?("mountainArr") && method_name == "findInMountainArray"
      values[keys.index("mountainArr")] = MockMountainArray.new(args["mountainArr"])
    end
    if arg_types["return"] == "void"
      callable.call(*values)
      if keys.include?("root")
        actual = tree_to_list(values[keys.index("root")])
      elsif keys.include?("nums")
        actual = values[keys.index("nums")]
      elsif keys.include?("arr") && values[keys.index("arr")].is_a?(Array)
        actual = values[keys.index("arr")]
      elsif keys.include?("chars")
        actual = values[keys.index("chars")]
      end
    else
      actual = callable.call(*values)
      actual = convert_result(actual, arg_types["return"]) unless inplace_expected?(expected)
    end
  end

  ok = if nary_tree_compare
         nary_trees_equal(actual, expected)
       elsif inplace_expected?(expected)
         parsed = parse_inplace_expected(expected)
         if parsed.nil?
           false
         else
           expected_count, expected_prefix = parsed
           field_index = keys.index("nums") || keys.index("chars")
           mutated = field_index && values ? values[field_index] : nil
           actual == expected_count && mutated && mutated.take(expected_count) == expected_prefix
         end
       else
         deep_equal(actual, expected)
       end

  if ok
    passed += 1
    puts "  PASS case #{index + 1}"
  else
    puts "  FAIL case #{index + 1}: expected #{expected.inspect}, got #{actual.inspect}"
  end
end

puts "Result: #{passed}/#{cases_doc['cases'].length} passed"
exit(passed == cases_doc["cases"].length ? 0 : 1)
