# LeetCode 0721 - Accounts Merge
# https://leetcode.com/problems/accounts-merge/

# @param {String[][]} accounts
# @return {String[][]}
def accounts_merge(accounts)
  parent = {}
  email_name = {}

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    parent[find.call(a)] = find.call(b)
  end

  accounts.each do |account|
    name = account[0]
    first = account[1]
    account[1..].each do |email|
      parent[email] = email unless parent.key?(email)
      email_name[email] = name
      union.call(first, email)
    end
  end

  groups = Hash.new { |h, k| h[k] = [] }
  parent.each_key { |email| groups[find.call(email)] << email }

  groups.values.map { |emails| [email_name[emails[0]]] + emails.sort }
end
